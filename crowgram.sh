#!/bin/bash

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'

# Variables [FOR DEVS]
URL="https://github.com/iniridwanul/Crowgram"

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
    echo -e "${RED}Creating .env file...${NC}"

    echo -e "${GREEN}Enter your api_id:${NC}"
    read api_id
    echo -e "${GREEN}Enter your api_hash:${NC}"
    read api_hash
    echo -e "${GREEN}Enter your string:${NC}"
    string_confirmation
    read string
    echo -e "${GREEN}Enter your bot_token:${NC}"
    read bot_token
    echo -e "${GREEN}Enter your assistant_bot:${NC}"
    read assistant_bot
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
    python3 crowgram
}

check_dir
check_venv
install_requirements
check_env
run
