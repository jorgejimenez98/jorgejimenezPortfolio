import React, { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import SocialMedia from "../containers/SocialMedia";
import { getConfigurations } from "../redux/actions";

function ContactSocialMedia() {
  const dispatch = useDispatch();
  const { portfolio } = useSelector((state) => state.languaje);
  const { settings: user } = useSelector((state) => state.settings);

  useEffect(() => {
    dispatch(getConfigurations());
  }, [dispatch]);

  return (
    <div>
      <div className={"contact-text-div"}>
        <a className="contact-detail" href={"tel:" + user?.phone_number}>
          {portfolio.labels.spain} {user?.phone_number}
        </a>
        <br />
        <br />
        <a
          className="contact-detail-email"
          href={"mailto:" + user?.developer_email}
        >
          {user?.developer_email}
        </a>
        <br />
        <br />
        <SocialMedia />
      </div>
    </div>
  );
}

export default ContactSocialMedia;
