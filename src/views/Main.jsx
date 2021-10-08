import React from "react";
import { Fade } from "react-awesome-reveal";
import Experience from "../views/Experience";
import Home from "../views/Home";

function Main() {
  return (
    <div className="app">
      <Fade bottom duration={1000} distance="40px">
        <Home />
        <Experience />
      </Fade>
    </div>
  );
}

export default Main;