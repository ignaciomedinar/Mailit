from django.contrib import admin
from .models import Tipousuario, Empresa, Usuario, Proyecto, Target, Assets, eMail

# Register your models here.


class TipousuarioAdmin(admin.ModelAdmin):
    """se sobre escribe lo que hace __str__"""
    list_display = ("id", "tipo")
admin.site.register(Tipousuario, TipousuarioAdmin)


class EmpresaAdmin(admin.ModelAdmin):
    """se sobre escribe lo que hace __str__"""
    list_display = ("id", "empresa", "short_empresa")
admin.site.register(Empresa, EmpresaAdmin)


class UsuarioAdmin(admin.ModelAdmin):
    """se sobre escribe lo que hace __str__"""
    list_display = ("id", "username", "nombre", "apellidos", "profile_image", "password", "email", "group", "company")#, "email")
admin.site.register(Usuario, UsuarioAdmin)


class ProyectoAdmin(admin.ModelAdmin):
    """se sobre escribe lo que hace __str__"""
    list_display = ("id", "nombreProyecto", "username", "fechaProyecto")
admin.site.register(Proyecto, ProyectoAdmin)


class TargetAdmin(admin.ModelAdmin):
    """se sobre escribe lo que hace __str__"""
    list_display = ("id", "nombreTarget", "short_target","proyecto", "LLN", "asset1", "asset2", "asset3", "asset4", "asset5", "asset6")
admin.site.register(Target, TargetAdmin)


class AssetsAdmin(admin.ModelAdmin):
    """se sobre escribe lo que hace __str__"""
    list_display = ("id", "assetName", "asset_image", "image_size", "texto", "text_size", "text_font", "text_color")
admin.site.register(Assets, AssetsAdmin)

class eMailAdmin(admin.ModelAdmin):
    """se sobre escribe lo que hace __str__"""
    list_display = ("id", "emailName", "target", "finalhtml", "cssfolder")
admin.site.register(eMail, eMailAdmin)
