from django.conf.urls import url
from first_app import views

urlpatterns = [
    url(r'^&',views.login,name='login'),
   # url(r'^&',views.student,name='student'),
   #  url(r'^&',views.Chat,name='Chat'),
   #  url(r'^&',views.BookAppointment,name='BookAppointment'),
   # url(r'^&',views.GetCourseInfo,name='GetCourseInfo'),

]