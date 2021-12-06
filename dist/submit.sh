#!/usr/bin/bash

# SUBMIT SCRIPT

read -p "Still remember your project codename? " PJCODENAME

if [ $PJCODENAME == "yes" ] || [ $PJCODENAME == "y" ] || [ $PJCODENAME == "YES" ] || [ $PJCODENAME == "Y" ] || [ $PJCODENAME == "Yes" ]; then
    read -p "Enter codename: " CODENAME
    printf "\nSubmitting $CODENAME..."
    wtc-lms grade $CODENAME
    sleep 5
    wtc-lms history $CODENAME
    printf "\nDone.\n"

elif [ $PJCODENAME == "no" ] || [ $PJCODENAME == "n" ] || [ $PJCODENAME == "NO" ] || [ $PJCODENAME == "N" ] || [ $PJCODENAME == "No" ]; then
    printf "Fetching topics...\n"
    wtc-lms topics giant-green-cycle
    echo ""
    read -p "Which topic? " TOPIC2
    wtc-lms problems $TOPIC
    read -p "Problem codename: " PROBLEM
    printf "\nSubmitting $PROBLEM..."
    wtc-lms grade $PROBLEM
    sleep 5
    wtc-lms history $PROBLEM
    printf "\nDone.\n"

else
    echo "Sorry couldn't understand that..."
fi

