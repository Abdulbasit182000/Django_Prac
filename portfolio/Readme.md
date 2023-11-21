- To use these Queries navigate to the `project` app

- Make sure to add all the dependencies of the project using:

       pip install -r requirements.txt

- Make Migration to file using:

        python manage.py makemigrations

- Now Migrate using:

        python manage.py migrate
         
- To Fill Database write: 500 is the number to rows to populate database

        py manage.py fill_db 500

- Now run the queries below and check the outputs.

- Retrieve all patients admitted on a specific date.

         Patient.objects.filter(date_admitted='2015-07-07')

- Get the names of all doctors who have patients with a specific diagnosis.

        Doctor.objects.filter(patients__records__diagnoses='Data cultural stop age kind gun meeting.').distinct().values_list('name', flat=True)

- Find all patients treated by a particular nurse.

        Patient.objects.prefetch_related('nurse').filter(nurse__name='Tony Davis')


- Retrieve the contact number of the doctor for a given patient.

        Doctor.objects.filter(patients__name='Annette Andrews').all().distinct().values_list('contact_number', flat=True)

- Get the total number of patients admitted to the hospital.

        Hospital.objects.count()

- Retrieve the names of nurses who have patients with a specific prescription.

        Nurse.objects.filter(patients__records__perscription='Myself experience allow pay popular remember.').values_list('name',flat=True)

- Get the average age of patients in the hospital.

        Hospital.objects.aggregate(Avg("age", default=0))

- Find the most recently admitted patient.

        Patient.objects.latest('date_admitted')

- Retrieve all doctors who have more than five patients.

        Doctor.objects.annotate(num_patients=Count('patients')).filter(num_patients__gt=5).values_list('name',flat=True)

- Get the number of patients assigned to each nurse.

        Nurse.objects.annotate(num_patients=Count('patients')).values_list('name','num_patients')

- Retrieve the names of patients who have a specific doctor.

        Patient.objects.filter(doctor__name='Eric Henry').values_list('name',flat=True)

- Find the doctors who specialize in a specific medical field.

        Doctor.objects.filter(specialization='Mental health nurse').distinct().values()

- Get the names of patients treated by a doctor with a specific specialization.

        Patient.objects.filter(doctor__specialization='Mental health nurse').values_list('name',flat=True)

- Find the nurses who have not been assigned any patients.

        Nurse.objects.annotate(num_patients=Count('patients')).filter(num_patients=0.).values_list('name',flat=True)

- Retrieve the latest medical record for a given patient.

        MedicalRecord.objects.filter(patient__name='Jacob Olsen').values().last()

- Get the names of patients with a specific diagnosis.

        Patient.objects.filter(records__diagnoses='Wife start down view black.').values_list('name',flat=True)

- Find the doctors who have patients of a certain age group.

        Doctor.objects.filter(patients__age__gt=20,patients__age__lt=50).distinct().values()

- Retrieve all patients with a specific prescription.

        Patient.objects.filter(records__perscription='Myself experience allow pay popular remember.').values()

- Find the nurses who have patients with a specific age.

        Nurse.objects.filter(patients__age=22).values()

- Get the total number of medical records in the system.

        MedicalRecord.objects.all().count()

- Retrieve the names of patients treated by a nurse with a specific contact number.

        Patient.objects.filter(nurse__contact_number='').distinct().values()

- Find the patients who are treated by more than one doctor.

        Patient.objects.annotate(num_doctors=Count('doctor')).filter(num_doctors__gt=1).values()

- Get the names of doctors who have treated patients with a specific prescription.

        Doctor.objects.filter(patients__records__perscription='Full network describe structure stage most. Employee vote community usually leave.').distinct().values_list('name',flat=True)

- Find the patients who have not been assigned to any doctor.

        Patient.objects.annotate(num_doctors=Count('doctor')).filter(num_doctors=0).values()

- Retrieve the doctors who have patients admitted on a specific date.

        Doctor.objects.filter(patients__date_admitted='2015-04-20').values()

- Find the patients with the highest age in the hospital.

        Hospital.objects.aggregate(Max("patient__age", default=0))

- Retrieve all nurses who have patients admitted on a specific date.

        Nurse.objects.filter(patients__date_admitted='2015-04-20').values()

- Find the doctors who have patients with a specific age.

        Doctor.objects.filter(patients__age=23).values()

- Get the number of patients treated by each doctor.

        Doctor.objects.annotate(num_patients=Count('patients')).values()

- Retrieve the names of patients with a specific age.

        Patient.objects.filter(age=30).values_list('name',flat=True)

- Find the nurses who have patients with a specific diagnosis.

        Nurse.objects.filter(patients__records__diagnoses='Wife start down view black.').values()

- Get the names of patients treated by a nurse with a specific contact number.

        Patient.objects.filter(nurse__contact_number='').values_list('name',flat=True)

- Find the doctors who have not been assigned any patients.

        Doctor.objects.annotate(num_patients=Count('patients')).filter(num_patients=0).values()
    
- Retrieve the patients who have medical records with a specific prescription.

        Patient.objects.filter(records__perscription='Full network describe structure stage most. Employee vote community usually leave.').distinct().values()

- Get the average age of patients treated by each doctor.

        Doctor.objects.annotate(avg_age=Avg('patients__age')).values()

- Find the doctors who have patients with a specific prescription.

        Doctor.objects.filter(patients__records__perscription='Full network describe structure stage most. Employee vote community usually leave.').distinct().values()

- Retrieve the names of patients treated by a doctor with a specific contact number.

        Patient.objects.filter(doctor__contact_number='').values_list('name',flat=True)

- Find the nurses who have patients with a specific prescription.

        Nurse.objects.filter(patients__records__perscription='Full network describe structure stage most. Employee vote community usually leave.').values()

- Retrieve the patients who have not been assigned to any nurse.

        Patient.objects.annotate(num_nurses=Count('nurse')).filter(num_nurses=0).values()

- Get the names of patients with a specific diagnosis treated by a specific doctor.

        Patient.objects.filter(records__diagnoses='Current significant law pay should inside stop important.',doctor__specialization='Primary school teacher').values_list('name',flat=True)

- Find the nurses who have patients with a specific age group.

        Nurse.objects.filter(patients__age__gt=20,patients__age__lt=50).distinct().values()
      
- Retrieve the doctors who have patients with a specific diagnosis and age group.

        Doctor.objects.filter(patients__age__gt=20,patients__age__lt=50,patients__records__diagnoses='Current significant law pay should inside stop important.').distinct().values()

- Retrieve all patients with the count of their medical records.

        Patient.objects.annotate(num_records=Count('records')).values()

- Get the average age of patients and annotate it to each patient instance.

        Patient.objects.annotate(avg_age=Avg('age')).values()

- Find the total number of patients admitted and annotate it to each doctor.

        Doctor.objects.annotate(num_patients=Count('patients')).values()

- Retrieve all doctors with the count of their assigned patients.

        Doctor.objects.annotate(num_patients=Count('patients')).values()

- Get the names of nurses with the total number of patients they have treated.

        Nurse.objects.annotate(num_patients=Count('patients')).values()

- Find the patients with the latest medical record date annotated to each patient.

        Patient.objects.annotate(Diagnoses=F('records__diagnoses')).annotate(Perscription=F('records__perscription')).values()

- Retrieve all doctors with the average age of their patients.

        Doctor.objects.annotate(avg_age=Avg('patients__age')).values()

- Get the total number of medical records and annotate it to each patient.

        Patient.objects.annotate(num_records=Count('records')).values()

- Find the nurses with the count of patients they have treated of a specific age group.

        Nurse.objects.filter(patients__age__gte=20, patients__age__lte=50).annotate(num_patients=Count('patients')).values()

- Retrieve all patients with the sum of their medical records ages.

        #medical record does not have age

- Get the names of doctors with the count of patients treated for a specific diagnosis.

        Doctor.objects.filter(patients__records__diagnoses='Current significant law pay should inside stop important.').annotate(num_patients=Count('patients')).values_list('name','num_patients')

- Find the nurses with the average age of their patients.

        Nurse.objects.annotate(avg_age_patient=Avg('patients__age')).values()

- Retrieve all patients with the earliest admission date annotated.

        #patients alreasdy have earliest date annotated

- Get the names of doctors with the total number of patients treated for a specific prescription.

        Doctor.objects.filter(patients__records__perscription='').annotate(num_patients=Count('patients')).values_list('name',flat=True)

- Find the nurses with the highest age of patients they have treated.

        Nurse.objects.annotate(hightest_patient_age=Max('patients__age'))

- Retrieve all patients with the count of doctors treating them.

        Patient.objects.annotate(num_doctors=Count('doctor')).values()

- Get the names of doctors with the count of patients admitted on a specific date.

        Doctor.objects.filter(patients__date_admitted='2015-04-20').annotate(num_patients=Count('patients')).values()

- Find the nurses with the total number of patients treated for a specific diagnosis.

        Nurse.objects.filter(patients__records__diagnoses='Current significant law pay should inside stop important.').annotate(num_patients=Count('patients')).values()

- Retrieve all patients with the total number of medical records and the average age.

        Patient.objects.annotate(num_records=Count('records')).annotate(avg_age=Avg('age')).values()

- Get the names of doctors with the count of patients treated for a specific age group.

        Doctor.objects.filter(patients__age__gte=20,patients__age__lte=50).annotate(num_patients=Count('patients')).values_list('name','num_patients')

- Find the nurses with the total number of patients assigned to them.

        Nurse.objects.annotate(num_patients=Count('patients')).values()

- Retrieve all patients with the count of nurses assigned to them.

        Patient.objects.annotate(num_nurses=Count('nurse')).values()

- Get the names of doctors with the average age of patients treated for a specific prescription.

        Doctor.objects.filter(patients__records__perscription='Full network describe structure stage most. Employee vote community usually leave.').annotate(avg_age=Avg('patients__age')).values_list('name','avg_age')

- Find the nurses with the count of patients treated for a specific prescription.

        Nurse.objects.filter(patients__records__perscription='Full network describe structure stage most. Employee vote community usually leave.').annotate(num_patients=Count('patients')).values()

- Retrieve all patients with the total number of nurses treating them.

        Patient.objects.annotate(num_nurses=Count('nurse')).values()

- Get the names of doctors with the highest age of patients treated.

        Doctor.objects.annotate(max_patient_age=Max('patients__age')).values_list('name','max_patient_age')

- Find the nurses with the total number of patients admitted on a specific date.

        Nurse.objects.filter(patients__date_admitted='2015-04-20').annotate(num_patients=Count('patients')).values()

- Retrieve all patients with the count of medical records for a specific prescription.

        Patient.objects.filter(records__perscription='Full network describe structure stage most. Employee vote community usually leave.').values()
- Get the names of doctors with the total number of patients treated for a specific age group and diagnosis.

        Doctor.objects.filter(patients__age__gt=20,patients__age__lt=50,patients__records__persciption='Current significant law pay should inside stop important.').distinct().values_list('name',flat=True)

- Find the nurses with the average age of patients treated for a specific prescription.

        Nurse.objects.filter(patients__records__perscription='Full network describe structure stage most. Employee vote community usually leave.').annotate(avg_age_patients=Avg('patients__age')).values()

- Retrieve all patients with the sum of ages and count of medical records for a specific prescription.

        Patient.objects.filter(records__perscription='Full network describe structure stage most. Employee vote community usually leave.').annotate(num_reccords=Count('records')).annotate(num_age=Sum('age')).values()

- Get the names of doctors with the count of patients treated for a specific age group and diagnosis.

        Doctor.objects.filter(patients__age__gte=20,patients__age__lte=50,patients__records__diagnoses='Current significant law pay should inside stop important.').annotate(num_patients=Count('patients')).values_list('name','num_patients')

- Find the nurses with the total number of patients treated for a specific age group and diagnosis.

        Nurse.objects.filter(patients__age__gte=20,patients__age__lte=50,patients__records__diagnoses='Current significant law pay should inside stop important.').annotate(num_patients=Count('patients')).values()

- Retrieve all patients with the total number of nurses treating them for a specific prescription.

        Patient.objects.filter(records__perscription='Full network describe structure stage most. Employee vote community usually leave.').annotate(num_nurses=Count('nurse')).values()

- Get the names of doctors with the count of patients treated for a specific age group, diagnosis, and prescription.

        Doctor.objects.filter(patients__age__gte=20,patients__age__lte=50,patients__records__diagnoses='Current significant law pay should inside stop important.',patients__records__perscription='Full network describe structure stage most. Employee vote community usually leave.').annotate(num_patients=Count('patients')).values_list('name','num_patients')

- Find the nurses with the average age of patients treated for a specific age group and diagnosis.

        Nurse.objects.filter(patients__age__gte=20,patients__age__lte=50,patients__records__diagnoses='Current significant law pay should inside stop important.').annotate(avg_patient_age=Avg('patients__age')).values()

- Retrieve all patients with the total number of medical records, average age, and count of nurses for a specific prescription.

        Patient.objects.filter(records__perscription='Full network describe structure stage most. Employee vote community usually leave.').annotate(num_records=Count('records')).annotate(num_nurses=Count('nurse')).annotate(avg_age=Avg('age')).values()

- Get the names of doctors with the count of patients treated for a specific age group, diagnosis, and prescription.

        Doctor.objects.filter(patients__age__gte=20,patients__age__lte=50,patients__records__diagnoses='Current significant law pay should inside stop important.',patients__records__perscription='Full network describe structure stage most. Employee vote community usually leave.').annotate(num_patients=Count('patients')).values_list('name','num_patients')

- Find the nurses with the total number of patients treated for a specific age group, diagnosis, and prescription.

        Nurse.objects.filter(patients__age__gte=20,patients__age__lte=50,patients__records__diagnoses='Current significant law pay should inside stop important.',patients__records__perscription='Full network describe structure stage most. Employee vote community usually leave.').annotate(num_patients=Count('patients')).values()

- Retrieve all patients with the sum of ages and count of medical records for a specific age group, diagnosis, and prescription.

        Patient.objects.filter(age__gte=20,age__lte=50,records__diagnoses='Current significant law pay should inside stop important.',records__perscription='Full network describe structure stage most. Employee vote community usually leave.').annotate(num_records=Count('records')).annotate(sum_ages=Sum('age'))

- Get the names of doctors with the count of patients treated for a specific age group, diagnosis, prescription, and admission date.

        Doctor.objects.filter(patients__age__gte=20,patients__age__lte=50,patients__records__diagnoses='Current significant law pay should inside stop important.',patients__records__perscription='Full network describe structure stage most. Employee vote community usually leave.',patients__date_admitted='2015-04-20').annotate(num_patients=Count('patients')).values_list('name','num_patients')

- Find the nurses with the average age of patients treated for a specific age group, diagnosis, prescription, and admission date.

        Nurse.objects.filter(patients__age__gte=20,patients__age__lte=50,patients__records__diagnoses='Current significant law pay should inside stop important.',patients__records__perscription='Full network describe structure stage most. Employee vote community usually leave.',patients__date_admitted='2015-04-20').annotate(num_patients=Avg('patients__age')).values()

- Retrieve all patients with the total number of medical records, average age, and count of nurses for a specific age group, diagnosis, and prescription.

        Patient.objects.filter(age__gte=20,age__lte=50,records__diagnoses='Current significant law pay should inside stop important.',records__perscription='Full network describe structure stage most. Employee vote community usually leave.').annotate(num_records=Count('records')).annotate(avg_age=Sum('age')).annotate(num_nurses=Count('nurse'))

- Get the names of doctors with the count of patients treated for a specific age group, diagnosis, prescription, and admission date.

        Doctor.objects.filter(patients__age__gte=20,patients__age__lte=50,patients__records__diagnoses='Current significant law pay should inside stop important.',patients__records__perscription='Full network describe structure stage most. Employee vote community usually leave.',patients__date_admitted='2015-04-20').annotate(num_patients=Count('patients')).values_list('name','num_patients')

- Find the nurses with the total number of patients treated for a specific age group, diagnosis, prescription, and admission date.

        Nurse.objects.filter(patients__age__gte=20,patients__age__lte=50,patients__records__diagnoses='Current significant law pay should inside stop important.',patients__records__perscription='Full network describe structure stage most. Employee vote community usually leave.',patients__date_admitted='2015-04-20').annotate(num_patients=Count('patients')).values()

- Retrieve all patients with the sum of ages and count of medical records for a specific age group, diagnosis, prescription, and admission date.

        Patient.objects.filter(age__gte=20,age__lte=50,records__diagnoses='Current significant law pay should inside stop important.',records__perscription='Full network describe structure stage most. Employee vote community usually leave.',date_admitted='2015-04-20').annotate(num_records=Count('records')).annotate(total_age=Sum('age')).annotate(num_records=Count('records'))

- Get the names of doctors with the count of patients treated for a specific age group, diagnosis, prescription, admission date, and specialization.

        Doctor.objects.filter(patients__age__gte=20,patients__age__lte=50,patients__records__diagnoses='Current significant law pay should inside stop important.',patients__records__perscription='Full network describe structure stage most. Employee vote community usually leave.',patients__date_admitted='2015-04-20',specialization='Mental Health Nurse').annotate(num_patients=Count('patients')).values_list('name','num_patients')

- Find the nurses with the average age of patients treated for a specific age group, diagnosis, prescription, admission date, and specialization.

        Nurse.objects.filter(patients__age__gte=20,patients__age__lte=50,patients__records__diagnoses='Current significant law pay should inside stop important.',patients__records__perscription='Full network describe structure stage most. Employee vote community usually leave.',patients__date_admitted='2015-04-20',patients__doctor__specialization='Mental Health Nurse').annotate(avg_age=Count('patients__age')).values()

- Retrieve all patients with the total number of medical records, average age, and count of nurses for a specific age group, diagnosis, prescription, admission date, and specialization.

        Patient.objects.filter(age__gte=20,age__lte=50,records__diagnoses='Current significant law pay should inside stop important.',records__perscription='Full network describe structure stage most. Employee vote community usually leave.',date_admitted='2015-04-20',doctor_specialization='Mental Health Nurse').annotate(num_records=Count('records')).annotate(AVG_AGE=Sum('age')).annotate(num_records=Count('nurse'))

- Get the names of doctors with the count of patients treated for a specific age group, diagnosis, prescription, admission date, and specialization.

        Doctor.objects.filter(patients__age__gte=20,patients__age__lte=50,patients__records__diagnoses='Current significant law pay should inside stop important.',patients__records__perscription='Full network describe structure stage most. Employee vote community usually leave.',patients__date_admitted='2015-04-20',specialization='Mental Health Nurse').annotate(num_patients=Count('patients')).values_list('name','num_patients')
