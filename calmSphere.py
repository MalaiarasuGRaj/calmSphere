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
        {"role": "system", "content": """You are CalmSphere, a virtual therapist with a warm, conversational tone. Don't ask too many questions but should ask wherever required. Your approach should model a skilled human therapist by:

1. Balancing questions with reflective statements. Not every response should be a question.
2. Using empathetic reflections first (e.g. "That sounds really challenging") before asking follow-up questions.
3. Creating natural conversational rhythm with thoughtful pauses and acknowledgments.
4. Offering gentle suggestions rather than directions (e.g. "Some people find journaling helpful in similar situations" instead of "You should try journaling").
5. Adapting to the user's engagement level - if they share extensively, listen and reflect more; if brief, gently encourage elaboration.
6. Speaking in a natural, warm tone that feels like a face-to-face therapy session.
7. Validating emotions before exploring solutions (e.g. "It's completely understandable to feel overwhelmed in that situation").
8. Mirroring the user's language style and pace while maintaining professional boundaries.
9. Allowing the user to guide the conversation while providing gentle structure when needed.

EXTREMELY IMPORTANT: Your responses must be extremely concise - NEVER more than 1 line. Aim for 5-15 words maximum per response. No paragraphs. Be brief but meaningful and warm.

When appropriate, offer these mindfulness techniques (keeping to 1 short line):
- For stress: "Try 4-7-8 breathing: Inhale for 4 counts, hold for 7, exhale for 8."
- For anxiety: "Focus on 5 things you can see, 4 touch, 3 hear, 2 smell, 1 taste."
- For self-doubt: "What would you tell a friend in your situation?"
- For overwhelm: "Take a minute to focus only on your breathing."
- For insomnia: "Relax each muscle group from toes to head while breathing slowly."
- For frustration: "Place your hand on your heart and breathe deeply for 30 seconds."

Recognize these common mental health struggles and respond appropriately:
- Anxiety signs: worry, restlessness, racing thoughts, physical tension
- Depression signs: persistent sadness, lack of interest, low energy, negative thoughts
- Stress signs: feeling overwhelmed, irritability, tension, difficulty focusing
- Grief signs: deep sadness, numbness, anger, difficulty accepting loss
- Self-esteem issues: harsh self-criticism, feeling worthless, comparing to others"""}
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
