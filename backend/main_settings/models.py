from django.db import models
from solo.models import SingletonModel
from .constants import LANGUAJES_CHOICES

class TranslationText(models.Model):
    language = models.CharField(max_length=2, choices=LANGUAJES_CHOICES)
    text = models.TextField()

    def __str__(self) -> str:
        return f'{self.language} - {self.text}'


def uploadProfilePath(x, filename):
    return '/'.join(['profile', filename])

class SiteConfiguration(SingletonModel):
    developer_name = models.CharField(max_length=255, default="")
    main_presentations = models.ManyToManyField(TranslationText)
    years_of_experience = models.FloatField(default=0.0)
    is_open_to_work = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=255, default="")
    repository_project_url = models.URLField(default="")
    developer_email = models.EmailField(default="")
    profilePicture = models.ImageField(blank=True, null=True, upload_to=uploadProfilePath)

    def __str__(self):
        return "Site Configuration"

    class Meta:
        verbose_name = "Site Configuration"