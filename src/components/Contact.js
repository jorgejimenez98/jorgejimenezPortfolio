import React from "react";
import SocialMedia from "./SocialMedia";
import { contactInfo } from "../portfolio";
import { Fade } from "react-reveal";
import contactMailDark from "../assets/img/contactMaiDark.svg";

export default function Contact() {
  return (
    <Fade bottom duration={1000} distance="20px">
      <div className="main contact-margin-top" id="contact">
        <div className="contact-div-main">
          <div className="contact-header">
            <h1 className="heading contact-title">{contactInfo.title}</h1>
            <p className={"subTitle contact-subtitle"}>
              {contactInfo.subtitle}
            </p>
            <div className={"contact-text-div"}>
              <a className="contact-detail" href={"tel:" + contactInfo.number}>
                Spain {contactInfo.number}
              </a>
              <br />
              <br />
              <a
                className="contact-detail"
                href={"tel:" + contactInfo.cubaNumber}
              >
                Cuba {contactInfo.cubaNumber}
              </a>
              <br />
              <br />
              <a
                className="contact-detail-email"
                href={"mailto:" + contactInfo.emailAddress}
              >
                {contactInfo.emailAddress}
              </a>
              <br />
              <br />
              <SocialMedia />
            </div>
          </div>
          <div className="contact-image-div">
            <img alt="Man working" src={contactMailDark}></img>
          </div>
        </div>
      </div>
    </Fade>
  );
}
