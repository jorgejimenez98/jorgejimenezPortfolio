import  CONFIGURATION  from "../constants/configConstants";
import reduxFunc from '../redux.helpers'
import urls  from '../back.urls';

const getConfigurations = () => async (dispatch) => {
    try {
        reduxFunc.request(dispatch, CONFIGURATION.REQUEST_SEND);
        const data  = await reduxFunc.send_request('GET', urls.configurations);
        reduxFunc.success(dispatch, CONFIGURATION.SUCCESS_SEND, data);
    } catch (error) {
        reduxFunc.error(dispatch, CONFIGURATION.ERROR_SEND, error);
    }
};

export default getConfigurations