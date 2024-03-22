from django.forms import ModelForm
from .models import User

#clase que importa el modelo User con todos sus campos definidos en el modelo
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'