import Main from "./views/Main";
import Contact from "./views/Contact";

export const routes = [
  { path: "/home", component: Main, exact: true },
  { path: "/contact", component: Contact },
];
