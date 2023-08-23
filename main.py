import time

frontend_lang = ["JavaScript", "Typescript", "HTML", "CSS", "Swift"]
backend_lang = ["Advanced Python", "JavaScript",
                "C#", "Java", "Ruby", "PHP", "Golang", "SQL"]
game_lang = ["Advanced Python", "C#", "C++", "JavaScript"]
data_lang = ["SQL", "Advanced Python", "Java", "R", "Scala"]
app_lang = ["C#", "HTML5", "Java"]
known_languages = ["Python"]


def join_list(list):
    return ", ".join(list)


def add_to_do(langs):
    c = open("tolearn.txt", "w")
    c.write("To learn:\n")
    for item in langs:
        c.write("- "+item+"\n")


print("***** Don't Know Which Coding Language to Learn, We Are Here to Help *****")
time.sleep(2)
name = input("What is your name? ")
print("Let's find out which coding language you should learn next,", name + "!")
print("First, let's find out a bit more about you.")
time.sleep(3)
other_lang = input(
    "We know you now know python.\nBut do you know any other coding languages? (y/n) ")
if other_lang == "y":
    correct = "n"
    while correct == "n":
        more = "y"
        while more == "y":
            knowledge = input("What coding language do you know? ")
            known_languages.append(knowledge)
            more = input("Do you know any other coding languages? (y/n) ")
        print("So you know", ", ".join(known_languages)+".")
        time.sleep(2)
        correct = input("Is that correct? ")
time.sleep(2)
print("Ok now we need to know your purpose.")
time.sleep(1)
print("Why are you trying to learn a new language?")
time.sleep(1)
purpose = int(input("Is it for:\n1. Web Development\n2. Creating games\n3. Creating mobile apps\n4. Data analysis\n5. Building further coding knowledge? (input number) "))

if purpose == 1:
    print("Web development is a little more complex because you have to learn to code the backend (the side that coand frontend.")
    time.sleep(1)
    print("The backend comprises of the physical infrasturture of the website. This is the part that a user would not see")
    time.sleep(1)
    print("For backend web development, you should try learning",
          join_list(backend_lang))
    time.sleep(1)
    print("The frontend of a website is the part that the user will interact with. This is the graphical user interface (GUI).")
    time.sleep(1)
    print("For frontend web development, you should try learning",
          join_list(frontend_lang))
    add_to_do(backend_lang)
    add_to_do(frontend_lang)
elif purpose == 2:
    print("For game development, you should try learning", join_list(game_lang))
    add_to_do(game_lang)
elif purpose == 3:
    print("For mobile app development, you should try learning", join_list(app_lang))
    add_to_do(app_lang)
elif purpose == 4:
    print("For data analysis/manipulation, you should try learning",
          join_list(data_lang))
    add_to_do(data_lang)
elif purpose == 5:
    print("To build further coding knowledge, stick to what you know and improve on it.")
    time.sleep(1)
    print("Look for tutorials and courses that help you advance your",
          join_list(known_languages), "skills.")
    add_to_do(known_languages)
else:
    print("Not really one of the options is it...")


# print("( 0 _ 0 ) Your answer has broken our system, please try again ( 0 _ 0 )")
