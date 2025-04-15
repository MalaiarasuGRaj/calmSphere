
# CalmSphere 🧠

CalmSphere is an AI-powered virtual therapist designed to provide accessible, empathetic, and context-aware mental health support through natural language conversations. Built using a fine-tuned micro-LLaMA 2-7B model, CalmSphere bridges the gap between human empathy and scalable machine intelligence.


## 🔍 Project Overview

Mental health issues such as anxiety, depression, and emotional fatigue are growing concerns globally. However, access to affordable, timely, and personalized mental health care is still limited by cost, social stigma, and lack of professionals.

CalmSphere offers a solution through:

- Emotionally aware AI conversations
- Fine-tuned therapy-specific datasets
- Personalized memory-driven interaction
- Built-in safety, bias mitigation, and hallucination control
- Lightweight model deployment with QLoRA for low-resource systems



## 💡 Features

- Active listening and empathetic response generation
- Long-term memory for user-specific follow-up
- Real-time mental health chat using `Streamlit` interface
- Powered by the fine-tuned model [`Dhanyavarthini/Llama-2-7b-chat-finetune`](https://huggingface.co/Dhanyavarthini/Llama-2-7b-chat-finetune) hosted on Hugging Face
- Trained on datasets including:
  - CounselChat
  - Empathetic Dialogues
  - ICD & DSM references



## 🧠 Model Details

- **Base Model**: [LLaMA 2-7B](https://huggingface.co/meta-llama/Llama-2-7b)
- **Fine-tuning Technique**: QLoRA (Quantized Low-Rank Adaptation)
- **Training Platform**: Google Colab (using 4-bit quantization for efficiency)
- **Hosted On**: Hugging Face – [`Dhanyavarthini/Llama-2-7b-chat-finetune`](https://huggingface.co/Dhanyavarthini/Llama-2-7b-chat-finetune)

---

## 🛠️ Tech Stack

| Layer        | Technology Used                  |
|--------------|----------------------------------|
| Frontend     | [Streamlit](https://streamlit.io) |
| Backend      | Hugging Face Transformers & Tokenizers |
| Model Training | Google Colab (QLoRA Fine-tuning) |
| Model Hosting | Hugging Face Hub |
| Language     | Python 3.10+ |

---

## 🖥️ Installation & Running

**Clone the repository:**

```bash
git clone https://github.com/yourusername/calmsphere.git
cd calmsphere
```

**Install Dependencies:**

```bash
pip install -r requirements.txt
```

**Run the App:**

```bash
streamlit run app.py
```

---

## 📦 Hugging Face Integration

This project uses a fine-tuned LLaMA 2 model hosted on Hugging Face:

🔗 [Dhanyavarthini/Llama-2-7b-chat-finetune](https://huggingface.co/Dhanyavarthini/Llama-2-7b-chat-finetune)

To use this model in your own project:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("Dhanyavarthini/Llama-2-7b-chat-finetune")
tokenizer = AutoTokenizer.from_pretrained("Dhanyavarthini/Llama-2-7b-chat-finetune")
```


## 👨‍💻 Contributors

- **Malaiarasu G**   
- **Nivetha S**    
- **Pushpa Dharini S**    
- **Dhanyavarthini A S**   

🎓 Department of Artificial Intelligence & Data Science  
📍 National Engineering College, Kovilpatti  
