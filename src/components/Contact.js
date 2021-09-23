import React, { useState } from "react";
import Button from "@material-ui/core/Button";
import ContactSocialMedia from "./ContactSocialMedia";
import ContactForm from "./ContactForm";
import { contactInfo } from "../portfolio";
import { Fade } from "react-reveal";
import contactMailDark from "../assets/img/contactMaiDark.svg";

export default function Contact() {
  const [displayForm, setDisplayForm] = useState("none");
  const [displaySocialMedia, setDisplaySocialMedia] = useState("inline");
  const [buttomText, setButtomText] = useState("Send Direct Email");

  const changeVisibility = () => {
    if (displayForm === "none") {
      setDisplayForm("inline");
      setDisplaySocialMedia("none");
      setButtomText("Go Back");
    } else {
      setDisplayForm("none");
      setDisplaySocialMedia("inline");
      setButtomText("Send Direct Email");
    }
  };

  return (
    <Fade bottom duration={1000} distance="20px">
      <div className="main contact-margin-top" id="contact">
        <div className="contact-div-main">
          <div className="contact-header">
            <h1 className="heading contact-title">{contactInfo.title}</h1>

            <div style={{ display: displaySocialMedia }}>
              <ContactSocialMedia />
            </div>

            <div style={{ display: displayForm }}>
              <ContactForm />
            </div>

            <div className="container button-direct mt-4 mr-2">
              <Button
                variant="text"
                onClick={changeVisibility}
                className="animated infinite pulse"
              >
                {buttomText}
              </Button>
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
