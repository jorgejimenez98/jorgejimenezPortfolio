import { createStore, combineReducers, applyMiddleware } from "redux";
import thunk from "redux-thunk";
import { composeWithDevTools } from "redux-devtools-extension";

// REDUCERS
import { snackbarReducer } from "./redux/reducers/snackBarReducer";
import { emailSendReducer } from "./redux/reducers/emailReducers";
import { languajeReducer } from "./redux/reducers/languajeReducers";

const reducer = combineReducers({
  snackbar: snackbarReducer,
  emailSend: emailSendReducer,
  languaje: languajeReducer,
});

const middleware = [thunk];

const store = createStore(
  reducer,
  {},
  composeWithDevTools(applyMiddleware(...middleware))
);

export default store;
