# for i in 'Portland':
#     print(i, end=' ')

# For the first bot, the steps are as follows:
    # Ask the user at least two questions.
    # Respond to each answer. Include the answer in the response.

# For the second bot, the steps are as follows:
#
#     Ask a question that can be answered with a number scale, such as "On a scale of 1-10…".
#     Respond differently depending on the answer given.
#     State a different question following each answer that can be answered with a number scale.
#     Respond differently depending on the answer given.
#
# while True:
#     question = input("What is your question?")
#
#     if "how are you" in question:
#         print('I am fine')
#     elif "do" in question:
#         print("What are you saying")
#     elif "break" in question or question.upper():
#         break
#     else:
#         continue
while True:
    print("What is your name?")
    name = input()
    print("Hi", name, end=". " "So nice to meet you!")
    break
print()
while True:
    print("How did your day go on a scale of 1 - 10?")
    day_scale = int(input())
    if day_scale == 1:
        print("Awwww, what happened?")
        reason = input()
        print("Don't worry dear. You shall win")
    elif day_scale == 2:
        print("Can you share?")

        reason = input()
        print("Don't worry dear. You shall win")
    elif day_scale == 3:
        print("It is going to be fine Hun. Talk to me.")

        reason = input()
        print("I can only imagine. You shall win")
    elif day_scale == 4:
        print("Talk to me, Hun.")

        reason = input()
        print("So sorry dear. You shall win")
    elif day_scale == 5:
        print("Half is a great way to start. What's up?")

        reason = input()
        print("Just a little longer. You shall win")
    elif day_scale == 6:
        print("In this Buhari regime? Gist me.")

        reason = input()
        print("I see ritualism")
    elif day_scale == 7:
        print("You are most likely a ritualist. Talk to us")

        reason = input()
        print("Lol. You always win. Kisses.")
    elif day_scale == 8:
        print("Yippeee. Can I know how it went?")

        reason = input()
        print("Beautiful dear. You always win")
    elif day_scale == 9:
        print("What a great day it must have been for you. Congrats!.")
    elif day_scale == 10:
        print("Yassss. More winsssss Hun")
    elif day_scale == "break":
        break