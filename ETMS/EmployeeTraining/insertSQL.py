from EmployeeTraining.models import *

E10001 = EmployeeTraining(lname="Liu",fname="Jingxiao",email="jingxial@andrew.cmu.edu",DOB='1994-02-19',hireDate='2016-08-01',street="230 N Craig",city="Pittsburgh",state="PA",zip_code=15213,empPassword="E10001")
E10001.save()
E10002 = EmployeeTraining(lname="Agarwal",fname="Ajay",email="aragarwa@andrew.cmu.edu",DOB='1994-03-19',hireDate='2016-08-01',street="230 N Craig",city="Pittsburgh",state="PA",zip_code=15213,empPassword="E10002")
E10002.save()
E10003 = EmployeeTraining(lname="Ahn",fname="Jungho",email="jungho@andrew.cmu.edu",DOB='1994-04-19',hireDate='2016-08-01',street="230 N Craig",city="Pittsburgh",state="PA",zip_code=15213,empPassword="E10003")
E10003.save()
E10004 = EmployeeTraining(lname="Aravind",fname="Pritham",email="pritham@andrew.cmu.edu",DOB='1994-05-19',hireDate='2016-08-01',street="230 N Craig",city="Pittsburgh",state="PA",zip_code=15213,empPassword="E10004")
E10004.save()
E10005 = EmployeeTraining(lname="Bakert",fname="Andrew",email="andrew@andrew.cmu.edu",DOB='1994-06-19',hireDate='2016-08-01',street="230 N Craig",city="Pittsburgh",state="PA",zip_code=15213,empPassword="E10005")
E10005.save()

I9501 = Instructor(instrLname="Szczypula",instrFname="Janusz",instrPhone=4122686096,specialty="Database",instrPassword="I9501")
I9501.save()
I9502 = Instructor(instrLname="Esmall",instrFname="Zadeh",instrPhone=1881109911,specialty="Management",instrPassword="I9502")
I9502.save()
I9503 = Instructor(instrLname="Dwicedi",instrFname="Neelam",instrPhone=4122687246,specialty="Java",instrPassword="I9503")
I9503.save()
I9504 = Instructor(instrLname="Pastor",instrFname="Lynne",instrPhone=4122686725,specialty="Finance",instrPassword="I9504")
I9504.save()
I9505 = Instructor(instrLname="Alessandro",instrFname="Acquisti",instrPhone=4122686101,specialty="Economic",instrPassword="I9505")
I9505.save()

C95703 = Course(crs_Title="Database",crs_Type="Graduate",crs_Description="Databases systems are central to most organizations information systems strategies. At any organizational level, users can expect to have frequent contact with database systems. Therefore, skill in using such systems - understanding their capabilities and limitations, knowing how to access data directly or through technical specialists, knowing how to effectively use the information such systems can provide, and skills in designing new systems and related applications is a distinct advantage and necessity today. The Relational Database Management System (RDBMS) is one type of database systems that is most often used these days, and is the primary focus of this course. Further, to provide students with opportunity to apply the knowledge they learn from the lectures, various homework assignments, SQL assignments, and a database implementation project will be given.")
C95703.Instructor = I9501
C95703.save()
C95705 = Course(crs_Title="Telecommunications Management",crs_Type="Graduate",crs_Description="The purpose of this course is to provide an understanding of the key technical, managerial and policy issues in the effective development and use of broadband telecommunication by organizations. Discussion of technology, business and policy issues will be set in the context of services and contents. Topics covered will include basic concepts of telecommunication technology (data and voice), Internet and intranet technologies, issues related to the operational and strategic use of the technology, economics and policy aspects of telecommunication, and the changing structure of the telecommunications industry. A number of case studies will be included in the curriculum providing students the opportunity to apply the concepts to real world situations.")
C95705.Instructor = I9502
C95705.save()
C95706 = Course(crs_Title="Object Oriented Analysis and Design",crs_Type="Graduate",crs_Description="Large-scale software development has been described as one of the most difficult of human undertakings. This course examines the reasons for the inherent complexity of software construction and presents structured methods to deal effectively with it. The course will focus on the object-oriented approach for analysis and design. Students will gain an appreciation of the difference between writing programs and doing analysis and design. Problem formulation and decomposition (analysis) and solution building (design) will be covered. Students will work in small groups each group having the responsibility for analysis design and implementation of a software system. Case tools will be used in several stages of the development process. Knowledge of an Object-Oriented language such as Java or C++ is a pre-requisite for this course")
C95706.Instructor = I9503
C95706.save()
C95716 = Course(crs_Title="Principles of Finance",crs_Type="Graduate",crs_Description="A key aspect of getting a project going is getting it funded. Managers need to be able to convince C-level officers that investment in their project will make their company better off financially. This course focuses on financial techniques used in making business decisions. Fundamental principles of finance provide students with the basic tools necessary to analyze how managers evaluate investment and financing options. Students learn how to use a variety of capital budgeting techniques which shed light on the financial impact of choosing various projects.")
C95716.Instructor = I9504
C95716.save()
C95710 = Course(crs_Title="Economic Analysis",crs_Type="Graduate",crs_Description="This is a course in microeconomics and its implications for management and strategy - particularly (but not exclusively) in the context of information technology firms. Microeconomics, as discussed in this course, focuses on the models and methods by which managers can analyze their market and organizational environment to make optimal decisions. The key to such optimal decision- making is an understanding of the trade-offs in allocating scarce resources. The core models of microeconomics are fundamental to more applied areas of management such as strategy, marketing, production, and finance. The course will begin with an examination of the underlying structure and models of competitive markets, and the efficiency and welfare implications of those models. We will then examine economic models that describe firm output, pricing and entry/exit decisions.")
C95710.Instructor = I9505
C95710.save()

Ap = GradeScore(score=4.33)
Ap.save()
A = GradeScore(score=4.00)
A.save()
Am = GradeScore(score=3.67)
Am.save()
Bp = GradeScore(score=3.33)
Bp.save()
B = GradeScore(score=3.00)
B.save()
Bm = GradeScore(score=2.67)
Bm.save()
Cp = GradeScore(score=2.33)
Cp.save()
C = GradeScore(score=2.00)
C.save()
Cm = GradeScore(score=1.67)
Cm.save()
R = GradeScore(score=0.00)
R.save()

T001 = Training(appr_Date='2016-08-29',section="A1")
T001.EmployeeTraining = E10001
T001.Course = C95703
T001.GradeScore = Ap
T001.save()
T002 = Training(appr_Date='2015-08-29',section="A1")
T002.EmployeeTraining = E10002
T002.Course = C95705
T002.GradeScore = Am
T002.save()
T003 = Training(appr_Date='2015-08-29',section="A1")
T003.EmployeeTraining = E10003
T003.Course = C95706
T003.GradeScore = Bm
T003.save()
T004 = Training(appr_Date='2015-08-29',section="A1")
T004.EmployeeTraining = E10004
T004.Course = C95716
T004.GradeScore = C
T004.save()
T005 = Training(appr_Date='2016-08-29',section="A1")
T005.EmployeeTraining = E10005
T005.Course = C95710
T005.GradeScore = R
T005.save()

T006 = Training(appr_Date='2016-08-29',section="A1")
T006.EmployeeTraining = E10002
T006.Course = C95703
T006.GradeScore = Ap
T006.save()
T007 = Training(appr_Date='2015-08-29',section="A1")
T007.EmployeeTraining = E10003
T007.Course = C95705
T007.GradeScore = Bm
T007.save()
T008 = Training(appr_Date='2015-08-29',section="A1")
T008.EmployeeTraining = E10004
T008.Course = C95706
T008.GradeScore = Bm
T008.save()
T009 = Training(appr_Date='2015-08-29',section="A1")
T009.EmployeeTraining = E10005
T009.Course = C95716
T009.GradeScore = C
T009.save()
T010 = Training(appr_Date='2016-08-29',section="A1")
T010.EmployeeTraining = E10001
T010.Course = C95710
T010.GradeScore = A
T010.save()

T011 = Training(appr_Date='2016-08-29',section="A1")
T011.EmployeeTraining = E10003
T011.Course = C95703
T011.GradeScore = Ap
T011.save()
T012 = Training(appr_Date='2015-08-29',section="A1")
T012.EmployeeTraining = E10004
T012.Course = C95705
T012.GradeScore = C
T012.save()
T013 = Training(appr_Date='2015-08-29',section="A1")
T013.EmployeeTraining = E10005
T013.Course = C95706
T013.GradeScore = Bm
T013.save()
T014 = Training(appr_Date='2015-08-29',section="A1")
T014.EmployeeTraining = E10001
T014.Course = C95716
T014.GradeScore = C
T014.save()
T015 = Training(appr_Date='2016-08-29',section="A1")
T015.EmployeeTraining = E10002
T015.Course = C95710
T015.GradeScore = A
T015.save()