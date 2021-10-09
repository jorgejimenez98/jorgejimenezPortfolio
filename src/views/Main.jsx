import React from "react";
import { Fade } from "react-awesome-reveal";
import Home from "../views/Home";
import Skills from "./Skills";

function Main() {
  return (
    <div className="app">
      <Fade bottom duration={1000} distance="40px">
        <Home />
        <Skills />

      </Fade>
    </div>
  );
}

export default Main;
