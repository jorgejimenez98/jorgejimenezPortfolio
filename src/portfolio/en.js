import emoji from "react-easy-emoji";

// IMAGES
import Freelance from "../assets/img/Freelance.webp";
import UniversityCMG from "../assets/img/UniversityCMG.webp";

export const portfolioEn = {
  cv_links: {
    simple:
      "https://drive.google.com/file/d/1vGt9SvVAOv-2HceBGfNIs90MCgnDGbrr/view?usp=sharing",
    modern:
      "https://drive.google.com/file/d/1Q3--4nlcPTrohhNaGjTem5lhw-kXYE7g/view?usp=sharing",
  },
  labels: {
    contact: "Contact Me",
    send_email_direct: "Send email directly",
    go_back: "Go Back",
    spain: "Spain",
    experience: "Work Experience",
    madeBy: emoji("Made with ❤️ by Jorge Jiménez"),
    check: "Check code",
    here: "here",
    open: "Open to Work",
    cv_button: "See my CV",
    modal_title: "Download CV in English.",
    simple_design: "CV simple Design",
    simple_modern: "CV modern Design",
    change_lang_dialog: "If you want to consult the CV in another language, simply change it from the header",
  },
  conctactForm: {
    nameLabel: "Full Name",
    namePlaceHolder: "Write here your name",
    emailLabel: "Email",
    emailPlaceHolder: "Write here your email",
    messageLabel: "Message",
    messagePlaceHolder: "Write here the message",
    send: "Send",
    sended: "Email Sended successfully",
    validations: {
      emailRequired: "Email is required",
      validEmail: "Write a valid email. Example: name@gmail.com",
      nameRequired: "Full name is required",
      messRequired: "Message is required",
    },
  },
  socialMediaLinks: {
    display: true,
    github: "https://github.com/jorgejimenez98",
    gmail: "georgeguitarra07@gmail.com",
    linkedin:
      "https://www.linkedin.com/in/jorge-jimenez-6590b8206/",
    facebook: "https://www.facebook.com/profile.php?id=100014722274935",
  },
  contactInfo: {
    title: emoji("Contact Me ☎️"),
    subtitle:
      "Discuss a project or just want to say hi? My Inbox is open for all.",
    number: "(+34)653513286",
    emailAddress: "georgeguitarra07@gmail.com",
  },
  experience: {
    freelance: {
      date: "2020 - present",
      image: Freelance,
      job: "Full Stack Developer",
      place: "Freelance",
      location: "Camagüey, Camagüey Cuba",
      description:
        "Design and implementation of web and mobile applications such as e-commerce sites and business management systems.",
      tecnologies: [
        "Python",
        "Django",
        "Java Script",
        "React",
        "Redux.js",
        "Django Rest Framework",
        "PostgreSQL",
        "HTML",
        "CSS",
        "GIT",
        "Sequelize ORM",
        "Docker",
        "drf_jwt",
        "Material-ui",
        "GIT",
      ],
    },
    ucm: {
      date: "09/2020 - 09/2021",
      image: UniversityCMG,
      job: "Software Developer",
      place: "University of Camagüey",
      location: "Camagüey, Camagüey Cuba",
      description:
        "Design and implementation of web and mobile applications for the university and state companies of the locality.",
      tecnologies: [
        "Python",
        "Django",
        "Django Rest Framework",
        "PyQt5",
        "Android",
        "Java",
        "Angular",
        "TypeScript",
        "Apollo.js",
        "GraphQL",
        "NodeJS",
        "ExpressJS",
        "MongoDB",
        "PostgreSQL",
        "HTML",
        "CSS",
        "Bootstrap",
      ],
    },
  },
  techStack: {
    favorite: "My main technologies",
    tools: "Technologies",
    experience: [
      {
        Stack: "Backend with Django",
        progressPercentage: "98%",
      },
      {
        Stack: "Build APIS with django-rest-framework",
        progressPercentage: "95%",
      },
      {
        Stack: "Frontend with React",
        progressPercentage: "90%",
      },
    ],
  },
};
