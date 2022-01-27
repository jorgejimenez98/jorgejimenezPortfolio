import { CHANGE_LANGUAJE_MESSAGES } from "../constants/languajeConstants";

export const languajeReducer = (state = {}, action) => {
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
