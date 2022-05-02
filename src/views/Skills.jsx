import React, { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { getMainTechs, getTechsWithIcons } from "../redux/actions";
import { Fade } from "react-awesome-reveal";
import { Loader } from "../containers";

// Components
import SkillList from "../components/Skills/SkillList";
import SkillsMainSkills from "../components/Skills/SkillsMainSkills";

export default function Skills() {
  const dispatch = useDispatch();
  const { portfolio, languaje } = useSelector((state) => state.languaje);
  const { mainTechs, loading } = useSelector((state) => state.mainTechs);
  const { techs, loading: loadingTechs } = useSelector(
    (state) => state.technologies
  );

  useEffect(() => {
    dispatch(getMainTechs());
    dispatch(getTechsWithIcons());
  }, [dispatch]);

  return (
    <Fade bottom duration={1000} distance="20px">
      <div className="skills-container">
        {loading ? (
          <Loader />
        ) : (
          mainTechs.length > 0 && (
            <SkillsMainSkills
              portfolio={portfolio}
              mainTechs={mainTechs}
              languaje={languaje}
            />
          )
        )}

        <div className="software-skills-main-div ml-2">
          {loadingTechs ? (
            <Loader />
          ) : (
            techs.length > 0 && (
              <SkillList title={portfolio.techStack.tools} list={techs} />
            )
          )}
        </div>
      </div>
    </Fade>
  );
}
