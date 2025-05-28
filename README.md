# MindCrafter

An AI-powered learning platform that generates comprehensive study materials and answers questions.

## Setup

1. Clone the repository
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up the Gemini API key:
   - Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Set the API key as an environment variable:
     ```bash
     # On Windows (PowerShell)
     $env:GEMINI_API_KEY="your-api-key-here"
     
     # On Windows (Command Prompt)
     set GEMINI_API_KEY=your-api-key-here
     
     # On Linux/Mac
     export GEMINI_API_KEY=your-api-key-here
     ```

4. Run the application:
   ```bash
   python app.py
   ```

5. Open your browser and navigate to `http://localhost:5000`

## Features

- Generate comprehensive study notes
- Create practice questions and quizzes
- Get AI-powered answers to your questions
- Interactive learning interface

## Security Note

The Gemini API key is now handled securely on the backend. Never expose your API key in the frontend code or commit it to version control. 