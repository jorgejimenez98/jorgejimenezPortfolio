import React from "react";
import { useSelector } from "react-redux";
import { VerticalTimeline } from "react-vertical-timeline-component";
import ExperienceElement from "../components/ExperienceElement";
import "react-vertical-timeline-component/style.min.css";

function Experience() {
  const { portfolio } = useSelector((state) => state.languaje);

  return (
    <React.Fragment>
      <h1 className="text-center mb-4">{portfolio.labels.experience}</h1>
      <VerticalTimeline>
        <ExperienceElement experience={portfolio.experience.freelance} />
        <ExperienceElement experience={portfolio.experience.ucm} />
      </VerticalTimeline>
    </React.Fragment>
  );
}

export default Experience;
