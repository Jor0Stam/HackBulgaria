list_all_patients = '''
SELECT *
FROM PATIENTS'''

list_all_doctors = '''
SELECT *
FROM DOCTORS'''

add_new_patient = '''
INSERT
INTO PATIENTS
VALUES (?, ?, ?, ?, ?)'''

add_new_doctor = '''
INSERT
INTO DOCTORS
VALUES (?, ?)
'''

add_hospital_stay = '''
INSERT
INTO HOSPITAL_STAY
VALUES (?, ?, ?, ?, ?)
'''

update_patient = '''
UPDATE PATIENTS
SET FIRSTNAME = ?, LASTNAME = ?, AGE = ?, GENDER = ?,  DOCTOR = ?
WHERE id = ?
'''

update_doctor = '''
UPDATE DOCTORS
SET FIRSTNAME = ?, LASTNAME = ?
WHERE id = ?
'''

update_hospital_stay = '''
UPDATE HOSPITAL_STAY
SET ROOM = ?, STARTDATE = ?, ENDDATE = ?, INJURY = ?, PATIENT = ?
WHERE id = ?
'''

delete_patient = '''
DELETE
FROM PATIENTS
WHERE ID = ?
'''

delete_doctor = '''
DELETE
FROM DOCTORS
WHERE ID = ?
'''

delete_hospital_stay = '''
DELETE
FROM HOSPITAL_STAY
WHERE ID = ?'''

list_patients_of_doctor = '''
SELECT *
FROM PATIENTS
WHERE DOCTOR = ?'''

patients_with_injury = '''
SELECT *
FROM PATIENTS
WHERE INJURY = ?'''


# list all doctors and the diseases they treat

# show all patients from startdate_1 to startdate_2
