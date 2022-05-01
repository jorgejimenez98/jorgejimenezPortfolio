from django.core.management.base import BaseCommand
from ...models import SiteConfiguration, TranslationText


class Command(BaseCommand):
    help = 'Delete DB Data'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def handle(self, *args, **options):
        self._clean_database()
        self.stdout.write(self.style.SUCCESS(
            'DATABASE CLEANED SUCCESSFULLY !!!!\n----------------------'))

    def _clean_database(self):
        configs = SiteConfiguration.objects.get()
        configs.developer_name = ""
        configs.years_of_experience = 0.0
        configs.is_open_to_work = True
        configs.phone_number = ''
        configs.repository_project_url = ""
        configs.developer_email = ""
        configs.profilePicture = ''
        configs.save()
        for translation in TranslationText.objects.all():
            translation.delete()
