from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class DatosExtra(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    biografia = RichTextField(max_length=300)
    avatar = models.ImageField(upload_to="avatares", null=True, blank=True)