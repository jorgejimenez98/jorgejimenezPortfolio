import CURRICULUMNS from "../constants/curriculumns.constants";

const intialState = {
    loading: false,
    curriculumns: [],
    error: '',
}

export const curriculumnsReducer = (state = intialState, action) => {
  switch (action.type) {
    case CURRICULUMNS.REQUEST_SEND:
      return { ...intialState, loading: true };

    case CURRICULUMNS.SUCCESS_SEND:
      const curriculumns = action.payload
      return { ...intialState, loading: false, curriculumns };

    case CURRICULUMNS.ERROR_SEND:
      return { ...intialState, loading: false, error: action.payload };

    case CURRICULUMNS.RESET:
      return { ...intialState };

    default:
      return state;
  }
};
