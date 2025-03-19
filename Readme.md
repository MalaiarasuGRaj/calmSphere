# 🧠 CalmSphere - AI Therapy Assistant

CalmSphere is an AI-powered mental wellness platform that provides personalized support for stress management, anxiety reduction, and mindfulness practices. This application uses advanced language models to create a conversational interface that offers guidance and support for mental wellbeing.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Environment Variables](#environment-variables)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## 🔍 Overview

CalmSphere serves as a digital sanctuary for mental wellness, providing an accessible platform for users to express their thoughts and receive supportive guidance. The application leverages the Meta-Llama-3.3-70B-Instruct model through SambaNova's API to generate empathetic and helpful responses.

## ✨ Features

- **Conversational Interface**: Engage in natural, text-based conversations with the AI therapist
- **Personalized Support**: Receive tailored guidance for mental wellness concerns
- **Chat History**: Review previous interactions within a session
- **Clear Chat**: Reset the conversation at any time
- **Informative Sidebar**: Access information about CalmSphere's services and contact details

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/calmsphere.git
cd calmsphere
```

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the virtual environment:

On Windows:
```bash
venv\Scripts\activate
```

On macOS/Linux:
```bash
source venv/bin/activate
```

4. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## 🖥️ Usage

1. Set up your environment variables (see [Environment Variables](#environment-variables))

2. Run the Streamlit application:
```bash
streamlit run calmSphere.py
```

3. Open your web browser and navigate to the URL displayed in the terminal (typically http://localhost:8501)

4. Start interacting with the CalmSphere AI therapist by typing your questions or concerns in the chat input field

## 🔐 Environment Variables

Before running the application, you need to set up the following environment variable:

- `SAMBANOVA_API_KEY`: Your API key for accessing SambaNova's services

You can set this environment variable in your terminal:

On Windows:
```bash
set SAMBANOVA_API_KEY=your_api_key_here
```

On macOS/Linux:
```bash
export SAMBANOVA_API_KEY=your_api_key_here
```

Alternatively, you can create a `.env` file in the project root directory:
```
SAMBANOVA_API_KEY=your_api_key_here
```

## 💻 Technology Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **AI Model**: Meta-Llama-3.3-70B-Instruct via SambaNova API
- **API Integration**: OpenAI-compatible client

## 📁 Project Structure

```
calmsphere/
├── calmSphere.py        # Main application file
├── requirements.txt     # Project dependencies
├── .env                 # Environment variables (create this file)
├── README.md            # Project documentation
└── .gitignore           # Git ignore file
```

## 📋 Requirements

Create a `requirements.txt` file with the following dependencies:

```
streamlit>=1.28.0
openai>=1.3.0
python-dotenv>=1.0.0
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📞 Contact

- Email: support@calmsphere.ai
- Website: www.calmsphere.ai

---

CalmSphere - Your digital sanctuary for mental wellness and mindfulness.