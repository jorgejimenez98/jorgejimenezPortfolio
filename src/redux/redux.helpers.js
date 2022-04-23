import axios from "axios";

const dispatchErrorMessage = (dispatch, actionType, error) => {
  dispatch({
    type: actionType,
    payload:
      error.response && error.response.data.detail
        ? error.response.data.detail
        : error.message,
  });
};

const requestActionType = (dispatch, actionType) => {
  dispatch({
    type: actionType,
  });
};

const successActionType = (dispatch, actionType, data) => {
  dispatch({
    type: actionType,
    payload: data,
  });
};

const send_request = async (method, url) => {
  const { data } =  method === "GET" ? await axios.get(url) : "";
  return data;
};

const reduxFunc = {
  error: dispatchErrorMessage,
  request: requestActionType,
  success: successActionType,
  send_request,
};

export default reduxFunc;
