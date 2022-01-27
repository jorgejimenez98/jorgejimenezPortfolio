import { EMAIL } from "../constants/emailConstants";

export const emailSendReducer = (state = {}, action) => {
  switch (action.type) {
    case EMAIL.REQUEST_SEND:
      return { loading: true };

    case EMAIL.SUCCESS_SEND:
      return { loading: false, success: true };

    case EMAIL.ERROR_SEND:
      return { loading: false, error: action.payload };

    case EMAIL.RESET:
      return {};

    default:
      return state;
  }
};
