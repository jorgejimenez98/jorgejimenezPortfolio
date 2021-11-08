import React from "react";
import { useSelector } from "react-redux";
import { Fade } from "react-awesome-reveal";
import { skills } from "../portfolio/skills"

// Components
import SkillList from "../components/Skills/SkillList";
import SkillsMainSkills from "../components/Skills/SkillsMainSkills";;

export default function Skills() {
  const { portfolio } = useSelector((state) => state.languaje);

  return (
    <Fade bottom duration={1000} distance="20px">
      <div className="skills-container">
        <SkillsMainSkills portfolio={portfolio} />

        <div className="software-skills-main-div ml-2">
          <SkillList title={portfolio.techStack.tools} list={skills} />
        </div>
      </div>
    </Fade>
  );
}
