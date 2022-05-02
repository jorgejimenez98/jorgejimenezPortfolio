import MAIN_TECHS from "../constants/main_techs";

const intialState = {
  loading: false,
  mainTechs: [],
  error: "",
  settings: null,
};

export const getMainTechsReducer = (state = intialState, action) => {
  switch (action.type) {
    case MAIN_TECHS.REQUEST_SEND:
      return { ...intialState, loading: true };

    case MAIN_TECHS.SUCCESS_SEND:
      const mainTechs = action.payload;
      return { ...intialState, loading: false, mainTechs };

    case MAIN_TECHS.ERROR_SEND:
      return { ...intialState, loading: false, error: action.payload };

    case MAIN_TECHS.RESET:
      return { ...intialState };

    default:
      return state;
  }
};
