import React, { useEffect } from "react";
import emoji from "react-easy-emoji";
import { useSelector, useDispatch } from "react-redux";
import getConfigurations from "../redux/actions/configurationActions";
import SocialMedia from "../containers/SocialMedia";
import { Loader } from "../containers";

function Home() {
  const dispatch = useDispatch();
  const { languaje } = useSelector((state) => state.languaje);
  const { settings, loading } = useSelector((state) => state.settings);

  useEffect(() => {
    dispatch(getConfigurations());
  }, [dispatch]);

  const getTittle = () => {
    return settings.title_presentations.find(
      (item) => item.language === languaje
    )?.text;
  };

  const getPresentation = () => {
    return settings.main_presentations.find(
      (item) => item.language === languaje
    )?.text;
  };

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
                    {getTittle()}
                    <span className="wave-emoji">{emoji("👋")}</span>
                  </h1>
                  <p className={"greeting-text-p subTitle"}>
                    {getPresentation()}
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
