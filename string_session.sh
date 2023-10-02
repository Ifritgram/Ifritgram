#!/bin/bash

check_venv(){
    if [ ! -d "venv" ]; then
        python3 -m venv venv
        check_venv
    else
        source venv/bin/activate
        pip3 install Telethon
    fi
}

run_string_session_generator(){
    clear
    python3 string_session.py
}

check_venv
run_string_session_generator