<a name="top"></a>
<div align="center">

<div align="center"> <img src="https://capsule-render.vercel.app/api?type=waving&color=0:1b4332,50:52b788,100:1b4332&height=220&section=header&text=Paradise%20Nursery%20and%20EPR&fontSize=50&fontColor=ffffff&animation=fadeIn&fontAlignY=32&desc=A%20Beautiful%20Shopping%20Cart%20Experience%20for%20Plant%20Lovers&descAlignY=54&descSize=16" width="100%"/>

<br/>

<img src="https://readme-typing-svg.demolab.com/?font=Poppins&weight=600&size=19&duration=2800&pause=900&color=FF6B6B&center=true&vCenter=true&width=680&lines=Two+Capstones%2C+One+IBM+Full-Stack+Journey;Paradise+Nursery+%F0%9F%8C%BF+%2B+Express+Book+Review+%F0%9F%93%9A;React+%2B+Redux+on+the+Front%2C+Node+%2B+Express+on+the+Back" alt="Typing SVG" />

<br/><br/>

<img src="https://skillicons.dev/icons?i=react,redux,vite,css,nodejs,express&theme=dark" />

<br/><br/>

<a href="https://www.coursera.org/learn/developing-frontend-apps-with-react/home/welcome">
<img src="https://img.shields.io/badge/IBM%20Course-Developing%20Front--End%20Apps%20with%20React-1b4332?style=for-the-badge&labelColor=52b788" />
</a>
<br/>
<a href="https://www.coursera.org/learn/developing-backend-apps-with-nodejs-and-express">
<img src="https://img.shields.io/badge/IBM%20Course-Developing%20Back--End%20Apps%20with%20Node.js%20%26%20Express-1e3a5f?style=for-the-badge&labelColor=3b82f6" />
</a>

<br/><br/>

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:52b788,50:ff6b6b,100:3b82f6&height=4&section=header" width="60%"/>

</div>

<br/><br/>

> This repository contains **two final capstone projects** completed for IBM Developer Skills Network certifications on Coursera — a front-end plant shop built with **React & Redux Toolkit**, and a back-end bookstore API built with **Node.js & Express**.

<br/>

## 📖 Table of Contents

<details open>
<summary><b>▼ Click to expand / collapse</b></summary>

<br/>

<table>
<tr>
<td valign="top">

**🪴 Project 1 — Paradise Nursery**
- [Features](#1-paradise-nursery-features)
- [Product Categories](#product-categories)
- [Redux Data Flow](#redux-data-flow)
- [User Flow](#user-flow)
- [Tech Stack](#paradise-nursery-tech-stack)
- [Getting Started](#paradise-nursery-getting-started)

</td>
<td valign="top">

**📚 Project 2 — Express Book Review**
- [Features](#2-express-book-review-features)
- [Auth Flow](#auth-flow)
- [API Route Map](#api-route-map)
- [Tech Stack](#express-book-review-tech-stack)
- [Getting Started](#express-book-review-getting-started)

</td>
</tr>
</table>

[👤 Author](#author)

</details>

<br/>

---

<br/>

# 🪴 1. Paradise Nursery
**React.js & Redux Toolkit**

A beautiful, functional shopping cart application for an online plant shop — browse categorized houseplants, add them to a live cart, and manage quantities with instantly recalculated totals.

<br/>

### Paradise Nursery — Features

| | Feature | Description |
|:---:|---|---|
| 🌿 | **Landing Page** | Welcoming intro featuring the company name, a brief background, and a "Get Started" button |
| 🪴 | **Product Listing** | Browse houseplants organized by category, each with an image, name, description, and price |
| 🛒 | **Shopping Cart** | Add products to your cart — the cart icon updates live to reflect total item count |
| 🔧 | **Cart Management** | Increase/decrease quantities, remove items, and see totals recalculate automatically |

<br/>

### Product Categories

<div align="center">

<img src="https://img.shields.io/badge/🌬️_Air_Purifying-1b4332?style=for-the-badge&labelColor=52b788" />
<img src="https://img.shields.io/badge/🌸_Aromatic-1b4332?style=for-the-badge&labelColor=FF6B6B" />
<img src="https://img.shields.io/badge/🦟_Insect_Repellent-1b4332?style=for-the-badge&labelColor=52b788" />

</div>

<br/>

### Redux Data Flow

*How adding an item to the cart propagates through the app:*

```mermaid
flowchart LR
    PC["🪴 Product Card<br/>Add to Cart"] -->|dispatch addItem| ST[("🗄️ Redux Store<br/>cart slice")]
    ST -->|useSelector| CI["🛒 Cart Icon<br/>item count"]
    ST -->|useSelector| CP["📋 Cart View<br/>items & totals"]
    CP -->|dispatch increment / decrement / remove| ST

    style ST fill:#1b4332,color:#fff,stroke:#FF6B6B
    style PC fill:#52b788,color:#fff
```

<br/>

### User Flow

```mermaid
flowchart TD
    L[🌿 Landing Page] -->|Get Started| PL[🪴 Product Listing]
    PL --> CAT{Choose Category}
    CAT -- Air Purifying --> P1[View Products]
    CAT -- Aromatic --> P1
    CAT -- Insect Repellent --> P1
    P1 -->|Add to Cart| CART[🛒 Cart Updates]
    CART --> MNG[🔧 Adjust Quantity / Remove]
    MNG --> TOT[💰 Totals Recalculated]

    style L fill:#1b4332,color:#fff
    style TOT fill:#52b788,color:#fff
```

<br/>

### Paradise Nursery — Tech Stack

| Technology | Purpose |
|---|---|
| **React.js** | UI component library |
| **Redux Toolkit** | Centralized cart state management |
| **Vite** | Fast dev server and build tooling |
| **CSS3** | Styling |

<br/>

### Paradise Nursery — Getting Started

```bash
# 1. Install dependencies (from the project root)
npm install

# 2. Start the development server
npm run dev

# 3. Open your browser to the localhost port shown in the terminal
```

<br/>

---

<br/>

# 📚 2. Express Book Review
**Node.js & Express.js**

A server-side application for an online bookstore — book search, review management, and secure user authentication, built with asynchronous operations via Promises and Async/Await.

<br/>

### Express Book Review — Features

| | Feature | Description |
|:---:|---|---|
| 📚 | **Book Retrieval** | List all available books, or search by ISBN, author name, or title |
| 💬 | **Review Management** | View reviews for a book; authenticated users can add, modify, or delete their own reviews |
| 🔐 | **User Authentication** | Register and log in securely using JSON Web Tokens (JWT) and session management |
| ⚡ | **Asynchronous Operations** | Uses Promises and Async/Await via Axios to interact with data efficiently |

<br/>

### Auth Flow

```mermaid
sequenceDiagram
    actor User
    participant API as 🔐 Express Server
    participant JWT as 🔑 JWT / Session

    User->>API: POST /register (username, password)
    API-->>User: 201 Created

    User->>API: POST /customer/login (username, password)
    API->>JWT: Generate signed token
    JWT-->>API: Access token
    API-->>User: 200 OK + session token

    User->>API: Authenticated review request (with token)
    API->>JWT: Verify token
    JWT-->>API: Valid
    API-->>User: Review saved / updated / deleted
```

<br/>

### API Route Map

> ⚠️ *This reflects the standard route structure typical of this specific IBM capstone — verify it against your actual `router/` implementation before relying on exact paths.*

```mermaid
flowchart TD
    C[📱 Client / Postman] --> R[🚏 Express Router]
    R --> B1[📚 GET /books]
    R --> B2[🔍 GET /isbn/:isbn]
    R --> B3[✍️ GET /author/:author]
    R --> B4[📖 GET /title/:title]
    R --> REV1[💬 GET /review/:isbn]
    R --> REV2["✏️ PUT /customer/auth/review/:isbn 🔒"]
    R --> REV3["🗑️ DELETE /customer/auth/review/:isbn 🔒"]
    R --> AUTH1[🆕 POST /register]
    R --> AUTH2[🔑 POST /customer/login]

    style C fill:#1e3a5f,color:#fff
    style AUTH2 fill:#52b788,color:#fff
```

<br/>

### Express Book Review — Tech Stack

<div align="center">

<img src="https://skillicons.dev/icons?i=nodejs,express,postman&theme=dark" />

</div>

<br/>

| Technology | Purpose |
|---|---|
| **Node.js** | JavaScript runtime |
| **Express.js** | Web application / routing framework |
| **JSON Web Tokens (JWT) & Express Session** | Authentication and session management |
| **Axios** | Async/Await-based HTTP interactions |

<br/>

### Express Book Review — Getting Started

```bash
# 1. Navigate to the backend directory
cd expressBookReview

# 2. Install dependencies
npm install

# 3. Start the server
npm start
```

Server runs on **port `5000`** — test endpoints via Postman or cURL.

<br/>

---

<br/>

## 👤 Author

<div align="center">

### Talha Yaseen

<br/>

<a href="mailto:talhavectorarts@gmail.com">
  <img src="https://img.shields.io/badge/Gmail-EA4335?style=for-the-badge&logo=gmail&logoColor=white" />
</a>
<a href="https://www.linkedin.com/in/talha-yaseen-44a41a341">
  <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" />
</a>
<a href="https://github.com/Talha-Yaseen-Hub">
  <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" />
</a>

</div>

<br/><br/>

<div align="center">

[⬆ Back to Top](#top)

<br/><br/>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:3b82f6,50:2d6a4f,100:1b4332&height=100&section=footer" width="100%"/>

</div>
