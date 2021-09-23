import Main from "./components/Main";
import Contact from "./components/contact/Contact";
import AboutMe from "./components/AboutMe";
import Skills from "./components/Skills";
import Experience from "./components/Experience";

export const routes = [
  { path: "/home", component: Main, exact: true },
  { path: "/contact", component: Contact },
  { path: "/about", component: AboutMe },
  { path: "/skills", component: Skills },
  { path: "/experience", component: Experience },
];
