@echo off
REM Quick setup script for Agentic AI Roadmap (Windows)

echo.
echo ========================================
echo  Agentic AI Roadmap - Setup Script
echo ========================================
echo.

REM Check Python version
echo Checking Python version...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python not found. Please install Python 3.12 or higher.
    echo Visit: https://www.python.org/downloads/
    pause
    exit /b 1
)

python --version
echo.

REM Create virtual environment
echo Creating virtual environment...
if not exist ".venv" (
    python -m venv .venv
    echo Virtual environment created
) else (
    echo Virtual environment already exists
)
echo.

REM Activate virtual environment
echo Activating virtual environment...
call .venv\Scripts\activate.bat
if %errorlevel% neq 0 (
    echo ERROR: Failed to activate virtual environment
    pause
    exit /b 1
)
echo Virtual environment activated
echo.

REM Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip >nul 2>&1
echo Pip upgraded
echo.

REM Install dependencies
echo Installing dependencies...
echo This may take a few minutes...
pip install -r requirements.txt >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Failed to install dependencies
    echo Try running: pip install -r requirements.txt
    pause
    exit /b 1
)
echo Dependencies installed successfully
echo.

REM Create .env file if it doesn't exist
if not exist ".env" (
    echo Setting up environment variables...
    echo GOOGLE_API_KEY=your_api_key_here > .env
    echo .env file created
    echo.
    echo WARNING: Edit .env and add your actual API key!
    echo Get one at: https://aistudio.google.com/app/apikey
) else (
    echo .env file already exists
)
echo.

REM Create directories
echo Creating project directories...
if not exist "notebooks" mkdir notebooks
if not exist "examples" mkdir examples
if not exist "resources\cheatsheets" mkdir resources\cheatsheets
if not exist "resources\datasets" mkdir resources\datasets
if not exist "resources\templates" mkdir resources\templates
if not exist "tests" mkdir tests
echo Directories created
echo.

echo ========================================
echo  Setup complete!
echo ========================================
echo.
echo Next steps:
echo 1. Edit .env file and add your Google API key
echo    Get one at: https://aistudio.google.com/app/apikey
echo.
echo 2. Activate the virtual environment:
echo    .venv\Scripts\activate
echo.
echo 3. Start Jupyter Lab:
echo    jupyter lab
echo.
echo 4. Open notebooks\ch0_hello_world.ipynb and start learning!
echo.
echo For more info, see README.md or QUICKSTART.md
echo.
echo Happy Learning!
echo.
pause

