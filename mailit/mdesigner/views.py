from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User, Group
from .models import Usuario, Tipousuario, Empresa, Proyecto

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
        user = User.objects.get(username=username)
        grupo = user.groups.all()[0]
        grupon = user.groups.all()[0].name
        print("user : ",user)
        print("grupo : ",grupo)
        if grupo.name == "Designer":
            next = request.GET.get("next", "/dashboard/")
        elif grupo.name == "Administrator":
            next = request.GET.get("next","/dashboardadmin/")
            print("usuario: ", user)
        elif grupo.name == "Reviewer":
            next = request.GET.get("next","/dashboardrev/")
        else:
            msg = "El usuario no existe"
            next = request.GET.get("next","/login/")
            print("No lee los grupos ",grupo)

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
        email = request.POST["email_signup"]
        password = request.POST["password_signup"]
        password_confirmation = request.POST["password_confirmation"]
        user_image = request.FILES.get("profile_image")
        next = request.GET.get("next", "/dashboard/")
        group=Group.objects.get(name="Designer")

        if username and password and password_confirmation and email:
            if password== password_confirmation:
                if User.objects.filter(username=username).exists():
                    msg = "El usuario ya existe"
                else:
                    user = User(
                        username=username,
                        first_name=name,
                        last_name=lastname,
                        password= make_password(password),
                        email= email,
                    )
                    user.save()
                    user.groups.add(group)
                    if user_image:
                        usuario = Usuario(userdj=user, profile_image=user_image)
                    else:
                        usuario = Usuario(userdj=user)
                    usuario.save()
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
                msg="Contraseñas no coinciden!"
        else:
            msg="Datos incompletos!"

    else:
        # Si no hay datos POST
        msg = ""
    print("mensaje ", msg)
    return render(request, "registration/signup.html",
        {
            "msg":msg,
        }
    )

@login_required()
def dashboard_view(request):
    """ Vista para atender la petición de la url / """
    #usuario=Usuario.objects.get(pk=request.user.id)
    usuario=Usuario.objects.get(userdj=request.user)
    proyectos = Proyecto.objects.all()[:5]
    proyectos2 = Proyecto.objects.all()
    return render (request, "mdesigner/dashboard.html",{
        "usuario": usuario,
        "proyectos": proyectos,
        "proyectos2": proyectos2,
    })

@login_required()
def project_new_view(request):
    """ vista para project new"""
    if request.method == "POST":
        project_new = request.POST["nombreProyecto"]
        project= Proyecto(nombreProyecto=project_new)
        project.save()
        return redirect("/designer/")
    else:
        msn=""
    #print(project_new)

    return render(request, 'mdesigner/project_new.html')

@login_required()
#def designer_view(request, proyecto):
def designer_view(request):
    """ Vista para atender la petición de la url / """
    proyectos = Proyecto.objects.all()[:5]
    usuario=Usuario.objects.get(userdj=request.user)
    #grupo = usuario.groups.all()[0].name
    #nombreProyecto=Proyecto.objects.get(nombreProyecto=proyecto)
    return render (request, "mdesigner/designer.html",{
        "proyectos": proyectos,
        "usuario": usuario,
        #"grupo": grupo,
    })


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
    elif 'Assign' in request.POST:
        empresa = request.POST["company_assign"]
        usuario = request.POST["user_assign"]
    else:
        print('no sirve')
    companies=Empresa.objects.all()
    users=User.objects.all()
    print(companies)
    return render (request, "mdesigner/dashboardadmin.html",
        {
            "companies":companies,
            "users":users,
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
    if request.method=="POST":

        name = request.POST["name_signup"]
        lastname = request.POST["lastname_signup"]
        email = request.POST["email_signup"]
        password = request.POST["password_signup"]
        password_confirmation = request.POST["password_confirmation"]
        if not name:
            name=user.username
        if not lastname:
            lastname=user.lastname
        if not email:
            email=user.email
        user_image = request.FILES.get("profile_image")
        next = request.GET.get("next", "/dashboard/")
        if password== password_confirmation:
            user = User(
                username=username,
                first_name=name,
                last_name=lastname,
                password= make_password(password),
                email= email,
            )
            user.username.save()
            user.groups.add(group)
            if user_image:
                usuario = Usuario(userdj=user, profile_image=user_image)
            else:
                usuario = Usuario(userdj=user)
            usuario.save()

            print(name, email)
            #print(user)

            return redirect(next)
        else:
            msg="Contraseñas no coinciden!"
    else:
        msg=""
    return render (request, "mdesigner/profile.html")
