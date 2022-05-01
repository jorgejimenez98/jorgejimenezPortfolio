import SOCIAL_MEDIA from "../constants/socialMedias.constants";
import reduxFunc from "../redux.helpers";
import urls from "../back.urls";

const getSocialMedias = () => async (dispatch) => {
  try {
    reduxFunc.request(dispatch, SOCIAL_MEDIA.REQUEST_SEND);
    const data = await reduxFunc.send_request("GET", urls.socialMedia);
    reduxFunc.success(dispatch, SOCIAL_MEDIA.SUCCESS_SEND, data);
  } catch (error) {
    reduxFunc.error(dispatch, SOCIAL_MEDIA.ERROR_SEND, error);
  }
};

export default getSocialMedias;
