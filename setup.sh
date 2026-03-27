#!/bin/bash
# Jarves Setup Script

echo "🤖 Setting up Jarves..."

# Check Python version
python3 --version || { echo "Python 3 not found!"; exit 1; }

# Create virtual environment
echo "Creating virtual environment..."
cd "$(dirname "$0")"
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Create data directories
mkdir -p data logs config

# Make jarves.py executable
chmod +x jarves.py

echo ""
echo "✅ Setup complete!"
echo ""
echo "To start Jarves:"
echo "  source venv/bin/activate"
echo "  python3 jarves.py"
echo ""
echo "Or use the shortcut:"
echo "  ./jarves.py"
