import streamlit as st

st.set_page_config(
    page_title="Support Chatbot",
    page_icon="💬"
)

st.title("💬 MiniStore Support")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Product knowledge base
products = {
    "wireless bluetooth headphones": {
        "price": "$79.99",
        "category": "Electronics"
    },
    "smart fitness watch": {
        "price": "$129.99",
        "category": "Wearables"
    },
    "mechanical keyboard": {
        "price": "$89.99",
        "category": "Electronics"
    },
    "minimalist backpack": {
        "price": "$54.99",
        "category": "Fashion"
    },
    "portable coffee maker": {
        "price": "$39.99",
        "category": "Home & Kitchen"
    },
    "led desk lamp": {
        "price": "$29.99",
        "category": "Home & Kitchen"
    }
}

def get_response(user_text):
    text = user_text.lower()

    # Product Questions
    for product, details in products.items():
        if product in text:
            return (
                f"{product.title()} costs {details['price']} "
                f"and belongs to the {details['category']} category."
            )

    # Delivery
    if any(word in text for word in ["delivery", "shipping"]):
        return "Delivery usually takes 3–5 business days."

    # Refunds
    if "refund" in text:
        return "Refunds are processed within 5–7 business days."

    # Returns
    if "return" in text:
        return "Products can be returned within 30 days of purchase."

    # Payment
    if any(word in text for word in ["payment", "upi", "card"]):
        return (
            "We accept UPI, Credit Cards, Debit Cards and Net Banking."
        )

    # Order Status
    if any(word in text for word in ["order", "track", "status"]):
        return (
            "Your order is currently being processed and will ship soon."
        )

    return (
        "I can help with products, delivery, refunds, returns, "
        "payments and order tracking."
    )

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

prompt = st.chat_input("Ask a question...")

if prompt:

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.markdown(prompt)

    response = get_response(prompt)

    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })

    with st.chat_message("assistant"):
        st.markdown(response)

if st.button("⬅ Back to Home"):
    st.switch_page("app.py")