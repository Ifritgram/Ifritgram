#!/bin/bash

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'

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

# Check .env file
read_env() {
    if [ ! -f ".env" ]; then
        echo -e "${RED}.env file not found. Creating...${NC}"
        echo -e "${GREEN}Please consider creating one...${NC}"
        echo -e "${GREEN}For refernece you can use '.env.sample'${NC}"
    else
        echo -e "${GREEN}.env file found.${NC}"
    fi
}

# activates every lines of .env file
read_lines() {
    while read line; do
        if [[ $line == *"="* && $line != \#* ]]; then
            export $line
            # echo $line
        fi
    done < .env
}

# Run all functions
run() {
    python3 crowgram
}

check_venv
install_requirements
read_env
read_lines
run