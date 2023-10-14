#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import  request, make_response, request, session
from flask_restful import Resource
# from flask_migrate import Migrate
# from flask_cors import CORS

# Local imports
from config import app, db, api
# Add your model imports
from models import db, User, Prescriber, Prescription, Medication, Appointment

# Views go here!
validation_errors = {"errors":["validation errors"]}


class Signup ( Resource ) :
    
    def post ( self ) :
        
        rq = request.get_json()
        User.clear_validation_errors()
        try :
            
            new_user = User(
                username = rq[ 'username' ],
                
                password_hash = rq[ 'password' ]
            )

            if new_user.validation_errors :
                raise ValueError
            
         
            db.session.add( new_user )
            db.session.commit()

           
            session[ 'user_id' ] = new_user.id

           
            return new_user.to_dict(), 201
        except :
            errors = new_user.validation_errors
            new_user.clear_validation_errors()
            return { 'errors': errors }, 422
    
api.add_resource( Signup, '/signup', endpoint = 'signup' )


class Login ( Resource ) :
    def post ( self ) :
        username = request.get_json()[ 'username' ]
        password = request.get_json()[ 'password' ]

        user = User.query.filter( User.username.like( f'{ username }' ) ).first()

        if user and user.authenticate( password ) :
            session[ 'user_id' ] = user.id
            print( session[ 'user_id' ] )
            return user.to_dict(), 200
        else :
            return { 'errors':['Invalid username or password.'] }, 404

api.add_resource( Login, '/login', endpoint = 'login' )


class Logout ( Resource ) :
    def delete ( ) :
        session[ 'user_id' ] = None
        return {}, 204



class Users(Resource):
    def get(self):
        users = User.query.all()
        users_dict = [user.to_dict(rules = ("-prescriptions","-appointments")) for user in users]
        return make_response(users_dict, 201)
    
    def post(self):
        rq = request.get_json()
        try:
            new_user = User(
                first_name = rq.get('first_name'),
                last_name = rq.get('last_name'),
                username = rq.get('username') ,
                password_hash = rq.get('password_hash')
            )
            db.session.add(new_user)
            db.session.commit()
            return make_response(new_user.to_dict(rules = ("-prescriptions","-appointments")), 201)
        except:
            return make_response(validation_errors, 400)
api.add_resource(Users, '/users', endpoint = 'users')

class UserbyId(Resource):

    def get(self, id):
        user = User.query.get(id)
        
        if user is None:
            return make_response({"error":"User not found"}, 404)
        else:
            return make_response(user.to_dict(rules = ("-prescriptions","-appointments")), 200)
    
    def delete(self, id ):
        user = User.query.get(id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return make_response({}, 204)
        else:
            return make_response({"error":"User not found"}, 404)

api.add_resource(UserbyId, '/users/<int:id>')

class Prescribers(Resource):
    def get(self):
        prescribers = Prescriber.query.all()
        prescribers_dict = [prescriber.to_dict(rules = ("-prescriptions",)) for prescriber in prescribers]
        return make_response(prescribers_dict, 201)
    
    def post(self):
        rq = request.get_json()
        try:
            new_prescriber = Prescriber(
                first_name = rq.get('first_name'),
                last_name = rq.get('last_name'),
                npi = rq.get('npi'),
                address = rq.get('address')
            )
            db.session.add(new_prescriber)
            db.session.commit()
            return make_response(new_prescriber.to_dict(), 201)
        except:
            return make_response(validation_errors, 400)
        
api.add_resource(Prescribers, '/prescribers')

class PresciberById(Resource):
    def get(self,id):
        prescriber = Prescriber.query.get(id)
        
        if prescriber is None:
            return make_response({"error":"Prescriber not found"}, 404)
        else:
            return make_response(prescriber.to_dict(rules = ("-prescriptions",)), 200)

    def delete(self, id ):
        prescriber = Prescriber.query.get(id)
        if prescriber:
            db.session.delete(prescriber)
            db.session.commit()
            return make_response({}, 204)
        else:
            return make_response({"error":"Prescriber not found"}, 404)

api.add_resource(PresciberById, '/prescribers/<int:id>')

class Medications(Resource):
    def get(self):
        medications = Medication.query.all()
        medications_dict = [medication.to_dict(rules = ("-prescriptions",)) for medication in medications]
        return make_response(medications_dict, 201)

    def post(self):
        rq = request.get_json()
        try:
            new_medication = Medication(
                image = rq.get('image'),
                medication_name = rq.get('medication_name'), 
                dosage = rq.get('dosage'),
                medication_description = rq.get('medication_description'),  
                side_effects = rq.get('side_effects'),  
                interactions = rq.get('interactions')
            )
            db.session.add(new_medication)
            db.session.commit()
            return make_response(new_medication.to_dict(), 201)
        except:
            return make_response(validation_errors, 400)
        
api.add_resource(Medications, '/medications')

class MedicationById(Resource):
    def get(self,id):

        medication = Medication.query.get(id)

        if medication:
            return make_response(medication.to_dict(rules = ("-prescriptions",)), 201)
        else:
            return make_response({"error":"Medication not found. "}, 404)

    def patch(self, id):
        medication = Medication.query.get(id)
        req = request.get_json()
        
        if medication:
            try:
                for attr in req:
                    setattr(medication, attr, req.get(attr))
                db.session.commit()

                return make_response(medication.to_dict(), 202)
            except:
                return make_response(validation_errors, 422)
                
        else:
            return make_response({"error":"Medication not found"}, 404)
        
    def delete(self, id ):
        medication = Medication.query.get(id)
        if medication:
            db.session.delete(medication)
            db.session.commit()
            return make_response({}, 204)
        else:
            return make_response({"error":"Medication not found"}, 404)

api.add_resource(MedicationById, '/medications/<int:id>')


class Appointments(Resource):
    def get(self):
        appointments = Appointment.query.all()
        appointments_dict = [appointment.to_dict() for appointment in appointments]
        return make_response(appointments_dict, 201)
    
    def post(self):
        rq = request.get_json()
        try:
            new_appointment = Appointment(
                user_id = rq.get('user_id'),
                appointment_date = rq.get('appointment_date') 
            )
            db.session.add(new_appointment)
            db.session.commit()
            return make_response(new_appointment.to_dict(), 201)
        except:
            return make_response(validation_errors, 400)

api.add_resource(Appointments, '/appointments')

class AppointmentById(Resource):
    def get(self,id):
        appointment = Appointment.query.get(id)
        
        if appointment is None:
            return make_response({"error":"Appointment not found"}, 404)
        else:
            return make_response(appointment.to_dict(), 202)
        
    def patch(self, id):
        appointment = Appointment.query.get(id)
        req = request.get_json()
        
        if appointment:
            try:
                for attr in req:
                    setattr(appointment, attr, req.get(attr))
                db.session.commit()

                return make_response(appointment.to_dict(), 202)
            except:
                return make_response(validation_errors, 422)
                
        else:
            return make_response({"error":"Appointment not found"}, 404)
        
    def delete(self, id ):
        appointment = Appointment.query.get(id)
        if appointment:
            db.session.delete( appointment)
            db.session.commit()
            return make_response({}, 204)
        else:
            return make_response({"error":"Appointment not found"}, 404)

api.add_resource(AppointmentById, '/apppointments/<int:id>')

class Prescriptions(Resource):
    def get(self):
        prescriptions = Prescription.query.all()
        prescriptions_dict = [prescription.to_dict() for prescription in prescriptions]
        return make_response(prescriptions_dict, 201)
    
    def post(self):
        rq = request.get_json()
        try:
            new_prescription = User(
                medication_name = rq.get('medication_name') ,
                instructions = rq.get('instructions'),
                date_written = rq.get('date_written'),
                user_id = rq.get('user_id') ,
                prescriber_id = rq.get('prescriber_id') ,
                medication_id = rq.get('medication_id') 
            )
            db.session.add(new_prescription)
            db.session.commit()
            return make_response(new_prescription.to_dict(), 201)
        except:
            return make_response(validation_errors, 400)
        
api.add_resource(Prescriptions, '/prescriptions/')

class PrescriptionsById(Resource):
    def get(self,id):
        prescription = Prescription.query.get(id)
        
        if prescription is None:
            return make_response({"error":"Prescription not found"}, 404)
        else:
            return make_response(prescription.to_dict(), 200)
        
    def patch(self, id):
        prescription = Prescription.query.get(id)
        req = request.get_json()
        
        if prescription:
            try:
                for attr in req:
                    setattr(prescription, attr, req.get(attr))
                db.session.commit()

                return make_response(prescription.to_dict(), 202)
            except:
                return make_response(validation_errors, 422)
                
        else:
            return make_response({"error":"Prescription not found"}, 404)

    def delete(self, id ):
        prescription = Prescription.query.get(id)
        if prescription:
            db.session.delete(prescription)
            db.session.commit()
            return make_response({}, 204)
        else:
            return make_response({"error":"Prescription not found"}, 404)

api.add_resource(PrescriptionsById, '/prescriptions/<int:id>')



if __name__ == '__main__':
    app.run(port=5555, debug=True)