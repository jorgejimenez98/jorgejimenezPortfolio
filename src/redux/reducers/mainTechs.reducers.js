import { MAIN_TECHS, TECHS_ICONS } from "../constants/main_techs";

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

const intialStateTechs = {
  loading: false,
  techs: [],
  error: "",
  settings: null,
};

export const techsIconsReducers = (state = intialStateTechs, action) => {
  switch (action.type) {
    case TECHS_ICONS.REQUEST_SEND:
      return { ...intialStateTechs, loading: true };

    case TECHS_ICONS.SUCCESS_SEND:
      const techs = action.payload;
      return { ...intialStateTechs, loading: false, techs };

    case TECHS_ICONS.ERROR_SEND:
      return { ...intialStateTechs, loading: false, error: action.payload };

    case TECHS_ICONS.RESET:
      return { ...intialStateTechs };

    default:
      return state;
  }
};
