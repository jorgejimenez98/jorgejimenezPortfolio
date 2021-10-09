import React from "react";
import { useSelector } from "react-redux";
import { VerticalTimeline } from "react-vertical-timeline-component";
import ExperienceElement from "../components/ExperienceElement";
import "react-vertical-timeline-component/style.min.css";

function Experience() {
  const { portfolio } = useSelector((state) => state.languaje);

  return (
    <React.Fragment>
      <h1 className="text-center mt-4 text-muted">
        {portfolio.labels.experience}
      </h1>
      <h1 className="animated infinite pulse text-muted text-open mt-4 mb-3">
        {portfolio.labels.open}
      </h1>
      <VerticalTimeline>
        <ExperienceElement experience={portfolio.experience.freelance} />
        <ExperienceElement experience={portfolio.experience.ucm} />
      </VerticalTimeline>
    </React.Fragment>
  );
}

export default Experience;
