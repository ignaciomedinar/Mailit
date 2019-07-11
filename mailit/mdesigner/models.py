from django.db import models
from django.conf import settings
import os

# Create your models here.
class Tipousuario(models.Model):
    """Defin la tabla del tipo de usuario"""
    tipo = models.CharField(max_length=2)
    # A - Admin, R - Revisor, D - Designer

    def __str__(self):
        """ Se define la representación en str para tipoUsuario """
        return self.tipo


class Empresa(models.Model):
    """Define la tabla del tipo de empresa"""
    # EMPRESA_OPCIONES = [
    #     ("BG", "BeyondGroup"),
    #     ("AMEX", "AmericanExpress"),
    #     ("NS", "NacioSushi"),
    #     ("CDC", "CirculoCredito"),
    #     ("BM", "Bocamel"),
    #     ("UCO", "PreparatoriaUco"),
    # ]
    empresa = models.CharField(max_length=100)
    short_empresa = models.CharField(max_length=6, null=True, blank=True)

    def __str__(self):
        """ Se define la representación en str para empresa """
        return self.empresa


class Usuario(models.Model):
    """Define la tabla tipo usuario"""
    #username = models.CharField(max_length=40)
    #nombre = models.CharField(max_length=40,null=True, blank= True)
    #apellidos = models.CharField(max_length=80,null=True, blank= True)
    profile_image = models.FileField(null=True, blank= True, default='avatar.png')
    #password = models.CharField(max_length=50)
    #email = models.EmailField(max_length=100)
    #group = models.ForeignKey(Tipousuario,on_delete=models.CASCADE, related_name="grupo",default="D")
    company = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name="company",null=True, blank=True)
    userdj = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
    )


    def __str__(self):
        """ Se define la representación en str para Usuario """
        return "{}".format(self.userdj)


class Proyecto(models.Model):
    """define la tabla proyecto"""
    ##usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nombreProyecto = models.CharField(max_length=60, unique=True)
    models.ManyToManyField(Usuario, related_name="username")
    #username = models.ForeignKey(Usuario,on_delete=models.CASCADE, related_name="user") #manytomany?
    fechaProyecto = models.DateField(auto_now_add=True)
##    fechaProyecto = models.DateField(auto_now_add=True)

    def __str__(self):
        """se define la representacion en str para Proyecto"""
        return "{}".format(self.nombreProyecto)

class Assets(models.Model):
    assetName = models.CharField(max_length=40)
    asset_image = models.FileField(null=True, blank= True)
    image_size = models.SmallIntegerField(null=True, blank= True)
    texto = models.CharField(max_length=300,null=True, blank= True)
    text_size = models.SmallIntegerField(null=True, blank= True)
    text_font = models.CharField(max_length=20,null=True, blank= True)
    text_color = models.CharField(max_length=20,null=True, blank= True)


class Target(models.Model):
    """define la tabla target"""
    # TARGET_OPCIONES = [
    #     ("CORP", "Corporate"),
    #     ("SM", "ShopSmall"),
    #     ("AU", "AllUsers"),
    #     ("PL", "Platinum"),
    #     ("CEN", "Centurion"),
    #     ("UCO", "PreparatoriaUco"),
    # ]
    nombreTarget = models.CharField(max_length=100)
    short_target = models.CharField(max_length=6, null=True, blank=True)
    proyecto = models.ForeignKey(Proyecto,on_delete=models.CASCADE, related_name="proyecto")
    LLN = models.CharField(max_length=40, null=True, blank=True)
    asset1 = models.ForeignKey(Assets,on_delete=models.CASCADE, related_name="asset1", null=True, blank=True) #manytomany
    asset2 = models.ForeignKey(Assets,on_delete=models.CASCADE, related_name="asset2", null=True, blank=True)
    asset3 = models.ForeignKey(Assets,on_delete=models.CASCADE, related_name="asset3", null=True, blank=True)
    asset4 = models.ForeignKey(Assets,on_delete=models.CASCADE, related_name="asset4", null=True, blank=True) #manytomany
    asset5 = models.ForeignKey(Assets,on_delete=models.CASCADE, related_name="asset5", null=True, blank=True)
    asset6 = models.ForeignKey(Assets,on_delete=models.CASCADE, related_name="asset6", null=True, blank=True)

    def __str__(self):
        """ Se define la representación en str para Target """
        return self.target


    def __str__(self):
        """ Se define la representación en str para Assets """
        return self.assetName


class eMail(models.Model):
    emailName = models.CharField(max_length=50) #preguntar si se puede project+target+date
    target = models.ForeignKey(Target,on_delete=models.CASCADE, related_name="target")
    finalhtml = models.CharField(max_length=2000)
    cssfolder = models.FileField(null=True, blank= True)
    ##fechaMail = models.DateField(auto_now_add=True)

    def __str__(self):
        """ Se define la representación en str para eMail """
        ##return self.LLN
        return str(self.id)
