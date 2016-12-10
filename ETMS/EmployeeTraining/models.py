from __future__ import unicode_literals

from django.db import models

# Create your models here.
class EmployeeTraining(models.Model):
    lname = models.TextField(max_length=30)
    fname = models.TextField(max_length=30)
    email = models.TextField(max_length=50)
    DOB = models.DateTimeField('Date of birth')
    hireDate = models.DateTimeField('Hire date')
    street = models.TextField(max_length=30)
    city = models.TextField(max_length=30)
    state = models.TextField(max_length=2)
    zip_code = models.IntegerField()
    empPassword = models.TextField(max_length=30)

class Instructor(models.Model):
    instrLname = models.TextField(max_length=30)
    instrFname = models.TextField(max_length=30)
    instrPhone = models.IntegerField()
    specialty = models.TextField(max_length=30)
    instrPassword = models.TextField(max_length=30)

class Course(models.Model):
    crs_Title = models.TextField(max_length=30)
    crs_Type = models.TextField(max_length=30)
    crs_Description = models.TextField(max_length=3000)
    Instructor = models.ForeignKey(Instructor)


class GradeScore(models.Model):
    score = models.IntegerField()

class Training(models.Model):
    EmployeeTraining = models.ForeignKey(EmployeeTraining)
    appr_Date = models.DateTimeField('Approve Date')
    Course= models.ForeignKey(Course)
    section = models.TextField(max_length=2)
    GradeScore = models.ForeignKey(GradeScore)