import { EMAIL } from "../constants/emailConstants";
import reduxFunc from "../redux.helpers";
import urls from "../back.urls";

export const send_email = (params) => async (dispatch) => {
  try {
    reduxFunc.request(dispatch, EMAIL.REQUEST_SEND);
    const data = await reduxFunc.send_request("POST", urls.sendEmail, params);
    reduxFunc.success(dispatch, EMAIL.SUCCESS_SEND, data);
  } catch (error) {
    reduxFunc.error(dispatch, EMAIL.ERROR_SEND, error);
  }
};
