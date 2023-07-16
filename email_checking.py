'''

witten by davlatbek_kobiljonov
07/16/23

'''

import re

# first we create the pattern for matching the actual email
email_pattern = re.compile("^[a-zA-Z0 -9\.\-_]+@{1}(gmail)+\.{1}(com|ru)$")

while (True):
    email = input("Enter your email: ")
    # now we are matching if the email entered by the user
    s = re.match(email_pattern, email)
    if email == 'exit':
        break
    elif s:
        print("Valid email ")
    else:
        print('Invalid email ')
