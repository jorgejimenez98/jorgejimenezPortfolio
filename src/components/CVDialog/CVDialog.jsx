import React, { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { BootstrapDialog, BootstrapDialogTitle, Transition } from "./settings";
import { getCurriculumns } from "../../redux/actions";
import { Loader } from "../../containers";
import DialogContent from "@mui/material/DialogContent";
import Typography from "@mui/material/Typography";
import Button from "@mui/material/Button";

export default function CVDialog({ open, handleClose }) {
  const dispatch = useDispatch();
  const { portfolio, languaje } = useSelector((state) => state.languaje);
  const { curriculumns, loading } = useSelector((state) => state.curriculumns);

  const getCurrLink = (type) => {
    return curriculumns.find(
      (item) => item.language === languaje && item.name === type
    ).link;
  };

  useEffect(() => {
    dispatch(getCurriculumns());
  }, [dispatch]);

  return (
    <div>
      {loading ? (
        <Loader />
      ) : (
        curriculumns.length > 0 && (
          <BootstrapDialog
            onClose={handleClose}
            aria-labelledby="customized-dialog-title"
            fullWidth={true}
            maxWidth={"sm"}
            TransitionComponent={Transition}
            open={open}
          >
            <BootstrapDialogTitle
              id="customized-dialog-title"
              onClose={handleClose}
            >
              {portfolio.labels.modal_title}
            </BootstrapDialogTitle>
            <DialogContent dividers>
              <div>
                <Button
                  variant="outlined"
                  fullWidth
                  target="_blank"
                  href={getCurrLink("Simple")}
                >
                  {portfolio.labels.simple_design}
                </Button>
              </div>
              <div className="mt-2">
                <Button
                  variant="outlined"
                  fullWidth
                  target="_blank"
                  href={getCurrLink("Modern")}
                >
                  {portfolio.labels.simple_modern}
                </Button>
              </div>

              <div className="mt-2 text-center">
                <Typography variant="caption" display="block" gutterBottom>
                  {portfolio.labels.change_lang_dialog}
                </Typography>
              </div>
            </DialogContent>
          </BootstrapDialog>
        )
      )}
    </div>
  );
}
