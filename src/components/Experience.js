import React from "react";
import {
  VerticalTimeline,
  VerticalTimelineElement,
} from "react-vertical-timeline-component";
import "react-vertical-timeline-component/style.min.css";
import WorkIcon from "@material-ui/icons/Work";
import ExperienceElement from "./ExperienceElement";

function Experience() {
  return (
    <VerticalTimeline>
      <ExperienceElement />
      <VerticalTimelineElement
        className="vertical-timeline-element--work"
        date="2010 - 2011"
        contentStyle={{ background: "rgb(33, 150, 243)", color: "#fff" }}
        iconStyle={{ background: "rgb(33, 150, 243)", color: "#fff" }}
        dateClassName="text-dark"
        icon={<WorkIcon />}
      >
        <h3 className="vertical-timeline-element-title">Art Director</h3>
        <h4 className="vertical-timeline-element-subtitle">
          San Francisco, CA
        </h4>
        <p>
          Creative Direction, User Experience, Visual Design, SEO, Online
          Marketing
        </p>
      </VerticalTimelineElement>
    </VerticalTimeline>
  );
}

export default Experience;
