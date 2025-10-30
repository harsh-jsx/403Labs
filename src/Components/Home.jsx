import React from "react";
import gsap from "gsap";
import { useState, useRef, useLayoutEffect } from "react";

const Home = () => {
  return (
    <div
      className="home-container text-black"
      style={{ marginTop: "100px", padding: "2rem" }}
    >
      <h1 className="home-title text-5xl font-bold font-inter">
        Brands for the next
      </h1>
      <video src="/public/main-bg.mp4" autoPlay muted loop></video>
    </div>
  );
};

export default Home;
