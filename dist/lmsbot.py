import subprocess
# GREET USER

print("Hello friend, I'm your wtc-lms assistant.")
while True:
    todo = input("What can I assist with? ").lower()
    if todo == "login":
        subprocess.run(["lmslogin"])
    
    elif todo == "review":
        subprocess.run(["review"])

    elif todo == "details":
        subprocess.run(["details"])
    
    else:
        subprocess.run(["echo", "Did not understand..."])