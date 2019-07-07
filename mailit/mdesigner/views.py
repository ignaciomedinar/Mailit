from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Usuario, Tipousuario

import datetime

# Create your views here.


def index(request):
    """ Vista para atender la petición de la url / """
    return render (request, "mdesigner/index.html")


def login_user(request):
    """ Atiende las peticiones de GET /login/ """

    # Si hay datos vía POST se procesan
    if request.method == "POST":
        # Se obtienen los datos del formulario
        username = request.POST["username"]
        password = request.POST["password"]
        next = request.GET.get("next", "/dashboard/")
        print(username)
        acceso = authenticate(username=username, password=password)
        if acceso is not None:
            # Se agregan datos al request para mantener activa la sesión
            login(request, acceso)
            # Y redireccionamos a next
            return redirect(next)
        else:
            # Usuario malo
            msg = "Datos incorrectos, intente de nuevo!"
    else:
        # Si no hay datos POST
        msg = ""
    #tipoUsuarios= Tipousuario.object.all() #por qué no me deja
    return render(request, "registration/login.html",
        {
            "msg":msg,
            #"tipoUsuarios":tipoUsuarios,
        }
    )


def signup_user(request):
    """ Atiende las peticiones de GET /login/ """

    # Si hay datos vía POST se procesan
    if request.method == "POST":
        # Se obtienen los datos del formulario
        username = request.POST["username_signup"]
        name = request.POST["name_signup"]
        lastname = request.POST["lastname_signup"]
        username = request.POST["email_signup"]
        password = request.POST["password_signup"]
        password_confirmation = request.POST["password_confirmation"]
        next = request.GET.get("next", "/")
        acceso = authenticate(username=username, password=password)
        if acceso is not None:
            # Se agregan datos al request para mantener activa la sesión
            login(request, acceso)
            # Y redireccionamos a next
            return redirect(next)
        else:
            # Usuario malo
            msg = "Datos incorrectos, intente de nuevo!"
    else:
        # Si no hay datos POST
        msg = ""
    return render(request, "registration/signup.html",
        {
            "msg":msg,
        }
    )

@login_required()
def dashboard_view(request):
    """ Vista para atender la petición de la url / """
    return render (request, "mdesigner/dashboard.html")

@login_required()
def project_new_view(request):
    """ vista para project new"""
    #form = OptionForm()
    #options = Target.objects.filter()
    return render(request, 'mdesigner/project_new.html')

@login_required()
def designer_view(request):
    """ Vista para atender la petición de la url / """
    return render (request, "mdesigner/designer.html")

@login_required()
def dashboard_reviewer_view(request):
    """ Vista para atender la petición de la url / """
    return render (request, "mdesigner/dashboardrev.html")

@login_required()
def dashboard_admin_view(request):
    """ Vista para atender la petición de la url / """
    return render (request, "mdesigner/dashboardadmin.html")

@login_required()
def designer_reviewer_view(request):
    """ Vista para atender la petición de la url / """
    return render (request, "mdesigner/designerrev.html")

@login_required()
def designer_admin_view(request):
    """ Vista para atender la petición de la url / """
    return render (request, "mdesigner/designeradmin.html")
