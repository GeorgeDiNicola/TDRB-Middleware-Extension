CREATE DATABASE moon_comparison;

USE moon_comparison;

create table doctor(
   id INT NOT NULL,
   name VARCHAR(25) NOT NULL,
   address VARCHAR(25) NOT NULL,
   date_of_birth DATE NOT NULL,
   specialty VARCHAR(25) NOT NULL,
   PRIMARY KEY ( id )
);

create table laboratory_worker(
   id INT NOT NULL,
   name VARCHAR(25) NOT NULL,
   address VARCHAR(25) NOT NULL,
   date_of_birth DATE NOT NULL,
   occupation VARCHAR(25) NOT NULL,
   PRIMARY KEY ( id )
);

create table patient(
   id INT NOT NULL,
   name VARCHAR(25) NOT NULL,
   address VARCHAR(25) NOT NULL,
   date_of_birth DATE NOT NULL,
   gender VARCHAR(6) NOT NULL,
   PRIMARY KEY ( id )
);

create table exam(
   id INT NOT NULL,
   id_doctor INT,
   id_lab_worker INT,
   id_patient INT,
   date_exam VARCHAR(10) NOT NULL,
   glucose DECIMAL(5,1) NOT NULL,
   insulin DECIMAL(5,1) NOT NULL,
   leptin DECIMAL(5,1) NOT NULL,
   adiponecti DECIMAL(5,1) NOT NULL,
   resistin DECIMAL(5,1) NOT NULL,
   mcp_1 DECIMAL(5,1) NOT NULL,
   PRIMARY KEY ( id )
);


insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (1, 16, 20, 93, '7/1/2021', 33.5, 25.4, 56.4, 10.8, 5.3, 0.4);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (2, 23, 16, 47, '5/19/2021', 12.9, 95.7, 93.5, 67.6, 95.5, 0.2);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (3, 1, 20, 94, '1/14/2022', 88.5, 19.5, 43.0, 31.6, 85.3, 0.2);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (4, 24, 13, 44, '6/28/2021', 22.5, 21.1, 3.6, 80.1, 73.4, 0.0);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (5, 24, 4, 53, '4/26/2022', 54.8, 47.3, 62.4, 96.2, 8.2, 0.4);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (6, 12, 1, 32, '3/19/2022', 85.2, 40.3, 23.1, 81.7, 28.7, 0.7);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (7, 19, 3, 90, '2/19/2022', 55.1, 34.8, 34.0, 4.0, 75.3, 0.6);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (8, 21, 19, 14, '10/9/2021', 39.5, 63.1, 44.1, 71.7, 91.6, 0.2);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (9, 26, 4, 12, '8/31/2021', 32.0, 91.9, 61.5, 62.2, 6.6, 0.6);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (10, 17, 17, 24, '10/6/2021', 69.9, 14.8, 98.4, 14.7, 90.1, 0.4);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (11, 3, 17, 39, '8/4/2021', 55.0, 50.1, 63.8, 30.7, 91.2, 0.1);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (12, 17, 10, 16, '4/25/2021', 73.6, 76.7, 76.0, 10.5, 51.5, 0.4);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (13, 7, 14, 61, '9/22/2021', 92.9, 41.0, 53.9, 32.6, 83.3, 0.8);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (14, 22, 3, 14, '12/10/2021', 92.1, 20.5, 56.0, 9.4, 53.1, 0.9);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (15, 30, 18, 9, '4/14/2022', 72.4, 61.1, 91.7, 47.7, 87.9, 0.4);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (16, 15, 4, 27, '7/25/2021', 51.1, 29.5, 52.0, 69.8, 36.2, 0.5);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (17, 12, 14, 11, '3/4/2022', 14.6, 65.7, 36.3, 51.4, 64.9, 0.1);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (18, 9, 15, 46, '5/17/2021', 45.8, 9.6, 10.8, 60.6, 77.9, 0.8);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (19, 16, 2, 35, '11/17/2021', 26.1, 20.6, 75.1, 89.7, 74.3, 1.0);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (20, 5, 2, 37, '1/2/2022', 66.8, 9.7, 45.7, 54.0, 44.3, 0.4);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (21, 20, 19, 84, '4/21/2021', 8.6, 21.8, 69.2, 97.7, 26.1, 0.3);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (22, 5, 6, 48, '10/24/2021', 7.1, 33.7, 68.9, 71.3, 99.8, 0.2);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (23, 9, 19, 2, '12/22/2021', 63.1, 34.2, 52.9, 13.1, 51.4, 0.7);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (24, 24, 20, 49, '4/16/2021', 77.0, 1.3, 74.4, 64.9, 25.6, 0.9);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (25, 8, 2, 76, '6/8/2021', 17.0, 88.9, 25.3, 18.7, 57.7, 0.7);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (26, 9, 16, 30, '2/18/2022', 60.0, 98.4, 0.8, 1.6, 75.0, 0.7);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (27, 20, 16, 37, '9/6/2021', 25.1, 72.6, 96.8, 53.4, 76.2, 0.4);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (28, 24, 14, 99, '3/3/2022', 26.2, 60.4, 94.2, 25.7, 10.0, 0.5);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (29, 27, 2, 43, '4/17/2022', 98.4, 83.4, 69.2, 31.5, 24.9, 0.6);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (30, 24, 9, 66, '6/27/2021', 98.5, 32.1, 1.4, 6.2, 24.4, 0.6);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (31, 5, 1, 96, '10/6/2021', 42.6, 92.1, 34.3, 61.5, 75.3, 0.8);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (32, 20, 8, 69, '4/25/2022', 69.5, 94.9, 75.5, 63.9, 38.0, 0.6);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (33, 14, 1, 75, '11/2/2021', 91.3, 34.7, 17.9, 23.5, 92.3, 0.6);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (34, 20, 17, 41, '9/16/2021', 41.1, 1.6, 7.0, 23.1, 39.1, 0.6);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (35, 18, 10, 60, '3/9/2022', 65.1, 88.3, 1.6, 77.7, 31.5, 0.2);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (36, 19, 10, 59, '10/19/2021', 63.6, 83.8, 13.5, 13.5, 70.9, 0.3);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (37, 8, 15, 1, '1/1/2022', 29.9, 48.5, 67.8, 33.7, 90.4, 0.0);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (38, 8, 1, 86, '1/30/2022', 7.7, 20.1, 73.5, 41.2, 67.9, 0.4);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (39, 1, 8, 63, '9/12/2021', 22.3, 16.7, 46.0, 60.4, 32.0, 1.0);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (40, 5, 16, 2, '12/1/2021', 59.3, 81.8, 64.1, 94.6, 3.1, 0.2);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (41, 21, 17, 68, '8/19/2021', 9.8, 10.7, 25.4, 99.6, 38.4, 0.5);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (42, 3, 20, 23, '6/23/2021', 99.4, 79.5, 3.4, 51.1, 35.9, 0.3);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (43, 26, 20, 20, '5/21/2021', 53.1, 85.3, 56.5, 80.8, 97.2, 0.5);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (44, 29, 4, 24, '6/11/2021', 3.2, 0.2, 87.4, 11.1, 14.2, 0.1);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (45, 25, 5, 83, '12/18/2021', 58.5, 87.8, 76.8, 70.9, 69.0, 1.0);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (46, 5, 9, 77, '7/31/2021', 17.0, 3.6, 53.7, 59.4, 7.6, 0.0);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (47, 5, 5, 69, '1/11/2022', 73.9, 32.8, 54.9, 63.2, 39.6, 0.3);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (48, 17, 3, 52, '10/9/2021', 79.0, 74.8, 82.6, 31.2, 95.0, 0.4);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (49, 30, 5, 80, '11/17/2021', 78.4, 36.7, 53.5, 24.2, 58.8, 0.7);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (50, 12, 19, 32, '1/3/2022', 27.7, 27.8, 1.8, 66.1, 49.8, 0.8);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (51, 7, 1, 33, '3/11/2022', 16.4, 64.6, 29.6, 94.8, 10.4, 0.0);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (52, 23, 5, 59, '11/24/2021', 59.6, 41.6, 42.3, 78.2, 70.5, 0.1);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (53, 21, 15, 19, '6/28/2021', 89.0, 14.3, 5.5, 2.3, 44.3, 0.1);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (54, 1, 10, 12, '5/16/2021', 82.5, 43.5, 47.2, 76.0, 95.8, 0.1);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (55, 19, 6, 32, '12/27/2021', 37.4, 55.9, 44.0, 10.0, 65.2, 0.7);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (56, 26, 20, 31, '4/6/2022', 1.4, 81.5, 92.4, 18.7, 93.3, 0.7);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (57, 29, 1, 42, '10/6/2021', 63.1, 97.0, 42.5, 67.9, 23.4, 0.1);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (58, 11, 17, 9, '5/23/2021', 56.2, 78.8, 81.8, 20.2, 60.4, 0.9);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (59, 18, 8, 83, '4/6/2022', 38.0, 10.3, 85.9, 7.5, 65.0, 0.3);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (60, 11, 18, 81, '2/27/2022', 52.3, 2.5, 97.7, 65.2, 86.5, 0.6);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (61, 23, 5, 58, '8/6/2021', 81.0, 10.4, 39.1, 99.2, 94.2, 0.6);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (62, 10, 2, 3, '5/12/2021', 57.5, 49.8, 46.0, 98.9, 7.9, 0.4);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (63, 4, 10, 12, '8/22/2021', 30.6, 69.6, 89.0, 38.9, 85.9, 1.0);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (64, 6, 10, 97, '9/3/2021', 71.6, 9.9, 89.8, 3.3, 60.3, 0.8);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (65, 14, 16, 53, '6/30/2021', 52.7, 46.0, 93.9, 7.4, 20.7, 0.8);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (66, 18, 6, 82, '2/8/2022', 50.7, 36.0, 41.2, 24.0, 76.1, 0.8);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (67, 24, 14, 37, '11/9/2021', 28.2, 96.7, 82.6, 11.0, 63.7, 0.4);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (68, 3, 1, 53, '3/30/2022', 44.7, 35.9, 89.5, 71.2, 21.0, 0.9);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (69, 23, 16, 65, '4/9/2022', 35.8, 0.6, 7.0, 58.4, 3.5, 0.5);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (70, 20, 2, 71, '5/22/2021', 26.6, 55.2, 81.7, 48.7, 97.3, 1.0);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (71, 27, 7, 61, '3/15/2022', 99.2, 92.9, 14.2, 60.9, 54.9, 0.7);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (72, 10, 16, 74, '1/11/2022', 51.5, 58.9, 84.6, 3.4, 65.7, 0.8);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (73, 16, 20, 53, '10/13/2021', 33.9, 74.1, 67.9, 65.2, 1.5, 0.8);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (74, 20, 10, 13, '11/25/2021', 7.6, 57.0, 63.1, 61.5, 42.8, 0.2);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (75, 13, 19, 72, '9/22/2021', 37.4, 27.1, 9.1, 0.3, 67.0, 0.0);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (76, 24, 2, 88, '12/23/2021', 37.3, 58.8, 16.8, 2.7, 94.6, 0.0);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (77, 21, 12, 17, '1/23/2022', 11.4, 26.8, 89.2, 41.6, 62.9, 0.6);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (78, 16, 19, 1, '8/6/2021', 41.5, 9.0, 46.0, 74.0, 93.7, 0.9);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (79, 12, 7, 67, '8/26/2021', 69.2, 60.5, 50.1, 63.9, 3.1, 0.1);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (80, 24, 5, 7, '3/21/2022', 68.9, 90.0, 90.4, 12.4, 15.0, 0.9);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (81, 12, 12, 62, '11/12/2021', 46.2, 80.7, 90.7, 46.6, 55.7, 0.4);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (82, 26, 5, 67, '3/8/2022', 76.0, 91.0, 23.0, 89.1, 97.1, 0.1);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (83, 13, 16, 25, '5/4/2021', 36.5, 31.7, 89.8, 60.5, 98.1, 0.5);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (84, 8, 12, 87, '1/1/2022', 23.0, 64.0, 16.3, 79.8, 41.7, 0.2);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (85, 22, 4, 49, '8/17/2021', 37.4, 47.8, 84.1, 31.1, 72.5, 0.3);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (86, 26, 16, 3, '9/25/2021', 22.4, 2.5, 29.6, 91.0, 51.7, 0.9);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (87, 8, 4, 52, '12/26/2021', 90.9, 61.5, 42.9, 82.2, 33.6, 0.2);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (88, 18, 18, 9, '11/4/2021', 74.8, 25.3, 36.2, 1.7, 77.3, 0.5);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (89, 28, 9, 78, '3/26/2022', 63.0, 4.1, 53.7, 15.7, 25.6, 0.1);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (90, 1, 20, 98, '4/20/2021', 39.4, 93.1, 4.1, 83.3, 9.6, 0.0);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (91, 16, 14, 47, '7/28/2021', 70.0, 58.1, 11.5, 3.8, 7.5, 0.6);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (92, 13, 8, 54, '4/21/2022', 74.4, 63.5, 31.5, 66.7, 89.9, 0.7);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (93, 30, 15, 62, '11/10/2021', 3.3, 50.7, 20.1, 88.1, 12.2, 0.3);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (94, 21, 4, 75, '6/6/2021', 4.0, 77.6, 6.0, 40.1, 12.9, 0.1);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (95, 15, 20, 46, '11/21/2021', 14.9, 8.4, 84.2, 1.7, 6.0, 0.2);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (96, 10, 17, 98, '12/6/2021', 29.3, 44.8, 12.8, 73.8, 75.7, 0.3);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (97, 10, 2, 76, '12/28/2021', 71.0, 97.9, 57.0, 35.4, 88.1, 0.3);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (98, 28, 13, 46, '6/10/2021', 34.1, 32.3, 90.2, 18.7, 0.7, 0.2);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (99, 9, 1, 3, '7/31/2021', 99.2, 82.5, 33.4, 57.5, 52.0, 0.1);
insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (100, 24, 6, 15, '3/6/2022', 56.1, 90.0, 54.2, 27.6, 60.7, 0.4);
