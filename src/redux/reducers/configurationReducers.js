import CONFIGURATION from "../constants/configConstants";

const intialState = {
    loading: false,
    success: null,
    error: '',
    settings: null
}

export const getConfigReducer = (state = intialState, action) => {
  switch (action.type) {
    case CONFIGURATION.REQUEST_SEND:
      return { ...intialState, loading: true };

    case CONFIGURATION.SUCCESS_SEND:
      const settings = action.payload
      return { ...intialState, loading: false, success: true, settings: settings };

    case CONFIGURATION.ERROR_SEND:
      return { ...intialState, loading: false, error: action.payload };

    case CONFIGURATION.RESET:
      return { ...intialState };

    default:
      return state;
  }
};
