from django.contrib.auth.models import AbstractUser
from django.db import models
from Base.models import BaseModel
from .managers import UserManager
from django.core.exceptions import ValidationError
import uuid
from time import timezone

class Role(BaseModel):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Role"
        verbose_name_plural = "Roles"

    def clean(self):
        super().clean()

        if Role.objects.filter(name__iexact=self.name).exclude(pk=self.pk).exists():
            raise ValidationError({
                "name": "A role with this name already exists."
            })

    def save(self, *args, **kwargs):
        self.full_clean()  # Runs clean() before saving
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class User(AbstractUser, BaseModel):
    username = None
    role = models.ForeignKey(
        Role,
        on_delete=models.PROTECT,
        related_name="users",
    )    
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = UserManager()

