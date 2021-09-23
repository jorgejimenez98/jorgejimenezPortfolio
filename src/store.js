import { createStore, combineReducers, applyMiddleware } from "redux";
import thunk from "redux-thunk";
import { composeWithDevTools } from "redux-devtools-extension";

// REDUCERS
import { snackbarReducer } from "./redux/reducers/snackBarReducer";
import { emailSendReducer } from "./redux/reducers/emailReducers";

const reducer = combineReducers({
  snackbar: snackbarReducer,
  emailSend: emailSendReducer,
});

const middleware = [thunk];

const store = createStore(
  reducer,
  {},
  composeWithDevTools(applyMiddleware(...middleware))
);

export default store;
