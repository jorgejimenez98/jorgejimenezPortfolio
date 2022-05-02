import  CURRICULUMNS  from "../constants/curriculumns.constants";
import reduxFunc from '../redux.helpers'
import urls  from '../back.urls';

const getCurriculumns = () => async (dispatch) => {
    try {
        reduxFunc.request(dispatch, CURRICULUMNS.REQUEST_SEND);
        const data  = await reduxFunc.send_request('GET', urls.curriculumns);
        reduxFunc.success(dispatch, CURRICULUMNS.SUCCESS_SEND, data);
    } catch (error) {
        reduxFunc.error(dispatch, CURRICULUMNS.ERROR_SEND, error);
    }
};

export default getCurriculumns