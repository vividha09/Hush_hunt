import React from "react";
import "./Trends.css";
import H2 from "../images/H2.jpg";
import H3 from "../images/H3.jpg";
import shampoo from "../images/products/mamaearth.webp";
import jewellery from "../images/products/watch-1.jpg";
import { Link } from "react-router-dom";

const Trends = () => {
  return (
    <header>
      <div className="tagline">
        <h2 className="tagline-text">SHOP WITH CONFIDENCE</h2>
      </div>

      <div className="tagline">
        <h2 className="tagline-text2">
          Let us take care of your shopping decisions
        </h2>

        <h2 className="tagline-text2">
          Unlock the confidence to shop smarter, not harder
        </h2>
      </div>
      <section class="section cta">
        <div class="container">
          <ul class="cta-list">
            <li>
              <div
                class="cta-card"
                // style="background-image: url('./images/H2.jpg')"
                style={{ backgroundImage: `url(${H2})` }}
              >
                {/* <img
                  src={H2}
                  alt="women's latest fashion sale"
                  class="cta-card"
                /> */}
                <p class="card-subtitle">Adidas Shoes</p>

                <h3 class="h2 card-title">The Summer Sale Off 50%</h3>

                <Link to="/products" class="btn btn-link">
                  <span>Shop Now</span>

                  <ion-icon
                    name="arrow-forward-outline"
                    aria-hidden="true"
                  ></ion-icon>
                </Link>
              </div>
            </li>

            <li>
              <div class="cta-card" style={{ backgroundImage: `url(${H3})` }}>
                <p class="card-subtitle">SALE</p>

                <h3 class="h2 card-title">Get sales calender!</h3>

                <Link to="/calendar" class="btn btn-link">
                  <span>Click Here</span>
                  <ion-icon
                    name="arrow-forward-outline"
                    aria-hidden="true"
                  ></ion-icon>
                </Link>
              </div>
            </li>
          </ul>
        </div>
      </section>

      <section>
        {" "}
        <div class="product-featured">
          <h2 class="title">Deals of the day</h2>

          <div class="showcase-wrapper has-scrollbar">
            <div class="showcase-container">
              <div class="showcase">
                <div class="showcase-banner">
                  <img
                    src={shampoo}
                    alt="shampoo, conditioner & facewash packs"
                    class="showcase-img"
                  />
                </div>

                <div class="showcase-content">
                  <div class="showcase-rating">
                    <ion-icon name="star"></ion-icon>
                    <ion-icon name="star"></ion-icon>
                    <ion-icon name="star"></ion-icon>
                    <ion-icon name="star-outline"></ion-icon>
                    <ion-icon name="star-outline"></ion-icon>
                  </div>

                  <a href="#">
                    <h3 class="showcase-title">
                      shampoo, conditioner & facewash packs
                    </h3>
                  </a>

                  <p class="showcase-desc">
                    Lorem ipsum dolor sit amet consectetur Lorem ipsum dolor
                    dolor sit amet consectetur Lorem ipsum dolor
                  </p>

                  <div class="price-box">
                    <p class="price">$150.00</p>

                    <del>$200.00</del>
                  </div>

                  <button class="add-cart-btn">add to cart</button>

                  <div class="showcase-status">
                    <div class="wrapper">
                      <p>
                        already sold: <b>20</b>
                      </p>

                      <p>
                        available: <b>40</b>
                      </p>
                    </div>

                    <div class="showcase-status-bar"></div>
                  </div>

                  <div class="countdown-box">
                    <p class="countdown-desc">Hurry Up! Offer ends in:</p>

                    <div class="countdown">
                      <div class="countdown-content">
                        <p class="display-number">360</p>

                        <p class="display-text">Days</p>
                      </div>

                      <div class="countdown-content">
                        <p class="display-number">24</p>
                        <p class="display-text">Hours</p>
                      </div>

                      <div class="countdown-content">
                        <p class="display-number">59</p>
                        <p class="display-text">Min</p>
                      </div>

                      <div class="countdown-content">
                        <p class="display-number">00</p>
                        <p class="display-text">Sec</p>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <div class="showcase-container">
              <div class="showcase">
                <div class="showcase-banner">
                  <img
                    src={jewellery}
                    alt="Rose Gold diamonds Earring"
                    class="showcase-img"
                  />
                </div>

                <div class="showcase-content">
                  <div class="showcase-rating">
                    <ion-icon name="star"></ion-icon>
                    <ion-icon name="star"></ion-icon>
                    <ion-icon name="star"></ion-icon>
                    <ion-icon name="star-outline"></ion-icon>
                    <ion-icon name="star-outline"></ion-icon>
                  </div>

                  <h3 class="showcase-title">
                    <a href="#" class="showcase-title">
                      Digital Watch
                    </a>
                  </h3>

                  <p class="showcase-desc">
                    Lorem ipsum dolor sit amet consectetur Lorem ipsum dolor
                    dolor sit amet consectetur Lorem ipsum dolor
                  </p>

                  <div class="price-box">
                    <p class="price">$1990.00</p>
                    <del>$2000.00</del>
                  </div>

                  <button class="add-cart-btn">add to cart</button>

                  <div class="showcase-status">
                    <div class="wrapper">
                      <p>
                        {" "}
                        already sold: <b>15</b>{" "}
                      </p>

                      <p>
                        {" "}
                        available: <b>40</b>{" "}
                      </p>
                    </div>

                    <div class="showcase-status-bar"></div>
                  </div>

                  <div class="countdown-box">
                    <p class="countdown-desc">Hurry Up! Offer ends in:</p>

                    <div class="countdown">
                      <div class="countdown-content">
                        <p class="display-number">360</p>
                        <p class="display-text">Days</p>
                      </div>

                      <div class="countdown-content">
                        <p class="display-number">24</p>
                        <p class="display-text">Hours</p>
                      </div>

                      <div class="countdown-content">
                        <p class="display-number">59</p>
                        <p class="display-text">Min</p>
                      </div>

                      <div class="countdown-content">
                        <p class="display-number">00</p>
                        <p class="display-text">Sec</p>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
    </header>
  );
};

export default Trends;
