from django.contrib import auth
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response

from EmployeeTraining.models import *


# Create your views here.
def login(request):
    c = {}
    c.update(request)
    return render(request, 'login.html', c)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    type = request.POST.get('type', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        if type=="employee":
            auth.login(request, user)
            return HttpResponseRedirect('/employee/')
        elif type=="instructor":
            auth.login(request, user)
            return HttpResponseRedirect('/instructor/')
    else:
        return HttpResponseRedirect('/invalid/')

def employee(request):
    args = {}
    args.update(request)
    args['userID'] = request.user.username
    args['Courses'] = Course.objects.all()
    args['Trainings'] = Training.objects.all()
    return render_to_response('employee.html', args)

def instructor(request):
    args = {}
    args.update(request)
    args['userID'] = request.user.username
    args['Courses'] = Course.objects.all()
    args['Trainings'] = Training.objects.all()
    return render_to_response('instructor.html', args)

def invalid_login(request):
    return render_to_response('invalid_login.html')

def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')

def employeeRequest(request):
    employees = EmployeeTraining.objects.all()
    result = ""
    for employee in employees:
        result = result + employee.lname + " "
        result = result + employee.fname + ","
        result = result + employee.email + ","
        result = result + str(employee.DOB) + ","
        result = result + str(employee.hireDate) + ","
        result = result + employee.street + " "
        result = result + employee.city + " "
        result = result + employee.state + " "
        result = result + str(employee.zip_code) + ","
        result = result + str(employee.empPassword) + ";"
    return HttpResponse(result)

def instructorRequest(request):
    instructors = Instructor.objects.all()
    result = ""
    for instructor in instructors:
        result = result + instructor.instrLname + " "
        result = result + instructor.instrFname + ","
        result = result + str(instructor.instrPhone) + ","
        result = result + instructor.specialty + ","
        result = result + str(instructor.instrPassword) + ";"
    return HttpResponse(result)

def search_Course(request):
    if request.method == "POST":
        search_text = request.POST['search_text']
    else:
        search_text = ''

    Courses = Course.objects.filter(crs_Title__contains=search_text)

    return render_to_response('ajax_search.html', {'Courses' : Courses})

def courseDetail(request, Course_id=1):
    return render_to_response('Course.html',
                              {'Course': Course.objects.get(id=Course_id)})

def addCourse(request):
    title = request.GET["title"]
    description = request.GET["description"]
    level = request.GET["level"]
    phone = int(request.GET["phone"])
    inst = Instructor.objects.filter(instrPhone=phone)[0]
    newCourse = Course(crs_Title=title, crs_Type=level, crs_Description=description)
    newCourse.Instructor = inst
    newCourse.save()
    return HttpResponse("OK")
