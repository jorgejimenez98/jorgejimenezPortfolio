import SOCIAL_MEDIA from "../constants/socialMedias.constants";

const intialState = {
  loading: false,
  socialMedias: [],
  error: "",
};

export const socialMediasReducer = (state = intialState, action) => {
  switch (action.type) {
    case SOCIAL_MEDIA.REQUEST_SEND:
      return { ...intialState, loading: true };

    case SOCIAL_MEDIA.SUCCESS_SEND:
      const socialMedias = action.payload;
      return { ...intialState, loading: false, socialMedias };

    case SOCIAL_MEDIA.ERROR_SEND:
      return { ...intialState, loading: false, error: action.payload };

    case SOCIAL_MEDIA.RESET:
      return { intialState };

    default:
      return state;
  }
};
