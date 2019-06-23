#from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# Create your views here.
def index(request):
    """ Vista para atender la petición de la url / """
    #return HttpResponse("<h2>Soy la página de inicio! Soy el amor te tu vida!</h2>")
    return render(request,'designer/designer.html')
