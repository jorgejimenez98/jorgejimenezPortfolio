import * as React from "react";
import { BootstrapDialog, BootstrapDialogTitle, Transition } from "./settings";
import DialogContent from "@mui/material/DialogContent";
import Tabs from "@mui/material/Tabs";
import Tab from "@mui/material/Tab";

export default function CVDialog({ open, handleClose }) {
  const [value, setValue] = React.useState(1);

  const handleChange = (event, newValue) => {
    console.log(newValue);
    setValue(newValue);
  };

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
          Modal title
        </BootstrapDialogTitle>
        <DialogContent dividers>
          <Tabs
            value={value}
            onChange={handleChange}
            aria-label="disabled tabs example"
          >
            <Tab label="Active" />
            <Tab label="Active" />
          </Tabs>
        </DialogContent>
      </BootstrapDialog>
    </div>
  );
}
