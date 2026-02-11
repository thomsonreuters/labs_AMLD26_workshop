import streamlit as st
import requests
import uuid
from typing import Dict, List
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Customer Support Chat",
    page_icon="💬",
    layout="centered"
)

# API Configuration
API_URL = os.getenv("API_URL")
CUSTOMER_EMAIL = os.getenv("CUSTOMER_EMAIL")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "conversation_id" not in st.session_state:
    st.session_state.conversation_id = str(uuid.uuid4())

if "trial_count" not in st.session_state:
    st.session_state.trial_count = 0

if "successful_trials" not in st.session_state:
    st.session_state.successful_trials = 0

def send_message(prompt: str) -> str:
    """
    Send a message to the customer support API and return the response.

    Args:
        prompt: The user's message

    Returns:
        The chatbot's response
    """
    try:
        payload = {
            "message": prompt,
            "conversationId": st.session_state.conversation_id,
            "email": CUSTOMER_EMAIL
        }

        headers = {
            "Content-Type": "application/json"
        }

        response = requests.post(
            API_URL,
            json=payload,
            headers=headers,
            timeout=30
        )

        response.raise_for_status()
        data = response.json()

        # Extract response based on transformResponse: json.response
        return data.get("response", "No response received")

    except requests.exceptions.RequestException as e:
        return f"Error communicating with support: {str(e)}"
    except Exception as e:
        return f"An error occurred: {str(e)}"

# App header
st.image("background.tiff", width='stretch')
st.title("💬 Customer Support Chat")
st.markdown("Welcome! How can we help you today?")

# Sidebar with conversation info
with st.sidebar:

    #st.header("Conversation Info")
    #st.text(f"Session ID:\n{st.session_state.conversation_id[:8]}...")
    #st.text(f"Email: {CUSTOMER_EMAIL}")
    st.header(f"Number of trials: {st.session_state.trial_count}")
    st.header(f"Successful attacks: {st.session_state.successful_trials}")

    col1, col2 = st.columns([1, 1], gap="small")
    with col1:
        if st.button("➖", key="decrement", width='stretch'):
            if st.session_state.successful_trials > 0:
                st.session_state.successful_trials -= 1
                st.rerun()

    with col2:
        if st.button("➕", key="increment", width='stretch'):
            st.session_state.successful_trials += 1
            st.rerun()


    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("Start New Conversation"):
        st.session_state.messages = []
        st.session_state.conversation_id = str(uuid.uuid4())
        st.session_state.trial_count += 1
        st.rerun()



# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Type your message here..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get bot response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = send_message(prompt)
            st.markdown(response)

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
