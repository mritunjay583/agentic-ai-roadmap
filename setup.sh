#!/bin/bash
# Quick setup script for Agentic AI Roadmap

echo "🚀 Agentic AI Roadmap - Setup Script"
echo "====================================="
echo ""

# Check Python version
echo "📋 Checking Python version..."
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
    echo "✅ Python $PYTHON_VERSION found"
    
    # Check if version is 3.12+
    MAJOR=$(echo $PYTHON_VERSION | cut -d'.' -f1)
    MINOR=$(echo $PYTHON_VERSION | cut -d'.' -f2)
    
    if [ "$MAJOR" -lt 3 ] || ([ "$MAJOR" -eq 3 ] && [ "$MINOR" -lt 12 ]); then
        echo "⚠️  Warning: Python 3.12+ is recommended. You have $PYTHON_VERSION"
    fi
else
    echo "❌ Python 3 not found. Please install Python 3.12 or higher."
    exit 1
fi

echo ""

# Create virtual environment
echo "🔧 Creating virtual environment..."
if [ ! -d ".venv" ]; then
    python3 -m venv .venv
    echo "✅ Virtual environment created"
else
    echo "ℹ️  Virtual environment already exists"
fi

echo ""

# Activate virtual environment
echo "📦 Activating virtual environment..."
source .venv/bin/activate
echo "✅ Virtual environment activated"

echo ""

# Upgrade pip
echo "⬆️  Upgrading pip..."
pip install --upgrade pip > /dev/null 2>&1
echo "✅ Pip upgraded"

echo ""

# Install dependencies
echo "📚 Installing dependencies..."
echo "   This may take a few minutes..."
pip install -r requirements.txt > /dev/null 2>&1
if [ $? -eq 0 ]; then
    echo "✅ Dependencies installed successfully"
else
    echo "❌ Error installing dependencies. Check requirements.txt"
    exit 1
fi

echo ""

# Create .env file if it doesn't exist
if [ ! -f ".env" ]; then
    echo "🔑 Setting up environment variables..."
    echo "GOOGLE_API_KEY=your_api_key_here" > .env
    echo "✅ .env file created"
    echo "⚠️  IMPORTANT: Edit .env and add your actual API key!"
else
    echo "ℹ️  .env file already exists"
fi

echo ""

# Create directories
echo "📁 Creating project directories..."
mkdir -p notebooks examples resources/cheatsheets resources/datasets resources/templates tests
echo "✅ Directories created"

echo ""

echo "🎉 Setup complete!"
echo ""
echo "Next steps:"
echo "1. Edit .env file and add your Google API key"
echo "   Get one at: https://aistudio.google.com/app/apikey"
echo ""
echo "2. Activate the virtual environment (if not already active):"
echo "   source .venv/bin/activate"
echo ""
echo "3. Start Jupyter Lab:"
echo "   jupyter lab"
echo ""
echo "4. Open notebooks/ch0_hello_world.ipynb and start learning!"
echo ""
echo "📚 For more info, see README.md or QUICKSTART.md"
echo ""
echo "Happy Learning! 🚀"

