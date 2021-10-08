import emoji from "react-easy-emoji";

// IMAGES
import Freelance from "../assets/img/Freelance.webp";
import UniversityCMG from "../assets/img/UniversityCMG.webp";
import MyImage from "../assets/img/my_photo1.jpg";

export const portfolioEs = {
  greeting: {
    username: "Jorge Jiménez Díaz",
    title: "Hola, Soy Jorge",
    subTitle: emoji(
      "Soy desarrollador de software con 2 año de experiencia  🚀 como full-stack con Django y React, con capacidad para desarrollar aplicaciones web y android (Java). Disfruto trabajando en equipo, soy automotivado, de aprendizaje rápido, razonamiento sólido, habilidades para resolver problemas y estoy capacitado para crear código limpio,, probado y eficiente."
    ),
    displayGreeting: true,
    image: MyImage,
  },
  socialMediaLinks: {
    display: true,
    github: "https://github.com/jorgejimenez98",
    gmail: "georgeguitarra07@gmail.com",
    linkedin:
      "https://www.linkedin.com/in/jorge-jim%C3%A9nez-d%C3%ADaz-6590b8206/",
    facebook: "https://www.facebook.com/profile.php?id=100014722274935",
  },
  contactInfo: {
    title: emoji("Contact Me ☎️"),
    subtitle:
      "Discutir sobre un proyecto o solo quieres decir hola? No hay problema, mi inbox está abierto para todos",
    number: "(+34)653513286",
    cubaNumber: "(+53)54046483",
    emailAddress: "georgeguitarra07@gmail.com",
  },
  experience: {
    freelance: {
      date: "2020 - actualidad",
      image: Freelance,
      job: "Desarrollador Full Stack",
      place: "Freelance",
      location: "Camagüey, Camagüey Cuba",
      description:
        "Diseño e implementación de aplicaciones web y móviles tales como sitios de comercio electrónico y sistemas de gestión empresarial para clientes de mi localidad.",
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
      date: "2019 - 09/2021",
      image: UniversityCMG,
      job: "Desarrollador de Software",
      place: "Universidad de Camagüey",
      location: "Camagüey, Camagüey Cuba",
      description:
        "Diseño e implementación de aplicaciones web y móviles para la universidad, clientes de la misma y empresas estatales de la localidad.",
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
};
