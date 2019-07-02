from django.db import models

# Create your models here.



class Tipousuario(models.Model):
    """Defin la tabla del tipo de usuario"""
    TIPO_USUARIO = [
        ("D", "Designer"),
        ("R", "Revizador"),
        ("A", "Administrador"),
    ]
    tipousuario = models.CharField(max_length=1, choices=TIPO_USUARIO)

    def __str__(self):
        """ Se define la representación en str para tipoUsuario """
        return self.tipousuario


class Empresa(models.Model):
    """Define la tabla del tipo de empresa"""
    EMPRESA_OPCIONES = [
        ("BG", "BeyondGroup"),
        ("AMEX", "AmericanExpress"),
        ("NS", "NacioSushi"),
        ("CDC", "CirculoCredito"),
        ("BM", "Bocamel"),
        ("UCO", "PreparatoriaUco"),
    ]
    empresa = models.CharField(max_length=5, choices=EMPRESA_OPCIONES)

    def __str__(self):
        """ Se define la representación en str para empresa """
        return self.empresa


class Usuario(models.Model):
    """Define la tabla tipo usuario"""
    nombre = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=80)
    edad = models.SmallIntegerField()
    GENERO_OPCIONES = [
        ("M", "Mujer"),
        ("H", "Hombre"),
    ]
    genero = models.CharField(max_length=1, choices=GENERO_OPCIONES)
    direccion = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        """ Se define la representación en str para Usuario """
        return "{} {}".format(self.nombre, self.apellidos)


class Proyecto(models.Model):
    """define la tabla proyecto"""
    ##usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nombreProyecto = models.CharField(max_length=60)
##    fechaProyecto = models.DateField(auto_now_add=True)

    def __str__(self):
        """se define la representacion en str para Proyecto"""
        return str(self.id)


class Target(models.Model):
    """define la tabla target"""
    TARGET_OPCIONES = [
        ("CORP", "Corporate"),
        ("SM", "ShopSmall"),
        ("AU", "AllUsers"),
        ("PL", "Platinum"),
        ("CEN", "Centurion"),
        ("UCO", "PreparatoriaUco"),
    ]
    target = models.CharField(max_length=5, choices=TARGET_OPCIONES)

    def __str__(self):
        """ Se define la representación en str para Target """
        return self.target


class Assets(models.Model):
    assetName = models.CharField(max_length=40)

    def __str__(self):
        """ Se define la representación en str para Assets """
        return self.assetName


class eMail(models.Model):
    LLN = models.CharField(max_length=40)
    ##fechaMail = models.DateField(auto_now_add=True)

    def __str__(self):
        """ Se define la representación en str para eMail """
        ##return self.LLN
        return str(self.id)
