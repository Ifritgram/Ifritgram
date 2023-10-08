#!/bin/bash

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'

# Variables [FOR DEVS]
URL="https://github.com/iniridwanul/Crowgram"

archlinux() {
    echo -e "${RED}Installing dependencies...${NC}"
    sudo pacman -Syyu --noconfirm
    sudo pacman -S --noconfirm --needed git python python-pip python-setuptools python-wheel python-virtualenv ffmpeg nodejs npm
    echo -e "${GREEN}Dependencies installed.${NC}"
}

ubuntu() {
    echo -e "${RED}Installing dependencies...${NC}"
    sudo apt-get update
    sudo apt-get upgrade -y
    sudo apt-get install -y git python3 python3-pip python3-setuptools python3-wheel python3-virtualenv ffmpeg nodejs npm
    echo -e "${GREEN}Dependencies installed.${NC}"
}

fedora() {
    echo -e "${RED}Installing dependencies...${NC}"
    sudo dnf update
    sudo dnf install -y git python3 python3-pip python3-setuptools python3-wheel python3-virtualenv ffmpeg nodejs npm
    echo -e "${GREEN}Dependencies installed.${NC}"
}

termux() {
    echo -e "${RED}Installing dependencies...${NC}"
    pkg update
    pkg upgrade -y
    pkg install -y git python python-pip python-setuptools python-wheel python-virtualenv ffmpeg nodejs npm
    echo -e "${GREEN}Dependencies installed.${NC}"
}

other_os() {
    echo -e "${RED}Please install the dependencies manually.${NC}"
    echo -e "${GREEN}Dependencies:${NC}"
    echo -e "${GREEN}1. Python Version 3+${NC}"
    echo -e "${GREEN}2. Git${NC}"
    echo -e "${GREEN}3. Python3-pip${NC}"
    echo -e "${GREEN}4. NodeJS${NC}"
}

check_os() {
    echo -e "${RED}What is your OS?${NC}"
    echo -e "${GREEN}Enter 1 for Ubuntu/Debian${NC}"
    echo -e "${GREEN}Enter 2 for Arch/Manjaro${NC}"
    echo -e "${GREEN}Enter 3 for Termux${NC}"
    echo -e "${GREEN}Enter 4 for fedora${NC}"
    echo -e "${GREEN}Enter 5 for other${NC}"
    read os

    if [ $os == "1" ]; then
        ubuntu
    elif [ $os == "2" ]; then
        archlinux
    elif [ $os == "3" ]; then
        termux
    elif [ $os == "4" ]; then
        fedora
    elif [ $os == "5" ]; then
        other_os
    else
        echo -e "${RED}Invalid option.${NC}"
        check_os
    fi
}
# Check directory
check_dir() {
    if [ ! -f "crowgram.sh" ]; then
        echo -e "${RED}crowgram.sh file not found.${NC}"
        echo -e "${GREEN}Git cloning...${NC}"
        git clone $URL
        if [ -d "Crowgram" ]; then
            echo -e "${GREEN}Entering into directory...${NC}"
            cd Crowgram
        fi
    else
        echo -e "${GREEN}crowgram.sh file found.${NC}"
        echo -e "${GREEN}Directory exists!${NC}"
        echo -e "${GREEN}Synchronizing latest changes...${NC}"
        git pull
    fi
}

# Check python virtual environment
check_venv() {
    if [ ! -d "venv" ]; then
        echo -e "${RED}Python virtual environment not found. Installing...${NC}"
        python3 -m venv venv
        check_venv
    else
        echo -e "${GREEN}Python virtual environment found.${NC}"
        source venv/bin/activate
        echo -e "${GREEN}Python virtual environment activated.${NC}"
    fi
}

# Install requirements
install_requirements() {
    echo -e "${RED}Installing requirements...${NC}"
    pip install -r requirements.txt
    echo -e "${GREEN}Requirements installed.${NC}"
}

# activates every lines of .env file
read_lines() {
    while read line; do
        if [[ $line == *"="* && $line != \#* ]]; then
            export $line
            # echo $line
        fi
    done <.env
    echo -e "${GREEN}Variables exported.${NC}"
}

# string generation
string_gen() {
    echo -e "${RED}Generating string session...${NC}"
    echo -e "${GREEN}Please strore it for future references!${NC}"
    python3 string_session.py
    echo -e "${GREEN}String session generated.${NC}"
}

# String session confirmation
string_confirmation() {
    echo -e "${RED}Do you want to generate string session?${NC}"
    echo -e "${GREEN}Enter y/n:${NC}"
    read answer
    if [ $answer == "y" ]; then
        string_gen
    else
        echo -e "${GREEN}Skipping...${NC}"
    fi
}

# Automatically create a .env file for above variables
env_make() {
    clear
    echo -e "${RED}Creating .env file...${NC}"

    echo -e "${GREEN}Enter your api_id:${NC}"
    read api_id
    echo -e "${GREEN}Enter your api_hash:${NC}"
    read api_hash
    string_confirmation
    echo -e "${GREEN}Enter your string:${NC}"
    read string

    echo -e "${GREEN}Enter your bot_token:${NC}"
    read bot_token
    echo -e "${GREEN}Enter your assistant_bot:${NC}"
    read assistant_bot

    echo -e "${GREEN}Enter your assistant_api_id:${NC}"
    read assistant_api_id
    echo -e "${GREEN}Enter your assistant_api_hash:${NC}"
    read assistant_api_hash
    string_confirmation
    echo -e "${GREEN}Enter your assistant_string:${NC}"
    read assistant_string

    echo -e "${GREEN}Enter your owner:${NC}"
    read owner
    echo -e "${GREEN}Enter your log_group:${NC}"
    read log_group
    echo -e "${GREEN}Enter your pm_log_location:${NC}"
    read pm_log_location
    echo -e "${GREEN}Enter your mention_log_location:${NC}"
    read mention_log_location

    echo -e "${GREEN}Writing to .env file...${NC}"
    echo "api_id=$api_id" >>.env
    echo "api_hash=$api_hash" >>.env
    echo "string=$string" >>.env
    echo "bot_token=$bot_token" >>.env
    echo "assistant_bot=$assistant_bot" >>.env
    echo "assistant_api_id=$assistant_api_id" >>.env
    echo "assistant_api_hash=$assistant_api_hash" >>.env
    echo "assistant_string=$assistant_string" >>.env
    echo "owner=$owner" >>.env
    echo "log_group=$log_group" >>.env
    echo "pm_log_location=$pm_log_location" >>.env
    echo "mention_log_location=$mention_log_location" >>.env
    echo -e "${GREEN}.env file created.${NC}"
}

# Check .env file
check_env() {
    if [ ! -f ".env" ]; then
        echo -e "${RED}.env file not found.${NC}"
        echo -e "${RED}Do you want to create .env file?${NC}"
        echo -e "${GREEN}Enter y/n:${NC}"
        read answer
        if [ $answer == "y" ]; then
            env_make
            read_lines
        else
            echo -e "${GREEN}Skipping...${NC}"
            exit 0
        fi
    else
        echo -e "${GREEN}.env file found.${NC}"
        read_lines
    fi
}

# Run all functions
run() {
    clear
    python3 crowgram
}

check_dir
check_venv
install_requirements
check_env
run
