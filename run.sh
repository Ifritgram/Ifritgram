#!/usr/bin/bash

export_variables(){
    while read line; do
        if [[ $line == *"="* && $line != \#* ]]; then
            export $line
        fi
    done <.env
    echo -e "Variables exported"
}

ifritgram_run(){
    if [ -d "venv" ]; then
        source venv/bin/activate
        echo -e "The virtual environment has been successfully activated"
        if [ -f ".env" ]; then
            export_variables
            python3 ifritgram
        else
            clear
            bash deploy.sh
            exit
        fi
    else
        clear
        bash deploy.sh
        exit
    fi
}

ifritgram_run