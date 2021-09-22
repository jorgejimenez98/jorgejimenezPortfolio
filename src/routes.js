import Main from "./components/Main";
import Contact from "./components/Contact";
import AboutMe from "./components/AboutMe";
import Skills from "./components/Skills";
import Projects from "./components/Projects";
import Experience from "./components/Experience";

export const routes = [
  { path: "/home", component: Main, exact: true },
  { path: "/contact", component: Contact },
  { path: "/about", component: AboutMe },
  { path: "/skills", component: Skills },
  { path: "/projects", component: Projects },
  { path: "/experience", component: Experience },
];
