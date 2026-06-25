from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class UserModel(AbstractUser):
    pass

class studentModel(models.Model):
    name = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=20,null=True)
    image = models.ImageField(upload_to='Media/Image',null=True)

    def __str__(self):
        return self.name
    
class FineModel(models.Model):
    title = models.CharField(max_length=300,null=True)
    amount = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.title
    
class ActionModel(models.Model):
    student = models.ForeignKey(
        studentModel,
        on_delete= models.CASCADE,
        null=True,
        related_name='stu_info'
    )
    fine = models.ForeignKey(
        FineModel,
        on_delete=models.SET_NULL,
        null=True,
        related_name='stu_fine',
    )
    created_by = models.ForeignKey(
    UserModel,
    on_delete=models.SET_NULL,
    null=True,
    related_name='action_user',
    )
    date = models.DateField(auto_now_add=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student} - {self.fine}"
