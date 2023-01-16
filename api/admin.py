from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(FormData)
admin.site.register(Addon)
admin.site.register(Plan)
