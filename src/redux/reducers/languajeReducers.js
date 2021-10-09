import { CHANGE_LANGUAJE_MESSAGES } from "../constants/languajeConstants";
import { portfolioEn } from "../../portfolio/en";

const initialState = {
  languaje: "en",
  portfolio: portfolioEn,
};

export const languajeReducer = (state = initialState, action) => {
  switch (action.type) {
    case CHANGE_LANGUAJE_MESSAGES:
      const { languaje, portfolio } = action.payload;
      return {
        languaje: languaje,
        portfolio: portfolio,
      };
    default:
      return state;
  }
};
