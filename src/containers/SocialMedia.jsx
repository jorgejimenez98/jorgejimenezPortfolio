import React, { useState, useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { Button } from "@mui/material";
import { Loader } from "../containers";
import { getSocialMedias } from "../redux/actions";
import CVDialog from "../components/CVDialog/CVDialog";

export default function SocialMedia({ showResumeButtom }) {
  const dispatch = useDispatch();
  const [open, setOpen] = useState(false);
  const { portfolio } = useSelector((state) => state.languaje);
  const { socialMedias, loading } = useSelector((state) => state.socialMedias);

  useEffect(() => {
    dispatch(getSocialMedias());
  }, [dispatch]);

  const handleClose = () => {
    setOpen(false);
  };

  return (
    <div className="social-media-div">
      {loading ? (
        <Loader />
      ) : (
        socialMedias.length > 0 && (
          <React.Fragment>
            {socialMedias.map((item) => (
              <a
                href={item.link}
                className={item.className}
                target="_blank"
                rel="noopener noreferrer"
              >
                <i className={item.iconClassName}></i>
              </a>
            ))}

            {showResumeButtom && (
              <Button
                variant="contained"
                onClick={() => setOpen(true)}
                style={{ marginLeft: "25px" }}
              >
                {portfolio.labels.cv_button}
              </Button>
            )}

            <CVDialog open={open} handleClose={handleClose} />
          </React.Fragment>
        )
      )}
    </div>
  );
}
