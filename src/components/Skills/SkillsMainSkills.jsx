import React from "react";
import { getTextTranslated } from "../../helpers";

function SkillsMainSkills({ portfolio, mainTechs, languaje }) {
  return (
    <div className="skills-bar">
      <h3 className="skills-heading text-muted">
        {portfolio.techStack.favorite}
      </h3>
      {mainTechs.map((exp) => {
        const progressStyle = {
          width: exp.proccessPorcent,
        };
        return (
          <div key={exp.id} className="skill">
            <p style={{'marginBottom': '-3px'}}>{getTextTranslated(exp.texts, languaje)}</p>
            <div className="meter">
              <span style={progressStyle}></span>
            </div>
          </div>
        );
      })}
    </div>
  );
}

export default SkillsMainSkills;
