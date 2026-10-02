<a name="top"></a>
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:1b4332,50:52b788,100:1b4332&height=220&section=header&text=Paradise%20Nursery&fontSize=50&fontColor=ffffff&animation=fadeIn&fontAlignY=32&desc=A%20Beautiful%20Shopping%20Cart%20Experience%20for%20Plant%20Lovers&descAlignY=54&descSize=16" width="100%"/>

<br/>

<img src="https://readme-typing-svg.demolab.com/?font=Poppins&weight=600&size=20&duration=2800&pause=900&color=FF6B6B&center=true&vCenter=true&width=680&lines=Browse+%F0%9F%8C%BF+Add+to+Cart+%F0%9F%9B%92+Checkout-Ready+%E2%9C%A8;Built+with+React+%2B+Redux+Toolkit;Houseplants%2C+Made+Simple+to+Shop" alt="Typing SVG" />

<br/><br/>

<img src="https://skillicons.dev/icons?i=react,redux,vite,css&theme=dark" />

<br/><br/>

<img src="https://img.shields.io/badge/Categories-3-1b4332?style=for-the-badge&labelColor=52b788" />
<img src="https://img.shields.io/badge/Live%20Cart%20Count-Dynamic-1b4332?style=for-the-badge&labelColor=52b788" />
<img src="https://img.shields.io/badge/State%20Management-Redux%20Toolkit-1b4332?style=for-the-badge&labelColor=FF6B6B" />

<br/><br/>

<a href="https://www.coursera.org/learn/developing-frontend-apps-with-react/home/welcome">
<img src="https://img.shields.io/badge/IBM%20Final%20Project-Developing%20Front--End%20Apps%20with%20React-1b4332?style=for-the-badge&labelColor=0f766e" />
</a>

<br/><br/>

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:52b788,50:ff6b6b,100:52b788&height=4&section=header" width="60%"/>

</div>

<br/><br/>

> A modern, functional shopping cart application for an online plant shop — browse categorized houseplants, add them to a live cart, and manage quantities with instantly recalculated totals. Built with **React** and **Redux Toolkit** for clean, predictable state management.
>
> This project is the **final capstone project** for IBM's [*Developing Front-End Apps with React*](https://www.coursera.org/learn/developing-frontend-apps-with-react/home/welcome) course on Coursera.

<br/>

## 📖 Table of Contents

<details open>
<summary><b>▼ Click to expand / collapse</b></summary>

<br/>

- [✨ Features](#features)
- [🪴 Product Categories](#product-categories)
- [🧠 Redux Data Flow](#redux-data-flow)
- [🛍️ User Flow](#user-flow)
- [🛠️ Tech Stack](#tech-stack)
- [🚀 Getting Started](#getting-started)
- [👤 Author](#author)

</details>

<br/>

---

<br/>

## ✨ Features

| | Feature | Description |
|:---:|---|---|
| 🌿 | **Landing Page** | Welcoming intro featuring the company name, a brief background, and a "Get Started" button |
| 🪴 | **Product Listing** | Browse houseplants organized by category, each with an image, name, description, and price |
| 🛒 | **Shopping Cart** | Add products to your cart — the cart icon updates live to reflect total item count |
| 🔧 | **Cart Management** | Increase/decrease quantities, remove items, and see totals recalculate automatically |

<br/>

---

<br/>

## 🪴 Product Categories

<div align="center">

<img src="https://img.shields.io/badge/🌬️_Air_Purifying-1b4332?style=for-the-badge&labelColor=52b788" />
<img src="https://img.shields.io/badge/🌸_Aromatic-1b4332?style=for-the-badge&labelColor=FF6B6B" />
<img src="https://img.shields.io/badge/🦟_Insect_Repellent-1b4332?style=for-the-badge&labelColor=52b788" />

</div>

<br/>

---

<br/>

## 🧠 Redux Data Flow

*How adding an item to the cart propagates through the app — a typical Redux Toolkit pattern:*

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

---

<br/>

## 🛍️ User Flow

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

---

<br/>

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| **React** | UI component library |
| **Redux Toolkit** | Predictable, centralized cart state management |
| **Vite** | Fast dev server and build tooling |
| **CSS3** | Styling |

<br/>

---

<br/>

## 🚀 Getting Started

<div align="center">

<img src="https://img.shields.io/badge/Node.js-Required-339933?style=for-the-badge&logo=node.js&logoColor=white" />

</div>

<br/>

```bash
# Install dependencies
npm install

# Start the development server
npm run dev
```

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

<br/><br/>

<sub>📌 Assumed this follows your established identity from your other repos — let me know if this project has different author details.</sub>

</div>

<br/><br/>

<div align="center">

[⬆ Back to Top](#top)

<br/><br/>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:52b788,100:1b4332&height=100&section=footer" width="100%"/>

</div>
