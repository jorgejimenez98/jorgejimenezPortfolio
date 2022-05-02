import React from "react";

function SkillList({ title, list }) {
  return (
    <div>
      <h3 className="skills-heading text-center text-muted">{title}</h3>
      <ul className="dev-icons">
        {list.map((skill) => {
          return (
            <li key={skill.id} className="software-skill-inline" name={skill.name}>
              {skill.has_logo ? (
                <React.Fragment>
                  <img
                    alt="django"
                    src={skill.image_logo}
                    className="black-white"
                  />
                  <p>{skill.name}</p>
                </React.Fragment>
              ) : (
                <React.Fragment>
                  <i className={skill.icon_class}></i>
                  <p>{skill.name}</p>
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
