import React from "react";
import { useSelector, useDispatch } from "react-redux";
import { changeLanguaje } from "../redux/actions/languajeActions";
import { Box, MenuItem, FormControl, Select } from "@mui/material";
// Images
import SPAIN from "../assets/img/spain.png";
import USA from "../assets/img/usa.png";

function SelectLanguaje() {
  const dispatch = useDispatch();
  const { languaje } = useSelector((state) => state.languaje);

  const handleChange = (event) => {
    dispatch(changeLanguaje(event.target.value));
  };

  return (
    <Box sx={{ minWidth: 120 }} className="select-lang">
      <FormControl fullWidth variant="outlined">
        <Select value={languaje} onChange={handleChange}>
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
