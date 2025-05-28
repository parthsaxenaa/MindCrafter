# 🧠 MindCrafter

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0%2B-lightgrey)](https://flask.palletsprojects.com/)
[![Gemini AI](https://img.shields.io/badge/Gemini%20AI-API-orange)](https://ai.google.dev/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

An intelligent learning platform powered by Google's Gemini AI that generates comprehensive study materials and provides personalized learning experiences.

[🌐 Visit Live Site](https://mindcrafter.onrender.com)

</div>

## ✨ Features

- 🤖 AI-powered content generation
- 📚 Comprehensive study materials
- ❓ Interactive Q&A system
- 🎯 Difficulty-based explanations
- 🔒 Secure API key handling
- 🌐 Modern web interface

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Google Gemini API key
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/MindCrafter.git
   cd MindCrafter
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API Key**

   Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey) and set it as an environment variable:

   ```bash
   # Windows (PowerShell)
   $env:GEMINI_API_KEY="your-api-key-here"
   
   # Windows (Command Prompt)
   set GEMINI_API_KEY=your-api-key-here
   
   # Linux/Mac
   export GEMINI_API_KEY=your-api-key-here
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access the application**
   Open your browser and navigate to `http://localhost:5000`

## 🔧 API Endpoints

### Generate Content
```http
POST /api/gemini/generate
Content-Type: application/json

{
    "question": "Your question here",
    "context": "Optional context",
    "difficulty": "beginner|intermediate|advanced"
}
```

## 🔒 Security

- API keys are handled securely on the backend
- Never expose API keys in frontend code
- Environment variables for sensitive data
- Input validation and sanitization

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Google Gemini AI](https://ai.google.dev/) for providing the AI capabilities
- [Flask](https://flask.palletsprojects.com/) for the web framework
- All contributors who have helped shape this project 