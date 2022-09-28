-- These are the Database Manipulation queries for the OSMC Website


-- ------------------------------------------
-- Queries to insert into tables (CREATE)
-- ------------------------------------------


-- Query for adding a new patient

INSERT INTO Patients (`first_name`, `last_name`, `date_of_birth`, `gender`, `address`, `zip_code`, `phone_number`, `email`, `provider_id`)
VALUES (:first_name_input, :last_name_input, :date_of_birth_input, :gender_input, :address_input, :zip_code_input, :phone_number_input, :email_input, (SELECT provider_id
    FROM
        Providers
    WHERE
        first_name  = :provider_first_name_input AND last_name = :provider_last_name_input));

-- Query for adding a new provider

INSERT INTO Providers (`first_name`, `last_name`, `credential_id`, `date_of_birth`, `gender`, `address`, `zip_code`, `phone_number`, `email`)
VALUES (:first_name_input, :last_name_input, (SELECT credential_id
    FROM
        Credentials
    WHERE
        credential = :credential_id_input), :date_of_birth_input, :gender_input, :address_input, :zip_code_input, :phone_number_input, :email_input);

-- Query for adding a new nurse

INSERT INTO Nurses (`first_name`, `last_name`, `credential_id`, `date_of_birth`, `gender`, `address`, `zip_code`, `phone_number`, `email`)
VALUES (:first_name_input, :last_name_input, (SELECT credential_id
    FROM
        Credentials
    WHERE
        credential = :credential_id_input), :date_of_birth_input, :gender_input, :address_input, :zip_code_input, :phone_number_input, :email_input);

-- Query for adding a new credential

INSERT INTO Credentials (`credential`)
VALUES (:credential_input);

-- Query for adding a new medical category

INSERT INTO MedicalCategories (`category`)
VALUES (:category_input);

-- Query for adding a new diagnosis

INSERT INTO Diagnoses (`name`, `medical_category_id`)
VALUES (:name_input, (SELECT medical_category_id
    FROM
        MedicalCategories
    WHERE
        category = :medical_category_id_input));

-- Query for adding a new test type

INSERT INTO TestTypes (`type`)
VALUES (:type_input);

-- Query for adding a new test

INSERT INTO Tests (`test_type_id`, `name`)
VALUES ((SELECT test_type_id
    FROM
        TestTypes
    WHERE
        type = :test_type_id_input), :name_input);

-- Query for adding a new medication route

INSERT INTO MedicationRoutes (`route`)
VALUES (:route_input);

-- Query for adding a new medication class

INSERT INTO MedicationClasses (`class`)
VALUES (:class_input);

-- Query for adding a new medication

INSERT INTO Medications (`name`, `standard_dose`, `medication_route_id`, `medication_class_id`)
VALUES (:name_input, :standard_dose_input, (SELECT medication_route_id
    FROM
        MedicationRoutes
    WHERE
        route = :medication_route_id_input), (SELECT medication_class_id
    FROM
        MedicationClasses
    WHERE
        class = :medication_class_id_input));

-- Query for adding a new prescription

INSERT INTO Prescriptions (`name`, `standard_dose`, `medication_route_id`, `medication_class_id`)
VALUES (:name_input, :standard_dose_input, (SELECT medication_route_id
    FROM
        MedicationRoutes
    WHERE
        route = :medication_route_id_input), (SELECT medication_class_id
    FROM
        MedicationClasses
    WHERE
        class = :medication_class_id_input));

-- Query for adding a visit

INSERT INTO Visits (`date`, `reason_for_visit`, `patient_id`, `provider_id`, `nurse_id`)
VALUES (:date_input, :reason_for_visit_input, (SELECT patient_id
    FROM
        Patients
    WHERE
        first_name  = :patient_first_name_input AND last_name = :patient_last_name_input), (SELECT provider_id
    FROM
        Providers
    WHERE
        first_name  = :provider_first_name_input AND last_name = :provider_last_name_input), (SELECT nurse_id
    FROM
        Nurses
    WHERE
        first_name  = :nurse_first-name_input AND last_name = :nurse_last_name_input));

-- Query for adding a diagnosis to a visit

INSERT INTO VisitDiagnoses (`visit_id`, `diagnosis_id`)
VALUES (:visit_id_input, (SELECT diagnosis_id
    FROM
        Diagnoses
    WHERE
        name = :diagnosis_id_input));

-- Query for adding a test result to a visit

INSERT INTO VisitTestResults (`visit_id`, `test_id`, `result`, `detail`)
VALUES (:visit_id_input, (SELECT test_id
    FROM
        Tests
    WHERE
        name = :test_id_input), :result_input, :detail_input);

-- Query for adding a prescriptions to a visit

INSERT INTO VisitPrescriptions (`visit_id`, `prescription_id`, `dose_prescribed`, `instruction`)
VALUES (:visit_id_input, (SELECT prescription_id
    FROM
        Prescriptions
    WHERE
        name = :prescription_id_input), :dose_prescribed_input, :instruction_input);

-- Query for adding a medication to a visit

INSERT INTO VisitMedications (`visit_id`, `medication_id`, `dose_administered`)
VALUES (:visit_id_input, (SELECT medication_id
    FROM
        Medications
    WHERE
        name = :medication_id_input), :dose_administered_input);


-- ------------------------------------------
-- Queries to select from tables (READ)
-- ------------------------------------------


-- Query for all patients information, replacing provider_id with provider full name

SELECT Patients.patient_id, Patients.first_name, Patients.last_name, Patients.date_of_birth, Patients.gender, Patients.address, Patients.zip_code, Patients.phone_number, Patients.email, CONCAT (Providers.first_name, " ", Providers.last_name) AS 'provider'
	FROM Providers
    	RIGHT JOIN Patients
        ON Providers.provider_id = Patients.provider_id;

-- Query for all providers information, replacing credential_id with credential name

SELECT Providers.provider_id, Providers.first_name, Providers.last_name, Credentials.credential AS 'credential', Providers.date_of_birth, Providers.gender, Providers.address, Providers.zip_code, Providers.phone_number, Providers.email
	FROM Providers
    	INNER JOIN Credentials
        ON Providers.credential_id = Credentials.credential_id;

-- Query for all nurses information, replacing credential_id with credential name

SELECT Nurses.nurse_id, Nurses.first_name, Nurses.last_name, Credentials.credential AS 'credential', Nurses.date_of_birth, Nurses.gender, Nurses.address, Nurses.zip_code, Nurses.phone_number, Nurses.email
	FROM Nurses
    	INNER JOIN Credentials
        ON Nurses.credential_id = Credentials.credential_id;

-- Query for all credentials information 

SELECT * FROM Credentials;

-- Query for all medical categories information 

SELECT * FROM MedicalCategories;

-- Query for all diagnoses information, replacing medical_category_id with medical category name

SELECT Diagnoses.diagnosis_id, Diagnoses.name, MedicalCategories.category as 'medical_category'
	FROM Diagnoses
    	INNER JOIN MedicalCategories
        ON MedicalCategories.medical_category_id = Diagnoses.medical_category_id;

-- Query for all test types information 

SELECT * FROM TestTypes;

-- Query for all tests information, replacing test_type_id with name of the test type

SELECT Tests.test_id, Tests.name, TestTypes.type as 'test_type'
	FROM Tests
    	INNER JOIN TestTypes
        ON TestTypes.test_type_id = Tests.test_type_id;

-- Query for all medication routes information 

SELECT * FROM MedicationRoutes;

-- Query for all medication classes information 

SELECT * FROM MedicationClasses;

-- Query for all medications information, replacing medication_route_id and medication_class_id with the route name and class name

SELECT Medications.medication_id, Medications.name, Medications.standard_dose, MedicationRoutes.route as 'route', MedicationClasses.class as 'class'
	FROM Medications
    	INNER JOIN MedicationRoutes
        ON Medications.medication_route_id = MedicationRoutes.medication_route_id
        INNER JOIN MedicationClasses
        ON Medications.medication_class_id = MedicationClasses.medication_class_id;

-- Query for all prescriptions information, replacing medication_route_id and medication_class_id with the route name and class name

SELECT Prescriptions.prescription_id, Prescriptions.name, Prescriptions.standard_dose, MedicationRoutes.route as 'route', MedicationClasses.class as 'class'
	FROM Prescriptions
    	INNER JOIN MedicationRoutes
        ON Prescriptions.medication_route_id = MedicationRoutes.medication_route_id
        INNER JOIN MedicationClasses
        ON Prescriptions.medication_class_id = MedicationClasses.medication_class_id;

-- Query for all visits information replacing patient_id, provider_id, and nurse_id with corresponding full name

SELECT Visits.visit_id, Visits.date, Visits.reason_for_visit, CONCAT (Patients.first_name, " ", Patients.last_name) AS 'patient', CONCAT (Providers.first_name, " ", Providers.last_name) AS 'provider', CONCAT (Nurses.first_name, " ", Nurses.last_name) AS 'nurse'
	FROM Visits
    	INNER JOIN Patients
        ON Visits.patient_id = Patients.patient_id
        INNER JOIN Providers
        ON Visits.provider_id = Providers.provider_id
        INNER JOIN Nurses
        ON Visits.nurse_id = Nurses.nurse_id
       	ORDER BY Visits.visit_id ASC;

-- Query for all visit diagnoses information, uses visit_id to add patient full name and date of visit, replaces diagnosis_id with name of diagnosis

SELECT VisitDiagnoses.visit_diagnosis_id, VisitDiagnoses.visit_id, CONCAT (Patients.first_name, " ", Patients.last_name) AS 'patient', Visits.date, Diagnoses.name as 'diagnosis'
	FROM VisitDiagnoses
    	INNER JOIN Visits
        ON VisitDiagnoses.visit_id = Visits.visit_id
        INNER JOIN Patients
        ON Patients.patient_id = Visits.patient_id
        INNER JOIN Diagnoses
        ON VisitDiagnoses.diagnosis_id = Diagnoses.diagnosis_id
		ORDER BY VisitDiagnoses.visit_diagnosis_id ASC;
        
-- Query for search/filter of visit diagnoses (user input of diagnosis name), returns date, patient full name, age calculated from date of birth, gender, and location
        
SELECT Visits.date, CONCAT (Patients.first_name, " ", Patients.last_name) AS 'patient', TIMESTAMPDIFF(YEAR, Patients.date_of_birth, CURDATE()) AS 'age', Patients.gender, Patients.zip_code AS 'location'
	FROM VisitDiagnoses
    	INNER JOIN Visits
        ON VisitDiagnoses.visit_id = Visits.visit_id
        INNER JOIN Patients
        ON Patients.patient_id = Visits.patient_id
        INNER JOIN Diagnoses
        ON VisitDiagnoses.diagnosis_id = Diagnoses.diagnosis_id
        WHERE Diagnoses.diagnosis_id = (SELECT diagnosis_id
    FROM
        Diagnoses
    WHERE
        name = :diagnosis_id_input);
 

-- Query for all visit test results information, uses visit_id to add patient full name and date of visit, replaces test_id with name of test, replaces 1 with positive and 0 with negative result

SELECT VisitTestResults.visit_test_result_id, VisitTestResults.visit_id, CONCAT (Patients.first_name, " ", Patients.last_name) AS 'patient', Visits.date, Tests.name as 'test', CASE WHEN VisitTestResults.result = '1' THEN 'Positive'
         ELSE 'Negative' END as 'result', VisitTestResults.detail
	FROM VisitTestResults
    	INNER JOIN Visits
        ON VisitTestResults.visit_id = Visits.visit_id
        INNER JOIN Patients
        ON Patients.patient_id = Visits.patient_id
        INNER JOIN Tests
        ON VisitTestResults.visit_test_result_id = Tests.test_id
		ORDER BY VisitTestResults.visit_test_result_id ASC;

-- Query for all visit prescriptions information, uses visit_id to add patient full name and date of visit, replaces prescription_id with name of prescription

SELECT VisitPrescriptions.visit_prescription_id, VisitPrescriptions.visit_id, CONCAT (Patients.first_name, " ", Patients.last_name) AS 'patient', Visits.date, Prescriptions.name as 'prescription', VisitPrescriptions.dose_prescribed, VisitPrescriptions.instruction
	FROM VisitPrescriptions
    	INNER JOIN Visits
        ON VisitPrescriptions.visit_id = Visits.visit_id
        INNER JOIN Patients
        ON Patients.patient_id = Visits.patient_id
        INNER JOIN Prescriptions
        ON VisitPrescriptions.prescription_id = Prescriptions.prescription_id
		ORDER BY VisitPrescriptions.visit_prescription_id ASC;

-- Query for all visit medications information, uses visit_id to add patient full name and date of visit, replaces medication_id with name of medication

SELECT VisitMedications.visit_medication_id, VisitMedications.visit_id, CONCAT (Patients.first_name, " ", Patients.last_name) AS 'patient', Visits.date, Medications.name as 'medication', VisitMedications.dose_administered
	FROM VisitMedications
    	INNER JOIN Visits
        ON VisitMedications.visit_id = Visits.visit_id
        INNER JOIN Patients
        ON Patients.patient_id = Visits.patient_id
        INNER JOIN Medications
        ON VisitMedications.medication_id = Medications.medication_id
		ORDER BY VisitMedications.visit_medication_id ASC;


-- ------------------------------------------
-- Queries to update tables (UPDATE)
-- ------------------------------------------


-- Query for updating a patient

UPDATE Patients SET `first_name` = :first_name_input, `last_name` = :last_name_input, `date_of_birth` = :date_of_birth_input, `address` = :address_input, `zip_code` = :zip_code_input, `phone_number` = :phone_number_input, `email` = :email_input, `provider_id` = (SELECT provider_id
    FROM
        Providers
    WHERE
        first_name  = :provider_first_name_input AND last_name = :provider_last_name_input) WHERE `patient_id` = :patient_id_input;

-- Query for updating a provider

UPDATE Providers SET `first_name` = :first_name_input, `last_name` = :last_name_input, `credential_id` = (SELECT credential_id
    FROM
        Credentials
    WHERE
        credential = :credential_id_input), `date_of_birth` = :date_of_birth_input, `address` = :address_input, `zip_code` = :zip_code_input, `phone_number` = :phone_number_input, 
`email` = :email_input WHERE `provider_id` = :provider_id_input;

-- Query for updating a nurse

UPDATE Nurses SET `first_name` = :first_name_input, `last_name` = :last_name_input, `credential_id` = (SELECT credential_id
    FROM
        Credentials
    WHERE
        credential = :credential_id_input), `date_of_birth` = :date_of_birth_input,
`address` = :address_input, `zip_code` = :zip_code_input, `phone_number` = :phone_number_input, `email` = :email_input WHERE `nurse_id` = :nurse_id_input;

-- Query for updating a credential

UPDATE Credentials SET `credential` = :credential_input WHERE `credential_id` = :credential_id_input;

-- Query for updating a medical category

UPDATE MedicalCategories SET `category` = :category_input WHERE `medical_category_id` = :medical_category_id_input;

-- Query for updating a diagnosis

UPDATE Diagnoses SET `name` = :name_input, `medical_category_id` = (SELECT medical_category_id
    FROM
        MedicalCategories
    WHERE
        category = :medical_category_id_input) WHERE `diagnosis_id` = :diagnosis_id_input;

-- Query for updating a test type

UPDATE TestTypes SET `type` = :type_input WHERE `test_type_id` = :test_type_id_input;

-- Query for updating a test

UPDATE Tests SET `test_type_id` = (SELECT test_type_id
    FROM
        TestTypes
    WHERE
        type = :test_type_id_input), `name` = :name_input WHERE `test_id` = :test_id_input;

-- Query for updating a medication route

UPDATE MedicationRoutes SET `route` = :route_input WHERE `medication_route_id` = :medication_route_id_input;

-- Query for updating a medication class

UPDATE MedicationClasses SET `class` = :class_input WHERE `medication_class_id` = :medication_class_id_input;

-- Query for updating a medication

UPDATE Medications SET `name` = :name_input, `standard_dose` = :standard_dose_input, `medication_route_id` = (SELECT medication_route_id
    FROM
        MedicationRoutes
    WHERE
        route = :medication_route_id_input), `medication_class_id` = (SELECT medication_class_id
    FROM
        MedicationClasses
    WHERE
        class = :medication_class_id_input) WHERE `medication_id` = :medication_id_input;

-- Query for updating a prescription

UPDATE Prescriptions SET `name` = :name_input, `standard_dose` = :standard_dose_input, `medication_route_id` = (SELECT medication_route_id
    FROM
        MedicationRoutes
    WHERE
        route = :medication_route_id_input), `medication_class_id` = (SELECT medication_class_id
    FROM
        MedicationClasses
    WHERE
        class = :medication_class_id_input) WHERE `prescription_id` = :prescription_id_input;

-- Query for updating a visit

UPDATE Visits SET `date` = :date_input, `reason_for_visit` = :reason_for_visit_input, `patient_id` = (SELECT patient_id
    FROM
        Patients
    WHERE
        first_name  = :patient_first_name_input AND last_name = :patient_last_name_input), `provider_id` = (SELECT provider_id
    FROM
        Providers
    WHERE
        first_name  = :provider_first_name_input AND last_name = :provider_last_name_input), `nurse_id` = (SELECT nurse_id
    FROM
        Nurses
    WHERE
        first_name  = :nurse_first-name_input AND last_name = :nurse_last_name_input) WHERE `visit_id` = :visit_id_input;

-- Query for updating a visit diagnosis

UPDATE VisitDiagnoses SET `visit_id` = :visit_id_input, `diagnosis_id` = (SELECT diagnosis_id
    FROM
        Diagnoses
    WHERE
        name = :diagnosis_id_input) WHERE `visit_diagnosis_id` = :visit_diagnosis_id_input;

-- Query for updating a visit test result

UPDATE VisitTestResults SET `visit_id` = :visit_id_input, `test_id` = (SELECT test_id
    FROM
        Tests
    WHERE
        name = :test_id_input), `result` = :result_input, `detail` = :detail_input WHERE `visit_test_result_id` = :visit_test_result_id_input;

-- Query for updating a visit prescription

UPDATE VisitPrescriptions SET `visit_id` = :visit_id_input, `prescription_id` = (SELECT prescription_id
    FROM
        Prescriptions
    WHERE
        name = :prescription_id_input), `dose_prescribed` = :dose_prescribed_input, `instruction` = :instruction_input WHERE `visit_prescription_id` = :visit_prescription_id_input;

-- Query for updating a visit medication

UPDATE VisitMedications SET `visit_id` = :visit_id_input, `medication_id` = (SELECT medication_id
    FROM
        Medications
    WHERE
        name = :medication_id_input), `dose_administered` = :dose_administered_input WHERE `visit_medication_id` = :visit_medication_id_input;


-- ------------------------------------------
-- Queries to delete from tables (DELETE)
-- ------------------------------------------


-- Query for deleting a patient, ON DELETE CASCADE set up in DDL will also delete associated Visits

DELETE FROM Patients WHERE `patient_id` = :patient_id_input;

-- Query for deleting a provider, ON DELETE CASCADE set up in DDL will also delete associated Visits

DELETE FROM Providers WHERE `provider_id` = :provider_id_input;

-- Query for deleting a nurse, ON DELETE CASCADE set up in DDL will also delete associated Visits

DELETE FROM Nurses WHERE `nurse_id` = :nurse_id_input;

-- Query for deleting a credential, ON DELETE CASCADE set up in DDL will also delete associated Providers/Nurses

DELETE FROM Credentials WHERE `credential_id` = :credential_id_input;

-- Query for deleting a medical category, ON DELETE CASCADE set up in DDL will also delete associated Diagnoses

DELETE FROM MedicalCategories WHERE `medical_category_id` = :medical_category_id_input;

-- Query for deleting a diagnosis, ON DELETE CASCADE set up in DDL will also delete associated VisitDiagnoses

DELETE FROM Diagnoses WHERE `diagnosis_id` = :diagnosis_id_input;

-- Query for deleting a test type, ON DELETE CASCADE set up in DDL will also delete associated Tests

DELETE FROM TestTypes WHERE `test_type_id` = :test_type_id_input;

-- Query for deleting a test, ON DELETE CASCADE set up in DDL will also delete associated VisitTestResults

DELETE FROM Tests WHERE `test_id` = :test_id_input;

-- Query for deleting a medication route, ON DELETE CASCADE set up in DDL will also delete associated Medications/Prescriptions

DELETE FROM MedicationRoutes WHERE `medication_route_id` = :medication_route_id_input;

-- Query for deleting a medication class, ON DELETE CASCADE set up in DDL will also delete associated Medications/Prescriptions

DELETE FROM MedicationClasses WHERE `medication_class_id` = :medication_class_id_input;

-- Query for deleting a medication, ON DELETE CASCADE set up in DDL will also delete associated VisitMedications

DELETE FROM Medications WHERE `medication_id` = :medication_id_input;

-- Query for deleting a prescription, ON DELETE CASCADE set up in DDL will also delete associated VisitPrescriptions

DELETE FROM Prescriptions WHERE `prescription_id` = :prescription_id_input;

-- Query for deleting a visit, ON DELETE CASCADE set up in DDL will also delete associated VisitPrescriptions, VisitMedications, VisitDiagnoses, VisitTestResults

DELETE FROM Visits WHERE `visit_id` = :visit_id_input;

-- Query for deleting a visit diagnosis

DELETE FROM VisitDiagnoses WHERE `visit_diagnosis_id` = :visit_diagnosis_id_input;

-- Query for deleting a visit test result

DELETE FROM VisitTestResults WHERE `visit_testresult_id` = :visit_testresult_id_input;

-- Query for deleting a visit prescription

DELETE FROM VisitPrescriptions WHERE `visit_prescription_id` = :visit_prescription_id_input;

-- Query for deleting a visit medication

DELETE FROM VisitMedications WHERE `visit_medication_id` = :visit_medication_id_input
