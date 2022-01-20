print('What is your name?\n')

name = input()

print('Hello, {} '.format(name))

print('Hello! Please rate your day on a scale of 1-10.')
day = input()
print("""Your day is rated {} by you.
Thank you for taking part in this questionnaire"""
      .format(day))