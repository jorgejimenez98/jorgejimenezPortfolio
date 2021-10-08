import emoji from "react-easy-emoji";

// IMAGES
import Freelance from "../assets/img/Freelance.webp";
import UniversityCMG from "../assets/img/UniversityCMG.webp";
import MyImage from "../assets/img/my_photo1.jpg";

export const portfolioEn = {
  greeting: {
    username: "Jorge Jiménez Díaz",
    title: "Hi all, I'm George",
    subTitle: emoji(
      "I am a software developer with 2 years 🚀 of full-stack experience with Django and React, with the ability to develop web systems and android applications. I enjoy working as a team, I'm self-motivated, fast learner, strong reasoning, problem solving skills, and skilled in creating clean, proven and efficient code"
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
      "Discuss a project or just want to say hi? My Inbox is open for all.",
    number: "(+34)653513286",
    cubaNumber: "(+53)54046483",
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
      date: "2019 - 09/2021",
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
};
