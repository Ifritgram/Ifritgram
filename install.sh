#!/bin/bash
# Will be deleted soon

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
        echo -e "${GREEN}Git clonning...${NC}"
        git clone $URL
        if [ -d "Crowgram" ]; then
            echo -e "${GREEN}Entering into directory...${NC}"
            cd Crowgram
        fi
    else
        echo -e "${GREEN}crowgram.sh file found.${NC}"
        echo -e "${GREEN}Directory exists!${NC}"
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

check_dir
env_make
bash crowgram.sh
