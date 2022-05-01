from django.db import models
from datetime import date
from technologie.models import TechnologieItem

class KeyExperience(models.Model):
    text = models.CharField(max_length=255)

    def __str__(self):
        return f'Key Experience {self.text}'



def uploadExperiencePath(x, filename):
    return '/'.join(['experience', filename])


class Experience(models.Model):
    date_start = models.DateField()
    date_end = models.DateField()
    is_currently_working = models.BooleanField(default=False)
    company_logo = models.ImageField(blank=True, null=True, upload_to=uploadExperiencePath)
    job_rol = models.CharField(max_length=255)
    conmpany_name = models.CharField(max_length=255)
    description = models.TextField(default="")
    key_experiences = models.ManyToManyField(KeyExperience, related_name='experiences_key')
    techs = models.ManyToManyField(TechnologieItem, related_name='experiences_items')

    def __str__(self):
        return f'Experience {self.job_rol} - {self.conmpany_name}'

    def get_time_working(self):
        if self.is_currently_working:
            return date.today() - self.date_start
        return self.date_end - self.date_start
