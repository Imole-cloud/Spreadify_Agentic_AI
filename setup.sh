#!/bin/bash
# Spreadify Agents Setup Script

echo "🚀 Setting up Spreadify Agents..."

# Install Python dependencies
pip install -r requirements.txt

# Install Playwright browsers
playwright install chromium

# Copy environment template
cp .env.template .env

# Initialize git (if not already done)
git init
git add .
git commit -m "Initial commit: Spreadify Agents"

# Add remote and push to GitHub (replace with your repo URL)
git remote add origin https://github.com/Lightiam/Spreadify_Agentic_AI.git
git branch -M main
git push -u origin main

echo "✅ Setup complete!"
echo "📱 Run: python spreadify_agent.py"
echo "🌐 Then open: http://localhost:5000"
