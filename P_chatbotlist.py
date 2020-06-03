# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 17:27:11 2020

@author: goldy
"""

reflections = {
  "i am"       : "you are",
  "i was"      : "you were",
  "i"          : "you",
  "i'm"        : "you are",
  "i'd"        : "you would",
  "i've"       : "you have",
  "i'll"       : "you will",
  "my"         : "your",
  "you are"    : "I am",
  "you were"   : "I was",
  "you've"     : "I have",
  "you'll"     : "I will",
  "your"       : "my",
  "yours"      : "mine",
  "you"        : "me",
  "me"         : "you"
}
from googletrans import Translator
from nltk.chat.util import Chat,reflections

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?",]
    ],
    [
     r"i am (.*)",
     ["Hi %1, How are you today ?",]
     ],
     [
        r"what is your name ?",
        ["My name is Dora and I'm a chatbot.",]
    ],
    [
        r"how are you ?| how is your health ?",
        ["I'm doing good\nHow about You ?",]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind",]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that","Alright :)",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"(.*) age?",
        ["I'm a computer program dude\nSeriously you are asking me this?",]
        
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
        
    ],
    [
        r"(.*) created ?",
        ["Bujji created me using Python's NLTK library ","top secret ;)",]
    ],
    [
        r"(.*) (location|city) ?",
        ['Chennai, Tamil Nadu',]
    ],
    [
        r"how is weather in (.*)?",
        ["Weather in %1 is awesome like always","Too hot man here in %1","Too cold man here in %1","Never even heard about %1"]
    ],
    [
        r"i work in (.*)?",
        ["%1 is an Amazing company, I have heard about it. But they are in huge loss these days.",]
    ],
[
        r"(.*)raining in (.*)",
        ["No rain since last week here in %2","Damn its raining too much here in %2"]
    ],
    [
        r"how (.*) health(.*)",
        ["I'm a computer program, so I'm always healthy ",]
    ],
    [
        r"(.*) (sports|game) ?",
        ["I'm a very big fan of Cricket",]
    ],
    [
        r"who (.*) sportsperson ?",
        ["MS Dhoni","Virat Kohli","P V Sindhu"]
],
    [
        r"who (.*) (moviestar|actor)?",
        ["Amitabh Bacchan","Thalaivar","Thala","Chiranjevi","Savithri","Anushka"]
],
    [
        r"quit",
        ["Bye take care. See you soon :) ","It was nice talking to you. See you soon :)"]
],
    [ r"good morning|good Morning",
     ["Good Morning. Have a nice day"]
     ],
    [ r"good night",
     ["Good night. Sweet dreams!"]
     ]
]

def dora():
    print("Hi, I'm Dora and I chat alot ;)\nConverse and get rid of boredom. Type quit to leave ") #default message at the start

    #translator=Translator()
    #chat = Chat(pairs, reflections)
    while (1):
        s=input()
        if s=="quit":
            break
        translator=Translator()
        chat = Chat(pairs, reflections)
        d=translator.translate(s)
        language=d.src
        string=chat.respond(d.text)
        #print(d.text)
        #print(string)
        print((translator.translate(string,src="en",dest=language)).text)
dora()