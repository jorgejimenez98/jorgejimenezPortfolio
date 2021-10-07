import React from "react";
import { VerticalTimeline } from "react-vertical-timeline-component";
import "react-vertical-timeline-component/style.min.css";
import ExperienceElement from "./ExperienceElement";
import { experience } from "../portfolio";

function Experience() {
  return (
    <React.Fragment>
      <h1 className="text-center mb-4">Work Experience</h1>
      <VerticalTimeline>
        <ExperienceElement experience={experience.freelance} />
        <ExperienceElement experience={experience.ucm} />
      </VerticalTimeline>
    </React.Fragment>
  );
}

export default Experience;
