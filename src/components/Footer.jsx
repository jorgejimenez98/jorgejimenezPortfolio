import React from "react";
import { Fade } from "react-awesome-reveal";
import { useSelector } from "react-redux";

export default function Footer() {
  const { portfolio } = useSelector((state) => state.languaje);
  const { settings: user } = useSelector((state) => state.settings);

  return (
    <Fade bottom duration={1000} distance="5px">
      <div className="footer-div">
        <p className={"footer-text"}>{portfolio.labels.madeBy}</p>
        <p className={"footer-text"}>
          {portfolio.labels.check}{" "}
          <a
            href={user?.repository_project_url}
            target="_blank"
            rel="noopener noreferrer"
          >
            {portfolio.labels.here}
          </a>
        </p>
      </div>
    </Fade>
  );
}
