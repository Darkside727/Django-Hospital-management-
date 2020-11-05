from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.core.mail import BadHeaderError, send_mail, EmailMessage
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.conf import settings
# Create your views here.


def Home(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    error = None
    if request.method == "POST":
        name = request.POST["txtName"]
        email = request.POST["txtEmail"]
        phn = request.POST["txtPhone"]
        mess = request.POST["txtMsg"]

        if name and email and phn and mess:
            try:
                send_mail(name, email, mess,["alialtaf1998@gmail.com"])
                error = "yes"
            except BadHeaderError:
                error = "Bad Email Formate"
        else:
            error = "Please Fill Contact Form activly"

    error = {"error" : error}

    return render(request, "contact.html", error)


def LoginView(request):
    error = ""
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["pass"]
        user = authenticate(email=email, password = password)
        try:
            login(user)
            error = "Accept"
        except:
            error = "None"
    error = {"error" : error}

    return render(request, "login.html", error)


def RegistrationView(request):
    error = ""
    if request.method == "POST":
        name = request.POST["uname"]
        email = request.POST["email"]
        contact = request.POST["contact"]
        password = request.POST["password"]
        confrim = request.POST["againpass"]

        if password == confrim:
            if User.objects.filter(username=name).exists():
                error = "UserName already"
            elif User.objects.filter(email=email).exists():
                error = "email already"
            else:
                user_data = User.objects.create_user(username = name, email = email, password = password)
                regis = User_registration.objects.create(user = user_data, Username=name, Email=email, Contact=contact, Password=password, confrim= confrim)
                error = "pass"
                # redirect("LoginView")
        else:
            error = "password"
        # return redirect("LoginView")
    messg = {"error" : error}
    return render(request, "singup.html", messg)


def playlist(request):
    all_data = Category.objects.all()
    dic = {"playlist" : all_data}
    # categories = Category.get_all()
    return render(request, "playlist.html", dic)


def video_course(request):
    # all_data = Category.objects.get(pk=pid)
    # data_list = Videos.objects.filter(cat=all_data)
    print(request.GET)
    dic = {}
    categoryId = request.GET["tutorials"]
    print("f")

    try:
        if categoryId:
            tutorials = Videos.objects.filter(cat=categoryId)

    except:
        video_url = request.GET["Videos"]
        get_specific_video = Videos.objects.get(pk=vid)
        unique_video = get_specific_video.video_upload

    # get_specific_video = Videos.objects.get(pk=vid)
    # unique_video = get_specific_video.video_upload
    if tutorials != "":
        dic = {"tutorials" : tutorials}
    else:
        dic = {"get" : unique_video, }


    # dic = {"all_data" : data_list}
    return render(request, "videos.html", dic)



# def spcific_video(request, vid):
#     all_data = Videos.objects.get(pk=vid)
#     myvideo = all_data.video_upload
#     dic = {"spvideo":myvideo}
#     return render(request, "videos.html", dic)

























# <!-- clie 6LcphcEZAAAAAGQESuEYEK2Iwkf0tVoEdYyB_OqE
#  -->

# <!-- serv 6LcphcEZAAAAABH8-ReFSGIpON2PgJ46pZ4EcREC
#  -->
# <!--  <link rel="stylesheet" href="{% static 'css/Login.css' %}"> -->






# <!--     <img src="{% static 'img/dark2.png' %}" class="imgset"> </img>
#  -->

