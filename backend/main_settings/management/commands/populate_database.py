from django.core.management.base import BaseCommand
from ...models import SiteConfiguration, TranslationText
from ...constants import ENGLISH, SPANISH

class Command(BaseCommand):
    help = 'Initialize DB Data'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def handle(self, *args, **options):
        self._create_site_configurations()
        self.stdout.write(self.style.SUCCESS('DATABASE COMPLETED SUCCESSFULLY !!!!\n----------------------'))

    def _create_site_configurations(self):
        self.stdout.write(self.style.NOTICE('Creating Site Configurations !!!!'))
        # Configurations
        try:
            configs = SiteConfiguration.objects.get()
            configs.developer_name = "Jorge Jimenez"
            configs.years_of_experience = 2.5
            configs.is_open_to_work = True
            configs.phone_number = '653513286'
            configs.repository_project_url = "https://github.com/jorgejimenez98/jorgejimenezPortfolio"
            configs.developer_email = "georgeguitarra07@gmail.com"
            configs.profilePicture = 'profile/foto.jpg'
        except SiteConfiguration.DoesNotExist:
            configs = SiteConfiguration.objects.create(
                developer_name='Jorge Jimenez',
                years_of_experience=2.5,
                is_open_to_work=True,
                phone_number='653513286',
                repository_project_url='https://github.com/jorgejimenez98/jorgejimenezPortfolio',
                developer_email='georgeguitarra07@gmail.com',
                profilePicture='profile/foto.jpg'
            )
        # Translation Texts
        text_spanish = TranslationText.objects.create(language=ENGLISH, text="I am a software developer with 2 years 🚀 of full-stack experience with Django and React, with the ability to develop web systems and android applications. I enjoy working as a team, I'm self-motivated, fast learner, strong reasoning, problem solving skills, and skilled in creating clean, proven and efficient code")
        text_english = TranslationText.objects.create(language=SPANISH, text="Soy desarrollador de software con 2 años de experiencia 🚀 como full-stack con Django y React, con capacidad para desarrollar aplicaciones web y android (Java). Disfruto trabajando en equipo, soy automotivado, de aprendizaje rápido, razonamiento sólido, habilidades para resolver problemas y estoy capacitado para crear código limpio, probado y eficiente.")
        configs.main_presentations.add(text_spanish)
        configs.main_presentations.add(text_english)
        title_spanish = TranslationText.objects.create(language=SPANISH, text="Hola, Soy Jorge")
        title_english = TranslationText.objects.create(language=ENGLISH, text="Hi all, I'm George")
        configs.title_presentations.add(title_spanish)
        configs.title_presentations.add(title_english)
        configs.save()
        self.stdout.write(self.style.NOTICE('Site Configurations Created Successfully !!!!'))