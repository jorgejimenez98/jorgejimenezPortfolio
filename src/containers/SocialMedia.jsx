import React, { useState } from "react";
import { useSelector } from "react-redux";
import { Button } from "@mui/material";
import CVDialog from "../components/CVDialog/CVDialog";

export default function SocialMedia({ showResumeButtom }) {
  const [open, setOpen] = useState(false);
  const { portfolio } = useSelector((state) => state.languaje);

  const handleClose = () => {
    setOpen(false);
  };

  if (!portfolio.socialMediaLinks.display) {
    return null;
  }
  return (
    <div className="social-media-div">
      <a
        href={portfolio.socialMediaLinks.github}
        className="icon-button github"
        target="_blank"
        rel="noopener noreferrer"
      >
        <i className="fab fa-github"></i>
        <span></span>
      </a>

      <a
        href={`mailto:${portfolio.socialMediaLinks.gmail}`}
        className="icon-button google"
        target="_blank"
        rel="noopener noreferrer"
      >
        <i className="fab fa-google"></i>
        <span></span>
      </a>

      <a
        href={portfolio.socialMediaLinks.linkedin}
        className="icon-button linkedin"
        target="_blank"
        rel="noopener noreferrer"
      >
        <i className="fab fa-linkedin-in"></i>
        <span></span>
      </a>

      <a
        href={portfolio.socialMediaLinks.facebook}
        className="icon-button facebook"
        target="_blank"
        rel="noopener noreferrer"
      >
        <i className="fab fa-facebook-f"></i>
        <span></span>
      </a>

      {showResumeButtom && (
        <Button
          variant="contained"
          onClick={() => setOpen(true)}
          style={{ marginLeft: "25px" }}
        >
          Ver mi CV
        </Button>
      )}

      <CVDialog open={open} handleClose={handleClose} />
    </div>
  );
}
