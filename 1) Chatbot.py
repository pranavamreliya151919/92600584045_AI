print("Welcome To AI ChatBot :)")
print("I am For You Please Say Hello")

while True:
    msg=input("You :").lower()
    if 'hello' in msg:
        print("Bot : How are You ?")
    elif 'fine' in msg:
        print("Great...!, Can I Help For Your Study?")
    elif 'yes' in msg:
        print("What Help You Needed?")
    elif 'course' in msg:
        print("You Have Select AI Course :)")
    elif 'why' in msg:
        print("AI is Best option for Future. And you Learn About AI for that You Learn The Language")
        print("You Clear For the Languge which would to like?")
    elif 'language' in msg:
        print("Python Is Best For This...")
    elif 'learn' in msg:
        print("In Youtube and also With Proper Courses at low cost")
    elif 'fee':
        print("2500 but in youtube also learn as free")
    elif 'how' in msg:
        print("Any Python Youtube Channel to join and Learn")
    elif 'thank' in msg:
        print("Can You Any Other Quetion ?")
    elif 'No' in msg:
        print("Ok Then Please Bye...")
    elif 'bye' in msg:
        print("Good Bye Have A Nice Day :)")
        break
    else:
        print("Sorry, I Can't Understand Your Question:(")


