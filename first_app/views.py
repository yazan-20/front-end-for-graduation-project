from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def login(request):
   #my_dict = {'insert_me':"Heloo Iam from views.py !,,,,context=my_dict"}
   return render(request,'login.html')

def student(request):
   #my_dict2 = {'insert2_me'}    
   return render(request,'student.html')

def BookAppointment(request):
   #my_dict3 = {'insert3_me'}    
   return render(request,'BookAppointment.html')

def Chat(request):
   #my_dict4 = {'insert4_me'}    
   return render(request,'Chat.html')

def GetCourseInfo(request):
   #my_dict5 = {'insert5_me'}   
   return render(request,'GetCourseInfo.html')


