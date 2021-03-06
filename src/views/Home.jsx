import React, { useEffect } from "react";
import emoji from "react-easy-emoji";
import { useSelector, useDispatch } from "react-redux";
import getConfigurations from "../redux/actions/configurationActions";
import SocialMedia from "../containers/SocialMedia";
import { Loader } from "../containers";
import { getTextTranslated } from "../helpers";

function Home() {
  const dispatch = useDispatch();
  const { languaje } = useSelector((state) => state.languaje);
  const { settings, loading } = useSelector((state) => state.settings);

  useEffect(() => {
    dispatch(getConfigurations());
  }, [dispatch]);

  return (
    <React.Fragment>
      {loading ? (
        <Loader />
      ) : (
        settings !== null && (
          <div className="greet-main" id="greeting">
            <div className="greeting-main">
              <div className="greeting-text-div">
                <div>
                  <h1 className={"greeting-text"}>
                    {getTextTranslated(settings.title_presentations, languaje)}
                    <span className="wave-emoji">{emoji("👋")}</span>
                  </h1>
                  <p className={"greeting-text-p subTitle"}>
                    {getTextTranslated(settings.main_presentations, languaje)}
                  </p>
                  <SocialMedia showResumeButtom={true} />
                </div>
              </div>
              <div className="greeting-image-div text-center">
                <img
                  alt="man sitting on table"
                  className="image"
                  src={settings.profilePicture}
                ></img>
              </div>
            </div>
          </div>
        )
      )}
    </React.Fragment>
  );
}

export default Home;
