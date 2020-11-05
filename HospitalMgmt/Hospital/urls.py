from django.urls import path
from . import views
urlpatterns = [
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('', views.index, name="home"),
    path('login', views.login_view, name="login"),
    path('logout', views.logout_view, name="logout"),
    path('views_doctor', views.views_doctor, name="views_doctor"),
    path('check', views.check, name="check"),
    path('add_doctor', views.add_doctor, name="add_doctor"),
    path('remove(?P<int:pid>)', views.remove, name="remove"),
    path('add_patient', views.add_patient, name="add_patient"),
    path('views_patient', views.views_patient, name="views_patient"),
    path('remove_patient(?P<int:pid>)', views.remove_patient, name="remove_patient"),
    path('views_appoiment', views.views_appoiment, name="views_appoiment"),
    path('add_appoiment', views.add_appoiment, name="add_appoiment"),
    path('remove_appoiment(?P<int:pid>)', views.remove_appoiment, name="remove_appoiment"),

]
