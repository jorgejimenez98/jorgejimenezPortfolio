import React, { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { getMainTechs } from "../redux/actions";
import { Fade } from "react-awesome-reveal";
import { Loader } from "../containers";
import { skills } from "../portfolio/skills";

// Components
import SkillList from "../components/Skills/SkillList";
import SkillsMainSkills from "../components/Skills/SkillsMainSkills";

export default function Skills() {
  const dispatch = useDispatch();
  const { portfolio, languaje } = useSelector((state) => state.languaje);
  const { mainTechs, loading } = useSelector((state) => state.mainTechs);

  useEffect(() => {
    dispatch(getMainTechs());
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
          <SkillList title={portfolio.techStack.tools} list={skills} />
        </div>
      </div>
    </Fade>
  );
}
