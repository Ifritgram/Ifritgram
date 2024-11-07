#!/usr/bin/bash

arch_linux(){
    clear
    echo -e "Installing dependencies on Arch Linux to deploy Ifritgram"
    sudo pacman -Syyu --noconfirm
    sudo pacman -S --noconfirm --needed python git
    echo -e "Dependencies have been successfully installed on Arch Linux to deploy Ifritgram"
}

select_os(){
    echo -e "Select OS:\n\n1. Arch Linux\n"
    read -p "guest@ifritgram: " os
    if [ $os == "1" ]; then
        arch_linux
    else
        echo -e "Your preferred operating system is not supported by Ifritgram, or you have entered the wrong input"
        exit
    fi
}

ifritgram_venv(){
    if [ ! -d "venv" ]; then
        echo -e "Virtual environment not found, so creating a virtual environment"
        python3 -m venv venv
        echo -e "Creating the virtual environment was successful"
        ifritgram_venv
    else
        source venv/bin/activate
        echo -e "The virtual environment has been successfully activated"
    fi
}

install_requirements(){
    echo -e "Ifritgram requirements installing"
    pip3 install -r requirements.txt
    echo -e "All the requirements of Ifritgram have been successfully installed in the virtual environment"
    clear
}

generate_string_session(){
    echo -e "Generating String Session for Ifritgram"
    python3 string_session.py
    echo -e "String Session has been successfully generated"
}

create_environment_file(){
    echo -e "Creating a .env file"
    read -p "Enter Your api_id: " api_id
    read -p "Enter Your api_hash: " api_hash
    read -p "Enter Your string_session: " string_session
    read -p "Enter Your ifritgram_gallery: " ifritgram_gallery
    read -p "Enter Your bot_token: " bot_token
    read -p "Enter Your User ID: " owner
    read -p "Enter Your assistant_bot: " assistant_bot
    echo -e "Writing to .env file"
    echo "api_id=$api_id" >>.env
    echo "api_hash=$api_hash" >>.env
    echo "string_session=$string_session" >>.env
    echo "ifritgram_gallery=$ifritgram_gallery" >>.env
    echo "bot_token=$bot_token" >>.env
    echo "owner=$owner" >>.env
    echo "assistant_bot=$assistant_bot" >>.env
    echo -e "Successfully created .env file"
}

export_variables(){
    while read line; do
        if [[ $line == *"="* && $line != \#* ]]; then
            export $line
        fi
    done <.env
    clear
    echo -e "Variables exported"
}

run_ifritgram(){
    python3 ifritgram
}

select_os
ifritgram_venv
install_requirements
generate_string_session
create_environment_file
export_variables
run_ifritgram