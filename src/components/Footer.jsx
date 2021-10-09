import React from "react";
import { Fade } from "react-awesome-reveal";
import { useSelector } from "react-redux";

export default function Footer() {
  const { portfolio } = useSelector((state) => state.languaje);

  return (
    <Fade bottom duration={1000} distance="5px">
      <div className="footer-div">
        <p className={"footer-text"}>{portfolio.labels.madeBy}</p>
        <p className={"footer-text"}>
          {portfolio.labels.check}{" "}
          <a href="https://github.com/jorgejimenez98/jorgejimenezPortfolio.git">
            {portfolio.labels.here}
          </a>
        </p>
      </div>
    </Fade>
  );
}
