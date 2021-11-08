import { createStore, combineReducers, applyMiddleware } from "redux";
import thunk from "redux-thunk";
import { composeWithDevTools } from "redux-devtools-extension";

// REDUCERS
import { snackbarReducer } from "./redux/reducers/snackBarReducer";
import { emailSendReducer } from "./redux/reducers/emailReducers";
import { languajeReducer } from "./redux/reducers/languajeReducers";

// Languajes
import { portfolioEn } from "./portfolio/en";
import { portfolioEs } from "./portfolio/es";

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

const reducer = combineReducers({
  snackbar: snackbarReducer,
  emailSend: emailSendReducer,
  languaje: languajeReducer,
});

const middleware = [thunk];

const store = createStore(
  reducer,
  initialState,
  composeWithDevTools(applyMiddleware(...middleware))
);

export default store;
