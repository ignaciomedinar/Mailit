from django.contrib import admin
from .models import Tipousuario, Empresa, Usuario, Proyecto, Target, Assets, eMail

# Register your models here.


class TipousuarioAdmin(admin.ModelAdmin):
    """se sobre escribe lo que hace __str__"""
    list_display = ("id", "tipousuario")
admin.site.register(Tipousuario, TipousuarioAdmin)


class EmpresaAdmin(admin.ModelAdmin):
    """se sobre escribe lo que hace __str__"""
    list_display = ("id", "empresa")
admin.site.register(Empresa, EmpresaAdmin)


class UsuarioAdmin(admin.ModelAdmin):
    """se sobre escribe lo que hace __str__"""
    list_display = ("id", "nombre", "apellidos", "edad", "genero", "direccion")
admin.site.register(Usuario, UsuarioAdmin)


class ProyectoAdmin(admin.ModelAdmin):
    """se sobre escribe lo que hace __str__"""
    list_display = ("id", "nombreProyecto")
admin.site.register(Proyecto, ProyectoAdmin)


class TargetAdmin(admin.ModelAdmin):
    """se sobre escribe lo que hace __str__"""
    list_display = ("id", "target")
admin.site.register(Target, TargetAdmin)


class AssetsAdmin(admin.ModelAdmin):
    """se sobre escribe lo que hace __str__"""
    list_display = ("id", "assetName")
admin.site.register(Assets, AssetsAdmin)

class eMailAdmin(admin.ModelAdmin):
    """se sobre escribe lo que hace __str__"""
    list_display = ("id", "LLN")
admin.site.register(eMail, eMailAdmin)
