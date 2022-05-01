import React, { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { VerticalTimeline } from "react-vertical-timeline-component";
import ExperienceElement from "../components/ExperienceElement";
import { getConfigurations, getExpertises } from "../redux/actions";
import { Loader } from "../containers";
import "react-vertical-timeline-component/style.min.css";

function Experience() {
  const dispatch = useDispatch();
  const { portfolio } = useSelector((state) => state.languaje);
  const { settings: user } = useSelector((state) => state.settings);
  const { expertises, loading } = useSelector((state) => state.expertises);

  useEffect(() => {
    dispatch(getConfigurations());
    dispatch(getExpertises());
  }, [dispatch]);

  return (
    <React.Fragment>
      {loading ? (
        <Loader />
      ) : (
        <React.Fragment>
          <h1 className="text-center mt-4 text-muted">
            {portfolio.labels.experience}
          </h1>
          <h1 className="animated infinite pulse text-muted text-open mt-4 mb-3">
            {user?.is_open_to_work ? (
              <React.Fragment>{portfolio.labels.open}</React.Fragment>
            ) : (
              <React.Fragment>
                {portfolio.labels.currentlyWorking}
              </React.Fragment>
            )}
          </h1>
          <VerticalTimeline>
            {expertises.map((experience) => (
              <ExperienceElement experience={experience} key={experience.id} />
            ))}
          </VerticalTimeline>
        </React.Fragment>
      )}
    </React.Fragment>
  );
}

export default Experience;
