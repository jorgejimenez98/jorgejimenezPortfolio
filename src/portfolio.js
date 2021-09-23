import emoji from "react-easy-emoji";

const greeting = {
  username: "Jorge Jiménez Díaz",
  title: "Hi all, I'm George",
  subTitle: emoji(
    "I am a software developer with 2 years 🚀 of full-stack experience with Django and React, with the ability to develop web systems and android applications. I enjoy working as a team, I'm self-motivated, fast learner, strong reasoning, problem solving skills, and skilled in creating clean, proven and efficient code"
  ),
  displayGreeting: true,
};

const socialMediaLinks = {
  display: true,
  github: "https://github.com/jorgejimenez98",
  gmail: "georgeguitarra07@gmail.com",
  linkedin:
    "https://www.linkedin.com/in/jorge-jim%C3%A9nez-d%C3%ADaz-6590b8206/",
  facebook: "https://www.facebook.com/profile.php?id=100014722274935",
  codersRank: "https://profile.codersrank.io/user/jorgejimenez98/",
};

const contactInfo = {
  title: emoji("Contact Me ☎️"),
  subtitle:
    "Discuss a project or just want to say hi? My Inbox is open for all.",
  number: "(+34)653513286",
  cubaNumber: "(+53)54046483",
  emailAddress: "georgeguitarra07@gmail.com",
};

export { greeting, socialMediaLinks, contactInfo };
