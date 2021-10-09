import React from "react";
import emoji from "react-easy-emoji";
import { useSelector } from "react-redux";
import SocialMedia from "../containers/SocialMedia";

function Home() {
  const { portfolio } = useSelector((state) => state.languaje);

  return (
    <div className="greet-main" id="greeting">
      <div className="greeting-main">
        <div className="greeting-text-div">
          <div>
            <h1 className={"greeting-text"}>
              {portfolio.greeting.title}
              <span className="wave-emoji">{emoji("👋")}</span>
            </h1>
            <p className={"greeting-text-p subTitle"}>
              {portfolio.greeting.subTitle}
            </p>
            <SocialMedia />
          </div>
        </div>
        <div className="greeting-image-div text-center">
          <img
            alt="man sitting on table"
            className="image"
            src={portfolio.greeting.image}
          ></img>
        </div>
      </div>
    </div>
  );
}

export default Home;
