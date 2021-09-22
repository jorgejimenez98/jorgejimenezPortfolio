import React from "react";
import { Fade } from "react-reveal";
import emoji from "react-easy-emoji";
import SocialMedia from "./SocialMedia";
import manOnTable from "../assets/img/manOnTable.svg";
import { greeting } from "../portfolio";

export default function Greeting() {
  if (!greeting.displayGreeting) {
    return null;
  }
  return (
    <Fade bottom duration={1000} distance="40px">
      <div className="greet-main" id="greeting">
        <div className="greeting-main">
          <div className="greeting-text-div">
            <div>
              <h1 className={"greeting-text"}>
                {greeting.title}
                <span className="wave-emoji">{emoji("👋")}</span>
              </h1>
              <p className={"greeting-text-p subTitle"}>{greeting.subTitle}</p>
              <SocialMedia />
            </div>
          </div>
          <div className="greeting-image-div">
            <img alt="man sitting on table" src={manOnTable}></img>
          </div>
        </div>
      </div>
    </Fade>
  );
}
