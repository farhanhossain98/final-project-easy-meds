#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, User, Prescriber, Prescription, Medication, Appointment

from config import app, db, api

fake = Faker()
if __name__ == '__main__':
    
    with app.app_context():
        Prescriber.query.delete()
        User.query.delete()
        Prescription.query.delete()
        Medication.query.delete()
        Appointment.query.delete()
        db.session.commit()
        
        print("Starting seed...")
        # Seed code goes here!


        print('Making Prescibers...')

        prescribers = []

        pr1 = Prescriber(first_name = "Josh", last_name = "Smith", npi= 1234567890, address = "23 East 56 St 10019 NY, NY")
        pr2 = Prescriber(first_name = "Aaron", last_name = "Justice", npi= 1234567890, address = "23 East 56 St 10019 NY, NY")
        pr3 = Prescriber(first_name = "Gabrielle", last_name = "Nosh", npi= 1234567890, address = "23 East 56 St 10019 NY, NY")
        pr4 = Prescriber(first_name = "Elle", last_name = "Nonce", npi= 1234567890, address = "23 East 56 St 10019 NY, NY")
        pr5 = Prescriber(first_name = "Ruth", last_name = "Hash", npi= 1234567890, address = "23 East 56 St 10019 NY, NY")

        prescribers.append(pr1)
        prescribers.append(pr2)
        prescribers.append(pr3)
        prescribers.append(pr4)
        prescribers.append(pr5)

        db.session.add_all(prescribers)
        db.session.commit()

        print('Making Users...')

        users = []
        
        u1 = User(first_name = "David", last_name = "Nash", username = "dnash123", password = "hello123")
        u2 = User(first_name = "Carol", last_name = "Williams", username = "cwill2", password = "crazy123")
        u3 = User(first_name = "Jhason", last_name = "Kidd", username = "jkidd", password = "jkid123")
        u4 = User(first_name = "Henjuto", last_name = "Calem", username = "henco", password = "devil")
        u5 = User(first_name = "Camel", last_name = "Bong", username = "cabbey", password = "failed123")

        users.append(u1)
        users.append(u2)
        users.append(u3)
        users.append(u4)
        users.append(u5)

        db.session.add_all(users)
        db.session.commit()

        print('Making Medicine...')

        medications = []

        m1 = Medication(
            image = 'https://img.medscapestatic.com/pi/features/drugdirectory/octupdate/ING01560.jpg',
            medication_name = "Metformin",
            dosage = "1000 mg",
            medication_description = "Metformin is used with a proper diet and exercise program and possibly with other medications to control high blood sugar. It is used in patients with type 2 diabetes. Controlling high blood sugar helps prevent kidney damage, blindness, nerve problems, loss of limbs, and sexual function problems. Proper control of diabetes may also lessen your risk of a heart attack or stroke. Metformin works by helping to restore your body's proper response to the insulin you naturally produce. It also decreases the amount of sugar that your liver makes and that your stomach/intestines absorb.",
            side_effects = "Nausea, vomiting, stomach upset, diarrhea, weakness, or a metallic taste in the mouth may occur. If any of these effects last or get worse, tell your doctor or pharmacist promptly. If stomach symptoms return later (after taking the same dose for several days or weeks), tell your doctor right away. Stomach symptoms that occur after the first days of your treatment may be signs of lactic acidosis.",
            interactions = "Beta-blocker medications (such as metoprolol, propranolol, glaucoma eye drops such as timolol) may prevent the fast/pounding heartbeat you would usually feel when your blood sugar falls too low (hypoglycemia). Other symptoms of low blood sugar, such as dizziness, hunger, or sweating, are unaffected by these drugs."     
            )
        m2 = Medication(
            image = 'https://img.medscapestatic.com/pi/features/drugdirectory/octupdate/00207445.jpg',
            medication_name = "Clonazepam",
            dosage = '0.5 mg',
            medication_description = "Clonazepam is used to prevent and control seizures. This medication is known as an anticonvulsant or antiepileptic drug. It is also used to treat panic attacks. Clonazepam works by calming your brain and nerves. It belongs to a class of drugs called benzodiazepines.",
            side_effects = "Drowsiness, dizziness, tiredness, loss of coordination, or increased saliva production may occur. If any of these effects last or get worse, tell your doctor or pharmacist promptly.",
            interactions = "The risk of serious side effects (such as slow/shallow breathing, severe drowsiness/dizziness) may be increased if this medication is taken with other products that may also cause drowsiness or breathing problems. Tell your doctor or pharmacist if you are taking other products such as opioid pain or cough relievers (such as codeine, hydrocodone), alcohol, marijuana (cannabis), drugs for sleep or anxiety (such as alprazolam, lorazepam, zolpidem), muscle relaxants (such as carisoprodol, cyclobenzaprine), or antihistamines (such as cetirizine, diphenhydramine)."     
            )
        
        m3 = Medication(
            image = 'https://img.medscapestatic.com/pi/features/drugdirectory/octupdate/BMP08940.jpg',
            medication_name = "Eliquis",
            dosage = '5 mg',
            medication_description = "Take this medication by mouth with or without food as directed by your doctor, usually twice daily (every 12 hours). If you cannot swallow the tablet whole, you may crush the tablet and mix with water, apple juice, or applesauce and take it right away.The dosage is based on your medical condition, age, weight, kidney function, response to treatment, and other medications you may be taking. Be sure to tell your doctor and pharmacist about all the products you use (including prescription drugs, nonprescription drugs, and herbal products). If you are taking apixaban to prevent blood clots from forming after surgery, the length of treatment is based on the type of surgery that you had.",
            side_effects = "Nausea, easy bruising, or minor bleeding (such as nosebleed, bleeding from cuts) may occur. If any of these effects last or get worse, tell your doctor or pharmacist promptly.",
            interactions = "Some products that may interact with this drug include: mifepristone, other drugs that can cause bleeding/bruising (including antiplatelet drugs such as clopidogrel, NSAIDs such as ibuprofen/naproxen, 'blood thinners' such as warfarin/enoxaparin), certain antidepressants (including SSRIs such as fluoxetine, SNRIs such as desvenlafaxine/venlafaxine).."     
            )
        m4 = Medication(
            image = 'https://img.medscapestatic.com/pi/features/drugdirectory/octupdate/EPC07140.jpg',
            medication_name = "Benzonatate",
            dosage = '100 mg',
            medication_description = "This medication is used to treat coughs caused by the common cold and other breathing problems (such as pneumonia, bronchitis, emphysema, asthma). It works by reducing the reflex in the lungs that causes the urge to cough.Use of this medication is not recommended in children younger than 10 years. Discuss the risks and benefits with your doctor.",
            side_effects = "Drowsiness, dizziness, headache, nausea, stomach upset, constipation, and stuffy nose may occur. If any of these effects last or get worse, tell your doctor or pharmacist promptly.",
            interactions = "Tell your doctor or pharmacist if you are taking other products that cause drowsiness such as opioid pain or cough relievers (such as codeine, hydrocodone), alcohol, marijuana (cannabis), drugs for sleep or anxiety (such as alprazolam, lorazepam, zolpidem), muscle relaxants (such as carisoprodol, cyclobenzaprine), or antihistamines (such as cetirizine, diphenhydramine)."     
            )
        
        m5 = Medication(
            image = 'https://img.medscapestatic.com/pi/features/drugdirectory/octupdate/CAL01220.jpg',
            medication_name = "Famotidine",
            dosage = '40 mg',
            medication_description = "Famotidine is used to treat ulcers of the stomach and intestines and to prevent intestinal ulcers from coming back after they have healed. This medication is also used to treat certain stomach and throat (esophagus) problems (such as erosive esophagitis, gastroesophageal reflux disease-GERD, Zollinger-Ellison syndrome). It works by decreasing the amount of acid your stomach makes. It relieves symptoms such as cough that doesn't go away, stomach pain, heartburn, and difficulty swallowing.",
            side_effects = "Headache, constipation, or diarrhea may occur. If any of these effects last or get worse, tell your doctor or pharmacist promptly.",
            interactions = "Some products need stomach acid so that the body can absorb them properly. Famotidine decreases stomach acid, so it may change how well these products work. Some affected products include atazanavir, dasatinib, certain azole antifungals (such as itraconazole, ketoconazole), levoketoconazole, pazopanib, sparsentan, among others."     
            )
        m6 = Medication(
            image = 'https://img.medscapestatic.com/pi/features/drugdirectory/octupdate/BMS00070.jpg',
            medication_name = "Abilify",
            dosage = '5 mg',
            medication_description = "Take this medication by mouth with or without food as directed by your doctor, usually once daily. The dosage is based on your medical condition, response to treatment, age, and other medications you may be taking. Be sure to tell your doctor and pharmacist about all the products you use (including prescription drugs, nonprescription drugs, and herbal products). To reduce your risk of side effects, your doctor may direct you to start this medication at a low dose and gradually increase your dose. Follow your doctor's instructions carefully.",
            side_effects = "Dizziness, lightheadedness, drowsiness, nausea, vomiting, tiredness, excess saliva/drooling, blurred vision, weight gain, constipation, headache, and trouble sleeping may occur. If any of these effects last or get worse, tell your doctor or pharmacist promptly.",
            interactions = "Tell your doctor or pharmacist if you are taking other products that cause drowsiness such as opioid pain or cough relievers (such as codeine, hydrocodone), alcohol, marijuana (cannabis), drugs for sleep or anxiety (such as alprazolam, lorazepam, zolpidem), muscle relaxants (such as carisoprodol, cyclobenzaprine), or antihistamines (such as cetirizine, diphenhydramine)."     
            )
        m7 = Medication(
            image = 'https://img.medscapestatic.com/pi/features/drugdirectory/octupdate/DIS31050.jpg',
            medication_name = "Prozac",
            dosage = '20 mg',
            medication_description = "Fluoxetine is used to treat depression, panic attacks, obsessive compulsive disorder, a certain eating disorder (bulimia), and a severe form of premenstrual syndrome (premenstrual dysphoric disorder).This medication may improve your mood, sleep, appetite, and energy level and may help restore your interest in daily living. ",
            side_effects = "Nausea, drowsiness, dizziness, anxiety, trouble sleeping, loss of appetite, tiredness, sweating, or yawning may occur. If any of these effects last or get worse, tell your doctor promptly.",
            interactions = "Fluoxetine can stay in your body for many weeks after your last dose and may interact with many other medications. Before using any medication, tell your doctor or pharmacist if you have taken fluoxetine in the previous 5 weeks.Taking MAO inhibitors with his medication may cause a serious (possibly fatal) drug interaction. Avoid taking MAO inhibitors (isocarboxazid, linezolid, metaxalone, methylene blue, moclobemide, phenelzine, procarbazine, rasagiline, safinamide, selegiline, tranylcypromine) during treatment with this medication. Most MAO inhibitors should also not be taken for 2 weeks before and at least 5 weeks after treatment with this medication. Ask your doctor when to start or stop taking this medication."     
            )
        m8 = Medication(
            image = 'https://img.medscapestatic.com/pi/features/drugdirectory/octupdate/CAM02070.jpg',
            medication_name = "Citalopram",
            dosage = '20 mg',
            medication_description = "Citalopram is used to treat depression. It may improve your energy level and feelings of well-being. Citalopram is known as a selective serotonin reuptake inhibitor (SSRI). This medication works by helping to restore the balance of a certain natural substance (serotonin) in the brain.",
            side_effects = "Nausea, dry mouth, loss of appetite, tiredness, drowsiness, sweating, blurred vision, and yawning may occur. If any of these effects last or get worse, tell your doctor or pharmacist promptly.",
            interactions = "Some products that may interact with this drug are: other drugs that can cause bleeding/bruising (including antiplatelet drugs such as clopidogrel, NSAIDs such as ibuprofen/naproxen, 'blood thinners' such as dabigatran/warfarin). Aspirin can increase the risk of bleeding when used with this medication. However, if your doctor has directed you to take low-dose aspirin for heart attack or stroke prevention (usually 81-162 milligrams a day), you should continue taking it unless your doctor instructs you otherwise. Ask your doctor or pharmacist for more details."     
            )
        m9 = Medication(
            image = 'https://img.medscapestatic.com/pi/features/drugdirectory/octupdate/CBR04060.jpg',
            medication_name = "Gabapentin",
            dosage = '800 mg',
            medication_description = "Gabapentin is used with other medications to prevent and control seizures. It is also used to relieve nerve pain following shingles (a painful rash due to herpes zoster infection) in adults. Gabapentin is known as an anticonvulsant or antiepileptic drug.",
            side_effects = "Drowsiness, dizziness, loss of coordination, tiredness, blurred/double vision, unusual eye movements, or shaking (tremor) may occur. If any of these effects last or get worse, tell your doctor or pharmacist promptly.",
            interactions = "The risk of serious side effects (such as slow/shallow breathing, severe drowsiness/dizziness) may be increased if this medication is taken with other products that may also cause drowsiness or breathing problems. Tell your doctor or pharmacist if you are using other products such as opioid pain or cough relievers (such as codeine, hydrocodone), alcohol, marijuana (cannabis), drugs for sleep or anxiety (such as alprazolam, lorazepam, zolpidem), muscle relaxants (such as carisoprodol, cyclobenzaprine), or antihistamines (such as cetirizine, diphenhydramine)."     
            )
        
        m10 = Medication(
            image = 'https://img.medscapestatic.com/pi/features/drugdirectory/octupdate/AUR06950.jpg',
            medication_name = "Metronidazole",
            dosage = '500 mg',
            medication_description = "Metronidazole is an antibiotic that is used to treat a wide variety of infections. It works by stopping the growth of certain bacteria and parasites.This antibiotic treats only certain bacterial and parasitic infections. It will not work for viral infections (such as common cold, flu). Using any antibiotic when it is not needed can cause it to not work for future infections.Metronidazole may also be used with other medications to treat certain stomach/intestinal ulcers caused by a bacteria (H. pylori).",
            side_effects = "Dizziness, headache, stomach upset, nausea, vomiting, loss of appetite, diarrhea, constipation, or metallic taste in your mouth may occur. If any of these effects last or get worse, tell your doctor or pharmacist promptly.",
            interactions = "Some products that may interact with this drug include: alcohol-containing products (such as cough and cold syrups, aftershave), products containing propylene glycol, lopinavir/ritonavir solution, lithium. Do not take metronidazole if you are also taking disulfiram or if you have taken disulfiram within the last 2 weeks."     
            )
        m11 = Medication(
            image = 'https://img.medscapestatic.com/pi/features/drugdirectory/octupdate/ACT05001.jpg',
            medication_name = "Morphine",
            dosage = '90 mg',
            medication_description = "This medication is used to help relieve severe ongoing pain (such as due to cancer). Morphine belongs to a class of drugs known as opioid analgesics. It works in the brain to change how your body feels and responds to pain.",
            side_effects = "Nausea, vomiting, constipation, lightheadedness, dizziness, or drowsiness may occur. Some of these side effects may decrease after you have been using this medication for a while. If any of these effects last or get worse, tell your doctor or pharmacist promptly. To prevent constipation, eat dietary fiber, drink enough water, and exercise. You may also need to take a laxative. Ask your pharmacist which type of laxative is right for you.",
            interactions = "Some products that may interact with this drug include: certain pain medications (mixed opioid agonist-antagonists such as butorphanol, nalbuphine, pentazocine), naltrexone, products that contain alcohol (such as cough-and-cold syrups), samidorphan."     
            )
        m12 = Medication(
            image = 'https://img.medscapestatic.com/pi/features/drugdirectory/octupdate/ACI01830.jpg',
            medication_name = "Hydrochlorothiazide",
            dosage = '25 mg',
            medication_description = "Take this medication by mouth as directed by your doctor, usually once daily in the morning with or without food. If you take this drug too close to bedtime, you may need to wake up to urinate. It is best to take this medication at least 4 hours before your bedtime.",
            side_effects = "Upset stomach, dizziness, or headache may occur as your body adjusts to the medication. If any of these effects last or get worse, tell your doctor or pharmacist promptly. To reduce the risk of dizziness and lightheadedness, get up slowly when rising from a sitting or lying position.",
            interactions = "Some products have ingredients that could raise your blood pressure or worsen your swelling. Tell your pharmacist what products you are using, and ask how to use them safely (especially cough-and-cold products, diet aids, or NSAIDs such as ibuprofen/naproxen)."     
            )
        m13 = Medication(
            image = 'https://img.medscapestatic.com/pi/features/drugdirectory/octupdate/FOR20200.jpg',
            medication_name = "Lexapro",
            dosage = '20 mg',
            medication_description = "Escitalopram is used to treat depression and anxiety. It works by helping to restore the balance of a certain natural substance (serotonin) in the brain. Escitalopram belongs to a class of drugs known as selective serotonin reuptake inhibitors (SSRI). It may improve your energy level and feelings of well-being and decrease nervousness.",
            side_effects = "Nausea, dry mouth, trouble sleeping, constipation, tiredness, drowsiness, dizziness, and increased sweating may occur. If any of these effects last or get worse, tell your doctor promptly.",
            interactions = "Aspirin can increase the risk of bleeding when used with this medication. However, if your doctor has directed you to take low-dose aspirin for heart attack or stroke prevention (usually 81-162 milligrams a day), you should continue taking it unless your doctor instructs you otherwise. Ask your doctor or pharmacist for more details."     
            )
        m14 = Medication(
            image = 'https://img.medscapestatic.com/pi/features/drugdirectory/octupdate/PKD01580.jpg',
            medication_name = "Lipitor",
            dosage = '80 mg', 
            medication_description = "Take this medication regularly in order to get the most benefit from it. Remember to take it at the same time each day. Keep taking this medication even if you feel well. Most people with high cholesterol or triglycerides do not feel sick.",
            side_effects = "This drug may rarely cause muscle problems (which can rarely lead to very serious conditions called rhabdomyolysis and autoimmune myopathy). Tell your doctor right away if you develop any of these symptoms during treatment and if these symptoms last after your doctor stops this drug: muscle pain/tenderness/weakness (especially with fever or unusual tiredness), signs of kidney problems (such as change in the amount of urine).",
            interactions = "Do not take any red yeast rice products while you are taking atorvastatin because some red yeast rice products may also contain a statin called lovastatin. Taking atorvastatin and red yeast rice products together can increase your risk of serious muscle and liver problems."     
            )
        m15 = Medication(
            image = "https://img.medscapestatic.com/pi/features/drugdirectory/octupdate/LUP05170.jpg",
            medication_name = "Lisinopril",
            dosage = '40 mg',
            medication_description = "For the treatment of high blood pressure, it may take 2 to 4 weeks before you get the full benefit of this medication. For the treatment of heart failure, it may take weeks to months before you get the full benefit of this medication. Tell your doctor if your condition does not get better or if it gets worse (for example, your blood pressure readings remain high or increase).",
            side_effects = "Dizziness, lightheadedness, tiredness, or headache may occur as your body adjusts to the medication. Dry cough may also occur. If any of these effects last or get worse, tell your doctor or pharmacist promptly.",
            interactions = "Some products that may interact with this drug are: aliskiren, certain drugs that weaken the immune system/increase the risk of infection (such as everolimus, sirolimus), lithium, drugs that may increase the level of potassium in the blood (such as ARBs including losartan/valsartan, birth control pills containing drospirenone), sacubitril."     
            )
        
        medications.append(m1)
        medications.append(m2)
        medications.append(m3)
        medications.append(m4)
        medications.append(m5)
        medications.append(m6)
        medications.append(m7)
        medications.append(m8)
        medications.append(m9)
        medications.append(m10)
        medications.append(m11)
        medications.append(m12)
        medications.append(m13)    
        medications.append(m14)
        medications.append(m15)
        
        db.session.add_all(medications)
        db.session.commit()



        # print('Making Appointments')


        # appointments = []

        # a1 = Appointment(
        #     user_id = User.id,
        #     prescriber_id = Prescriber.id,
        #     appointment_date = 1/23/2023
        # )
        # a2 = Appointment(
        #     user_id = User.id,
        #     prescriber_id = Prescriber.id,
        #     appointment_date = 12/3/2023
        # )
        # a3 = Appointment(
        #     user_id = User.id,
        #     prescriber_id = Prescriber.id,
        #     appointment_date = 11/23/2023
        # )
        # a4 = Appointment(
        #     user_id = User.id,
        #     prescriber_id = Prescriber.id,
        #     appointment_date = 9/9/2023
        # )
        # a5 = Appointment(
        #     user_id = User.id,
        #     prescriber_id = Prescriber.id,
        #     appointment_date = 4/1/2023
        # )

        # appointments.extend([a1,a2,a3,a4,a5])

        # db.session.add_all(appointments)
        # db.session.commit()

        print('Making Prescriptions')

        prescriptions = []
        p1 = Prescription (
            medication_name ='Metformin', 
            instructions = 'Take one pill by mouth once per day',
            user_id = 1,
            prescriber_id = 2,
            medication_id = 1
            )
        p2 = Prescription (
            medication_name ='Clonazepam', 
            instructions = 'Take one pill by mouth twice per day', 
            user_id = 3,
            prescriber_id = 1,
            medication_id = 2
            )
        p3 = Prescription (
            medication_name ='Eliquis', 
            instructions = 'Take one pill by mouth twice per day', 
            user_id = 3,
            prescriber_id = 1,
            medication_id = 3
            )
        p4 = Prescription (
            medication_name ='Benzonatate', 
            instructions = 'Take one pill by mouth every 6 hours as needed', 
            user_id = 4,
            prescriber_id = 4,
            medication_id = 4
            )
        p5 = Prescription (
            medication_name ='Famotadine', 
            instructions = 'Take one pill by mouth per day', 
            user_id = 5,
            prescriber_id = 3,
            medication_id = 5
            )
        
        prescriptions.extend([p1,p2,p3,p4,p5])

        db.session.add_all(prescriptions)
        db.session.commit()