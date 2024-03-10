import React, { useState } from "react";
import "./Arvr.css";
import jacketImage from "../images/vase.jpg";
import jacketImage1 from "../images/qr_vase.png";
import shirt from "../images/coffee.png";
import shirt1 from "../images/qr_coffee.png";

const Arvr = () => {
  const [showModal, setShowModal] = useState(false);
  const [modalImage, setModalImage] = useState("");

  const handleImageClick = (image) => {
    setShowModal(true);
    setModalImage(image);
  };

  const handleCloseModal = () => {
    setShowModal(false);
    setModalImage("");
  };

  return (
    <header>
      <div className="product-main">
        <h2 className="title">New Products</h2>
        <div className="product-grid">
          <div className="showcase">
            <div className="showcase-banner">
              <img
                src={jacketImage}
                alt="Mens Winter Leathers Jackets"
                width="300"
                className="product-img default"
                onClick={() => handleImageClick(jacketImage)}
              />
              <img
                src={jacketImage1}
                alt="Mens Winter Leathers Jackets"
                width="300"
                className="product-img hover"
                onClick={() => handleImageClick(jacketImage1)}
              />
              <p className="showcase-badge">15%</p>
              <div className="showcase-actions">
                <button className="btn-action">
                  <ion-icon name="heart-outline"></ion-icon>
                </button>
                <button className="btn-action">
                  <ion-icon name="eye-outline"></ion-icon>
                </button>
                <button className="btn-action">
                  <ion-icon name="repeat-outline"></ion-icon>
                </button>
                <button className="btn-action">
                  <ion-icon name="bag-add-outline"></ion-icon>
                </button>
              </div>
            </div>
            <div className="showcase-content">
              <a href="#" className="showcase-category">
                Vase
              </a>
              <a href="#">
                <h3 className="showcase-title">Mens Winter Leathers Jackets</h3>
              </a>
              <div className="showcase-rating">
                <ion-icon name="star"></ion-icon>
                <ion-icon name="star"></ion-icon>
                <ion-icon name="star"></ion-icon>
                <ion-icon name="star-outline"></ion-icon>
                <ion-icon name="star-outline"></ion-icon>
              </div>
              <div className="price-box">
                <p className="price">$48.00</p>
                <del>$75.00</del>
              </div>
            </div>
          </div>
          <div className="showcase">
            <div className="showcase-banner">
              <img
                src={shirt}
                alt="Pure Garment Dyed Cotton Shirt"
                className="product-img default"
                width="300"
                onClick={() => handleImageClick(shirt)}
              />
              <img
                src={shirt1}
                alt="Pure Garment Dyed Cotton Shirt"
                className="product-img hover"
                width="300"
                onClick={() => handleImageClick(shirt1)}
              />
              <p className="showcase-badge angle black">sale</p>
              <div className="showcase-actions">
                <button className="btn-action">
                  <ion-icon name="heart-outline"></ion-icon>
                </button>
                <button className="btn-action">
                  <ion-icon name="eye-outline"></ion-icon>
                </button>
                <button className="btn-action">
                  <ion-icon name="repeat-outline"></ion-icon>
                </button>
                <button className="btn-action">
                  <ion-icon name="bag-add-outline"></ion-icon>
                </button>
              </div>
            </div>
            <div className="showcase-content">
              <a href="#" className="showcase-category">
                shirt
              </a>
              <h3>
                <a href="#" className="showcase-title">
                  Pure Garment Dyed Cotton Shirt
                </a>
              </h3>
              <div className="showcase-rating">
                <ion-icon name="star"></ion-icon>
                <ion-icon name="star"></ion-icon>
                <ion-icon name="star"></ion-icon>
                <ion-icon name="star-outline"></ion-icon>
                <ion-icon name="star-outline"></ion-icon>
              </div>
              <div className="price-box">
                <p className="price">$45.00</p>
                <del>$56.00</del>
              </div>
            </div>
          </div>
        </div>
      </div>
      {showModal && (
        <div className="modal-overlay">
          <div className="modal">
            <button className="close-btn" onClick={handleCloseModal}>
              &times;
            </button>
            <div className="modal-content">
              <img src={modalImage} alt="Enlarged Image" />
            </div>
          </div>
        </div>
      )}
    </header>
  );
};

export default Arvr;
