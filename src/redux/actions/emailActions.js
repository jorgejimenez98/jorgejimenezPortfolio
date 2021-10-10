import { EMAIL } from "../constants/emailConstants";

export const send_email = (serviceId, templateId, values, languaje) => async (
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
      const messageEn =
        "Sorry, the server is not working. Press the (Go Back) button and use the other ways to contact me";
      const messageEs =
        "Perdóm, ha ocurrido un error en el servidos. Presiona el botón de (VOLVER) y usa las demás formas de ponerse en contacto conmigo";
      if (languaje === "en") {
        dispatch({
          type: EMAIL.ERROR_SEND,
          payload: messageEn,
        });
      } else {
        dispatch({
          type: EMAIL.ERROR_SEND,
          payload: messageEs,
        });
      }
    });
};
