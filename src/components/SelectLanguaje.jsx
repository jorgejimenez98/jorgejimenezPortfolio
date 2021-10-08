import React from "react";
import { Box, MenuItem, FormControl, Select } from "@mui/material";

import SPAIN from "../assets/img/spain.png";
import USA from "../assets/img/usa.png";

function SelectLanguaje() {
  const [age, setAge] = React.useState("en");

  const handleChange = (event) => {
    setAge(event.target.value);
  };

  return (
    <Box sx={{ minWidth: 120 }} border="none">
      <FormControl fullWidth>
        <Select value={age} label="Select languaje" onChange={handleChange}>
          <MenuItem value={"en"}>
            <img src={USA} alt="English" className="languaje-image" />
            &nbsp; English
          </MenuItem>
          <MenuItem value={"es"}>
            <img src={SPAIN} alt="Spanish" className="languaje-image" />
            &nbsp; Español
          </MenuItem>
        </Select>
      </FormControl>
    </Box>
  );
}

export default SelectLanguaje;
