-To run Querysets uses the 'project' app.

-To Fill Database write: 500 is the number to rows to populate database

        py manage.py Fill_DB 500

- Retrieve all patients admitted on a specific date.

         Patient.objects.filter(date_admitted='2015-07-07')

- Get the names of all doctors who have patients with a specific diagnosis.

        Doctor.objects.filter(doctor_of__Medical_Records__diagnoses='Data cultural stop age kind gun meeting.').distinct().values_list('name', flat=True)

- Find all patients treated by a particular nurse.

        Patient.objects.prefetch_related('nurse').filter(nurse__name='Tony Davis')


- Retrieve the contact number of the doctor for a given patient.

        Doctor.objects.filter(doctor_of__name='Annette Andrews').all().distinct().values_list('contact_number', flat=True)

- Get the total number of patients admitted to the hospital.

        Patient.objects.count()

- Retrieve the names of nurses who have patients with a specific prescription.

        Nurse.objects.filter(Patients__Medical_Records__perscription='Myself experience allow pay popular remember.').values_list('name',flat=True)

- Get the average age of patients in the hospital.

        Patient.objects.aggregate(Avg("age", default=0))

- Find the most recently admitted patient.

        Patient.objects.latest('date_admitted')

- Retrieve all doctors who have more than five patients.

        Doctor.objects.annotate(num_patients=Count('doctor_of')).filter(num_patients__gt=5).values_list('name',flat=True)

- Get the number of patients assigned to each nurse.

        Nurse.objects.annotate(num_patients=Count('Patients')).values_list('name','num_patients')

- Retrieve the names of patients who have a specific doctor.

        Patient.objects.filter(doctor__name='Eric Henry').values_list('name',flat=True)

- Find the doctors who specialize in a specific medical field.

        Doctor.objects.filter(specialization='Mental health nurse').distinct().values()

- Get the names of patients treated by a doctor with a specific specialization.

        Patient.objects.filter(doctor__specialization='Mental health nurse').values_list('name',flat=True)

- Find the nurses who have not been assigned any patients.

        Nurse.objects.annotate(num_patients=Count('Patients')).filter(num_patients=0.).values_list('name',flat=True)

- Retrieve the latest medical record for a given patient.

        MedicalRecord.objects.filter(patient__name='Jacob Olsen').values().last()

- Get the names of patients with a specific diagnosis.

        Patient.objects.filter(Medical_Records__diagnoses='Wife start down view black.').values_list('name',flat=True)

- Find the doctors who have patients of a certain age group.

        Doctor.objects.filter(doctor_of__age__gt=20,doctor_of__age__lt=50).distinct().values()

- Retrieve all patients with a specific prescription.

        Patient.objects.filter(Medical_Records__perscription='Myself experience allow pay popular remember.').values()

- Find the nurses who have patients with a specific age.

        Nurse.objects.filter(Patients__age=22).values()

- Get the total number of medical records in the system.

        MedicalRecord.objects.all().count()

- Retrieve the names of patients treated by a nurse with a specific contact number.

        Patient.objects.filter(nurse__contact_number='').distinct().values()

- Find the patients who are treated by more than one doctor.

        Patient.objects.annotate(num_doctors=Count('doctor')).filter(num_doctors__gt=1).values()

- Get the names of doctors who have treated patients with a specific prescription.

        Doctor.objects.filter(doctor_of__Medical_Records__perscription='Full network describe structure stage most. Employee vote community usually leave.').distinct().values_list('name',flat=True)

- Find the patients who have not been assigned to any doctor.

        Patient.objects.annotate(num_doctors=Count('doctor')).filter(num_doctors=0).values()

- Retrieve the doctors who have patients admitted on a specific date.

        Doctor.objects.filter(doctor_of__date_admitted='2015-04-20').values()

- Find the patients with the highest age in the hospital.

        Patient.objects.aggregate(Max("age", default=0))

- Retrieve all nurses who have patients admitted on a specific date.

        Nurse.objects.filter(Patients__date_admitted='2015-04-20').values()

- Find the doctors who have patients with a specific age.

        Doctor.objects.filter(doctor_of__age=23).values()

- Get the number of patients treated by each doctor.

        Doctor.objects.annotate(num_patients=Count('doctor_of')).values()

- Retrieve the names of patients with a specific age.

        Patient.objects.filter(age=30).values_list('name',flat=True)

- Find the nurses who have patients with a specific diagnosis.

        Nurse.objects.filter(Patients__Medical_Records__diagnoses='Wife start down view black.').values()

- Get the names of patients treated by a nurse with a specific contact number.

        Patient.objects.filter(nurse__contact_number='').values_list('name',flat=True)

- Find the doctors who have not been assigned any patients.

        Doctor.objects.annotate(num_patients=Count('doctor_of')).filter(num_patients=0).values()
    
- Retrieve the patients who have medical records with a specific prescription.

        Patient.objects.filter(Medical_Records__perscription='Full network describe structure stage most. Employee vote community usually leave.').distinct().values()

- Get the average age of patients treated by each doctor.

        Doctor.objects.annotate(avg_age=Avg('doctor_of__age')).values()

- Find the doctors who have patients with a specific prescription.

        Doctor.objects.filter(doctor_of__Medical_Records__perscription='Full network describe structure stage most. Employee vote community usually leave.').distinct().values()

- Retrieve the names of patients treated by a doctor with a specific contact number.

        Patient.objects.filter(doctor__contact_number='').values_list('name',flat=True)

- Find the nurses who have patients with a specific prescription.

        Nurse.objects.filter(Patients__Medical_Records__perscription='Full network describe structure stage most. Employee vote community usually leave.').values()

- Retrieve the patients who have not been assigned to any nurse.

        Patient.objects.annotate(num_nurses=Count('nurse')).filter(num_nurses=0).values()

- Get the names of patients with a specific diagnosis treated by a specific doctor.

        Patient.objects.filter(Medical_Records__diagnoses='Current significant law pay should inside stop important.',doctor__specialization='Primary school teacher').values_list('name',flat=True)

- Find the nurses who have patients with a specific age group.

        Nurse.objects.filter(Patients__age__gt=20,Patients__age__lt=50).distinct().values()
      
- Retrieve the doctors who have patients with a specific diagnosis and age group.

        Doctor.objects.filter(doctor_of__age__gt=20,doctor_of__age__lt=50,doctor_of__Medical_Records__diagnoses='Current significant law pay should inside stop important.').distinct().values()

1. Retrieve all patients with the count of their medical records.

    Patient.objects.annotate(num_records=Count('Medical_Records')).values()

2. Get the average age of patients and annotate it to each patient instance.

        Patient.objects.annotate(avg_age=Avg('age')).values()

3. Find the total number of patients admitted and annotate it to each doctor.

        Doctor.objects.annotate(num_patients=Count('doctor_of')).values()

4. Retrieve all doctors with the count of their assigned patients.

        Doctor.objects.annotate(num_patients=Count('doctor_of')).values()

5. Get the names of nurses with the total number of patients they have treated.

        Nurse.objects.annotate(num_patients=Count('Patients')).values()

6. Find the patients with the latest medical record date annotated to each patient.

        Patient.objects.annotate(Diagnoses=F('Medical_Records__diagnoses')).annotate(Perscription=F('Medical_Records__perscription')).values()

7. Retrieve all doctors with the average age of their patients.

        Doctor.objects.annotate(avg_age=Avg('doctor_of__age')).values()

8. Get the total number of medical records and annotate it to each patient.

        Patient.objects.annotate(num_records=Count('Medical_Records')).values()

9. Find the nurses with the count of patients they have treated of a specific age group.

        Nurse.objects.filter(Patients__age__gte=20,Patients__age__lte=50).annotate(num_patients=Count('Patients')).values()

10. Retrieve all patients with the sum of their medical records ages.

        #medical record does not have age

11. Get the names of doctors with the count of patients treated for a specific diagnosis.

        Doctor.objects.filter(doctor_of__Medical_Records__diagnoses='Current significant law pay should inside stop important.').annotate(num_patients=Count('doctor_of')).values_list('name','num_patients')

12. Find the nurses with the average age of their patients.

        Nurse.objects.annotate(avg_age_patient=Avg('Patients__age')).values()

13. Retrieve all patients with the earliest admission date annotated.

        #Patients alreasdy have earliest date annotated

14. Get the names of doctors with the total number of patients treated for a specific prescription.

        Doctor.objects.filter(doctor_of__Medical_Records__perscription='').annotate(num_patients=Count('doctor_of')).values_list('name',flat=True)

15. Find the nurses with the highest age of patients they have treated.

        Nurse.objects.annotate(hightest_patient_age=Max('Patients__age'))

16. Retrieve all patients with the count of doctors treating them.

        Patient.objects.annotate(num_doctors=Count('doctor')).values()

17. Get the names of doctors with the count of patients admitted on a specific date.

        Doctor.objects.filter(doctor_of__date_admitted='2015-04-20').annotate(num_patients=Count('doctor_of')).values()

18. Find the nurses with the total number of patients treated for a specific diagnosis.

        Nurse.objects.filter(Patients__Medical_Records__diagnoses='Current significant law pay should inside stop important.').annotate(num_patients=Count('Patients')).values()

19. Retrieve all patients with the total number of medical records and the average age.

        Patient.objects.annotate(num_records=Count('Medical_Records')).annotate(avg_age=Avg('age')).values()

20. Get the names of doctors with the count of patients treated for a specific age group.

        Doctor.objects.filter(doctor_of__age__gte=20,doctor_of__age__lte=50).annotate(num_patients=Count('doctor_of')).values_list('name','num_patients')

21. Find the nurses with the total number of patients assigned to them.

        Nurse.objects.annotate(num_patients=Count('Patients')).values()

22. Retrieve all patients with the count of nurses assigned to them.

        Patient.objects.annotate(num_nurses=Count('nurse')).values()

23. Get the names of doctors with the average age of patients treated for a specific prescription.

        Doctor.objects.filter(doctor_of__Medical_Records__perscription='Full network describe structure stage most. Employee vote community usually leave.').annotate(avg_age=Avg('doctor_of__age')).values_list('name','avg_age')

24. Find the nurses with the count of patients treated for a specific prescription.

        Nurse.objects.filter(Patients__Medical_Records__perscription='Full network describe structure stage most. Employee vote community usually leave.').annotate(num_patients=Count('Patients')).values()

25. Retrieve all patients with the total number of nurses treating them.

        Patient.objects.annotate(num_nurses=Count('nurse')).values()

26. Get the names of doctors with the highest age of patients treated.

        Doctor.objects.annotate(max_patient_age=Max('doctor_of__age')).values_list('name','max_patient_age')

27. Find the nurses with the total number of patients admitted on a specific date.

        Nurse.objects.filter(Patients__date_admitted='2015-04-20').annotate(num_patients=Count('Patients')).values()

28. Retrieve all patients with the count of medical records for a specific prescription.

        Patient.objects.filter(Medical_Records__perscription='Full network describe structure stage most. Employee vote community usually leave.').values()
29. Get the names of doctors with the total number of patients treated for a specific age group and diagnosis.

        Doctor.objects.filter(doctor_of__age__gt=20,doctor_of__age__lt=50,doctor_of__Medical_Records__persciption='Current significant law pay should inside stop important.').distinct().values_list('name',flat=True)

30. Find the nurses with the average age of patients treated for a specific prescription.

        Nurse.objects.filter(Patients__Medical_Records__perscription='Full network describe structure stage most. Employee vote community usually leave.').annotate(avg_age_patients=Avg('Patients__age')).values()

31. Retrieve all patients with the sum of ages and count of medical records for a specific prescription.

        Patient.objects.filter(Medical_Records__perscription='Full network describe structure stage most. Employee vote community usually leave.').annotate(num_reccords=Count('Medical_Records')).annotate(num_age=Sum('age')).values()

32. Get the names of doctors with the count of patients treated for a specific age group and diagnosis.

        Doctor.objects.filter(doctor_of__age__gte=20,doctor_of__age__lte=50,doctor_of__Medical_Records__diagnoses='Current significant law pay should inside stop important.').annotate(num_patients=Count('doctor_of')).values_list('name','num_patients')

33. Find the nurses with the total number of patients treated for a specific age group and diagnosis.

        Nurse.objects.filter(Patients__age__gte=20,Patients__age__lte=50,Patients__Medical_Records__diagnoses='Current significant law pay should inside stop important.').annotate(num_patients=Count('Patients')).values()

34. Retrieve all patients with the total number of nurses treating them for a specific prescription.

        Patient.objects.filter(Medical_Records__perscription='Full network describe structure stage most. Employee vote community usually leave.').annotate(num_nurses=Count('nurse')).values()

35. Get the names of doctors with the count of patients treated for a specific age group, diagnosis, and prescription.

        Doctor.objects.filter(doctor_of__age__gte=20,doctor_of__age__lte=50,doctor_of__Medical_Records__diagnoses='Current significant law pay should inside stop important.',doctor_of__Medical_Records__perscription='Full network describe structure stage most. Employee vote community usually leave.').annotate(num_patients=Count('doctor_of')).values_list('name','num_patients')

36. Find the nurses with the average age of patients treated for a specific age group and diagnosis.

        Nurse.objects.filter(Patients__age__gte=20,Patients__age__lte=50,Patients__Medical_Records__diagnoses='Current significant law pay should inside stop important.').annotate(avg_patient_age=Avg('Patients__age')).values()

37. Retrieve all patients with the total number of medical records, average age, and count of nurses for a specific prescription.

        Patient.objects.filter(Medical_Records__perscription='Full network describe structure stage most. Employee vote community usually leave.').annotate(num_records=Count('Medical_Records')).annotate(num_nurses=Count('nurse')).annotate(avg_age=Avg('age')).values()

38. Get the names of doctors with the count of patients treated for a specific age group, diagnosis, and prescription.

        Doctor.objects.filter(doctor_of__age__gte=20,doctor_of__age__lte=50,doctor_of__Medical_Records__diagnoses='Current significant law pay should inside stop important.',doctor_of__Medical_Records__perscription='Full network describe structure stage most. Employee vote community usually leave.').annotate(num_patients=Count('doctor_of')).values_list('name','num_patients')

39. Find the nurses with the total number of patients treated for a specific age group, diagnosis, and prescription.

        Nurse.objects.filter(Patients__age__gte=20,Patients__age__lte=50,Patients__Medical_Records__diagnoses='Current significant law pay should inside stop important.',Patients__Medical_Records__perscription='Full network describe structure stage most. Employee vote community usually leave.').annotate(num_patients=Count('Patients')).values()

40. Retrieve all patients with the sum of ages and count of medical records for a specific age group, diagnosis, and prescription.

        Patient.objects.filter(age__gte=20,age__lte=50,Medical_Records__diagnoses='Current significant law pay should inside stop important.',Medical_Records__perscription='Full network describe structure stage most. Employee vote community usually leave.').annotate(num_records=Count('Medical_Records')).annotate(sum_ages=Sum('age'))

41. Get the names of doctors with the count of patients treated for a specific age group, diagnosis, prescription, and admission date.

        Doctor.objects.filter(doctor_of__age__gte=20,doctor_of__age__lte=50,doctor_of__Medical_Records__diagnoses='Current significant law pay should inside stop important.',doctor_of__Medical_Records__perscription='Full network describe structure stage most. Employee vote community usually leave.',doctor_of__date_admitted='2015-04-20').annotate(num_patients=Count('doctor_of')).values_list('name','num_patients')

42. Find the nurses with the average age of patients treated for a specific age group, diagnosis, prescription, and admission date.

        Nurse.objects.filter(Patients__age__gte=20,Patients__age__lte=50,Patients__Medical_Records__diagnoses='Current significant law pay should inside stop important.',Patients__Medical_Records__perscription='Full network describe structure stage most. Employee vote community usually leave.',Patients__date_admitted='2015-04-20').annotate(num_patients=Avg('Patients__age')).values()

43. Retrieve all patients with the total number of medical records, average age, and count of nurses for a specific age group, diagnosis, and prescription.

        Patient.objects.filter(age__gte=20,age__lte=50,Medical_Records__diagnoses='Current significant law pay should inside stop important.',Medical_Records__perscription='Full network describe structure stage most. Employee vote community usually leave.').annotate(num_records=Count('Medical_Records')).annotate(avg_age=Sum('age')).annotate(num_nurses=Count('nurse'))

44. Get the names of doctors with the count of patients treated for a specific age group, diagnosis, prescription, and admission date.

        Doctor.objects.filter(doctor_of__age__gte=20,doctor_of__age__lte=50,doctor_of__Medical_Records__diagnoses='Current significant law pay should inside stop important.',doctor_of__Medical_Records__perscription='Full network describe structure stage most. Employee vote community usually leave.',doctor_of__date_admitted='2015-04-20').annotate(num_patients=Count('doctor_of')).values_list('name','num_patients')

45. Find the nurses with the total number of patients treated for a specific age group, diagnosis, prescription, and admission date.

        Nurse.objects.filter(Patients__age__gte=20,Patients__age__lte=50,Patients__Medical_Records__diagnoses='Current significant law pay should inside stop important.',Patients__Medical_Records__perscription='Full network describe structure stage most. Employee vote community usually leave.',Patients__date_admitted='2015-04-20').annotate(num_patients=Count('Patients')).values()

46. Retrieve all patients with the sum of ages and count of medical records for a specific age group, diagnosis, prescription, and admission date.

        Patient.objects.filter(age__gte=20,age__lte=50,Medical_Records__diagnoses='Current significant law pay should inside stop important.',Medical_Records__perscription='Full network describe structure stage most. Employee vote community usually leave.',date_admitted='2015-04-20').annotate(num_records=Count('Medical_Records')).annotate(total_age=Sum('age')).annotate(num_records=Count('Medical_Records'))

47. Get the names of doctors with the count of patients treated for a specific age group, diagnosis, prescription, admission date, and specialization.

        Doctor.objects.filter(doctor_of__age__gte=20,doctor_of__age__lte=50,doctor_of__Medical_Records__diagnoses='Current significant law pay should inside stop important.',doctor_of__Medical_Records__perscription='Full network describe structure stage most. Employee vote community usually leave.',doctor_of__date_admitted='2015-04-20',specialization='Mental Health Nurse').annotate(num_patients=Count('doctor_of')).values_list('name','num_patients')

48. Find the nurses with the average age of patients treated for a specific age group, diagnosis, prescription, admission date, and specialization.

        Nurse.objects.filter(Patients__age__gte=20,Patients__age__lte=50,Patients__Medical_Records__diagnoses='Current significant law pay should inside stop important.',Patients__Medical_Records__perscription='Full network describe structure stage most. Employee vote community usually leave.',Patients__date_admitted='2015-04-20',Patients__doctor__specialization='Mental Health Nurse').annotate(avg_age=Count('Patients__age')).values()

49. Retrieve all patients with the total number of medical records, average age, and count of nurses for a specific age group, diagnosis, prescription, admission date, and specialization.

        Patient.objects.filter(age__gte=20,age__lte=50,Medical_Records__diagnoses='Current significant law pay should inside stop important.',Medical_Records__perscription='Full network describe structure stage most. Employee vote community usually leave.',date_admitted='2015-04-20',doctor_specialization='Mental Health Nurse').annotate(num_records=Count('Medical_Records')).annotate(AVG_AGE=Sum('age')).annotate(num_records=Count('nurse'))

50. Get the names of doctors with the count of patients treated for a specific age group, diagnosis, prescription, admission date, and specialization.

        Doctor.objects.filter(doctor_of__age__gte=20,doctor_of__age__lte=50,doctor_of__Medical_Records__diagnoses='Current significant law pay should inside stop important.',doctor_of__Medical_Records__perscription='Full network describe structure stage most. Employee vote community usually leave.',doctor_of__date_admitted='2015-04-20',specialization='Mental Health Nurse').annotate(num_patients=Count('doctor_of')).values_list('name','num_patients')
