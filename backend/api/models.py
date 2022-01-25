from django.db import models
from solo.models import SingletonModel

# Site configuration Model

class SiteConfiguration(SingletonModel):
    developer_name = models.CharField(max_length=255, default="")
    main_presentation_text = models.TextField(default="")
    years_of_experience = models.PositiveIntegerField(default=0)
    is_open_to_work = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=255, default="")
    repository_project_url = models.URLField(default="")
    developer_email = models.EmailField(default="")

    def __str__(self):
        return "Site Configuration"

    class Meta:
        verbose_name = "Site Configuration"