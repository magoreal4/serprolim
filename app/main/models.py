from django.contrib.admin import options
from django.db import models

class Banner(models.Model):
    name = models.CharField("name", max_length=50)
    titulo_h1 = models.CharField("titulo", max_length=50)
    titulo_h2 = models.CharField("slogan", max_length=50)
    imagebg = models.ImageField("imagenbg", upload_to='background', height_field=None, width_field=None, max_length=None)
    imagemain = models.ImageField("imagenmain", upload_to='imagemain', height_field=None, width_field=None, max_length=None)
    display = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = "Banner"
        verbose_name_plural = "Banners"
     
    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("Fondo_detail", kwargs={"pk": self.pk})

class Cliente(models.Model):
    titulo = models.CharField("titulo", max_length=50)
    resumen = models.CharField("resumen", max_length=250, default="", blank=True)
    imagen = models.ImageField("imagen", upload_to='clientes', height_field=None, width_field=None, max_length=None, null=True, blank=True )
    display = models.BooleanField(default=True)
    order = models.IntegerField("order", default=0)
    
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ['order'] 

    def __str__(self):
        return self.titulo

class Faq(models.Model):
    pregunta = models.TextField("titulo", max_length=350)
    respuesta = models.TextField("resumen", max_length=1000)

    class Meta:
        verbose_name = "Faq"
        verbose_name_plural = "Faqs"

    def __str__(self):
        return self.pregunta

    # def get_absolute_url(self):
    #     return reverse("Faq_detail", kwargs={"pk": self.pk})
