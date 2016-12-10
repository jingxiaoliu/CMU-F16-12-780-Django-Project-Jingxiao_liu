from django.contrib import admin
from EmployeeTraining.models import EmployeeTraining, Instructor, Course

# Register your models here.
admin.site.register(EmployeeTraining)
admin.site.register(Instructor)
admin.site.register(Course)