from django.contrib import admin

# Register your models here.
from .models import EventMaster, CategoryMaster

admin.site.register(EventMaster)
admin.site.register(CategoryMaster)
