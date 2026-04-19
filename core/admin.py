
# Register your models here.
from django.contrib import admin
from .models import Cliente, Veiculo, Agendamento

admin.site.register(Cliente)
admin.site.register(Veiculo)
admin.site.register(Agendamento)