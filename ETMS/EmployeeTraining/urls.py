from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^auth/$', views.auth_view, name='auth_view'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^employee/$', views.employee, name='employee'),
    url(r'^instructor/$', views.instructor, name='instructor'),
    url(r'^invalid/$', views.invalid_login, name='invalid_login'),
    url(r'^loadEmployee/$', views.employeeRequest, name='loadEmployee'),
    url(r'^loadInstructor/$', views.instructorRequest, name='loadInstructor'),
    url(r'^employee/search/$', views.search_Course, name='crouseSearch'),
    url(r'^employee/get/(?P<Course_id>\d+)/$',views.courseDetail, name='course'),
    url(r'^addCourse/', views.addCourse, name='addCourse'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)