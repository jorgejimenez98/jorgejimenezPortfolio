import React from "react";
import Badge from "react-bootstrap/Badge";

function TechList({ techArray, messageLabel }) {
  return (
    <div>
      <h5 className="mt-3">
        <strong>{messageLabel}</strong>
      </h5>

      {techArray?.map((item, i) => (
        <Badge pill className="experience-badge separate" key={i}>
          {item}
        </Badge>
      ))}
    </div>
  );
}

export default TechList;
