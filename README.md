# IBM Final Project: Developing Front-End Apps with React & Developing Back-End Apps with Node.js and Express

This repository contains two final capstone projects completed for the IBM Developer Skills Network certifications. 

---

## 1. Paradise Nursery (Front-End Application)
**React.js & Redux Toolkit**

A beautiful, functional shopping cart application for an online plant shop called Paradise Nursery. 

### Features
- **Landing Page**: A welcoming landing page featuring the company name, a brief background about the company, and a "Get Started" button.
- **Product Listing**: View a wide variety of houseplants categorized by their properties (e.g., Air Purifying, Aromatic, Insect Repellent). Each plant card features an image, name, description, and price.
- **Shopping Cart**: Add products to your cart. The cart icon dynamically updates to show the total number of items.
- **Cart Management**: Increase or decrease the quantity of items, remove items, and view total costs dynamically calculated based on your selections.

### Tech Stack
- React.js
- Redux Toolkit (State Management)
- Vite
- CSS3

### How to Run Locally
1. Run `npm install` in the root directory.
2. Run `npm run dev`.
3. Open your browser and navigate to the localhost port provided.

---

## 2. Express Book Review (Back-End Application)
**Node.js & Express.js**

A server-side application for an online bookstore built with Express.js. The application includes user authentication, book search functionalities, and review management, while also demonstrating asynchronous operations using Promises and Async/Await with Axios.

### Features
- **Book Retrieval**: Retrieve a list of all available books, or search for books by ISBN, author name, or title.
- **Review Management**: Access reviews for specific books. Authenticated users can add, modify, or delete their own book reviews.
- **User Authentication**: Register as a new user and login securely using JSON Web Tokens (JWT) and session management.
- **Asynchronous Operations**: Uses Promises and Async/Await via Axios simulations to interact with the database efficiently.

### Tech Stack
- Node.js
- Express.js
- JSON Web Tokens (JWT) & Express Session (Authentication)
- Axios (Async/Await)

### How to Run Locally
1. Navigate to the backend directory: `cd expressBookReview`
2. Run `npm install`
3. Run `npm start`
4. The server will start on port `5000`. You can test endpoints via Postman or cURL.
