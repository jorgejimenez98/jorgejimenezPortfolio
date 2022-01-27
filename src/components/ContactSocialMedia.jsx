import React from "react";
import { useSelector } from "react-redux";
import SocialMedia from "../containers/SocialMedia";

function ContactSocialMedia() {
  const { portfolio } = useSelector((state) => state.languaje);

  return (
    <div>
      <div className={"contact-text-div"}>
        <a
          className="contact-detail"
          href={"tel:" + portfolio.contactInfo.number}
        >
          {portfolio.labels.spain} {portfolio.contactInfo.number}
        </a>
        <br />
        <br />
        <a
          className="contact-detail-email"
          href={"mailto:" + portfolio.contactInfo.emailAddress}
        >
          {portfolio.contactInfo.emailAddress}
        </a>
        <br />
        <br />
        <SocialMedia />
      </div>
    </div>
  );
}

export default ContactSocialMedia;
