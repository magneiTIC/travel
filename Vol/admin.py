from django.contrib import admin
from .models import Vol
from .models import Trajet
from .models import Compagnie
# Register your models here.

admin.site.register(Vol)
admin.site.register(Trajet)
admin.site.register(Compagnie)