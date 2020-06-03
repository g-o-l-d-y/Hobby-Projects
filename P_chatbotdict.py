# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 10:13:40 2020

@author: goldy
"""

def sick(string,language):
    pairs = {
            "what is your name ?":"My name is Dora and I'm a chatbot.",
            "how are you ?":"I'm doing good\nHow about You ?",
            "sorry (.*)":"Its alright",
            "i'm (.*) doing good":"Nice to hear that",
            "hi":"Hello",
            "(.*) age?":"I'm a computer program dude\nSeriously you are asking me this?",
            "what (.*) want ?":"Make me an offer I can't refuse",
            "(.*) created ?":"Bujji created me using Python's NLTK library ",
            "(.*) (location|city) ?":"Chennai, Tamil Nadu",
            "how is weather in (.*)?":"Weather in %1 is awesome like always",
            "i work in (.*)?":"%1 is an Amazing company, I have heard about it. But they are in huge loss these days.",
            "(.*)raining in (.*)":"No rain since last week here in %2",
            "how (.*) health(.*)":"I'm a computer program, so I'm always healthy ",
            "(.*) (sports|game) ?":"I'm a very big fan of Cricket",
            "who (.*) sportsperson ?":"MS Dhoni",
            "who (.*) (moviestar|actor)?":"Amitabh Bacchan",
            "quit":"Bye take care. See you soon :) ",
            "good night":"Good Night, sweet dreams!",
            "good morning":"Good morning, have a great day!"
    }
    translator=Translator()
    print((translator.translate(pairs[string],src="en",dest=language)).text)

from googletrans import Translator
from nltk.chat.util import Chat,reflections

def dora():
    print("Hi, I'm Dora and I chat alot ;)\nConverse and get rid of boredom. Type quit to leave ")
    translator=Translator()
    while 1:
        s=input()
        if s=="quit":
            break
        d=translator.translate(s)
        language=d.src
        sick(d.text,language)
dora()