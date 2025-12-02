# BlogForge AI - Multi-Agent Content Generation Platform

An intelligent blog writing system powered by CrewAI and Google Gemini 2.0 Flash, featuring three specialized AI agents that collaborate to research, write, and refine blog content.

## 🚀 Features

- **Multi-Agent System**: 3 specialized AI agents working together
  - 🔍 Researcher Agent: Gathers information and key points
  - ✍️ Writer Agent: Creates engaging blog content
  - ✅ Editor Agent: Reviews and refines the final output

- **Powered by Gemini 2.0 Flash**: Free, fast, and powerful LLM
- **Customizable Tone**: Professional, casual, or technical writing styles
- **Real-time Processing**: See agent progress live
- **Easy Deployment**: One-click deploy to Render.com

## 🛠️ Tech Stack

- **Backend**: Flask (Python)
- **AI Framework**: CrewAI
- **LLM**: Google Gemini 2.0 Flash
- **Frontend**: HTML, CSS, JavaScript
- **Deployment**: Render.com

## 📦 Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd "CO22338_BlogForge AI"
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env and add your GOOGLE_API_KEY
```

5. Get Gemini API Key:
   - Visit: https://makersuite.google.com/app/apikey
   - Create a free API key
   - Add it to your `.env` file

6. Run the application:
```bash
python app.py
```

7. Open browser: `http://localhost:5000`

## 🌐 Deployment to Render.com

1. Push code to GitHub
2. Go to [Render.com](https://render.com)
3. Click "New +" → "Web Service"
4. Connect your GitHub repository
5. Configure:
   - **Name**: blogforge-ai
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
6. Add environment variable:
   - Key: `GOOGLE_API_KEY`
   - Value: Your Gemini API key
7. Click "Create Web Service"

## 🎯 How It Works

1. **User Input**: Enter a blog topic and select tone
2. **Researcher Agent**: Analyzes topic and gathers key information
3. **Writer Agent**: Creates structured blog post based on research
4. **Editor Agent**: Reviews, fact-checks, and polishes content
5. **Output**: Complete, publication-ready blog post

## 🤖 Agent Details

### Researcher Agent
- **Role**: Research Specialist
- **Goal**: Gather comprehensive information
- **Output**: Key points, facts, and insights

### Writer Agent
- **Role**: Content Creator
- **Goal**: Write engaging blog posts
- **Output**: Well-structured blog draft

### Editor Agent
- **Role**: Quality Assurance
- **Goal**: Refine and perfect content
- **Output**: Publication-ready blog post

## 🎓 Educational Value

This project demonstrates:
- Multi-agent AI systems
- Agent collaboration patterns
- LLM integration (Gemini)
- Full-stack web development
- Cloud deployment practices

## 📝 License

MIT License - Feel free to use for learning and projects

## 👨‍💻 Author

Developed By: Karanvir Singh (CO22338)

## 🙏 Acknowledgments

- CrewAI Framework
- Google Gemini API
- Flask Framework

~ BlogForge AI Web App Link: https://co22338-blogforge-ai.onrender.com
