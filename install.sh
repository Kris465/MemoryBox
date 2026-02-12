#!/bin/bash

# Installation script for Sound Terminal

echo "Installing Sound Terminal..."

# Check if we're in the correct directory
if [ ! -f "setup.py" ]; then
    echo "Error: setup.py not found. Please run this script from the sound_term directory."
    exit 1
fi

# Install system dependencies (Arch Linux)
echo "Installing system dependencies..."
sudo pacman -S --needed python python-pip portaudio

# Check if RHVoice is installed
if ! command -v RHVoice-test &> /dev/null; then
    echo "RHVoice not found. Installing..."
    sudo pacman -S --needed rhvoice
else
    echo "RHVoice is already installed."
fi

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install Python dependencies
echo "Installing Python dependencies..."
pip install -e .

# Make the sound script executable
chmod +x sound

# Create symlink in ~/.local/bin
if [ ! -d "$HOME/.local/bin" ]; then
    mkdir -p $HOME/.local/bin
fi

ln -sf $(pwd)/sound $HOME/.local/bin/sound

echo "Installation completed!"
echo "You can now run 'sound' from anywhere in your terminal."
echo "Make sure to add $HOME/.local/bin to your PATH if it's not already there."