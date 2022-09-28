-- phpMyAdmin SQL Dump
-- version 5.2.0-1.el7.remi
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jul 11, 2022 at 11:04 PM
-- Server version: 10.6.8-MariaDB-log
-- PHP Version: 7.4.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";
SET FOREIGN_KEY_CHECKS=0;
SET AUTOCOMMIT = 0;


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cs340_smithm33`
--

-- --------------------------------------------------------

--
-- Table structure for table `Credentials`
--

DROP TABLE IF EXISTS `Credentials`;
CREATE TABLE `Credentials` (
  `credential_id` int(11) UNIQUE NOT NULL AUTO_INCREMENT,
  `credential` varchar(45) NOT NULL,
  PRIMARY KEY (`credential_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `Credentials`
--

INSERT INTO `Credentials` (`credential_id`, `credential`) VALUES
(1, 'MD'),
(2, 'DO'),
(3, 'NP'),
(4, 'PA'),
(5, 'RN'),
(6, 'LPN');

-- --------------------------------------------------------

--
-- Table structure for table `Diagnoses`
--

DROP TABLE IF EXISTS `Diagnoses`;
CREATE TABLE `Diagnoses` (
  `diagnosis_id` int(11) UNIQUE NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `medical_category_id` int(11) NOT NULL,
  PRIMARY KEY (`diagnosis_id`),
  FOREIGN KEY (`medical_category_id`)
    REFERENCES `MedicalCategories`(`medical_category_id`)
    ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `Diagnoses`
--

INSERT INTO `Diagnoses` (`diagnosis_id`, `name`, `medical_category_id`) VALUES
(1, 'Hypertension', 1),
(2, 'Diarrhea', 4),
(3, 'Headache', 3),
(4, 'Pneumonia', 2),
(5, 'Kidney Stone', 5),
(6, 'Ankle Fracture', 6),
(7, 'Seizure', 3),
(8, 'COVID-19', 2),
(9, 'Flu', 2),
(10, 'Constipation', 4);

-- --------------------------------------------------------

--
-- Table structure for table `MedicalCategories`
--

DROP TABLE IF EXISTS `MedicalCategories`;
CREATE TABLE `MedicalCategories` (
  `medical_category_id` int(11) UNIQUE NOT NULL AUTO_INCREMENT,
  `category` varchar(45) NOT NULL,
  PRIMARY KEY (`medical_category_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `MedicalCategories`
--

INSERT INTO `MedicalCategories` (`medical_category_id`, `category`) VALUES
(1, 'Cardiac'),
(2, 'Respiratory'),
(3, 'Neurologic'),
(4, 'Gastrointestinal'),
(5, 'Genitourinary'),
(6, 'Musculoskeletal');

-- --------------------------------------------------------

--
-- Table structure for table `MedicationClasses`
--

DROP TABLE IF EXISTS `MedicationClasses`;
CREATE TABLE `MedicationClasses` (
  `medication_class_id` int(11) UNIQUE NOT NULL AUTO_INCREMENT,
  `class` varchar(45) NOT NULL,
  PRIMARY KEY (`medication_class_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `MedicationClasses`
--

INSERT INTO `MedicationClasses` (`medication_class_id`, `class`) VALUES
(1, 'Analgesics'),
(2, 'Antiemetics'),
(3, 'Antibiotics'),
(4, 'Antivirals'),
(5, 'Antihistamines'),
(6, 'Antihypertensives'),
(7, 'Diuretics');

-- --------------------------------------------------------

--
-- Table structure for table `MedicationRoutes`
--

DROP TABLE IF EXISTS `MedicationRoutes`;
CREATE TABLE `MedicationRoutes` (
  `medication_route_id` int(11) UNIQUE NOT NULL AUTO_INCREMENT,
  `route` varchar(45) NOT NULL,
  PRIMARY KEY (`medication_route_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `MedicationRoutes`
--

INSERT INTO `MedicationRoutes` (`medication_route_id`, `route`) VALUES
(1, 'Oral'),
(2, 'Sublingual'),
(3, 'Subcutaneous'),
(4, 'Intramuscular'),
(5, 'Ophthalmic'),
(6, 'Otic'),
(7, 'Inhalation');

-- --------------------------------------------------------

--
-- Table structure for table `Medications`
--

DROP TABLE IF EXISTS `Medications`;
CREATE TABLE `Medications` (
  `medication_id` int(11) UNIQUE NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `standard_dose` varchar(45) NOT NULL,
  `medication_route_id` int(11) NOT NULL,
  `medication_class_id` int(11) NOT NULL,
  PRIMARY KEY (`medication_id`),
  FOREIGN KEY (`medication_route_id`)
    REFERENCES `MedicationRoutes`(`medication_route_id`)
    ON DELETE CASCADE,
  FOREIGN KEY (`medication_class_id`)
    REFERENCES `MedicationClasses`(`medication_class_id`)
    ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `Medications`
--

INSERT INTO `Medications` (`medication_id`, `name`, `standard_dose`, `medication_route_id`, `medication_class_id`) VALUES
(1, 'Zofran', '4 mg', 2, 2),
(2, 'Lisinopril', '10 mg', 1, 6),
(3, 'Tylenol', '650 mg', 1, 1),
(4, 'Azithromycin', '500 mg', 1, 3),
(5, 'Phenergan', '25 mg', 4, 2);

-- --------------------------------------------------------

--
-- Table structure for table `Nurses`
--

DROP TABLE IF EXISTS `Nurses`;
CREATE TABLE `Nurses` (
  `nurse_id` int(11) UNIQUE NOT NULL AUTO_INCREMENT,
  `first_name` varchar(45) NOT NULL,
  `last_name` varchar(45) NOT NULL,
  `credential_id` int(11) NOT NULL,
  `date_of_birth` date DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `zip_code` varchar(10) DEFAULT NULL,
  `phone_number` varchar(15) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`nurse_id`),
  FOREIGN KEY (`credential_id`)
    REFERENCES `Credentials`(`credential_id`)
    ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `Nurses`
--

INSERT INTO `Nurses` (`nurse_id`, `first_name`, `last_name`, `credential_id`, `date_of_birth`, `gender`, `address`, `zip_code`, `phone_number`, `email`) VALUES
(1, 'Samwise', 'Gamgee', 5, NULL, 'Male', NULL, NULL, NULL, NULL),
(2, 'Peter', 'Parker', 6, '2001-08-10', 'Male', '20 Ingram Street', '11005', '407-224-1783', 'spider@web.net'),
(3, 'Cersei', 'Lannister', 6, NULL, 'Female', NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `Patients`
--

DROP TABLE IF EXISTS `Patients`;
CREATE TABLE `Patients` (
  `patient_id` int(11) UNIQUE NOT NULL AUTO_INCREMENT,
  `first_name` varchar(45) NOT NULL,
  `last_name` varchar(45) NOT NULL,
  `date_of_birth` date NOT NULL,
  `gender` varchar(10) NOT NULL,
  `address` varchar(100) NOT NULL,
  `zip_code` varchar(10) NOT NULL,
  `phone_number` varchar(15) NOT NULL,
  `email` varchar(45) DEFAULT NULL,
  `provider_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`patient_id`),
  FOREIGN KEY (`provider_id`)
    REFERENCES `Providers`(`provider_id`)  -- set null if no provider
    ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `Patients`
--

INSERT INTO `Patients` (`patient_id`, `first_name`, `last_name`, `date_of_birth`, `gender`, `address`, `zip_code`, `phone_number`, `email`, `provider_id`) VALUES
(1, 'Jon', 'Snow', '1993-02-28', 'Male', '123 Harington Dr', '12345', '123-456-7890', 'jon@targaryen.com', 1),
(2, 'Jaime', 'Lannister', '1983-08-23', 'Male', '123 Lannister Ct', '54321', '098-765-4321', 'eyeluvcersei@lannister.net', 2),
(3, 'Eddard', 'Stark', '1967-07-04', 'Male', '123 Chopping Block Dr', '55555', '555-555-5555', NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `Prescriptions`
--

DROP TABLE IF EXISTS `Prescriptions`;
CREATE TABLE `Prescriptions` (
  `prescription_id` int(11) UNIQUE NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `standard_dose` varchar(45) NOT NULL,
  `medication_route_id` int(11) NOT NULL,
  `medication_class_id` int(11) NOT NULL,
  PRIMARY KEY (`prescription_id`),
  FOREIGN KEY (`medication_route_id`)
    REFERENCES `MedicationRoutes`(`medication_route_id`)
    ON DELETE CASCADE,
  FOREIGN KEY (`medication_class_id`)
    REFERENCES `MedicationClasses`(`medication_class_id`)
    ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `Prescriptions`
--

INSERT INTO `Prescriptions` (`prescription_id`, `name`, `standard_dose`, `medication_route_id`, `medication_class_id`) VALUES
(1, 'Zofran', '4 mg', 1, 2),
(2, 'Metoprolol', '100 mg', 1, 6),
(3, 'Ibuprofen', '400 mg', 1, 1),
(4, 'Keflex', '250 mg', 1, 3),
(5, 'Toradol', '10 mg', 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `Providers`
--

DROP TABLE IF EXISTS `Providers`;
CREATE TABLE `Providers` (
  `provider_id` int(11) UNIQUE NOT NULL AUTO_INCREMENT,
  `first_name` varchar(45) NOT NULL,
  `last_name` varchar(45) NOT NULL,
  `credential_id` int(11) NOT NULL,
  `date_of_birth` date DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `zip_code` varchar(10) DEFAULT NULL,
  `phone_number` varchar(15) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`provider_id`),
  FOREIGN KEY (`credential_id`)
    REFERENCES `Credentials`(`credential_id`)
    ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `Providers`
--

INSERT INTO `Providers` (`provider_id`, `first_name`, `last_name`, `credential_id`, `date_of_birth`, `gender`, `address`, `zip_code`, `phone_number`, `email`) VALUES
(1, 'Tony', 'Stark', 1, '1970-05-29', 'Male', 'Malibu Point 10880', '90265', '212-970-4133', 'tstark@jarvis.com'),
(2, 'Bruce', 'Wayne', 2, '1972-04-17', 'Male', NULL, NULL, NULL, NULL),
(3, 'Frodo', 'Baggins', 3, NULL, 'Male', NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `Tests`
--

DROP TABLE IF EXISTS `Tests`;
CREATE TABLE `Tests` (
  `test_id` int(11) UNIQUE NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `test_type_id` int(11) NOT NULL,
  PRIMARY KEY (`test_id`),
  FOREIGN KEY (`test_type_id`)
    REFERENCES `TestTypes`(`test_type_id`)
    ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `Tests`
--

INSERT INTO `Tests` (`test_id`, `name`, `test_type_id`) VALUES
(1, 'CBC', 1),
(2, 'CMP', 1),
(3, 'UA', 1),
(4, 'XR Chest', 2),
(5, 'CT Head', 3),
(6, 'US Abdominal', 4);

-- --------------------------------------------------------

--
-- Table structure for table `TestTypes`
--

DROP TABLE IF EXISTS `TestTypes`;
CREATE TABLE `TestTypes` (
  `test_type_id` int(11) UNIQUE NOT NULL AUTO_INCREMENT,
  `type` varchar(45) NOT NULL,
  PRIMARY KEY (`test_type_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `TestTypes`
--

INSERT INTO `TestTypes` (`test_type_id`, `type`) VALUES
(1, 'Lab'),
(2, 'X-Ray'),
(3, 'CT Scan'),
(4, 'Ultrasound');

-- --------------------------------------------------------

--
-- Table structure for table `VisitDiagnoses`
--

DROP TABLE IF EXISTS `VisitDiagnoses`;
CREATE TABLE `VisitDiagnoses` (
  `visit_diagnosis_id` int(11) UNIQUE NOT NULL AUTO_INCREMENT,
  `visit_id` int(11) NOT NULL,
  `diagnosis_id` int(11) NOT NULL,
  PRIMARY KEY (`visit_diagnosis_id`),
  FOREIGN KEY (`visit_id`)
    REFERENCES `Visits`(`visit_id`)
    ON DELETE CASCADE,
  FOREIGN KEY (`diagnosis_id`)
    REFERENCES `Diagnoses`(`diagnosis_id`)
    ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `VisitDiagnoses`
--

INSERT INTO `VisitDiagnoses` (`visit_diagnosis_id`, `visit_id`, `diagnosis_id`) VALUES
(1, 3, 3),
(2, 1, 8),
(3, 2, 9);

-- --------------------------------------------------------

--
-- Table structure for table `VisitMedications`
--

DROP TABLE IF EXISTS `VisitMedications`;
CREATE TABLE `VisitMedications` (
  `visit_medication_id` int(11) UNIQUE NOT NULL AUTO_INCREMENT,
  `visit_id` int(11) NOT NULL,
  `medication_id` int(11) NOT NULL,
  `dose_administered` varchar(45) NOT NULL,
  PRIMARY KEY (`visit_medication_id`),
  FOREIGN KEY (`visit_id`)
    REFERENCES `Visits`(`visit_id`)
    ON DELETE CASCADE,
  FOREIGN KEY (`medication_id`)
    REFERENCES `Medications`(`medication_id`)
    ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `VisitMedications`
--

INSERT INTO `VisitMedications` (`visit_medication_id`, `visit_id`, `medication_id`, `dose_administered`) VALUES
(1, 1, 4, '1000 mg'),
(2, 2, 1, '8 mg'),
(3, 3, 3, '100 mg');

-- --------------------------------------------------------

--
-- Table structure for table `VisitPrescriptions`
--

DROP TABLE IF EXISTS `VisitPrescriptions`;
CREATE TABLE `VisitPrescriptions` (
  `visit_prescription_id` int(11) UNIQUE NOT NULL AUTO_INCREMENT,
  `visit_id` int(11) NOT NULL,
  `prescription_id` int(11) NOT NULL,
  `dose_prescribed` varchar(45) NOT NULL,
  `instruction` varchar(200) NOT NULL,
  PRIMARY KEY (`visit_prescription_id`),
  FOREIGN KEY (`visit_id`)
    REFERENCES `Visits`(`visit_id`)
    ON DELETE CASCADE,
  FOREIGN KEY (`prescription_id`)
    REFERENCES `Prescriptions`(`prescription_id`)
    ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `VisitPrescriptions`
--

INSERT INTO `VisitPrescriptions` (`visit_prescription_id`, `visit_id`, `prescription_id`, `dose_prescribed`, `instruction`) VALUES
(1, 3, 5, '10 mg', 'Please take one tablet every 8 hours, as needed for pain.'),
(2, 1, 3, '800 mg', 'Please take one tablet every 8 hours, as needed for fever/pain.'),
(3, 1, 4, '250 mg', 'Please take one tablet every twice daily.'),
(4, 2, 1, '4 mg', 'Please take one tablet every 6-8 hours, as needed for nausea/vomiting.');

-- --------------------------------------------------------

--
-- Table structure for table `Visits`
--

DROP TABLE IF EXISTS `Visits`;
CREATE TABLE `Visits` (
  `visit_id` int(11) UNIQUE NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `reason_for_visit` varchar(200) NOT NULL,
  `patient_id` int(11) NOT NULL,
  `provider_id` int(11) NOT NULL,
  `nurse_id` int(11) NOT NULL,
  PRIMARY KEY (`visit_id`),
  FOREIGN KEY (`patient_id`)
    REFERENCES `Patients`(`patient_id`)
    ON DELETE CASCADE,
  FOREIGN KEY (`provider_id`)
    REFERENCES `Providers`(`provider_id`)
    ON DELETE CASCADE,
  FOREIGN KEY (`nurse_id`)
    REFERENCES `Nurses`(`nurse_id`)
    ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `Visits`
--

INSERT INTO `Visits` (`visit_id`, `date`, `reason_for_visit`, `patient_id`, `provider_id`, `nurse_id`) VALUES
(1, '2022-07-04', 'cough, fever', 2, 3, 2),
(2, '2022-07-11', 'vomiting, diarrhea', 1, 2, 1),
(3, '2022-07-01', 'headache, dizziness', 3, 1, 3);

-- --------------------------------------------------------

--
-- Table structure for table `VisitTestResults`
--

DROP TABLE IF EXISTS `VisitTestResults`;
CREATE TABLE `VisitTestResults` (
  `visit_test_result_id` int(11) UNIQUE NOT NULL AUTO_INCREMENT,
  `visit_id` int(11) NOT NULL,
  `test_id` int(11) NOT NULL,
  `result` tinyint(4) NOT NULL,
  `detail` text NOT NULL,
  PRIMARY KEY (`visit_test_result_id`),
  FOREIGN KEY (`visit_id`)
    REFERENCES `Visits`(`visit_id`)
    ON DELETE CASCADE,
  FOREIGN KEY (`test_id`)
    REFERENCES  `Tests`(`test_id`)
    ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `VisitTestResults`
--

INSERT INTO `VisitTestResults` (`visit_test_result_id`, `visit_id`, `test_id`, `result`, `detail`) VALUES
(1, 1, 1, 0, 'Normal results.'),
(2, 1, 4, 1, 'Abnormal results, COVID-19 Pneumonia.'),
(3, 3, 5, 0, 'Normal results, no acute changes.'),
(4, 2, 2, 1, 'Abnormal results, potassium (2.3).'),
(5, 2, 6, 0, 'Normal results.');

--
-- Indexes for dumped tables
--

COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

SET FOREIGN_KEY_CHECKS=1;
SET AUTOCOMMIT=1;
COMMIT;