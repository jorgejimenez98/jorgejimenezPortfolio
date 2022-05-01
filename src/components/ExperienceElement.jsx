import React from "react";
import { useSelector } from "react-redux";
import { VerticalTimelineElement } from "react-vertical-timeline-component";
import WorkIcon from "@material-ui/icons/Work";
import TechList from "./TechList";
import { getTextTranslated } from "../helpers";
import "react-vertical-timeline-component/style.min.css";

function ExperienceElement({ experience }) {
  const { languaje, portfolio } = useSelector((state) => state.languaje);

  const getDateString = () => {
    const dateEnd = experience.is_currently_working
      ? portfolio.labels.present
      : experience.date_end;
    const timeWorking = getTextTranslated(experience.time_working, languaje);
    return `${experience.date_start} - ${dateEnd} (${timeWorking})`;
  };

  return (
    <VerticalTimelineElement
      className="vertical-timeline-element--work"
      contentStyle={{ boxShadow: "5px 5px 15px 5px rgba(135, 120, 120, 0.68)" }}
      date={getDateString()}
      dateClassName="text-dark"
      iconStyle={{ background: "rgb(33, 150, 243)", color: "#fff" }}
      icon={<WorkIcon />}
    >
      <div className="row">
        <div className="col-md-4">
          <img
            className="logo-experience"
            src={experience.company_logo}
            alt={"LOGO"}
          />
        </div>
        <div className="col-md-8">
          <h3 className="vertical-timeline-element-title mt-lg-4">
            <strong>{getTextTranslated(experience.job_rols, languaje)}</strong>
          </h3>
          <h5>{getTextTranslated(experience.company_names, languaje)}</h5>
          <h5 className="text-muted text-white mt-2">
            {getTextTranslated(experience.locations, languaje)}
          </h5>
        </div>
      </div>

      <p>{getTextTranslated(experience.descriptions, languaje)}</p>

      <TechList
        techArray={experience.techs}
        messageLabel={portfolio.labels.tech}
      />
      <TechList
        techArray={experience.key_experiences}
        messageLabel={portfolio.labels.keyExperience}
      />
    </VerticalTimelineElement>
  );
}

export default ExperienceElement;
