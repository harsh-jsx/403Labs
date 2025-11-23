import React, { useEffect } from "react";
import { gsap } from "gsap";
import { useGSAP } from "@gsap/react";
import { useRef, useLayoutEffect } from "react";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import ScrollReveal from "./scrollTrigger";
import { BentoGrid, BentoCard } from "./BentoGrid";
const Home = () => {
  gsap.registerPlugin(useGSAP, ScrollTrigger);
  const titleRef = useRef(null);
  const charsRef = useRef([]);
  const item1Ref = useRef(null);
  const item2Ref = useRef(null);
  useEffect(() => {
    const el = item1Ref.current;
    gsap.fromTo(
      el,
      { opacity: 0, y: 100 },
      { opacity: 1, duration: 1, ease: "power2.inOut", delay: 1 }
    );
  }, []);
  useLayoutEffect(() => {
    if (titleRef.current) {
      const text = titleRef.current.textContent;
      const chars = text.split("");
      titleRef.current.textContent = "";

      chars.forEach((char, i) => {
        const span = document.createElement("span");
        span.textContent = char === " " ? "\u00A0" : char;
        span.style.display = "inline-block";
        span.style.opacity = "0";
        span.style.filter = "blur(20px)";
        span.style.transform = "translateY(80px) rotateX(90deg) scale(0.5)";
        span.style.transformOrigin = "center bottom";
        titleRef.current.appendChild(span);
        charsRef.current.push(span);
      });
    }
  }, []);

  useGSAP(
    () => {
      if (charsRef.current.length > 0) {
        // Rich entrance animation - entire sentence animates together
        gsap.to(charsRef.current, {
          opacity: 1,
          y: 0,
          rotateX: 0,
          scale: 1,
          filter: "blur(0px)",
          duration: 2,
          ease: "power4.out",
        });

        // Continuous subtle floating animation for richness
      }
    },

    { scope: titleRef }
  );

  return (
    <div
      className="home-container text-black flex flex-col items-center justify-center gap-5"
      style={{ marginTop: "100px", padding: "2rem" }}
    >
      <div className="h-max w-max justify-center items-center flex">
        <h1
          ref={titleRef}
          className="home-title font-inter pb-4 text-center text-8xl font-medium -tracking-tight"
          style={{ perspective: "1000px" }}
        >
          Brands for the next
        </h1>{" "}
      </div>
      <div>
        <video
          src="/public/main-bg.mp4"
          className="w-full h-full pt-7 rounded-4xl"
          autoPlay
          muted
          loop
        ></video>
      </div>
      <div
        className="scrolltrigger text-center flex flex-col gap-10 items-center justify-center w-full"
        style={{ minHeight: "100vh", padding: "100px 0" }}
      >
        <ScrollReveal
          baseOpacity={0}
          enableBlur={true}
          blurStrength={8}
          textClassName="text-6xl font-medium "
        >
          For those who think beyond and think in the power of technology, Hi
          there! We are 403labs, an Innovation and Technology Company.
        </ScrollReveal>
      </div>
    </div>
  );
};

export default Home;
