import React from "react";

function SkillList({ title, list }) {
  return (
    <div>
      <h3 className="skills-heading text-center text-muted">{title}</h3>
      <ul className="dev-icons">
        {list.map((skills, i) => {
          return (
            <li
              key={i}
              className="software-skill-inline"
              name={skills.skillName}
            >
              {skills.icon ? (
                <React.Fragment>
                  <img alt="django" src={skills.icon} className="black-white" />
                  <p>{skills.skillName}</p>
                </React.Fragment>
              ) : (
                <React.Fragment>
                  <i className={skills.fontAwesomeClassname}></i>
                  <p>{skills.skillName}</p>
                </React.Fragment>
              )}
            </li>
          );
        })}
      </ul>
    </div>
  );
}

export default SkillList;
