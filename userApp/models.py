from django.db import models

# Create your models here.
class UserAddModel(models.Model):
    """Model definition for UserAddModel."""

    name = models.CharField(max_length=100,default="")
    image = models.CharField(max_length=100,default="")
    email = models.CharField(max_length=100,default="")
    password = models.CharField(max_length=100,default="")
    

    class Meta:
        """Meta definition for UserAddModel."""

        verbose_name = 'UserAddModel'
        verbose_name_plural = 'UserAddModels'

    def __str__(self):
        """Unicode representation of UserAddModel."""
        pass
