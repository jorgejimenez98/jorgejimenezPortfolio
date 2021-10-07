import React from "react";
import Headroom from "react-headroom";
import { greeting } from "../portfolio";
import { LinkContainer } from "react-router-bootstrap";
import { Link } from "react-router-dom";

export default function Header() {
  return (
    <Headroom>
      <header className={"header"}>
        <LinkContainer to={"/"}>
          <div className="logo pointer">
            <span className="grey-color"> &lt;</span>
            <span className="logo-name">{greeting.username}</span>
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
            <Link to="/contact">Contact Me</Link>
          </li>
        </ul>
      </header>
    </Headroom>
  );
}
