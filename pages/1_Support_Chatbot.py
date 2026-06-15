import streamlit as st

st.set_page_config(
    page_title="MiniStore Support",
    page_icon="💬",
    layout="wide"
)

# ---------------------------------------------------
# Product Knowledge Base
# ---------------------------------------------------
products = {
    "headphones": "$79.99",
    "fitness watch": "$129.99",
    "keyboard": "$89.99",
    "backpack": "$54.99",
    "coffee maker": "$39.99",
    "desk lamp": "$29.99"
}

# ---------------------------------------------------
# Chat Memory
# ---------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content":
            "Hello! Welcome to MiniStore Support. How can I help you today?"
        }
    ]

# ---------------------------------------------------
# Chatbot Logic
# ---------------------------------------------------
def generate_response(user_input):

    query = user_input.lower()

    # Product Questions
    if any(product in query for product in products):
        for product, price in products.items():
            if product in query:
                return f"Our {product.title()} is currently available for {price}."

    # Delivery
    if any(word in query for word in ["delivery", "shipping", "ship"]):
        return (
            "Standard delivery takes 3-5 business days. "
            "Express shipping takes 1-2 business days."
        )

    # Refunds
    if "refund" in query:
        return (
            "Refunds are processed within 5-7 business days after approval."
        )

    # Returns
    if "return" in query:
        return (
            "Products can be returned within 30 days if unused and in original packaging."
        )

    # Payment
    if any(word in query for word in ["payment", "card", "upi", "paypal"]):
        return (
            "We accept Credit Cards, Debit Cards, UPI, Net Banking, and PayPal."
        )

    # Order Status
    if any(word in query for word in ["order", "status", "track"]):
        return (
            "For demo purposes, your latest order is currently being processed."
        )

    return (
        "I'm not sure about that. "
        "You can ask me about products, refunds, returns, shipping, payments, or order status."
    )

# ---------------------------------------------------
# Header
# ---------------------------------------------------
st.title("💬 MiniStore Support Chatbot")

st.write(
    "Ask questions about products, delivery, refunds, returns, payments, or order status."
)

# ---------------------------------------------------
# Display Chat History
# ---------------------------------------------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ---------------------------------------------------
# Chat Input
# ---------------------------------------------------
user_prompt = st.chat_input(
    "Type your question here..."
)

if user_prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(user_prompt)

    response = generate_response(user_prompt)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )

    with st.chat_message("assistant"):
        st.markdown(response)

# ---------------------------------------------------
# Navigation Back Home
# ---------------------------------------------------
st.page_link(
    "app.py",
    label="⬅ Back to Home"
)