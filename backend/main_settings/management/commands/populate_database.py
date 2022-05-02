from django.core.management.base import BaseCommand
from experience.models import Experience, KeyExperience
from technologie.models import TechnologieItem, Main_Tech, Technologie
from social_media.models import SocialMedia, Curriculum
from ...models import SiteConfiguration, TranslationText
from ...constants import ENGLISH, SIMPLE, SPANISH, MODERN
from datetime import date


class Command(BaseCommand):
    help = 'Initialize DB Data'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def handle(self, *args, **options):
        self._create_site_configurations()
        self._create_technologie_items()
        self._create_techs()
        self._create_expertises()
        self._create_curriculumns()
        self._create_main_techs()
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

    def _create_social_media_links(self):
        SocialMedia.objects.bulk_create([
            SocialMedia(className="icon-button gitlab", iconClassName="fab fa-gitlab", link="https://gitlab.com/jorgejimenez98"),
            SocialMedia(className="icon-button github", iconClassName="fab fa-github", link="https://github.com/jorgejimenez98"),
            SocialMedia(className="icon-button linkedin", iconClassName="fab fa-linkedin-in", link="https://www.linkedin.com/in/jorge-jimenez-6590b8206/"),
            SocialMedia(className="icon-button google", iconClassName="fab fa-google", link="georgeguitarra07@gmail.com"),
            SocialMedia(className="icon-button facebook", iconClassName="fab fa-facebook-f", link="https://www.facebook.com/profile.php?id=100014722274935"),
        ])
        self.stdout.write(self.style.NOTICE('Social Medias Created Successfully !!!!'))
    
    def _create_main_techs(self):
        main_tech = Main_Tech.objects.create(proccessPorcent='98%')
        translation_1 = TranslationText.objects.create(language=SPANISH, text="Backend con Django")
        translation_2 = TranslationText.objects.create(language=ENGLISH, text="Backend with Django")
        main_tech.texts.add(translation_1)
        main_tech.texts.add(translation_2)
        main_tech.save()
        main_tech = Main_Tech.objects.create(proccessPorcent='95%')
        translation_1 = TranslationText.objects.create(language=SPANISH, text="Construir APIS con django-rest-framework")
        translation_2 = TranslationText.objects.create(language=ENGLISH, text="Build APIS with django-rest-framework")
        main_tech.texts.add(translation_1)
        main_tech.texts.add(translation_2)
        main_tech.save()
        main_tech = Main_Tech.objects.create(proccessPorcent='90%')
        translation_1 = TranslationText.objects.create(language=SPANISH, text="Frontend con React")
        translation_2 = TranslationText.objects.create(language=ENGLISH, text="Frontend with React")
        main_tech.texts.add(translation_1)
        main_tech.texts.add(translation_2)
        main_tech.save()
        self.stdout.write(self.style.NOTICE('Main Rols Created Successfully !!!!'))
    
    def _create_curriculumns(self):
        Curriculum.objects.bulk_create([
            Curriculum(name=MODERN, language=ENGLISH, link="https://drive.google.com/file/d/1Q3--4nlcPTrohhNaGjTem5lhw-kXYE7g/view?usp=sharing"),
            Curriculum(name=SIMPLE, language=ENGLISH, link="https://drive.google.com/file/d/1vGt9SvVAOv-2HceBGfNIs90MCgnDGbrr/view?usp=sharing"),
            Curriculum(name=SIMPLE, language=SPANISH, link="https://drive.google.com/file/d/1O33Pf7FEY46UI9ktle6eTOzaQlVm99Xn/view?usp=sharing"),
            Curriculum(name=MODERN, language=SPANISH, link="https://drive.google.com/file/d/1y07tg_5bi6WLuX1AppDTIMoYziVW-apy/view?usp=sharing"),
        ])
        self.stdout.write(self.style.NOTICE('Curriculums Created Successfully !!!!'))
    
    def _create_technologie_items(self):
        TechnologieItem.objects.bulk_create([
            TechnologieItem(text="Python"), TechnologieItem(text="Django"), 
            TechnologieItem(text="Django Rest Framework"), TechnologieItem(text="Android"), 
            TechnologieItem(text="Java"), TechnologieItem(text="Angular"), 
            TechnologieItem(text="TypeScript"), TechnologieItem(text="Apollo.js"),
            TechnologieItem(text="Nodejs"), TechnologieItem(text="Graphql"),
            TechnologieItem(text="MongoDB"), TechnologieItem(text="ExpressJs"), 
            TechnologieItem(text="CSS"), TechnologieItem(text="PostgreSQL"), 
            TechnologieItem(text="Bootstrapp"), TechnologieItem(text="Java Script"),
            TechnologieItem(text="React"), TechnologieItem(text="Redux.js"),
            TechnologieItem(text="HTML"), TechnologieItem(text="Git"),  
            TechnologieItem(text="Sequelize ORM"), TechnologieItem(text="Docker"),  
            TechnologieItem(text="drf_jwt"), TechnologieItem(text="Material-UI"),  
            TechnologieItem(text="Blockchain"), TechnologieItem(text="Vue.js"),
            TechnologieItem(text="Jira"), TechnologieItem(text="Trello"),
            TechnologieItem(text="Jest"), TechnologieItem(text="Factory-Boy"),
            TechnologieItem(text="Docker-Compose"), TechnologieItem(text="Bulma"),
            TechnologieItem(text="Ant-Design"), TechnologieItem(text="Gitlab"),
            TechnologieItem(text="PyQt5"), TechnologieItem(text="Vuex"),
        ])
        self.stdout.write(self.style.NOTICE('Technologie Items Created Successfully !!!!'))

    def _create_techs(self):
        Technologie.objects.bulk_create([
            Technologie(name='JavaScript', icon_class='fab fa-js', image_logo=None),
            Technologie(name='Python', icon_class='fab fa-python', image_logo=None),
            Technologie(name='Java', icon_class='fab fa-java', image_logo=None),
            Technologie(name='Android', icon_class='fab fa-android', image_logo=None),
            Technologie(name='Angular', icon_class='fab fa-angular', image_logo=None),
            Technologie(name='Reactjs', icon_class='fab fa-react', image_logo=None),
            Technologie(name='Nodejs', icon_class='fab fa-node', image_logo=None),
            Technologie(name='CSS3', icon_class='fab fa-css3-alt', image_logo=None),
            Technologie(name='Bootstrap', icon_class='fab fa-bootstrap', image_logo=None),
            Technologie(name='HTML5', icon_class='fab fa-html5', image_logo=None),
            Technologie(name='sql-database', icon_class='fas fa-database', image_logo=None),
            Technologie(name='Docker', icon_class='fab fa-docker', image_logo=None),
            Technologie(name='npm', icon_class='fab fa-npm', image_logo=None),
            Technologie(name='ReduxJS', icon_class='', image_logo='technology/redux.png'),
            Technologie(name='Django', icon_class='', image_logo='technology/django.png'),
            Technologie(name='REST API', icon_class='', image_logo='technology/rest-frame.png'),
            Technologie(name='MySQL', icon_class='', image_logo='technology/mysql.png'),
            Technologie(name='PostgreSQL', icon_class='', image_logo='technology/postgresql.svg'),
            Technologie(name='MongoDB', icon_class='', image_logo='technology/mongodb.png'),
            Technologie(name='SQL Server', icon_class='', image_logo='technology/sqlserver.png'),
            Technologie(name='GraphQL', icon_class='', image_logo='technology/graphql.png'),
            Technologie(name='Apollo.js', icon_class='', image_logo='technology/apollo.png'),
            Technologie(name='Linux', icon_class='', image_logo='technology/linux.png'),
        ])
        self.stdout.write(self.style.NOTICE('TECHS With Pictures Created Successfully !!!!'))

    def _create_expertises(self):
        # Experience 1
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
        experience.descriptions.add(description_spanish)
        experience.descriptions.add(description_english)

        key1 = KeyExperience.objects.create(text="Team Work")
        experience.key_experiences.add(key1)

        experience.techs.add(TechnologieItem.objects.get(text="Python"))
        experience.techs.add(TechnologieItem.objects.get(text="Django"))
        experience.techs.add(TechnologieItem.objects.get(text="Django Rest Framework"))
        experience.techs.add(TechnologieItem.objects.get(text="PyQt5"))
        experience.techs.add(TechnologieItem.objects.get(text="Android"))
        experience.techs.add(TechnologieItem.objects.get(text="Java"))
        experience.techs.add(TechnologieItem.objects.get(text="Angular"))
        experience.techs.add(TechnologieItem.objects.get(text="TypeScript"))
        experience.techs.add(TechnologieItem.objects.get(text="Apollo.js"))
        experience.techs.add(TechnologieItem.objects.get(text="Graphql"))
        experience.techs.add(TechnologieItem.objects.get(text="Nodejs"))
        experience.techs.add(TechnologieItem.objects.get(text="ExpressJs"))
        experience.techs.add(TechnologieItem.objects.get(text="MongoDB"))
        experience.techs.add(TechnologieItem.objects.get(text="PostgreSQL"))
        experience.techs.add(TechnologieItem.objects.get(text="CSS"))
        experience.techs.add(TechnologieItem.objects.get(text="Bootstrapp"))
        experience.save()

        # Experience 2
        experience = Experience.objects.create(
            date_start=date(2020, 1, 1),
            date_end=date(2022, 2, 1),
            is_currently_working=False,
            company_logo='experience/freelance.png'
        )
        job_rol_spanish = TranslationText.objects.create(
            language=SPANISH, text="Desarrollador Full Stack")
        job_rol_english = TranslationText.objects.create(
            language=ENGLISH, text="Full-Stack Developer")
        experience.job_rols.add(job_rol_spanish)
        experience.job_rols.add(job_rol_english)

        company_name_spanish = TranslationText.objects.create(
            language=SPANISH, text="Freelance")
        company_name_english = TranslationText.objects.create(
            language=ENGLISH, text="Freelance")
        experience.conmpany_names.add(company_name_spanish)
        experience.conmpany_names.add(company_name_english)

        location_name_spanish = TranslationText.objects.get(
            language=SPANISH, text="Camagüey, Camagüey Cuba")
        location_name_english = TranslationText.objects.get(
            language=ENGLISH, text="Camagüey, Camagüey Cuba")
        experience.locations.add(location_name_spanish)
        experience.locations.add(location_name_english)

        description_spanish = TranslationText.objects.create(
            language=SPANISH, text="Diseño e implementación de aplicaciones web y móviles tales como sitios de comercio electrónico y sistemas de gestión empresarial para clientes de mi localidad.")
        description_english = TranslationText.objects.create(
            language=ENGLISH, text="Design and implementation of web and mobile applications such as e-commerce sites and business management systems.")
        experience.descriptions.add(description_spanish)
        experience.descriptions.add(description_english)

        key1 = KeyExperience.objects.get(text="Team Work")
        experience.key_experiences.add(key1)

        experience.techs.add(TechnologieItem.objects.get(text="Python"))
        experience.techs.add(TechnologieItem.objects.get(text="Django"))
        experience.techs.add(TechnologieItem.objects.get(text="Django Rest Framework"))
        experience.techs.add(TechnologieItem.objects.get(text="Java Script"))
        experience.techs.add(TechnologieItem.objects.get(text="React"))
        experience.techs.add(TechnologieItem.objects.get(text="Redux.js"))
        experience.techs.add(TechnologieItem.objects.get(text="PostgreSQL"))
        experience.techs.add(TechnologieItem.objects.get(text="HTML"))
        experience.techs.add(TechnologieItem.objects.get(text="CSS"))
        experience.techs.add(TechnologieItem.objects.get(text="Git"))
        experience.techs.add(TechnologieItem.objects.get(text="Sequelize ORM"))
        experience.techs.add(TechnologieItem.objects.get(text="Docker"))
        experience.techs.add(TechnologieItem.objects.get(text="drf_jwt"))
        experience.techs.add(TechnologieItem.objects.get(text="Material-UI"))
        experience.save()

         # Experience 3
        experience = Experience.objects.create(
            date_start=date(2022, 2, 1),
            date_end=date(2022, 3, 1),
            is_currently_working=False,
            company_logo='experience/quentalLogo.png'
        )
        job_rol_spanish = TranslationText.objects.get(
            language=SPANISH, text="Desarrollador Full Stack")
        job_rol_english = TranslationText.objects.get(
            language=ENGLISH, text="Full-Stack Developer")
        experience.job_rols.add(job_rol_spanish)
        experience.job_rols.add(job_rol_english)

        company_name_spanish = TranslationText.objects.create(
            language=SPANISH, text="Quental Technologies")
        company_name_english = TranslationText.objects.create(
            language=ENGLISH, text="Quental Technologies")
        experience.conmpany_names.add(company_name_spanish)
        experience.conmpany_names.add(company_name_english)

        location_name_spanish = TranslationText.objects.create(
            language=SPANISH, text="España, Madrid")
        location_name_english = TranslationText.objects.create(
            language=ENGLISH, text="Madrid, Spain")
        experience.locations.add(location_name_spanish)
        experience.locations.add(location_name_english)

        description_spanish = TranslationText.objects.create(
            language=SPANISH, text="Quental es una empresa de servicios y soluciones tecnológicas de capital 100% español con un equipo humano de más de 500 personas que se fundamenta sobre la flexibilidad, la innovación y su apuesta por la calidad. Mi trabajo se enfoca en hacer nuevas funcionalidades a proyectos existentes del lado del servidor y del cliente e incluso crear proyectos desde cero")
        description_english = TranslationText.objects.create(
            language=ENGLISH, text="Quental is a 100% Spanish capital technology services and solutions company with a human team of more than 500 people that is based on flexibility, innovation and its commitment to quality. My work focuses on making new functionality to existing projects on the server and client side and even creating projects from scratch.")
        experience.descriptions.add(description_spanish)
        experience.descriptions.add(description_english)

        key1 = KeyExperience.objects.get(text="Team Work")
        experience.key_experiences.add(key1)

        experience.techs.add(TechnologieItem.objects.get(text="Python"))
        experience.techs.add(TechnologieItem.objects.get(text="Django"))
        experience.techs.add(TechnologieItem.objects.get(text="Django Rest Framework"))
        experience.techs.add(TechnologieItem.objects.get(text="Java Script"))
        experience.techs.add(TechnologieItem.objects.get(text="Vue.js"))
        experience.techs.add(TechnologieItem.objects.get(text="Vuex"))
        experience.techs.add(TechnologieItem.objects.get(text="PostgreSQL"))
        experience.techs.add(TechnologieItem.objects.get(text="HTML"))
        experience.techs.add(TechnologieItem.objects.get(text="CSS"))
        experience.techs.add(TechnologieItem.objects.get(text="Git"))
        experience.techs.add(TechnologieItem.objects.get(text="Gitlab"))
        experience.techs.add(TechnologieItem.objects.get(text="Blockchain"))
        experience.techs.add(TechnologieItem.objects.get(text="Docker"))
        experience.techs.add(TechnologieItem.objects.get(text="Bulma"))
        experience.save()

        # Experience 4
        experience = Experience.objects.create(
            date_start=date(2022, 3, 1),
            date_end=date.today(),
            is_currently_working=True,
            company_logo='experience/quentalLogo.png'
        )
        job_rol_spanish = TranslationText.objects.create(
            language=SPANISH, text="Líder de equipo y Desarrollador Full Stack")
        job_rol_english = TranslationText.objects.create(
            language=ENGLISH, text="Teamd Leader and Full-Stack Developer")
        experience.job_rols.add(job_rol_spanish)
        experience.job_rols.add(job_rol_english)

        company_name_spanish = TranslationText.objects.get(
            language=SPANISH, text="Quental Technologies")
        company_name_english = TranslationText.objects.get(
            language=ENGLISH, text="Quental Technologies")
        experience.conmpany_names.add(company_name_spanish)
        experience.conmpany_names.add(company_name_english)

        location_name_spanish = TranslationText.objects.get(
            language=SPANISH, text="España, Madrid")
        location_name_english = TranslationText.objects.get(
            language=ENGLISH, text="Madrid, Spain")
        experience.locations.add(location_name_spanish)
        experience.locations.add(location_name_english)

        description_spanish = TranslationText.objects.create(
            language=SPANISH, text="Mi trabajo consta en liderar a nivel técnico un equipo de programación full-stack empleando las mejores prácticas de desarrollo para un buen funcionamiento del sistema en el que se esté trabajando, además de hacer de Teach Lead ayudando a nuevos profesionales de otros proyectos en las tecnologías (Django, Django Rest Framework, Nodejs, Vue y React)")
        description_english = TranslationText.objects.create(
            language=ENGLISH, text="My job consists of leading a full-stack programming team at a technical level, using the best development practices for the proper functioning of the system in which they are working, as well as being a Teach Lead helping new professionals from other technology projects. (Django, Django Rest Framework, Nodejs, Vue and React)")
        experience.descriptions.add(description_spanish)
        experience.descriptions.add(description_english)

        key1 = KeyExperience.objects.get(text="Team Work")
        experience.key_experiences.add(key1)

        experience.techs.add(TechnologieItem.objects.get(text="Python"))
        experience.techs.add(TechnologieItem.objects.get(text="Django"))
        experience.techs.add(TechnologieItem.objects.get(text="Django Rest Framework"))
        experience.techs.add(TechnologieItem.objects.get(text="Java Script"))
        experience.techs.add(TechnologieItem.objects.get(text="Vue.js"))
        experience.techs.add(TechnologieItem.objects.get(text="Vuex"))
        experience.techs.add(TechnologieItem.objects.get(text="React"))
        experience.techs.add(TechnologieItem.objects.get(text="Redux.js"))
        experience.techs.add(TechnologieItem.objects.get(text="PostgreSQL"))
        experience.techs.add(TechnologieItem.objects.get(text="HTML"))
        experience.techs.add(TechnologieItem.objects.get(text="CSS"))
        experience.techs.add(TechnologieItem.objects.get(text="Git"))
        experience.techs.add(TechnologieItem.objects.get(text="Gitlab"))
        experience.techs.add(TechnologieItem.objects.get(text="Blockchain"))
        experience.techs.add(TechnologieItem.objects.get(text="Docker"))
        experience.techs.add(TechnologieItem.objects.get(text="Docker-Compose"))
        experience.techs.add(TechnologieItem.objects.get(text="Bulma"))
        experience.techs.add(TechnologieItem.objects.get(text="Trello"))
        experience.techs.add(TechnologieItem.objects.get(text="Jira"))
        experience.techs.add(TechnologieItem.objects.get(text="Factory-Boy"))
        experience.techs.add(TechnologieItem.objects.get(text="Jest"))
        experience.techs.add(TechnologieItem.objects.get(text="Ant-Design"))
        experience.techs.add(TechnologieItem.objects.get(text="Nodejs"))
        experience.save()

        self.stdout.write(self.style.NOTICE('Expertises Created Successfully !!!!'))