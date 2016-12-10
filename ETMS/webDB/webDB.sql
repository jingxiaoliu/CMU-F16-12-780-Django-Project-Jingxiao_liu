DROP TABLE employee           CASCADE CONSTRAINTS;
DROP TABLE training           CASCADE CONSTRAINTS; 
DROP TABLE course             CASCADE CONSTRAINTS; 
DROP TABLE instructor         CASCADE CONSTRAINTS; 
DROP TABLE grade_score        CASCADE CONSTRAINTS;

CREATE TABLE employee
(emp_ID     NUMBER(5),
 emp_Lname  VARCHAR2(30),
 emp_Fname  VARCHAR2(30),
 email      VARCHAR2(30),
 DOB        DATE DEFAULT SYSDATE,
 hire_Date  DATE DEFAULT SYSDATE,
 street     VARCHAR2(30),
 city       VARCHAR2(30),
 state      VARCHAR2(2),
 zip_code   NUMBER(5),
 password   VARCHAR2(30),
 CONSTRAINT employee_ID_PK PRIMARY KEY (emp_ID),
 CONSTRAINT employ_dates_CK CHECK (DOB <= hire_Date),
 CONSTRAINT manufacturer_email_CK CHECK (email LIKE '%@%.%')
);

CREATE TABLE instructor
(instr_ID       NUMBER(5),
 instr_Lname    VARCHAR2(30),
 instr_Fname    VARCHAR2(30),
 instr_Phone    NUMBER(10),
 specialty      VARCHAR2(30),
 password   VARCHAR2(30),
 CONSTRAINT instructor_ID_PK PRIMARY KEY (instr_ID)
);

CREATE TABLE course
(crs_ID         NUMBER(5),
 crs_Title      VARCHAR2(50),
 crs_Type       VARCHAR2(30),
 instr_ID       NUMBER(5),
 CONSTRAINT course_ID_PK PRIMARY KEY (crs_ID),
 CONSTRAINT course_instrID_FK FOREIGN KEY (instr_ID) REFERENCES instructor (instr_ID)
);

CREATE TABLE grade_score
(grade   VARCHAR2(2) NOT NULL,
 score   NUMBER(5) NOT NULL,
 CONSTRAINT grade_scoreID_PK PRIMARY KEY (grade),
 CONSTRAINT grade_scoregrade_CK CHECK (grade IN ('A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'R')),
 CONSTRAINT grade_scorescore_CK CHECK ((score <= 100) AND (score >= 0))
);

CREATE TABLE training
(TID            NUMBER(5),
 emp_ID         NUMBER(5),
 appr_Date      DATE,
 crs_ID         NUMBER(5),
 section        VARCHAR2(2),
 grade          VARCHAR2(2),
 CONSTRAINT training_TID_PK PRIMARY KEY (TID),
 CONSTRAINT training_crsID_FK FOREIGN KEY (crs_ID) REFERENCES course (crs_ID),
 CONSTRAINT training_grade_FK FOREIGN KEY (grade) REFERENCES grade_score (grade)
);

-- employee
INSERT INTO employee VALUES (10001,'Liu','Jingxiao','jingxial@andrew.cmu.edu','19-FEB-1994','01-AUG-2016','230 N Craig','Pittsburgh','PA',15213,'Jingxiao');
INSERT INTO employee VALUES (10002,'Agarwal','Ajay','aragarwa@andrew.cmu.edu','10-JAN-1994','02-AUG-2015','5710 Bartlett Street','Pittsburgh','PA',15217,'Ajay');
INSERT INTO employee VALUES (10003,'Ahn','Jungho','junghoa@andrew.cmu.edu','24-JUN-1994','01-AUG-2016','4750 Centre Avenue','Pittsburgh','PA',15213,'Jungho');
INSERT INTO employee VALUES (10004,'Aravind','Pritham','pvaravin@andrew.cmu.edu','09-APR-1994','02-AUG-2015','5738 Darlington','Pittsburgh','PA',15217,'Pritham');
INSERT INTO employee VALUES (10005,'Bakert','Andrew','abakert@andrew.cmu.edu','21-DEC-1994','01-AUG-2016','240 Melwood Ave','Pittsburgh','PA',15213,'Andrew');
INSERT INTO employee VALUES (10006,'Arora','Rajat','rarora1@cmu.edu','06-APR-1993','02-AUG-2015','5738 Darlington','Pittsburgh','PA',15217,'Rajat');
INSERT INTO employee VALUES (10007,'Chao','Shucheng','shuchenc@andrew.cmu.edu','21-NOV-1994','01-AUG-2016','230 N Craig','Pittsburgh','PA',15213,'Shucheng');
INSERT INTO employee VALUES (10008,'Chen','Dihong','dihonc@andrew.cmu.edu','09-APR-1994','02-AUG-2015','5738 Darlington','Pittsburgh','PA',15217,'Dihong');
INSERT INTO employee VALUES (10009,'Chen','Yiming','yimingc1@andrew.cmu.edu','21-SEP-1993','02-AUG-2015','5710 Bartlett Street','Pittsburgh','PA',15217,'Yiming');
INSERT INTO employee VALUES (10010,'Dennin','Luke','ldennin@andrew.cmu.edu','03-APR-1995','02-AUG-2015','5738 Darlington','Pittsburgh','PA',15217,'Luke');
INSERT INTO employee VALUES (10011,'Feng','Christopher','cf1@andrew.cmu.edu','27-FEB-1994','01-AUG-2016','4750 Centre Avenue','Pittsburgh','PA',15213,'Christopher');

-- instructor
INSERT INTO instructor VALUES (9501,'Szczypula','Janusz',4122686096,'Database','Janusz');
INSERT INTO instructor VALUES (9502,'Esmall','Zadeh',1881109911,'Management','Zadeh');
INSERT INTO instructor VALUES (9503,'Dwicedi','Neelam',4122687246,'Java','Neelam');
INSERT INTO instructor VALUES (9504,'Pastor','Lynne',4122686725,'Finance','Lynne');
INSERT INTO instructor VALUES (9505,'Alessandro','Acquisti',4122686101,'Economic','Acquisti');

--course
INSERT INTO course VALUES (95703,'Database Management','Graduate',9501);
INSERT INTO course VALUES (95705,'Telecommunications Management','Graduate',9502);
INSERT INTO course VALUES (95706,'Object Oriented Analysis and Design','Graduate',9503);
INSERT INTO course VALUES (95716,'Principles of Finance','Graduate',9504);
INSERT INTO course VALUES (95710,'Economic Analysis','Graduate',9505);

-- grade_score
INSERT INTO grade_score VALUES ('A',95);
INSERT INTO grade_score VALUES ('A-',90);
INSERT INTO grade_score VALUES ('B+',88);
INSERT INTO grade_score VALUES ('C',70);
INSERT INTO grade_score VALUES ('R',55);

--training
INSERT INTO training VALUES (001,10001,'29-AUG-2016',95703,'A1','A');
INSERT INTO training VALUES (002,10002,'29-AUG-2015',95705,'A1','A-');
INSERT INTO training VALUES (003,10003,'29-AUG-2016',95706,'A1','B+');
INSERT INTO training VALUES (004,10004,'29-AUG-2015',95716,'A1','A');
INSERT INTO training VALUES (005,10005,'29-AUG-2016',95710,'A1','R');
