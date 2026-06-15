import streamlit as st

# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------
st.set_page_config(
    page_title="MiniStore",
    page_icon="🛍️",
    layout="wide"
)

# ---------------------------------------------------
# Custom CSS Styling
# ---------------------------------------------------
st.markdown("""
<style>
    /* Main background */
    .stApp {
        background-color: #f5f7fb;
    }

    /* Hero section */
    .hero {
        background: linear-gradient(135deg, #4F46E5, #7C3AED);
        padding: 40px;
        border-radius: 20px;
        color: white;
        text-align: center;
        margin-bottom: 30px;
    }

    .hero h1 {
        font-size: 3rem;
        margin-bottom: 10px;
    }

    .hero p {
        font-size: 1.1rem;
        opacity: 0.95;
    }

    /* Product card */
    .product-card {
        background: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
        margin-bottom: 20px;
        transition: 0.3s;
        height: 260px;
    }

    .product-card:hover {
        transform: translateY(-5px);
        box-shadow: 0px 8px 18px rgba(0,0,0,0.15);
    }

    .product-title {
        font-size: 1.2rem;
        font-weight: bold;
        color: #111827;
    }

    .product-price {
        color: #16a34a;
        font-size: 1.1rem;
        font-weight: bold;
        margin-top: 10px;
        margin-bottom: 10px;
    }

    .product-category {
        display: inline-block;
        background: #EEF2FF;
        color: #4F46E5;
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 0.8rem;
        margin-bottom: 10px;
    }

    .section-title {
        font-size: 2rem;
        font-weight: 700;
        margin-top: 20px;
        margin-bottom: 15px;
        color: #111827;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# Sample Product Data
# ---------------------------------------------------
products = [
    {
        "name": "Wireless Bluetooth Headphones",
        "price": 79.99,
        "description": "Premium over-ear headphones with noise cancellation and 30-hour battery life.",
        "category": "Electronics"
    },
    {
        "name": "Smart Fitness Watch",
        "price": 129.99,
        "description": "Track your health, workouts, sleep, and notifications in real-time.",
        "category": "Wearables"
    },
    {
        "name": "Mechanical Keyboard",
        "price": 89.99,
        "description": "RGB backlit keyboard with tactile switches for productivity and gaming.",
        "category": "Electronics"
    },
    {
        "name": "Minimalist Backpack",
        "price": 54.99,
        "description": "Stylish and durable backpack designed for work, travel, and everyday use.",
        "category": "Fashion"
    },
    {
        "name": "Portable Coffee Maker",
        "price": 39.99,
        "description": "Brew fresh coffee anywhere with this compact travel-friendly coffee maker.",
        "category": "Home & Kitchen"
    },
    {
        "name": "LED Desk Lamp",
        "price": 29.99,
        "description": "Modern desk lamp with adjustable brightness and eye-care lighting technology.",
        "category": "Home & Kitchen"
    }
]

# ---------------------------------------------------
# Sidebar
# ---------------------------------------------------
st.sidebar.title("🛍️ MiniStore")

# Extract unique categories
categories = ["All"] + sorted(list(set(p["category"] for p in products)))

selected_category = st.sidebar.selectbox(
    "Browse Categories",
    categories
)

st.sidebar.markdown("---")

# Shopping cart demo summary
st.sidebar.subheader("🛒 Shopping Cart")
st.sidebar.write("Items: **3**")
st.sidebar.write("Subtotal: **$249.97**")
st.sidebar.write("Shipping: **Free**")
st.sidebar.success("Total: $249.97")

st.sidebar.markdown("---")
st.sidebar.info("Demo E-commerce Store")

# ---------------------------------------------------
# Hero / Homepage Section
# ---------------------------------------------------
st.markdown("""
<div class="hero">
    <h1>🛍️ MiniStore</h1>
    <p>Your one-stop destination for premium gadgets, lifestyle products, and everyday essentials.</p>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# Welcome Section
# ---------------------------------------------------
st.markdown(
    '<div class="section-title">Welcome to MiniStore</div>',
    unsafe_allow_html=True
)

st.write(
    """
    Discover high-quality products carefully selected to enhance your lifestyle.
    Browse our featured collection and find the perfect item for your needs.
    """
)

# ---------------------------------------------------
# Filter Products by Category
# ---------------------------------------------------
if selected_category == "All":
    filtered_products = products
else:
    filtered_products = [
        p for p in products
        if p["category"] == selected_category
    ]

# ---------------------------------------------------
# Featured Products Section
# ---------------------------------------------------
st.markdown(
    '<div class="section-title">Featured Products</div>',
    unsafe_allow_html=True
)

# Create responsive product grid using columns
cols = st.columns(3)

for index, product in enumerate(filtered_products):
    with cols[index % 3]:
        st.markdown(
            f"""
            <div class="product-card">
                <div class="product-category">{product['category']}</div>
                <div class="product-title">{product['name']}</div>
                <div class="product-price">${product['price']:.2f}</div>
                <p>{product['description']}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        # Demo button
        st.button(
            f"Add to Cart",
            key=f"cart_{index}"
        )

# ---------------------------------------------------
# Footer
# ---------------------------------------------------
st.markdown("---")
st.markdown(
    "<center>© 2026 MiniStore • Demo E-Commerce Website Built with Streamlit</center>",
    unsafe_allow_html=True
)
# ----------------------------------------
# Floating Support Button
# ----------------------------------------
st.markdown("""
<style>
.support-button {
    position: fixed;
    bottom: 25px;
    right: 25px;
    z-index: 999;
}

.support-button button {
    background-color: #4F46E5;
    color: white;
    border-radius: 50px;
    padding: 12px 20px;
    border: none;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([8, 1, 1])

with col3:
    if st.button("💬 Support"):
        st.switch_page("pages/1_Support_Chatbot.py")