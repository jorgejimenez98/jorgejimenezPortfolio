import EXPERTISES from "../constants/expertises.constants";

const intialState = {
    loading: false,
    expertises: [],
    error: '',
}

export const expertisesReducer = (state = intialState, action) => {
  switch (action.type) {
    case EXPERTISES.REQUEST_SEND:
      return { ...intialState, loading: true };

    case EXPERTISES.SUCCESS_SEND:
      const expertises = action.payload
      return { ...intialState, loading: false, expertises };

    case EXPERTISES.ERROR_SEND:
      return { ...intialState, loading: false, error: action.payload };

    case EXPERTISES.RESET:
      return { intialState };

    default:
      return state;
  }
};