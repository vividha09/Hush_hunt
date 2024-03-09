import React from "react";
import "./Trends.css";
import H2 from "../images/H2.jpg";
import H3 from "../images/H3.jpg";
import { Link } from "react-router-dom";

const Trends = () => {
  return (
    <header>
      <div className="tagline">
        <h2 className="tagline-text">SHOP WITH CONFIDENCE</h2>
      </div>

      <div className="tagline">
        <h2 className="tagline-text2">Let us take care of your </h2>
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

                <a href="#" class="btn btn-link">
                  <span>Shop Now</span>

                  <ion-icon
                    name="arrow-forward-outline"
                    aria-hidden="true"
                  ></ion-icon>
                </a>
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
    </header>
  );
};

export default Trends;
