import os
import streamlit as st
import openai
from typing import List, Dict

# Set page configuration
st.set_page_config(
    page_title="CalmSphere Chatbot",
    page_icon="🧘",
    layout="centered"
)

# Initialize session state for chat history if it doesn't exist
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": """You are an empathetic AI therapist. Follow these guidelines:
        
        1. Keep your responses brief and conversational - use short sentences and in very simple english that anyone can easily understand.
        2. It is not necessary to ask question in every response, if asking focus on one question at a time.
        3. Respond like a real therapist in a live session would - concisely and thoughtfully.
        4. Avoid long explanations or paragraphs of text.
        5. Use natural pauses and brief statements to encourage reflection.
        6. Listen more than you speak - don't overwhelm with information.
        7. Focus on understanding emotions before suggesting solutions.
        8. Use a warm, professional tone that invites further sharing.
        9. After gathering required details from the user, provide a opt solution for the mentall illness of the user.
        10. Do not asnwer any question beyond therapy.
        
        Example style:
        "I hear that you're feeling overwhelmed. What specifically triggered these feelings today?"
        "That sounds difficult. How long have you been experiencing this?"
        "I'm noticing a pattern in what you're sharing. Have you considered how these events might be connected?"
        
        Remember to keep responses under 3 sentences when possible."""}
    ]


def initialize_client():
    """Initialize the OpenAI client with SambaNova API"""
    api_key = "39e2ae22-9924-488c-b36e-f17740754edd"
    if not api_key:
        st.error("SAMBANOVA_API_KEY environment variable not set")
        st.stop()
    
    return openai.OpenAI(
        api_key=api_key,
        base_url="https://api.sambanova.ai/v1",
    )

def generate_response(messages: List[Dict[str, str]]):
    """Generate a response from the SambaNova API"""
    client = initialize_client()
    
    try:
        response = client.chat.completions.create(
            model="Meta-Llama-3.3-70B-Instruct",
            messages=messages,
            temperature=0.5,
            top_p=0.7,
            max_tokens=150
        )
        return response.choices[0].message.content
    except Exception as e:
        st.error(f"Error generating response: {str(e)}")
        return None


# App header
st.title("🧠 CalmSphere - Your AI Therapeutic Companion")
st.markdown("I'm here to listen and understand. Feel free to share what's on your mind at your own pace.")

# Display chat history
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.write(message["content"])

# Chat input
if prompt := st.chat_input("Share your thoughts or feelings..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.write(prompt)
    
    # Display assistant response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.text("Thinking...")
        
        # Generate response
        response = generate_response(st.session_state.messages)
        
        if response:
            message_placeholder.write(response)
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": response})
        else:
            message_placeholder.write("Sorry, I couldn't generate a response. Please try again.")

# Add a sidebar with information about CalmSphere
with st.sidebar:
    st.title("About CalmSphere")
    
    st.markdown("""
    ## CalmSphere
    
    CalmSphere is your digital sanctuary for mental wellness and mindfulness. 
    Our AI-powered platform offers personalized support for:
    
    * Stress management
    * Anxiety reduction
    * Mindfulness practices
    * Mental health resources
    * Guided meditation
    
    We combine cutting-edge AI technology with evidence-based mental health 
    practices to provide accessible, personalized support whenever you need it.
    """)
    
    
    # Add a clear chat button
    if st.button("Clear Chat"):
        st.session_state.messages = [
            {"role": "system", "content": "You are a helpful assistant"}
        ]
        st.rerun()
