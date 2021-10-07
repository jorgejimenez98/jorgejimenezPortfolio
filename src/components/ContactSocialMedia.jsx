import React from "react";
import { contactInfo } from "../portfolio";
import SocialMedia from "../containers/SocialMedia";

function ContactSocialMedia() {
  return (
    <div>
      <div className={"contact-text-div"}>
        <a className="contact-detail" href={"tel:" + contactInfo.number}>
          Spain {contactInfo.number}
        </a>
        <br />
        <br />
        <a className="contact-detail" href={"tel:" + contactInfo.cubaNumber}>
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
  );
}

export default ContactSocialMedia;
