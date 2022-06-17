from ast import Delete
import email
from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class UserType(models.Model):
    class Meta:
        db_table = "usertype"
    type = models.CharField("유저타입", max_length=128)

# Create your models here.

class UserModel(AbstractBaseUser):
    class Meta:
        db_table = "usermodel"
    email = models.EmailField("이메일", max_length=100)
    name = models.CharField("이름", max_length=128)
    user_type = models.OneToOneField(UserType, on_delete=models.Null, null=True)
    
    USERNAME_FIELD = 'email'

    is_admin = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.email}님의 프로필 입니다."
    @property
    def is_staff(self):
        return self.is_admin


