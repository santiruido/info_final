from .models import Usuario
from django.db import transaction
from django.contrib.auth.forms import UserCreationForm


class RegistrarUsuariosForm(UserCreationForm):
    
    class Meta:
        model = Usuario
        fields= ['nombre','apellido','edad', 'username','password1','password2', 'email','imagen']
        
    @transaction.atomic
    def save(self):
        user                =super().save(commit=False)
        user.is_superuser   =False
        user.is_staff       =False
        user.save()
        return user 