import MAIN_TECHS from "../constants/main_techs";
import reduxFunc from "../redux.helpers";
import urls from "../back.urls";

const getMainTechs = () => async (dispatch) => {
  try {
    reduxFunc.request(dispatch, MAIN_TECHS.REQUEST_SEND);
    const data = await reduxFunc.send_request("GET", urls.mainTechs);
    reduxFunc.success(dispatch, MAIN_TECHS.SUCCESS_SEND, data);
  } catch (error) {
    reduxFunc.error(dispatch, MAIN_TECHS.ERROR_SEND, error);
  }
};

export default getMainTechs;
