from flask import Flask, request, jsonify
import requests
import os
from config import GEMINI_API_KEY

app = Flask(__name__)

# Route to handle Gemini API requests
@app.route('/api/gemini/generate', methods=['POST'])
def generate_content():
    # Get data from request
    data = request.json
    question = data.get('question', '')
    context = data.get('context', '')
    difficulty = data.get('difficulty', 'intermediate')
    
    # Validate inputs
    if not question:
        return jsonify({'error': 'Question is required'}), 400
    
    if not GEMINI_API_KEY:
        return jsonify({'error': 'Gemini API key not configured on server'}), 500
    
    # Prepare the prompt based on difficulty level
    prompt = question
    if context:
        prompt += f"\n\nAdditional context: {context}"
    
    # Add difficulty level guidance
    if difficulty == 'beginner':
        prompt += '\n\nPlease explain in simple terms suitable for beginners.'
    elif difficulty == 'intermediate':
        prompt += '\n\nPlease provide a moderately detailed explanation.'
    elif difficulty == 'advanced':
        prompt += '\n\nPlease provide an in-depth, advanced explanation.'
    
    # Call Gemini API
    try:
        api_url = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={GEMINI_API_KEY}'
        
        response = requests.post(
            api_url,
            json={
                'contents': [{
                    'parts': [{
                        'text': prompt
                    }]
                }]
            },
            headers={'Content-Type': 'application/json'}
        )
        
        # Check for errors
        if response.status_code != 200:
            error_data = response.json()
            error_message = error_data.get('error', {}).get('message', 'Failed to get response from Gemini API')
            return jsonify({'error': error_message}), response.status_code
        
        # Extract response text
        data = response.json()
        response_text = data.get('candidates', [{}])[0].get('content', {}).get('parts', [{}])[0].get('text', 'No response generated')
        
        return jsonify({
            'success': True,
            'response': response_text
        })
        
    except Exception as e:
        return jsonify({'error': f'Failed to get response from Gemini: {str(e)}'}), 500

# Serve the static files
@app.route('/')
def index():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    # Create static folder if it doesn't exist
    os.makedirs('static', exist_ok=True)
    
    # Run the app
    app.run(host='0.0.0.0', port=5000, debug=True)
