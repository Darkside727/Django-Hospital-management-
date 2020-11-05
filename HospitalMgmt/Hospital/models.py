from django.db import models

# Create your models here.

class Doctor(models.Model):

    Name = models.CharField(max_length=50)
    Phone = models.IntegerField()
    Specialization = models.CharField(max_length=50)

    def __str__(self):
        return self.Name

class Patient(models.Model):

    Name = models.CharField(max_length=50)
    Gender = models.CharField(max_length=10)
    Phone = models.IntegerField(null=True)
    Address = models.CharField(max_length=100)

    def __str__(self):
        return self.Name


class Appointment(models.Model):

    Doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    Patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    Date1 = models.DateField()
    Time1 = models.TimeField()

    def __str__(self):
        return self.Doctor.Name + " " + self.Patient.Name

