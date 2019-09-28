from django.contrib import admin
from .models import User,Client,Psychologist
# Register your models here.
admin.site.register(User)
admin.site.register(Psychologist)
admin.site.register(Client)