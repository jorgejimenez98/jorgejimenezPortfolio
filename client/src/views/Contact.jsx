import React, { useState } from "react";
import { useSelector } from "react-redux";
import { Fade } from "react-awesome-reveal";
import contactMailDark from "../assets/img/contactMaiDark.svg";
// Components
import Button from "@material-ui/core/Button";
import ContactSocialMedia from "../components/ContactSocialMedia";
import ContactForm from "../components/ContactForm";

export default function Contact() {
  const { portfolio } = useSelector((state) => state.languaje);

  const [displayForm, setDisplayForm] = useState("none");
  const [displaySocialMedia, setDisplaySocialMedia] = useState("inline");

  const changeVisibility = () => {
    if (displayForm === "none") {
      setDisplayForm("inline");
      setDisplaySocialMedia("none");
    } else {
      setDisplayForm("none");
      setDisplaySocialMedia("inline");
    }
  };

  return (
    <Fade cascade duration={1000} distance="20px">
      <div className="main contact-margin-top" id="contact">
        <div className="contact-div-main">
          <div className="contact-header">
            <h1 className="heading contact-title">
              {portfolio.contactInfo.title}
            </h1>
            <p className={"subTitle contact-subtitle"}>
              {portfolio.contactInfo.subtitle}
            </p>

            <div style={{ display: displaySocialMedia }}>
              <Fade direction={"left"}>
                <ContactSocialMedia />
              </Fade>
            </div>

            <div style={{ display: displayForm }}>
              <Fade direction={"left"}>
                <ContactForm />
              </Fade>
            </div>

            <div className="container button-direct mt-4 mr-2">
              <Button
                variant="text"
                onClick={changeVisibility}
                className="animated infinite pulse"
              >
                {displayForm === "inline"
                  ? portfolio.labels.go_back
                  : portfolio.labels.send_email_direct}
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
