from django.contrib import admin
from .models import UserPartition,Folder,File,Cfolder
# Register your models here.
admin.site.register(Cfolder)
admin.site.register(UserPartition)
admin.site.register(Folder)
admin.site.register(File)
