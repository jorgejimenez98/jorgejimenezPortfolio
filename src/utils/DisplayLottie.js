/* eslint-disable react/prop-types */
import React, { Suspense } from "react";
import Lottie from "react-lottie";
import Loading from "./Loading";

export default function DisplayLottie(props) {
  const defaultOptions = {
    loop: true,
    autoplay: true,
    animationData: props.animationData,
  };

  return (
    <Suspense fallback={<Loading />}>
      {/* To override default onClick pause by Lottie */}
      <div onClick="null">
        <Lottie options={defaultOptions} />
      </div>
    </Suspense>
  );
}
