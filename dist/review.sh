#!/usr/bin/bash

# SCRIPT FOR REVIEWING STUDENTS ON LMS

printf "Fetching invited reviews...\n"
wtc-lms reviews | grep "Invited"

echo ""

read -p "Accept codename: " CODENAME
wtc-lms accept $CODENAME
printf "\nYou're assigned to $CODENAME. Showing details...\n"

sleep 3

wtc-lms review_details $CODENAME
echo ""

read -p "Review accepted. wanna clone the repo? " CLONE

if [ $CLONE == "yes" ] || [ $CLONE == "y" ] || [ $CLONE == "YES" ] || [ $CLONE == "Y" ] || [ $CLONE == "Yes" ]; then
	wtc-lms review_details $CODENAME | grep "git@gitlab" > repo
	sleep 3
	
	sed -i "s/Git Url:/git clone/" repo
	chmod +x repo
	./repo

	sleep 5
	rm repo

elif [ $CLONE == "no" ] || [ $CLONE == "n" ] || [ $CLONE == "NO" ] || [ $CLONE == "N" ] || [ $CLONE == "No" ]; then
	printf "\nOkay...\n"
else
	echo "Sorry I couldn't understand that..."
fi




