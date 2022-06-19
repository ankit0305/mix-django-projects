from django.db import models

class Contact(models.Model):
    
    name = models.CharField(max_length=20)
    city = models.CharField(max_length=20, blank=True)
    gender = models.CharField(max_length=1, blank=True)
    #phone = models.IntegerField(default=None)

    class Meta:
        ordering = [0]

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
