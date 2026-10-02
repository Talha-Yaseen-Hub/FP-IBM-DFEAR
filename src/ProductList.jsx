import React, { useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { addItem } from './CartSlice';
import CartItem from './CartItem';
import './ProductList.css';

function ProductList() {
    const [showCart, setShowCart] = useState(false); 
    const cartItems = useSelector(state => state.cart.items);
    const dispatch = useDispatch();

    const handleAddToCart = (plant) => {
        dispatch(addItem(plant));
    };

    const handleCartClick = (e) => {
        e.preventDefault();
        setShowCart(true); 
    };

    const handlePlantsClick = (e) => {
        e.preventDefault();
        setShowCart(false); 
    };
    
    const totalItems = cartItems.reduce((total, item) => total + item.quantity, 0);

    const plantsArray = [
        {
            category: "Air Purifying Plants",
            plants: [
                { name: "Snake Plant", image: "https://cdn.pixabay.com/photo/2021/01/22/06/04/snake-plant-5939187_1280.jpg", description: "Produces oxygen at night, improving air quality.", cost: "$15" },
                { name: "Spider Plant", image: "https://cdn.pixabay.com/photo/2018/07/11/06/47/chlorophytum-3530413_1280.jpg", description: "Filters formaldehyde and xylene from the air.", cost: "$12" },
                { name: "Peace Lily", image: "https://cdn.pixabay.com/photo/2019/06/12/14/14/peace-lilies-4269365_1280.jpg", description: "Removes mold spores and purifies the air.", cost: "$18" },
                { name: "Boston Fern", image: "https://cdn.pixabay.com/photo/2020/04/30/19/52/boston-fern-5114414_1280.jpg", description: "Adds humidity to the air and removes toxins.", cost: "$20" },
                { name: "Rubber Plant", image: "https://cdn.pixabay.com/photo/2020/02/15/11/49/flower-4850729_1280.jpg", description: "Easy to care for and absorbs indoor pollutants.", cost: "$17" },
                { name: "Aloe Vera", image: "https://cdn.pixabay.com/photo/2018/04/02/07/42/leaf-3283175_1280.jpg", description: "Purifies the air and has healing properties for skin.", cost: "$14" }
            ]
        },
        {
            category: "Aromatic Fragrant Plants",
            plants: [
                { name: "Lavender", image: "https://images.unsplash.com/photo-1611909023032-2d6b3134ecba?q=80&w=1074&auto=format&fit=crop", description: "Calming scent, used in aromatherapy.", cost: "$20" },
                { name: "Jasmine", image: "https://images.unsplash.com/photo-1592729645009-b96d1e63d14b?q=80&w=1170&auto=format&fit=crop", description: "Sweet fragrance, promotes relaxation.", cost: "$18" },
                { name: "Rosemary", image: "https://cdn.pixabay.com/photo/2019/10/11/07/12/rosemary-4541241_1280.jpg", description: "Invigorating scent, often used in cooking.", cost: "$15" },
                { name: "Mint", image: "https://cdn.pixabay.com/photo/2016/01/07/18/16/mint-1126282_1280.jpg", description: "Refreshing aroma, used in teas and cooking.", cost: "$12" },
                { name: "Lemon Balm", image: "https://cdn.pixabay.com/photo/2019/09/16/07/41/balm-4480134_1280.jpg", description: "Citrusy scent, relieves stress and promotes sleep.", cost: "$14" },
                { name: "Hyacinth", image: "https://cdn.pixabay.com/photo/2019/04/07/20/20/hyacinth-4110726_1280.jpg", description: "Hyacinth is a beautiful plant known for its fragrant.", cost: "$22" }
            ]
        },
        {
            category: "Insect Repellent Plants",
            plants: [
                { name: "Oregano", image: "https://cdn.pixabay.com/photo/2015/05/30/21/20/oregano-790702_1280.jpg", description: "The oregano plants contains compounds that can deter certain insects.", cost: "$10" },
                { name: "Marigold", image:"https://cdn.pixabay.com/photo/2022/02/22/05/45/marigold-7028063_1280.jpg", description: "Natural repellent for mosquitoes and aphids.", cost: "$8" },
                { name: "Geraniums", image: "https://cdn.pixabay.com/photo/2012/04/26/21/51/flowerpot-43270_1280.jpg", description: "Known for their insect-repelling properties while adding a pleasant scent.", cost: "$20" },
                { name: "Basil", image: "https://cdn.pixabay.com/photo/2016/07/24/20/48/tulsi-1539181_1280.jpg", description: "Repels flies and mosquitoes, also used in cooking.", cost: "$9" },
                { name: "Catnip", image: "https://cdn.pixabay.com/photo/2015/07/02/21/55/cat-829681_1280.jpg", description: "Repels mosquitoes and attracts cats.", cost: "$13" },
                { name: "Citronella", image: "https://cdn.pixabay.com/photo/2019/08/22/07/40/lemongrass-4422730_1280.jpg", description: "Well-known for its mosquito-repelling properties.", cost: "$18" }
            ]
        }
    ];

    return (
        <div>
             <div className="navbar">
                 <div className="navbar-logo">
                     <a href="/">
                         <div className="logoContent">
                             <img src="https://cdn.pixabay.com/photo/2020/08/05/13/12/eco-5465432_1280.png" alt="Logo" className="logoImg" />
                             <div className="logoText">
                                 <h3>Paradise Nursery</h3>
                                 <i>Where Green Meets Serenity</i>
                             </div>
                         </div>
                     </a>
                 </div>
                 <div className="navLinks">
                     <a href="#" onClick={handlePlantsClick}>Plants</a>
                     <a href="#" onClick={handleCartClick} className="cartLink">
                         <h1 className="cartIcon">
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" height="40" width="40">
                              <rect width="256" height="256" fill="none"></rect>
                              <circle cx="80" cy="216" r="12"></circle>
                              <circle cx="184" cy="216" r="12"></circle>
                              <path d="M42.3,72H221.7l-26.4,92.4A15.9,15.9,0,0,1,179.9,176H84.1a15.9,15.9,0,0,1-15.4-11.6L32.5,37.8A8,8,0,0,0,24.8,32H8" fill="none" stroke="#fff" strokeLinecap="round" strokeLinejoin="round" strokeWidth="16"></path>
                            </svg>
                            <span className="cart-badge">{totalItems}</span>
                         </h1>
                     </a>
                 </div>
             </div>

             {showCart ? (
                 <CartItem onContinueShopping={handlePlantsClick} />
             ) : (
                 <div className="product-grid">
                     {plantsArray.map((category, index) => (
                         <div key={index} className="categoryBlock">
                             <h2 className="categoryTitle">{category.category}</h2>
                             <div className="product-list">
                                 {category.plants.map((plant, plantIndex) => (
                                     <div className="product-card" key={plantIndex}>
                                         <img src={plant.image} alt={plant.name} className="productImage" />
                                         <h3 className="productName">{plant.name}</h3>
                                         <p className="productDescription">{plant.description}</p>
                                         <p className="productPrice">{plant.cost}</p>
                                         <button 
                                             className={cartItems.some(item => item.name === plant.name) ? 'addedButton' : 'addButton'}
                                             onClick={() => handleAddToCart(plant)} 
                                             disabled={cartItems.some(item => item.name === plant.name)}>
                                             {cartItems.some(item => item.name === plant.name) ? 'Added to Cart' : 'Add to Cart'}
                                         </button>
                                     </div>
                                 ))}
                             </div>
                         </div>
                     ))}
                 </div>
             )}
        </div>
    );
}

export default ProductList;
