# 🚀 Quick Start Guide

Get up and running in 5 minutes!

## Step 1: Prerequisites Check ✅

Make sure you have:
- [ ] Python 3.12 or higher installed
- [ ] Git installed
- [ ] A Google account (for Gemini API)

Check your Python version:
```bash
python --version
```

## Step 2: Clone and Setup 📦

```bash
# Clone the repository
git clone https://github.com/yourusername/agentic-ai-roadmap.git
cd agentic-ai-roadmap

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On macOS/Linux:
source .venv/bin/activate
# On Windows:
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Step 3: Get Your API Key 🔑

1. Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Click "Create API Key"
3. Copy your API key

## Step 4: Configure Environment 🔧

Create a `.env` file in the project root:

```bash
# On macOS/Linux:
echo "GOOGLE_API_KEY=your_api_key_here" > .env

# On Windows (PowerShell):
"GOOGLE_API_KEY=your_api_key_here" | Out-File -FilePath .env
```

**⚠️ IMPORTANT**: Replace `your_api_key_here` with your actual API key!

## Step 5: Run Your First Notebook 🎉

### Option A: Using Jupyter Lab (Recommended)
```bash
pip install jupyterlab
jupyter lab
```
Then open `notebooks/ch0_hello_world.ipynb`

### Option B: Using Google Colab
1. Go to [Google Colab](https://colab.research.google.com/)
2. File → Upload notebook
3. Upload `notebooks/ch0_hello_world.ipynb`
4. Run the first cell to set your API key

### Option C: Using VS Code
1. Install the Jupyter extension
2. Open the notebook file
3. Click "Run All"

## Verify Installation ✨

Run this quick test:

```python
from langchain_google_genai import ChatGoogleGenerativeAI
import os

# Load API key
api_key = "your_api_key_here"  # or use os.getenv("GOOGLE_API_KEY")

# Create LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0,
    api_key=api_key
)

# Test it!
response = llm.invoke("Say hello!")
print(response.content)
```

If you see a greeting message, you're all set! 🎊

## Troubleshooting 🔧

### Issue: "Module not found"
```bash
# Make sure virtual environment is activated
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows

# Reinstall dependencies
pip install -r requirements.txt
```

### Issue: "Invalid API key"
- Check that your API key is correct
- Verify the `.env` file exists in the project root
- Make sure there are no extra spaces in the API key

### Issue: "Rate limit exceeded"
- You may have hit the free tier limit
- Wait a few minutes and try again
- Consider upgrading your API plan

### Issue: Python version too old
```bash
# Check your version
python --version

# If less than 3.12, install Python 3.12+
# Visit: https://www.python.org/downloads/
```

## Next Steps 📚

1. ✅ Complete Chapter 0: Hello World
2. ⏭️ Move on to Chapter 1: Introduction & Setup
3. 🎥 Watch the accompanying YouTube videos
4. 💪 Complete the exercises
5. 🚀 Build your own projects!

## Need Help? 🆘

- 📖 Check the main [README.md](README.md)
- 💬 Open an issue on GitHub
- 🌐 Join our community discussions
- 📧 Contact: your.email@example.com

---

**Happy Learning! 🎓**

