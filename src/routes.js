import Main from "./views/Main";
import Contact from "./views/Contact";
import Experience from "./views/Experience";

export const routes = [
  { path: "/home", component: Main, exact: true },
  { path: "/contact", component: Contact },
  { path: "/experience", component: Experience },
];
