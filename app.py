from flask import Flask, render_template, request, jsonify
from crew.crew import BlogCrew
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/generate-blog', methods=['POST'])
def generate_blog():
    try:
        data = request.json
        topic = data.get('topic', '')
        tone = data.get('tone', 'professional')
        
        if not topic:
            return jsonify({'error': 'Topic is required'}), 400
        
        # Initialize and run the crew
        blog_crew = BlogCrew(topic, tone)
        result = blog_crew.run()
        
        return jsonify({
            'success': True,
            'blog_post': result.get('final_blog', ''),
            'research_summary': result.get('research', ''),
            'agent_logs': result.get('logs', [])
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)