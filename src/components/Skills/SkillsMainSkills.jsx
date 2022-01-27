import React from "react";

function SkillsMainSkills({ portfolio }) {
  return (
    <div className="skills-bar">
      <h3 className="skills-heading text-muted">{portfolio.techStack.favorite}</h3>
      {portfolio.techStack.experience.map((exp, i) => {
        const progressStyle = {
          width: exp.progressPercentage,
        };
        return (
          <div key={i} className="skill">
            <p>{exp.Stack}</p>
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
