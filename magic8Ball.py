import random

def ask8Ball():
    r = random.randint(1, 20)

    if r == 1:
        return "It is certain"
    elif r == 2:
        return "It is decidedly so"
    elif r == 3:
        return "Without a doubt"
    elif r == 4:
        return "Yes definitely"
    elif r == 5:
        return "You may rely on it"
    elif r == 6:
        return "As I see it, yes"
    elif r == 7:
        return "Most likely"
    elif r == 8:
        return "Outlook good"
    elif r == 9:
        return "Yes"
    elif r == 10:
        return "Signs point to yes"
    elif r == 11:
        return "Reply hazy try again"
    elif r == 12:
        return "Ask again later"
    elif r == 13:
        return "Better not tell you now"
    elif r == 14:
        return "Cannot predict now"
    elif r == 15:
        return "Concentrate and ask again"
    elif r == 16:
        return "Don't count on it"
    elif r == 17:
        return "My reply is no"
    elif r == 18:
        return "My sources say no"
    elif r == 19:
        return "Outlook not so good"
    elif r == 20:
        return "Very doubtful"
    else:
        return "Error: random number broken somehow."

message = ask8Ball()
print(message)