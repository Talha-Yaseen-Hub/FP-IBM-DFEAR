# Final Project: Microservices Deployment on IBM Cloud Code Engine

## Overview
This project integrates multiple microservices into an integrated web application for dealer product pricing and evaluation:
1. **Product Details Microservice (Python & Flask)**: Serves products list and supplier dealer lists.
2. **Dealer Pricing Microservice (Node.js & Express)**: Serves individual dealer pricing and multi-dealer price comparison endpoints.
3. **Dealer Evaluation Frontend Microservice (Python/HTML/JS)**: Dynamic web portal consuming both backend microservices.

---

## Architecture & Endpoints

### 1. Product Details Backend (Python / Flask)
* **Directory:** `backend/products_list/`
* **Port:** `5000`
* **Endpoints:**
  * `GET /products` — Returns JSON list of available products: `["Headphones", "Laptop", "Mouse", "Printer"]`
  * `GET /getdealers/<product>` — Returns dealers providing the specified product.

### 2. Dealer Pricing Backend (Node.js / Express)
* **Directory:** `backend/dealer_details/`
* **Port:** `8080`
* **Endpoints:**
  * `GET /price/:dealer/:product` — Returns price string for selected dealer & product.
  * `GET /allprice/:product` — Returns prices from all dealers offering the product.

### 3. Frontend Portal (HTML / Axios / Flask)
* **Directory:** `frontend/`
* **Port:** `5000` (or `5001`)
* Consumes backend endpoints to populate dynamic dropdowns and display real-time price comparisons.

---

## Submission Screenshots
All evaluation screenshots are located in [`screenshots/`](./screenshots/):
* `product_details_deploy.png` — Question 1
* `dealer_details_deploy.png` — Question 2
* `git_clone.png` — Question 3
* `index_urlchanges.png` — Question 4
* `frontend_deploy.png` — Question 5
* `homepage.png` — Question 6
* `product_dealer.png` — Question 7
* `product_dealer_price.png` — Question 8
* `product_all_dealers_prices.png` — Question 9
