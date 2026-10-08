
import streamlit as st
from groq import Groq

# =========================================================
# GROQ API KEY
# =========================================================

GROQ_API_KEY = "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"

# Create Groq client
client = Groq(api_key=GROQ_API_KEY)


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Keerthi AI Chatbot",
    page_icon="🤖",
    layout="centered"
)


# =========================================================
# TITLE
# =========================================================

st.title("🤖 Keerthi AI Chatbot")

st.write(
    "Ask me anything and I will answer using a Groq LLM."
)


# =========================================================
# CHAT HISTORY
# =========================================================

if "messages" not in st.session_state:

    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hello! 👋 How can I help you today?"
        }
    ]


# =========================================================
# DISPLAY PREVIOUS MESSAGES
# =========================================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


# =========================================================
# USER INPUT
# =========================================================

user_input = st.chat_input(
    "Type your message here..."
)


# =========================================================
# WHEN USER SENDS A MESSAGE
# =========================================================

if user_input:

    # ---------------------------------------------
    # Display user's message
    # ---------------------------------------------

    with st.chat_message("user"):

        st.markdown(user_input)


    # ---------------------------------------------
    # Add user message to history
    # ---------------------------------------------

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )


    # ---------------------------------------------
    # Generate Groq response
    # ---------------------------------------------

    with st.chat_message("assistant"):

        try:

            response = client.chat.completions.create(

                model="openai/gpt-oss-120b",

                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are a helpful and friendly AI assistant. "
                            "Give clear and easy-to-understand answers."
                        )
                    }
                ] + st.session_state.messages,

                temperature=0.7,

                max_tokens=1024
            )


            # Get assistant response
            assistant_response = response.choices[0].message.content


            # Display response
            st.markdown(assistant_response)


            # -----------------------------------------
            # Save assistant response to chat history
            # -----------------------------------------

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": assistant_response
                }
            )


        except Exception as e:

            st.error(
                f"Something went wrong: {e}"
            )


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.header("⚙️ Chatbot")

    st.write(
        "This chatbot uses:"
    )

    st.write("🐍 Python")
    st.write("⚡ Groq API")
    st.write("🎈 Streamlit")
    st.write("🧠 Llama LLM")

    st.divider()

    # Clear chat button
    if st.button("🗑️ Clear Chat"):

        st.session_state.messages = [
            {
                "role": "assistant",
                "content": "Chat cleared! 👋 How can I help you?"
            }
        ]

        st.rerun()
