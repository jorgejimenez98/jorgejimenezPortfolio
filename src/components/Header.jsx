import React from "react";
import { useSelector } from "react-redux";
import Headroom from "react-headroom";
import { LinkContainer } from "react-router-bootstrap";
import { Link } from "react-router-dom";
import SelectLanguaje from "./SelectLanguaje";

export default function Header() {
  const { portfolio } = useSelector((state) => state.languaje);

  return (
    <Headroom>
      <header className={"header"}>
        <LinkContainer to={"/"}>
          <div className="logo pointer">
            <span className="grey-color"> &lt;</span>
            <span className="logo-name">{portfolio.greeting.username}</span>
            <span className="grey-color">/&gt;</span>
          </div>
        </LinkContainer>

        <input className="menu-btn" type="checkbox" id="menu-btn" />
        <label
          className="menu-icon"
          htmlFor="menu-btn"
          style={{ color: "white" }}
        >
          <span className={"navicon"}></span>
        </label>

        <ul className={"menu"}>
          <li>
            <SelectLanguaje />
          </li>
          <li>
            <Link to="/experience">{portfolio.labels.experience}</Link>
          </li>
          <li>
            <Link to="/contact">{portfolio.labels.contact}</Link>
          </li>
        </ul>
      </header>
    </Headroom>
  );
}
