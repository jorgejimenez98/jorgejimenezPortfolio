import React from "react";
import { Fade } from "react-awesome-reveal";
import emoji from "react-easy-emoji";
import SocialMedia from "./SocialMedia";
//import manOnTable from "../assets/img/manOnTable.svg";
import MyImage from "../assets/img/my_photo1.jpg";
import { greeting } from "../portfolio";

function Main() {
  return (
    <div className="app">
      <Fade bottom duration={1000} distance="40px">
        {/* HOME SECTION */}
        <div className="greet-main" id="greeting">
          <div className="greeting-main">
            <div className="greeting-text-div">
              <div>
                <h1 className={"greeting-text"}>
                  {greeting.title}
                  <span className="wave-emoji">{emoji("👋")}</span>
                </h1>
                <p className={"greeting-text-p subTitle"}>
                  {greeting.subTitle}
                </p>
                <SocialMedia />
              </div>
            </div>
            <div className="greeting-image-div text-center">
              <img
                alt="man sitting on table"
                className="image"
                src={MyImage}
              ></img>
            </div>
          </div>
        </div>
      </Fade>
    </div>
  );
}

export default Main;
