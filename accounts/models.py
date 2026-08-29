from django.contrib.auth.models import AbstractUser
from django.db import models
from Base.models import BaseModel
from managers import UserManager

class Role(BaseModel):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Role"
        verbose_name_plural = "Roles"

    def __str__(self):
        return self.name
    
class User(AbstractUser, BaseModel):
    role = models.ForeignKey(
        Role,
        on_delete=models.PROTECT,
        related_name="users",
    )    
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['role']
    
    objects = UserManager()

