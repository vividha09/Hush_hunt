import React from "react";
import Header from "./components/Header";
import Banner from "./components/Banner";
import Trends from "./components/Trends";
import Product from "./components/Product";
import Footer from "./components/Footer";
import Calendar from "./components/Calendar";
import Products from "./components/Products";
import alanBtn from "@alan-ai/alan-sdk-web";
import { useEffect } from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

const App = () => {
  useEffect(() => {
    alanBtn({
      key: "22984363a97c93a3d023934315ea63912e956eca572e1d8b807a3e2338fdd0dc/stage",
      onCommand: (commandData) => {
        if (commandData.command === "go:back") {
        }
      },
    });
  }, []);
  return (
    <Router>
      <div>
        <Header />
        <Banner />
        <Routes>
          <Route
            path="/"
            element={
              <>
                <Trends />
                <Product />
                <Footer />
              </>
            }
          />
          <Route path="/calendar" element={<Calendar />} />
          <Route path="/products" element={<Products />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;
