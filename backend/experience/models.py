from django.db import models
from technologie.models import TechnologieItem
from main_settings.models import TranslationText
from datetime import date


class KeyExperience(models.Model):
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text


def uploadExperiencePath(x, filename):
    return '/'.join(['experience', filename])


class Experience(models.Model):
    date_start = models.DateField()
    date_end = models.DateField()
    is_currently_working = models.BooleanField(default=False)
    company_logo = models.ImageField(blank=True, null=True, upload_to=uploadExperiencePath)
    job_rols = models.ManyToManyField(TranslationText, related_name='expertise_job_rols', blank=True)
    conmpany_names = models.ManyToManyField(TranslationText, related_name='expertise_company_names', blank=True)
    descriptions = models.ManyToManyField(TranslationText, related_name='expertise_descriptions', blank=True)
    locations = models.ManyToManyField(TranslationText, related_name='expertise_locations', blank=True)
    key_experiences = models.ManyToManyField(KeyExperience, related_name='experiences_key', blank=True)
    techs = models.ManyToManyField(TechnologieItem, related_name='experiences_items', blank=True)

    def __str__(self):
        return f'Experience {self.id}'
    
    def dateStrings(self, language):
        if language == 'es':
            return 'mes', 'meses', 'año', 'años'
        return 'month', 'months', 'year', 'years'

    def get_time_working(self, language):
        monthStr, monthsStr, yearStr, yearsStr = self.dateStrings(language)
        if self.is_currently_working:
            startDate, endDate = self.date_start, date.today()
        startDate, endDate = self.date_start, self.date_end
        months_difference = (endDate.year - startDate.year) * 12
        months_difference -= startDate.month
        months_difference += endDate.month
        months_difference = 0 if months_difference <= 0 else months_difference
        if months_difference < 12:
            aux = monthStr if months_difference == 1 else monthsStr
            msg = f'{months_difference} {aux}'
        elif months_difference % 12 == 0:
            aux = yearStr if int(months_difference / 12) == 1 else yearsStr
            msg = f'{int(months_difference / 12)} {aux}'
        else:
            aux1 = yearStr if  int(months_difference / 12) == 1 else yearsStr
            aux2 = monthStr if months_difference % 12 == 1 else monthsStr
            msg = f'{int(months_difference / 12)} {aux1} {months_difference % 12} {aux2}'
        return msg