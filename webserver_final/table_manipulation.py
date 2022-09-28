
mysql = None

def sql_query(query):
    with mysql.connection.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

def query_table_to_list(table, column):
    query = ("SELECT %s FROM %s;" % (column, table)).replace('$.', '%s.' % table)
    result = sql_query(query)
    return [list(row.values())[0] for row in result]

tables = (
    'Credentials',
    'Diagnoses',
    'MedicalCategories',
    'MedicationClasses',
    'MedicationRoutes',
    'Medications',
    'Nurses',
    'Patients',
    'Prescriptions',
    'Providers',
    'TestTypes',
    'Tests',
    'Visits',
    'VisitDiagnoses',
    'VisitTestResults',
    'VisitPrescriptions',
    'VisitMedications',
)

def get_sql_input_fields(table):
    if table in ['Credentials', 'MedicalCategories', 'MedicationClasses', 'MedicationRoutes', 'TestTypes']:
        return {
            'Credentials': [
                {'label': 'Credential', 'name': 'credential_input', 'type': 'text'},
            ],
            'MedicalCategories': [
                {'label': 'Medical Category', 'name': 'medical_category_input', 'type': 'text'},
            ],
            'MedicationClasses': [
                {'label': 'Medication Class', 'name': 'medication_class_input', 'type': 'text'},
            ],
            'MedicationRoutes': [
                {'label': 'Medication Route', 'name': 'medication_route_input', 'type': 'text'},
            ],
            'TestTypes': [
                {'label': 'type', 'name': 'type_input', 'type': 'text'},
            ],
        }[table]
    else:
        return {
            'Diagnoses': lambda:[
                {'label': 'Name', 'name': 'name_input', 'type': 'text'},
                {
                    'label': 'Medical Category',
                    'name': 'medical_category_id_input',
                    'type': 'dropdown',
                    'options': query_table_to_list('MedicalCategories', '$.category')
                },
            ],
            'Medications': lambda:[
                {'label': 'Name', 'name': 'name_input', 'type': 'text'},
                {'label': 'Standard dose', 'name': 'standard_dose_input', 'type': 'text'},
                {'label': 'Medication route', 'name': 'medication_route_id_input', 'type': 'dropdown', 'options': query_table_to_list('MedicationRoutes', '$.route')},
                {'label': 'Medication class', 'name': 'medication_class_id_input', 'type': 'dropdown', 'options': query_table_to_list('MedicationClasses', '$.class')},
            ],
            'Prescriptions': lambda:[
                {'label': 'Name', 'name': 'name_input', 'type': 'text'},
                {'label': 'Standard dose', 'name': 'standard_dose_input', 'type': 'text'},
                {'label': 'Medication route', 'name': 'medication_route_id_input', 'type': 'dropdown', 'options': query_table_to_list('MedicationRoutes', '$.route')},
                {'label': 'Medication class', 'name': 'medication_class_id_input', 'type': 'dropdown', 'options': query_table_to_list('MedicationClasses', '$.class')},
            ],
            'Nurses': lambda:[
                {'label': 'First name', 'name': 'first_name_input', 'type': 'text'},
                {'label': 'Last name', 'name': 'last_name_input', 'type': 'text'},
                {'label': 'Credential', 'name': 'credential_input', 'type': 'dropdown', 'options': query_table_to_list('Credentials', '$.credential')},
                {'label': 'DOB', 'name': 'date_of_birth_input', 'type': 'date'},
                {'label': 'Gender', 'name': 'gender_input', 'type': 'text'},
                {'label': 'Address', 'name': 'address_input', 'type': 'text'},
                {'label': 'Zip code', 'name': 'zip_code_input', 'type': 'text'},
                {'label': 'Phone number', 'name': 'phone_number_input', 'type': 'text'},
                {'label': 'Email', 'name': 'email_input', 'type': 'text'}
            ],
            'Patients': lambda:[
                {'label': 'First name', 'name': 'first_name_input', 'type': 'text'},
                {'label': 'Last name', 'name': 'last_name_input', 'type': 'text'},
                {'label': 'DOB', 'name': 'date_of_birth_input', 'type': 'date'},
                {'label': 'Gender', 'name': 'gender_input', 'type': 'text'},
                {'label': 'Address', 'name': 'address_input', 'type': 'text'},
                {'label': 'Zip code', 'name': 'zip_code_input', 'type': 'text'},
                {'label': 'Phone number', 'name': 'phone_number_input', 'type': 'text'},
                {'label': 'Email', 'name': 'email_input', 'type': 'text'},
                {'label': 'Provider', 'name': 'provider_name_input', 'type': 'dropdown', 'options': ['None'] + query_table_to_list('Providers', 'CONCAT($.first_name, \' \', $.last_name)')},
            ],
            'Providers': lambda:[
                {'label': 'First name', 'name': 'first_name_input', 'type': 'text'},
                {'label': 'Last name', 'name': 'last_name_input', 'type': 'text'},
                {'label': 'Credential', 'name': 'credential_input', 'type': 'dropdown', 'options': query_table_to_list('Credentials', '$.credential')},
                {'label': 'DOB', 'name': 'date_of_birth_input', 'type': 'date'},
                {'label': 'Gender', 'name': 'gender_input', 'type': 'text'},
                {'label': 'Address', 'name': 'address_input', 'type': 'text'},
                {'label': 'Zip code', 'name': 'zip_code_input', 'type': 'text'},
                {'label': 'Phone number', 'name': 'phone_number_input', 'type': 'text'},
                {'label': 'Email', 'name': 'email_input', 'type': 'text'}
            ],
            'Tests': lambda:[
                {'label': 'name', 'name': 'name_input', 'type': 'text'},
                {'label': 'type', 'name': 'type_id_input', 'type': 'dropdown', 'options': query_table_to_list('TestTypes', '$.type')},
            ],
            'Visits': lambda:[
                {'label': 'Date', 'name': 'date_input', 'type': 'date'},
                {'label': 'Reason for visit', 'name': 'reason_for_visit_input', 'type': 'textarea'},
                {'label': 'Patient', 'name': 'patient_name_input', 'type': 'dropdown', 'options': query_table_to_list('Patients', 'CONCAT($.first_name, \' \', $.last_name)')},
                {'label': 'Provider', 'name': 'provider_name_input', 'type': 'dropdown', 'options': query_table_to_list('Providers', 'CONCAT($.first_name, \' \', $.last_name)')},
                {'label': 'Nurse', 'name': 'nurse_name_input', 'type': 'dropdown', 'options': query_table_to_list('Nurses', 'CONCAT($.first_name, \' \', $.last_name)')},
            ],
            'VisitDiagnoses': lambda:[
                {'label': 'Visit', 'name': 'visit_id_input', 'type': 'dropdown', 'options': query_table_to_list('Visits INNER JOIN Patients on Visits.patient_id = Patients.patient_id', 'CONCAT(Visits.date, \' \', Patients.first_name, \' \', Patients.last_name)')},
                {'label': 'Diagnosis', 'name': 'diagnosis_id_input', 'type': 'dropdown', 'options': query_table_to_list('Diagnoses', '$.name')},
            ],
            'VisitTestResults': lambda:[
                {'label': 'Visit', 'name': 'visit_id_input', 'type': 'dropdown', 'options': query_table_to_list('Visits INNER JOIN Patients on Visits.patient_id = Patients.patient_id', 'CONCAT(Visits.date, \' \', Patients.first_name, \' \', Patients.last_name)')},
                {'label': 'Test', 'name': 'test_id_input', 'type': 'dropdown', 'options': query_table_to_list('Tests', '$.name')},
                {'label': 'Result positive?', 'name': 'result_input', 'type': 'checkbox'},
                {'label': 'Detail', 'name': 'detail_input', 'type': 'textarea'},
            ],
            'VisitPrescriptions': lambda:[
                {
                    'label': 'Visit',
                    'name': 'visit_id_input',
                    'type': 'dropdown',
                    'options': query_table_to_list('Visits INNER JOIN Patients on Visits.patient_id = Patients.patient_id', 'CONCAT(Visits.date, \' \', Patients.first_name, \' \', Patients.last_name)')
                },
                {'label': 'Prescription', 'name': 'prescription_id_input', 'type': 'dropdown', 'options': query_table_to_list('Prescriptions', 'name')},
                {'label': 'Dose prescribed', 'name': 'dose_input', 'type': 'text'},
                {'label': 'Instruction', 'name': 'instruction_input', 'type': 'text'},
            ],
            'VisitMedications': lambda:[
                {'label': 'Visit', 'name': 'visit_id_input', 'type': 'dropdown', 'options': query_table_to_list('Visits INNER JOIN Patients on Visits.patient_id = Patients.patient_id', 'CONCAT(Visits.date, \' \', Patients.first_name, \' \', Patients.last_name)')},
                {'label': 'Medication', 'name': 'medication_id_input', 'type': 'dropdown', 'options': query_table_to_list('Medications', 'name')},
                {'label': 'Dose administered', 'name': 'dose_input', 'type': 'text'},
            ]
        }[table]()

row_drop_down_select = {
    'Credentials': ['credential'],
    'Diagnoses': ['name'],
    'MedicalCategories': ['category'],
    'MedicationClasses': ['class'],
    'MedicationRoutes': ['route'],
    'Medications': ['name'],
    'Prescriptions': ['name'],
    'Nurses': ['first_name', 'last_name'],
    'Patients': ['first_name', 'last_name'],
    'Providers': ['first_name', 'last_name'],
    'TestTypes': ['type'],
    'Tests': ['name'],
    'Visits': ['visit_id', 'patient', 'date'],
    'VisitDiagnoses': ['patient', 'date', 'diagnosis'],
    'VisitTestResults': ['patient', 'date', 'test'],
    'VisitPrescriptions': ['patient', 'date', 'prescription'],
    'VisitMedications': ['patient', 'date', 'medication'],
}

table_crud_operations = {  # Should all tables support deletion?
    'Credentials': 'CR',
    'Diagnoses': 'CR',
    'MedicalCategories': 'CR',
    'MedicationClasses': 'CR',
    'MedicationRoutes': 'CR',
    'Medications': 'CR',
    'Prescriptions': 'CR',
    'Nurses': 'CR',
    'Patients': 'CR',
    'Providers': 'CR',
    'TestTypes': 'CR',
    'Tests': 'CR',
    'Visits': 'CRUD',
    'VisitDiagnoses': 'CR',
    'VisitTestResults': 'CR',
    'VisitPrescriptions': 'CR',
    'VisitMedications': 'CR',
}

sql_create_queries = {
    'Credentials':"INSERT INTO Credentials (`credential`) VALUES (%s);",

    'Diagnoses':"""
        INSERT INTO Diagnoses (`name`, `medical_category_id`)
        VALUES (
            %s,
            (SELECT medical_category_id
            FROM MedicalCategories
            WHERE `category` = %s)
        );
    """,

    'MedicalCategories':"INSERT INTO MedicalCategories (`category`) VALUES (%s);",

    'MedicationClasses':"INSERT INTO MedicationClasses (`class`) VALUES (%s);",

    'MedicationRoutes':"INSERT INTO MedicationRoutes (`route`) VALUES (%s);",

    'Medications':"""
        INSERT INTO Medications (`name`, `standard_dose`, `medication_route_id`, `medication_class_id`)
        VALUES (%s, %s, (SELECT medication_route_id
            FROM
                MedicationRoutes
            WHERE
                route = %s), (SELECT medication_class_id
            FROM
                MedicationClasses
            WHERE
                class = %s));""",
    
    'Prescriptions':"""
        INSERT INTO Prescriptions (`name`, `standard_dose`, `medication_route_id`, `medication_class_id`)
        VALUES (%s, %s, (SELECT medication_route_id
            FROM
                MedicationRoutes
            WHERE
                route = %s), (SELECT medication_class_id
            FROM
                MedicationClasses
            WHERE
                class = %s));""",
    
    'Nurses':"""
        INSERT INTO Nurses (`first_name`, `last_name`, `credential_id`, `date_of_birth`, `gender`, `address`, `zip_code`, `phone_number`, `email`)
        VALUES (%s, %s, (SELECT credential_id
            FROM
                Credentials
            WHERE
                credential = %s), %s, %s, %s, %s, %s, %s);""",
    
    'Patients':"""
        INSERT INTO Patients (`first_name`, `last_name`, `date_of_birth`, `gender`, `address`, `zip_code`, `phone_number`, `email`, `provider_id`)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, (SELECT provider_id
            FROM
                Providers
            WHERE
                CONCAT(first_name, ' ', last_name) = %s));""",
    
    'Providers':"""
        INSERT INTO Providers (`first_name`, `last_name`, `credential_id`, `date_of_birth`, `gender`, `address`, `zip_code`, `phone_number`, `email`)
        VALUES (%s, %s, (SELECT credential_id
            FROM
                Credentials
            WHERE
                credential = %s), %s, %s, %s, %s, %s, %s);""",
    
    'TestTypes':"INSERT INTO TestTypes (`type`) VALUES (%s);",

    'Tests':"""
        INSERT INTO Tests (`name`, `test_type_id`)
        VALUES (%s, (SELECT test_type_id
            FROM
                TestTypes
            WHERE
                type = %s));""",
    
    'Visits':"""
        INSERT INTO Visits (`date`, `reason_for_visit`, `patient_id`, `provider_id`, `nurse_id`)
        VALUES (
            %s,
            %s,
            (SELECT patient_id
                FROM Patients
                WHERE CONCAT(first_name, ' ', last_name) = %s),
            (SELECT provider_id
                FROM Providers
                WHERE CONCAT(first_name, ' ', last_name) = %s),
            (SELECT nurse_id
                FROM Nurses
                WHERE CONCAT(first_name, ' ', last_name) = %s));""",
    
    'VisitDiagnoses':"""
        INSERT INTO VisitDiagnoses (`visit_id`, `diagnosis_id`)
        VALUES ((SELECT visit_id
            FROM Visits
                INNER JOIN Patients ON Visits.patient_id = Patients.patient_id
            WHERE CONCAT(date, ' ', Patients.first_name, ' ', Patients.last_name) = %s), (SELECT diagnosis_id
            FROM
                Diagnoses
            WHERE
                name = %s));""",
    
    'VisitTestResults':"""
        INSERT INTO VisitTestResults (`visit_id`, `test_id`, `result`, `detail`)
        VALUES ((SELECT visit_id
            FROM Visits
                INNER JOIN Patients ON Visits.patient_id = Patients.patient_id
            WHERE CONCAT(date, ' ', Patients.first_name, ' ', Patients.last_name) = %s),
        (SELECT test_id
            FROM
                Tests
            WHERE
                name = %s), %s, %s);""",
    
    'VisitPrescriptions':"""
        INSERT INTO VisitPrescriptions (`visit_id`, `prescription_id`, `dose_prescribed`, `instruction`)
        VALUES ((
            SELECT visit_id
            FROM Visits
                INNER JOIN Patients ON Visits.patient_id = Patients.patient_id
            WHERE CONCAT(date, ' ', Patients.first_name, ' ', Patients.last_name) = %s), (SELECT prescription_id
            FROM
                Prescriptions
            WHERE
                name = %s), %s, %s);""",
    
    'VisitMedications':"""
        INSERT INTO VisitMedications (`visit_id`, `medication_id`, `dose_administered`)
        VALUES ((
            SELECT visit_id
            FROM Visits
                INNER JOIN Patients ON Visits.patient_id = Patients.patient_id
            WHERE CONCAT(date, ' ', Patients.first_name, ' ', Patients.last_name) = %s), (SELECT medication_id
            FROM
                Medications
            WHERE
                name = %s), %s);"""
}

sql_get_queries = {  # R
    'Credentials': "SELECT * FROM Credentials;",

    'Diagnoses':"""
    SELECT Diagnoses.diagnosis_id, Diagnoses.name, MedicalCategories.category as 'medical_category'
    FROM Diagnoses
        INNER JOIN MedicalCategories
            ON MedicalCategories.medical_category_id = Diagnoses.medical_category_id
    ORDER BY Diagnoses.diagnosis_id ASC;""",

    'MedicalCategories': "SELECT * FROM MedicalCategories;",

    'MedicationClasses': "SELECT * FROM MedicationClasses;",

    'MedicationRoutes': "SELECT * FROM MedicationRoutes;",

    'Medications': """
        SELECT Medications.medication_id, Medications.name, Medications.standard_dose, MedicationRoutes.route as 'route', MedicationClasses.class as 'class'
        FROM Medications
            INNER JOIN MedicationRoutes
                ON Medications.medication_route_id = MedicationRoutes.medication_route_id
            Inner JOIN MedicationClasses
                ON Medications.medication_class_id = MedicationClasses.medication_class_id;""",

    'Prescriptions': """
        SELECT Prescriptions.prescription_id, Prescriptions.name, Prescriptions.standard_dose, MedicationRoutes.route as 'route', MedicationClasses.class as 'class'
        FROM Prescriptions
            INNER JOIN MedicationRoutes
                ON Prescriptions.medication_route_id = MedicationRoutes.medication_route_id
            INNER JOIN MedicationClasses
                ON Prescriptions.medication_class_id = MedicationClasses.medication_class_id;""",

    'Nurses': """
        SELECT Nurses.nurse_id, Nurses.first_name, Nurses.last_name, Credentials.credential AS 'credential', Nurses.date_of_birth, Nurses.gender, Nurses.address, Nurses.zip_code, Nurses.phone_number, Nurses.email
        FROM Nurses
            INNER JOIN Credentials
                ON Nurses.credential_id = Credentials.credential_id;""",

    'Patients': """
        SELECT Patients.patient_id, Patients.first_name, Patients.last_name, Patients.date_of_birth, Patients.gender, Patients.address, Patients.zip_code, Patients.phone_number, Patients.email, CONCAT (Providers.first_name, " ", Providers.last_name) AS 'provider'
        FROM Providers
            RIGHT JOIN Patients
                ON Providers.provider_id = Patients.provider_id;""",

    'Providers':"""
        SELECT Providers.provider_id, Providers.first_name, Providers.last_name, Credentials.credential AS 'credential', Providers.date_of_birth, Providers.gender, Providers.address, Providers.zip_code, Providers.phone_number, Providers.email
        FROM Providers
            INNER JOIN Credentials
                ON Providers.credential_id = Credentials.credential_id;""",

    'TestTypes': """
        SELECT * FROM TestTypes;""",

    'Tests': """
        SELECT Tests.test_id, Tests.name, TestTypes.type as 'test_type'
        FROM Tests
            INNER JOIN TestTypes
            ON TestTypes.test_type_id = Tests.test_type_id;""",
            
    'Visits': """
        SELECT Visits.visit_id, Visits.date, Visits.reason_for_visit, CONCAT (Patients.first_name, " ", Patients.last_name) AS 'patient', CONCAT (Providers.first_name, " ", Providers.last_name) AS 'provider', CONCAT (Nurses.first_name, " ", Nurses.last_name) AS 'nurse'
        FROM Visits
            INNER JOIN Patients
                ON Visits.patient_id = Patients.patient_id
            INNER JOIN Providers
                ON Visits.provider_id = Providers.provider_id
            INNER JOIN Nurses
                ON Visits.nurse_id = Nurses.nurse_id
        ORDER BY Visits.visit_id ASC;""",
    
    'VisitDiagnoses': """
        SELECT VisitDiagnoses.visit_diagnosis_id, VisitDiagnoses.visit_id, CONCAT (Patients.first_name, " ", Patients.last_name) AS 'patient', Visits.date, Diagnoses.name as 'diagnosis'
        FROM VisitDiagnoses
            INNER JOIN Visits
                ON VisitDiagnoses.visit_id = Visits.visit_id
            INNER JOIN Patients
                ON Patients.patient_id = Visits.patient_id
            INNER JOIN Diagnoses
                ON VisitDiagnoses.diagnosis_id = Diagnoses.diagnosis_id
        ORDER BY VisitDiagnoses.visit_diagnosis_id ASC;""",
    
    'VisitTestResults': """
        SELECT VisitTestResults.visit_test_result_id, VisitTestResults.visit_id, CONCAT (Patients.first_name, " ", Patients.last_name) AS 'patient', Visits.date, Tests.name as 'test', CASE WHEN VisitTestResults.result = '1' THEN 'Positive' ELSE 'Negative' END as 'result', VisitTestResults.detail
        FROM VisitTestResults
            INNER JOIN Visits
                ON VisitTestResults.visit_id = Visits.visit_id
            INNER JOIN Patients
                ON Patients.patient_id = Visits.patient_id
            INNER JOIN Tests
                ON VisitTestResults.test_id = Tests.test_id
        ORDER BY VisitTestResults.visit_test_result_id ASC;""",
    
    'VisitPrescriptions': """
        SELECT VisitPrescriptions.visit_prescription_id, VisitPrescriptions.visit_id, CONCAT (Patients.first_name, " ", Patients.last_name) AS 'patient', Visits.date, Prescriptions.name as 'prescription', VisitPrescriptions.dose_prescribed, VisitPrescriptions.instruction
        FROM VisitPrescriptions
            INNER JOIN Visits
                ON VisitPrescriptions.visit_id = Visits.visit_id
            INNER JOIN Patients
                ON Patients.patient_id = Visits.patient_id
            INNER JOIN Prescriptions
                ON VisitPrescriptions.prescription_id = Prescriptions.prescription_id
        ORDER BY VisitPrescriptions.visit_prescription_id ASC;""",
    
    'VisitMedications': """
        SELECT VisitMedications.visit_medication_id, VisitMedications.visit_id, CONCAT (Patients.first_name, " ", Patients.last_name) AS 'patient', Visits.date, Medications.name as 'medication', VisitMedications.dose_administered
        FROM VisitMedications
            INNER JOIN Visits
                ON VisitMedications.visit_id = Visits.visit_id
            INNER JOIN Patients
                ON Patients.patient_id = Visits.patient_id
            INNER JOIN Medications
                ON VisitMedications.medication_id = Medications.medication_id
        ORDER BY VisitMedications.visit_medication_id ASC;"""
}

sql_filter_queries = {
    'VisitDiagnoses': """
    SELECT VisitDiagnoses.visit_diagnosis_id, VisitDiagnoses.visit_id, CONCAT (Patients.first_name, " ", Patients.last_name) AS 'patient', Visits.date, Diagnoses.name as 'diagnosis'
    FROM VisitDiagnoses
        INNER JOIN Visits
            ON VisitDiagnoses.visit_id = Visits.visit_id
        INNER JOIN Patients
            ON Patients.patient_id = Visits.patient_id
        INNER JOIN Diagnoses
            ON VisitDiagnoses.diagnosis_id = Diagnoses.diagnosis_id
    WHERE Diagnoses.name = %s;
    """
}

sql_update_queries = {

}

sql_delete_queries = {

}