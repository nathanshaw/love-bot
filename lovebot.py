#!/usr/bin/env python
import smtplib
from random import randint
import os

GMAIL_USERNAME = 'nathanshawsemail'

def send_email(text):
    sender = 'nathan@kadenze.com'
    receivers = ['nathanshawsemail@gmail.com', 'kimbysemail@gmail.com']
    # receivers = ['nathanshawsemail@gmail.com']
    for person in receivers:
        headers = "\r\n".join(["from: " + GMAIL_USERNAME,
                            "subject: " + subject[randint(0, len(subject) - 1)],
                            "to: " + person,
                            "mime-version: 1.0",
                            "content-type: text/html"])
        body = text
        print(body)
        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.ehlo()
        session.starttls()
        session.login('nathanshawsemail', 'ns098930')
        message = headers + "\r\n\r\n" + body
    session.sendmail(sender, receivers, message)
    print("E-mail sent to {}".format(receivers))

subject = ['Some of my LOVE', 'Missing You!', 'Just a little note', 'Miss U!', 'Whatcha Doing?',
        'Lubba Dove!', "Lub!", "Pretty Woman", "The Apple of my Life",
        "My Forver Girl"]
kimby = ['Kimby', 'Darling', 'Sweetie', 'Buttercup', 'Kimbers',
         'Kimbella', 'Bella', 'My Delight', 'My Darling Wife',
         'My Dearest Wife', 'Beloved', 'My Treasure', 'My True Love',
         'My Fine Fox', 'My Hearts Desire', 'My Forever', 'My Sunshine',
         'Sunshine of my Love', "The Light of my Love", 'My Better Half']
nathan = ['Nathan', 'Pappa', 'Your Loving Husband', 'Your Soulmate',
          'Your Man', 'Your Hubby', "Your Lover", 'Your Worse Half']
short_action = ['dang girl!', 'missing U!', 'missing you!', 'thinking of you!',
                'wish you were here!', 'looking forward to seeing you tonight!',
                "can't wait to be back home with you!",
                'hope you and the cat are doing well!', 'wish I was with you!']
middle_action = ['you are my', 'you make me think of', 'you are the',
                 'soon we will', 'I cant wait to', 'I cant wait till', 'lets']
middle_word = ['happy', 'chocolate', 'Korean BBQ', 'relationship',
               'missing her', 'missing him', 'forever together',
               'never appart', 'legit', 'lub', 'always',
               'the best thing in my', 'I hate being appart from you',
               'I am thinking of you', 'whatcha doing? Anyways, I',
               'I am missing you', 'you have the best smile', 'peepee poopoo']

last_word = [' love ', ' forever ', ' together ', ' eternal ', ' Darling ',
             ' sweetie ', ' loving ', ' wishing ']
makeup = ['lipstick ', 'nail polish ', 'hair dye ', 'blush ', 'foundation ',
          'makeup ', 'cutical remover ', 'red velvet ', 'blue velvet ',
          'sily smooth ', 'looking good! ']
poem = kimby[randint(0, len(kimby) - 1)]
for i in range(0,2):
    poem = poem + ' ' + short_action[randint(0,len(short_action)-1)] + ' ' + \
                kimby[randint(0, len(kimby)-1)] + ' ' \
        + middle_action[randint(0, len(middle_action)-1)] + ' ' \
        + middle_word[randint(0, len(middle_word)-1)]# + ".\r\n\r\n\r\n"

    if i == 1:
        poem = poem + " " + makeup[randint(0, len(makeup) -1)]

poem = poem + "." + last_word[randint(0, len(last_word))] + nathan[randint(0, len(nathan))]
os.system("say " + poem.strip('\n').strip('\t'))
send_email(poem)
