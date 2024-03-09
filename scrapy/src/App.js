import React from "react";
import Header from "./components/Header";
import Banner from "./components/Banner";
import Trends from "./components/Trends";
import Product from "./components/Product";
import Footer from "./components/Footer";

const App = () => {
  return (
    <div>
      <Header />
      <Banner />
      <Trends />
      <Product />
      <Footer />
    </div>
  );
};

export default App;
