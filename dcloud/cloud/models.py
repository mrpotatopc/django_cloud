from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserPartition(models.Model):
    User = models.ForeignKey(User,on_delete=models.CASCADE)
    Name = modles.CharField(max_length=100)

    def __str__(self):
        return self.name

class Folder(models.Model):
    partition = models.ForeignKey(UserPartition,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class File(models.Model):
    Folder = models.ForeignKey(Folder,on_delete=models.CASCADE)
    file = models.FileField(upload_to=files)

    def __str__(self):
        return self.name

    def filename(self):
        return os.path.basename(self.file.name)        
