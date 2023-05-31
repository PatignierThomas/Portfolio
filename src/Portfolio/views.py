from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.mail import EmailMessage, get_connection, BadHeaderError

import app
from blog.forms import LogInForm
from .forms import EmailForm


def index(request):
    if request.method == 'POST':
        data = {
            "subject": request.POST.get("subject"),
            "message": request.POST.get("message"),
            "email_from": request.POST.get("email_from"),
            "recipient_list": ["patignier.contact@gmail.com", ]
        }
        form = EmailForm(data)
        if form.is_valid():
            email_from = form.cleaned_data["email_from"]
            subject = form.cleaned_data["subject"], email_from
            message = form.cleaned_data['message']
            try:
                with get_connection() as connection:
                    # subject = request.POST.get("subject")
                    # email_from = request.POST.get("mail")
                    recipient_list = ["patignier.contact@gmail.com", ]
                    # message = request.POST.get("message")
                    mail = EmailMessage(subject, message, email_from, recipient_list)
                    mail.send()
                    email_send = "Votre message a été envoyé avec succés."
                    messages.success(request, "Votre mail à bien été envoyé")
                    return HttpResponseRedirect("/home/#Acceuil")
                    # return render(request, "portfolio/index.html", {"email_send": email_send})
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
        else:
            erreur = form.errors
            return render(request, "Portfolio/index.html", {"erreur": erreur})

    return render(request, "Portfolio/index.html", )


def redirect_index(request):
    return redirect("home/")


def generator(request):
    if request.method == 'POST':
        result = [request.POST.get("taille"), request.POST.get("letters"), request.POST.get("digits"),
                  request.POST.get("symbols")]
        lenght, letters, digits, symbols = result[0], result[1], result[2], result[3]
        condition = app.generate_password(int(lenght), letters, digits, symbols)

        return render(request, "Portfolio/Generator.html", {"condition": condition})
    else:
        return render(request, "Portfolio/Generator.html")


def login_def(request):
    if request.method == 'POST':
        data = {
            "username": request.POST.get("username"),
            "password": request.POST.get("password"),
        }
        form = LogInForm(data)
        if form.is_valid():
            user = authenticate(request, username=data.get("username"), password=data.get("password"))
            if user is not None:
                login(request, user)
                return render(request, "Blog/blogpost_list.html")
            elif user is None:
                messages.error(request, "username or password not correct")
                return render(request, "Blog/login.html")
        else:
            erreur = form.errors
            return render(request, "blog/login.html", {"erreur": erreur})
            # return render(request, "Blog/login.html", {"global_error": "Cred invalid"})
    return render(request, "blog/login.html")

# def send_email(request):
#     if request.method == 'POST':
#
#         # subject = request.POST.get("subject")
#         # email_from = request.POST.get("mail")
#         # recipient_list = ["patignier.contacte@gmail.com", ]
#         # message = request.POST.get("message")
#
#         with get_connection(
#                 host=settings.EMAIL_HOST,
#                 port=settings.EMAIL_PORT,
#                 username=settings.EMAIL_HOST_USER,
#                 password=settings.EMAIL_HOST_PASSWORD,
#                 use_tls=settings.EMAIL_USE_TLS
#         ) as connection:
#             subject = request.POST.get("subject")
#             email_from = request.POST.get("mail")
#             recipient_list = [settings.EMAIL_HOST_USER, ]
#             message = request.POST.get("message")
#             EmailMessage(subject, message, email_from, recipient_list, connection=connection).send()
#     return render(request, 'home.html')
