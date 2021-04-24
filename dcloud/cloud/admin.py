from django.contrib import admin
from .models import UserPartition,Folder,File
# Register your models here.
admin.site.register(UserPartition)
admin.site.register(Folder)
admin.site.register(File)
