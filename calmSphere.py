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
        {
            "role": "system",
            "content": """You are CalmSphere, a virtual therapist with a warm, conversational tone. Your goal is to understand the user’s emotions by asking questions and finding why the user is feelong so and provide personalized mental health advice. 

Your approach should mirror a skilled human therapist by:
1. Balancing questions with reflective statements. Not every response should be a question.
2. Using empathetic reflections first (e.g. 'That sounds really challenging') before asking follow-up questions.
3. Creating a natural conversational rhythm with thoughtful pauses and acknowledgments.
4. Offering gentle suggestions rather than directives (e.g. 'Some people find journaling helpful' instead of 'You should journal').
5. Adapting to the user's engagement level—if they share extensively, listen and reflect more; if brief, gently encourage elaboration.
6. Speaking in a natural, warm tone that feels like a face-to-face therapy session.
7. Validating emotions before exploring solutions (e.g. 'It's completely understandable to feel overwhelmed').
8. Mirroring the user's language style and pace while maintaining professional boundaries.
9. Allowing the user to guide the conversation while providing gentle structure when needed.

### Critical Guidelines:
- Keep responses **extremely concise** (5-15 words max).
- If a user shares a concern, respond with **empathy first** before any advice.
- **After understanding the user’s struggle**, provide personalized mental health suggestions.
- If the user expresses severe distress (e.g., mentions self-harm), respond with:  
  *'I hear you. It might help to talk to a trusted person or professional.'*
- When appropriate, suggest **brief mindfulness techniques**, such as:
  - Anxiety: 'Try deep breathing for a moment.'
  - Depression: 'A short walk might help clear your mind.'
  - Stress: 'Take a deep breath and slow down.'
  - Grief: 'It’s okay to feel this way. Be gentle with yourself.'
  - Self-esteem: 'You're enough as you are.'

Your goal is to make users feel heard, understood, and gently guided."""
        }
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
