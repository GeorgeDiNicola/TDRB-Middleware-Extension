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
   id_doctor INT,
   id_lab_worker INT,
   id_patient INT,
   date_exam DATE NOT NULL,
   glucose DECIMAL(5,1) NOT NULL,
   insulin DECIMAL(5,1) NOT NULL,
   leptin DECIMAL(5,1) NOT NULL,
   adiponecti DECIMAL(5,1) NOT NULL,
   resistin DECIMAL(5,1) NOT NULL,
   mcp_1 DECIMAL(5,1) NOT NULL,
   FOREIGN KEY (id_doctor) REFERENCES doctor(id),
   FOREIGN KEY (id_lab_worker) REFERENCES laboratory_worker(id),
   FOREIGN KEY (id_patient) REFERENCES patient(id)
);