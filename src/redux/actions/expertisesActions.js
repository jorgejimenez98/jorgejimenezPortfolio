import  EXPERTISES  from "../constants/expertises.constants";
import reduxFunc from '../redux.helpers'
import urls  from '../back.urls';

const getExpertises = () => async (dispatch) => {
    try {
        reduxFunc.request(dispatch, EXPERTISES.REQUEST_SEND);
        const data  = await reduxFunc.send_request('GET', urls.expertises);
        reduxFunc.success(dispatch, EXPERTISES.SUCCESS_SEND, data);
    } catch (error) {
        reduxFunc.error(dispatch, EXPERTISES.ERROR_SEND, error);
    }
};

export default getExpertises