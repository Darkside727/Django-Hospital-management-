from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from .models import *
# Create your views here.

def check(request):
  return render(request, "check.html")

def about(request):
    if not request.user.is_staff:
        return redirect("login")
    return render(request, "about.html")


def contact(request):
    # if not request.user.is_staff:
    #     return redirect("login")
    return render(request, "contact.html")

def index(request):
    if not request.user.is_staff:
        return redirect("login")
    doctor = Doctor.objects.all()
    patient = Patient.objects.all()
    appointment = Appointment.objects.all()
    count_doctor = 0
    count_patient = 0
    count_appointment = 0
    for doc in doctor:
        count_doctor+= 1

    for doc in patient:
        count_patient+= 1

    for doc in appointment:
        count_appointment+= 1
    count_pass = {
        "doctor_count" : count_doctor,
        "patient_count" : count_patient,
        "appoinment_count" : count_appointment,

    }
    return render(request, "index.html", count_pass)

def login_view(request):
   error = ""
   if request.method == "POST":
       Name = request.POST["name"]
       password = request.POST["password"]
       user  = authenticate(username = Name, password = password)
       try:
           if user.is_staff:
               login(request, user)
               error = "yes"
           else:
               error = "no"
       except:
           error = "no"

   dic = {"error" : error}
   return render(request, 'login.html', dic)



def logout_view(request):
    if not request.user.is_staff:
        return redirect("login")
    logout(request)
    return redirect("login")



def views_doctor(request):
    if not request.user.is_staff:
        return redirect("login")
    viewsdco = Doctor.objects.all()
    passdoctor = {
    'viewsdoctor' : viewsdco
    }
    return render(request, "doctor.html", passdoctor)


def add_doctor(request):
   error = ""
   if request.method == "POST":
       Name = request.POST["name"]
       contact = request.POST["contact"]
       special = request.POST["special"]
       try:
           Doctor.objects.create(Name=Name, Phone=contact, Specialization=special)
           error = "yes"
       except:
            error = "no"

   dic = {"error" : error}
   return render(request, 'adddoctor.html', dic)


def remove(request, pid):
  doctor = Doctor.objects.get(id=pid)
  doctor.delete()
  return redirect("views_doctor")



def views_patient(request):
    if not request.user.is_staff:
        return redirect("login")
    viewspatient = Patient.objects.all()
    passpatient = {
    'viewspatient' : viewspatient
    }
    return render(request, "view_patient.html", passpatient)


def add_patient(request):
   error = ""
   if request.method == "POST":
       Name = request.POST["name"]
       gender = request.POST["gender"]
       phone = request.POST["phone"]
       address = request.POST["address"]
       try:
           Patient.objects.create(Name=Name, Gender=gender, Phone=phone, Address=address)
           error = "yes"
       except:
            error = "no"

   dic = {"error" : error}

   return render(request, 'add_patient.html', dic)


def remove_patient(request, pid):
  patient = Patient.objects.get(id=pid)
  patient.delete()
  return redirect("views_patient")


def views_appoiment(request):
    if not request.user.is_staff:
        return redirect("login")
    viewsAppointment = Appointment.objects.all()
    passAppointment = {
    'viewsAppointment' : viewsAppointment
    }
    return render(request, "view_appoiment.html", passAppointment)


def add_appoiment(request):
   error = ""
   doctor1 = Doctor.objects.all()
   patient1 = Patient.objects.all()
   if request.method == "POST":
       doctor = request.POST["doctor"]
       patient = request.POST["paitent"]
       date = request.POST["date"]
       time = request.POST["time"]
       doctor_filter = Doctor.objects.filter(Name=doctor).first()
       patient_filter = Patient.objects.filter(Name=patient).first()
       try:
           Appointment.objects.create(Doctor=doctor_filter, Patient=patient_filter, Date1=date, Time1=time)
           error = "yes"
       except:
            error = "no"

   dic = {
   "error" : error,
   "doctor" : doctor1,
   "patient" : patient1
   }

   return render(request, 'add_appoiment.html', dic)


def remove_appoiment(request, pid):
  appointment = Appointment.objects.get(id=pid)
  appointment.delete()
  return redirect("views_appoiment")
