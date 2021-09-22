import Main from "./components/Main";
import Contact from "./components/Contact";

export const routes = [
    { path: "/home", component: Main, exact: true },
    { path: "/contact", component: Contact },
];
