import { MAIN_TECHS, TECHS_ICONS } from "../constants/main_techs";
import reduxFunc from "../redux.helpers";
import urls from "../back.urls";

export const getMainTechs = () => async (dispatch) => {
  try {
    reduxFunc.request(dispatch, MAIN_TECHS.REQUEST_SEND);
    const data = await reduxFunc.send_request("GET", urls.mainTechs);
    reduxFunc.success(dispatch, MAIN_TECHS.SUCCESS_SEND, data);
  } catch (error) {
    reduxFunc.error(dispatch, MAIN_TECHS.ERROR_SEND, error);
  }
};

export const getTechsWithIcons = () => async (dispatch) => {
  try {
    reduxFunc.request(dispatch, TECHS_ICONS.REQUEST_SEND);
    const data = await reduxFunc.send_request("GET", urls.techs);
    reduxFunc.success(dispatch, TECHS_ICONS.SUCCESS_SEND, data);
  } catch (error) {
    reduxFunc.error(dispatch, TECHS_ICONS.ERROR_SEND, error);
  }
};
