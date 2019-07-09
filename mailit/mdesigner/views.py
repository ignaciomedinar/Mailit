from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Usuario, Tipousuario, Empresa

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
    #usuarios=Usuario.objects.get(id)
    #print(usuarios)
    return render (request, "mdesigner/dashboard.html",{
        #"usuarios": usuarios,
    })

@login_required()
def project_new_view(request):
    """ vista para project new"""
    if request.method == "POST":
        project_new = request.POST["nombreProyecto"]
        # LNN_new = request.POST["LNN"]
        print(project_new)

    return render(request, 'mdesigner/project_new.html')

@login_required()
def designer_view(request):
    """ Vista para atender la petición de la url / """
    return render (request, "mdesigner/designer.html")

@login_required()
def dashboard_reviewer_view(request):
    """ Vista para atender la petición de la url / """
    usuarios
    return render (request, "mdesigner/dashboardrev.html")

@login_required()
def dashboard_admin_view(request):
    """ Vista para atender la petición de la url / """
    if "Create_User" in request.POST: #dos botones, no sirve
        username_new = request.POST["username_signup"]
        email_new = request.POST["email_signup"]
        password_new = request.POST["password_confirmation"]
        print(username_new)
        print(email_new)
    elif 'Create_Company' in request.POST:
        company_new=request.POST["companyname_new"]
        short_company_new=request.POST["shortcompany_new"]
    elif 'Create_Target' in request.POST:
        company=request.POST["companyname_target"]
        target1=request.POST["targetname1"]
        target2=request.POST["targetname2"]
        target3=request.POST["targetname3"]
        target4=request.POST["targetname4"]
        target5=request.POST["targetname5"]
        target6=request.POST["targetname6"]
    else:
        print('no sirve')
    companies=Empresa.objects.all()
    print(companies)
    return render (request, "mdesigner/dashboardadmin.html",
        {
            "companies":companies,
        })

@login_required()
def designer_reviewer_view(request):
    """ Vista para atender la petición de la url / """
    if request.method == "POST":
        comments_new = request.POST["comments"]
        print(comments_new)
    return render (request, "mdesigner/designerrev.html")

@login_required()
def designer_admin_view(request):
    """ Vista para atender la petición de la url / """
    return render (request, "mdesigner/designeradmin.html")

@login_required()
def profile_view(request):
    """ Vista para atender la petición de la url / """
    return render (request, "mdesigner/profile.html")
