import { CHANGE_LANGUAJE_MESSAGES } from "../constants/languajeConstants";
import { portfolioEn } from "../../portfolio/en";
import { portfolioEs } from "../../portfolio/es";

export const changeLanguaje = (languaje) => async (dispatch) => {
  const isEnglish = languaje === "en";
  dispatch({
    type: CHANGE_LANGUAJE_MESSAGES,
    payload: {
      languaje: languaje,
      portfolio: isEnglish ? portfolioEn : portfolioEs,
    },
  });

  localStorage.setItem("languaje", languaje);
};
