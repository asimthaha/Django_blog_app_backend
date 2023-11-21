from django.db import models

# Create your models here.
class BlogAddModel(models.Model):
    """Model definition for BlogAddModel."""

    userid = models.IntegerField()
    title = models.CharField(max_length=100,default="")
    post = models.CharField(max_length=100,default="")
    

    class Meta:
        """Meta definition for BlogAddModel."""

        verbose_name = 'BlogAddModel'
        verbose_name_plural = 'BlogAddModels'

    def __str__(self):
        """Unicode representation of BlogAddModel."""
        pass
