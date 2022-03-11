#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os, re
from time import sleep
from termcolor import colored, cprint
from blessed import Terminal
import string
import random
import pyfiglet
from PyDictionary import PyDictionary
dictionary=PyDictionary()
term = Terminal()
import enchant
d = enchant.Dict("en_US")


class Wordle: 
    def __init__(self, word_list, word_len=0, debug=False): 
        self.secret_word = random.choice(word_list)
        if sys.argv[-1] in  string.digits: 
            for w in words: 
                if len(w) == int(sys.argv[-1]):
                    secret_word = w
                    break

        self.guesses = [ ]
        self.max_guesses = 5
        self.cur_inpt = ""
        self.debug = debug
        self.debug_dump = ""
        self.temp_secret_word = ""
        self.reward = r'''

                            ,.
                           (\(\)
           ,_              ;  o >
            {`-.          /  (_)
            `={\`-._____/`   |
             `-{ /    -=`\   |
           .="`={  -= = _/   /`"-.
          (M==M=M==M=M==M==M==M==M)
           \=N=N==N=N==N=N==N=NN=/
            \M==M=M==M=M==M===M=/
             \N=N==N=N==N=NN=N=/
          jgs \M==M==M=M==M==M/
               `-------------'
               '''


    def word_by_word(self, word_list, t=1):
        punishing_sentence = ""
        for i,w in enumerate(word_list): 
            os.system('clear')
            punishing_sentence = punishing_sentence +"   "+ w
            ascii_banner = pyfiglet.figlet_format(punishing_sentence)
            print(ascii_banner)
            sleep(t)

    def draw(self, word,  writing = False): 
        self.temp_secret_word = self.secret_word
        for i,l in enumerate(self.secret_word): 
            try:
                if writing:
                    c = "on_white"
                elif word[i] == l: 
                    self.temp_secret_word = self.temp_secret_word.replace(word[i], '', 1)
                    c = "on_green"
                elif word[i] in self.temp_secret_word: 
                    self.temp_secret_word = self.temp_secret_word.replace(word[i], '', 1)
                    c = "on_yellow"
                else: 
                    c = "on_red"
                cprint(word[i],'grey', c, end='  ')
            except:
                cprint(" ",'grey', "on_white", end='  ')
        print("\n")

    def draw_all(self):
        os.system('clear')
        if self.debug: 
            print("game data: \n ========================================== ")
            print(self.guesses)
            print(self.secret_word)
            print(self.cur_inpt)
            print(self.debug_dump)
            print(self.temp_secret_word)
            print("\n ========================================== ")
        cur_inpt = self.cur_inpt
        for i in range(self.max_guesses): 
            try:
                self.draw(self.guesses[i])
            except IndexError:
                self.draw(cur_inpt, True)
                l = []
                l += ([" "] * len(self.secret_word)) 
                cur_inpt = "".join(l)
    def inpt(self):
        self.cur_inpt = ""
        while True: 
            sleep(0.05)
            self.draw_all()
            with term.raw():
                inp = term.inkey()
                if str(inp) in string.ascii_lowercase and len(self.cur_inpt) < len(self.secret_word): 
                    self.cur_inpt=self.cur_inpt+inp
                    continue
                elif str(repr(inp)) == "KEY_ENTER" and len(self.cur_inpt) == len(self.secret_word):
                    break
                    #return cur_inpt
                elif str(repr(inp)) == "KEY_TAB": 
                    #cur_inpt=get_word()
                    self.cur_inpt=self.secret_word
                    continue
                elif repr(inp) == "KEY_BACKSPACE": 
                    self.cur_inpt = self.cur_inpt[:-1]
                    continue

    def animate_fail(self): 
        self.word_by_word(["game", "over"])
        self.word_by_word(["you", "lose"])
        self.word_by_word(["game", "over"], 0.5)
        self.word_by_word(["you", "lose"], 0.5)
        self.word_by_word(["game", "over"], 0.3)
        self.word_by_word(["you", "lose"], 0.3)
        self.word_by_word(["game", "over"], 0.1)
        self.word_by_word(["you", "lose"], 0.1)

    def play(self): 
        while True:
            self.inpt()
            user_input = self.cur_inpt 
            self.guesses.append(user_input)
            if user_input == self.secret_word: 
                os.system('clear')
                self.draw_all()
                text = colored('WINNER WINNER CHICKEN DINNER!', 'red', attrs=['reverse', 'blink'])
                print(text)
                print("\n")
                print(self.reward)
                print("\n\n")
                try:
                    text = colored('Definition of \"'+self.secret_word+"\"\n", 'green')
                    print(text)
                    do = dictionary.meaning(self.secret_word)
                    for k in do.keys(): 
                        print(colored("\t"+k+"\n", 'white', attrs=["underline"]))
                        for d in do[k]: 
                            print("\t\t -"+d)
                            print("\n")

                except: 
                    print("No definition found :( " ) 
                break
                
            elif self.max_guesses <= len(self.guesses):
                self.animate_fail()
                break


