import { EMAIL } from "../constants/emailConstants";

export const send_email = (serviceId, templateId, values) => async (
  dispatch
) => {
  dispatch({
    type: EMAIL.REQUEST_SEND,
  });

  window.emailjs
    .send(serviceId, templateId, {
      reply_to: values.email,
      fullName: values.fullName,
      message: values.message,
    })
    .then((res) => {
      dispatch({
        type: EMAIL.SUCCESS_SEND,
      });
    })
    .catch((err) => {
      const message =
        "Sorry, the server is not working. Press the (Go Back) button and use the other ways to contact me";
      dispatch({
        type: EMAIL.ERROR_SEND,
        payload: message,
      });
    });
};
