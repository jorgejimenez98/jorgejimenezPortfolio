import { combineReducers } from 'redux'

// REDUCERS
import { snackbarReducer } from "./reducers/snackBarReducer";
import { emailSendReducer } from "./reducers/emailReducers";
import { languajeReducer } from "./reducers/languajeReducers";
import { getConfigReducer } from './reducers/configurationReducers'
import { expertisesReducer } from './reducers/expertises.reducers'

// Languajes
import { portfolioEn } from "../portfolio/en";
import { portfolioEs } from "../portfolio/es";

// Check if there is a languaje on localStorage

const lang = localStorage.getItem("languaje")
  ? localStorage.getItem("languaje")
  : null;

let initialState = { languaje: { languaje: "", portfolio: {} } };
if (lang === null) {
  initialState.languaje.languaje = "en";
  initialState.languaje.portfolio = portfolioEn;
  localStorage.setItem("languaje", "en");
} else if (lang === "en") {
  initialState.languaje.languaje = "en";
  initialState.languaje.portfolio = portfolioEn;
} else {
  initialState.languaje.languaje = "es";
  initialState.languaje.portfolio = portfolioEs;
}

// Combine Reducers

export const reducers = combineReducers({
  snackbar: snackbarReducer,
  emailSend: emailSendReducer,
  languaje: languajeReducer,
  settings: getConfigReducer,
  expertises: expertisesReducer,
});

export default initialState