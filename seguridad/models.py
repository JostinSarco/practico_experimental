from django.db import models
from django.contrib.auth.models import User

# Si necesitas un perfil extra, puedes usar este modelo
class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Agrega más campos si necesitas

    def __str__(self):
        return self.user.username