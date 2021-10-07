import React from "react";
import { VerticalTimelineElement } from "react-vertical-timeline-component";
import "react-vertical-timeline-component/style.min.css";
import WorkIcon from "@material-ui/icons/Work";
import Badge from "react-bootstrap/Badge";

function ExperienceElement({ experience }) {
  return (
    <VerticalTimelineElement
      className="vertical-timeline-element--work"
      contentStyle={{ boxShadow: "5px 5px 15px 5px rgba(135, 120, 120, 0.68)" }}
      date={experience.date}
      dateClassName="text-dark"
      iconStyle={{ background: "rgb(33, 150, 243)", color: "#fff" }}
      icon={<WorkIcon />}
    >
      <div className="row">
        <div className="col-md-4">
          <img
            className="logo-experience"
            src={experience.image}
            alt={"LOGO"}
          />
        </div>
        <div className="col-md-8">
          <h3 className="vertical-timeline-element-title mt-lg-4">
            <strong>{experience.job}</strong>
          </h3>
          <h5>{experience.place}</h5>
          <h5 className="text-muted text-white mt-2">{experience.location}</h5>
        </div>
      </div>

      <p>{experience.description}</p>

      <h5 className="mt-3">
        <strong>Tecnologies</strong>
      </h5>

      {experience.tecnologies.map((tech, i) => (
        <Badge pill className="experience-badge separate" key={i}>
          {tech}
        </Badge>
      ))}
    </VerticalTimelineElement>
  );
}

export default ExperienceElement;
