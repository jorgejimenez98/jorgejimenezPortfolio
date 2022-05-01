from django.core.management.base import BaseCommand
from experience.models import Experience, KeyExperience
from technologie.models import TechnologieItem
from social_media.models import SocialMedia
from ...models import SiteConfiguration, TranslationText
from ...constants import ENGLISH, SPANISH
from datetime import date


class Command(BaseCommand):
    help = 'Initialize DB Data'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def handle(self, *args, **options):
        self._create_site_configurations()
        self._create_expertises()
        self._create_social_media_links()
        self.stdout.write(self.style.SUCCESS(
            'DATABASE COMPLETED SUCCESSFULLY !!!!\n----------------------'))

    def _create_site_configurations(self):
        # Configurations
        try:
            configs = SiteConfiguration.objects.get()
            configs.developer_name = "Jorge Jimenez"
            configs.years_of_experience = 2.5
            configs.is_open_to_work = True
            configs.phone_number = '(+34)653513286'
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
        text_spanish = TranslationText.objects.create(
            language=ENGLISH, text="I am a software developer with 2 years 🚀 of full-stack experience with Django and React, with the ability to develop web systems and android applications. I enjoy working as a team, I'm self-motivated, fast learner, strong reasoning, problem solving skills, and skilled in creating clean, proven and efficient code")
        text_english = TranslationText.objects.create(
            language=SPANISH, text="Soy desarrollador de software con 2 años de experiencia 🚀 como full-stack con Django y React, con capacidad para desarrollar aplicaciones web y android (Java). Disfruto trabajando en equipo, soy automotivado, de aprendizaje rápido, razonamiento sólido, habilidades para resolver problemas y estoy capacitado para crear código limpio, probado y eficiente.")
        configs.main_presentations.add(text_spanish)
        configs.main_presentations.add(text_english)
        title_spanish = TranslationText.objects.create(
            language=SPANISH, text="Hola, Soy Jorge")
        title_english = TranslationText.objects.create(
            language=ENGLISH, text="Hi all, I'm George")
        configs.title_presentations.add(title_spanish)
        configs.title_presentations.add(title_english)
        configs.save()
        self.stdout.write(self.style.NOTICE(
            'Site Configurations Created Successfully !!!!'))

    def _create_expertises(self):
        experience = Experience.objects.create(
            date_start=date(2020, 9, 1),
            date_end=date(2021, 9, 1),
            is_currently_working=False,
            company_logo='experience/university.png'
        )
        job_rol_spanish = TranslationText.objects.create(
            language=SPANISH, text="Desarrollador de Software")
        job_rol_english = TranslationText.objects.create(
            language=ENGLISH, text="Software Developer")
        experience.job_rols.add(job_rol_spanish)
        experience.job_rols.add(job_rol_english)

        company_name_spanish = TranslationText.objects.create(
            language=SPANISH, text="Universidad de Camagüey")
        company_name_english = TranslationText.objects.create(
            language=ENGLISH, text="University of Camagüey")
        experience.conmpany_names.add(company_name_spanish)
        experience.conmpany_names.add(company_name_english)

        location_name_spanish = TranslationText.objects.create(
            language=SPANISH, text="Camagüey, Camagüey Cuba")
        location_name_english = TranslationText.objects.create(
            language=ENGLISH, text="Camagüey, Camagüey Cuba")
        experience.locations.add(location_name_spanish)
        experience.locations.add(location_name_english)

        description_spanish = TranslationText.objects.create(
            language=SPANISH, text="Diseño e implementación de aplicaciones web y móviles para la universidad, clientes de la misma y empresas estatales de la localidad")
        description_english = TranslationText.objects.create(
            language=ENGLISH, text="Design and implementation of web and mobile applications for the university and state companies of the locality.")
        experience.locations.add(description_spanish)
        experience.locations.add(description_english)

        key1 = KeyExperience.objects.create(text="Team Work")
        experience.key_experiences.add(key1)

        tecnologies = ["Python", "Django", "Django Rest Framework", "PyQt5", "Android", "Java", "Angular", "TypeScript", "Apollo.js",
                       "Graphql", "Nodejs", "ExpressJs", "MongoDB", "PostgreSQL", "CSS", "Bootstrapp"]
        techs_created = []
        for i in tecnologies:
            tex = TechnologieItem.objects.create(text=i)
            techs_created.append(tex)
        for i in techs_created:
            experience.techs.add(i)

        experience.save()
        self.stdout.write(self.style.NOTICE(
            'Experience Created Successfully !!!!'))

    def _create_social_media_links(self):
        SocialMedia.objects.bulk_create([
            SocialMedia(className="icon-button gitlab", iconClassName="fab fa-gitlab", link="https://gitlab.com/jorgejimenez98"),
            SocialMedia(className="icon-button github", iconClassName="fab fa-github", link="https://github.com/jorgejimenez98"),
            SocialMedia(className="icon-button linkedin", iconClassName="fab fa-linkedin-in", link="https://www.linkedin.com/in/jorge-jimenez-6590b8206/"),
            SocialMedia(className="icon-button google", iconClassName="fab fa-google", link="http://georgeguitarra07@gmail.com"),
            SocialMedia(className="icon-button facebook", iconClassName="fab fa-facebook-f", link="https://www.facebook.com/profile.php?id=100014722274935"),
        ])