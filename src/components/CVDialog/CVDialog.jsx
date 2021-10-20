import * as React from "react";
import { useSelector } from "react-redux";
import { BootstrapDialog, BootstrapDialogTitle, Transition } from "./settings";
import DialogContent from "@mui/material/DialogContent";
import Button from "@mui/material/Button";

export default function CVDialog({ open, handleClose }) {
  const { portfolio } = useSelector((state) => state.languaje);

  return (
    <div>
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
              href={portfolio.cv_links.simple}
            >
              {portfolio.labels.simple_design}
            </Button>
          </div>
          <div className="mt-2">
            <Button
              variant="outlined"
              fullWidth
              target="_blank"
              href={portfolio.cv_links.modern}
            >
              {portfolio.labels.simple_modern}
            </Button>
          </div>
        </DialogContent>
      </BootstrapDialog>
    </div>
  );
}
