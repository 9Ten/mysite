# Create your models here.
from django.db import models
from ckeditor import fields

class News(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    title = models.CharField(max_length=250)
    content = fields.RichTextField()
    # published
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default='draft')

    def __str__(self):
        return self.title
        
    class Meta:
        ordering = ["-timestamp", "-updated"]
