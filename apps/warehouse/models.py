from django.db import models

from Base.models import BaseModel


class Warehouse(BaseModel):
    name = models.CharField(max_length=150)
    code = models.CharField(max_length=50, unique=True)
    address = models.TextField()
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name