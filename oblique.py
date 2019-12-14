#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created: Tue Dec 10 21:46:33 2019

@mcarlisle

#  A simple script to print a random message to the screen every few seconds using pygame.
"""

# -------------------------
#  START IMPORT STATEMENTS 
# -------------------------
import pygame
from random import choice
import string
import time
# -------------------------
#   END  IMPORT STATEMENTS
# -------------------------


# ------------------------
#  START GLOBAL VARIABLES 
# ------------------------
SCREEN_SIZE = (640, 480) # pixels
FONT_SIZE   = 36 # pixels
SLEEP_TIME  = 5 # seconds
ALLOWED_CHARS = string.ascii_letters + string.punctuation

# rgb
BLACK = (0, 0, 0)
WHITE = (255, 255, 255) 
GREEN = (0, 255, 0) 
BLUE = (0, 0, 128)
# ------------------------
#   END  GLOBAL VARIABLES 
# ------------------------


# ----------------------------
#  START FUNCTION DEFINITIONS 
# ----------------------------
def random_line(list_to_choose_from):
    return choice(list_to_choose_from)

def rewrite_string(s_in, split=False, words_before_line_break = 3):
    # Input:  a string
    # Output: a string
###    # Output: a list of shorter strings

    # cut off last char if bad
    if s_in[-1] not in ALLOWED_CHARS:
        s_in = s_in[:-1]
    # split into words
    s_split = s_in.split(' ')

    s = u''
    i = 0
    for w in s_split:
        s += w + u' '
        i += 1
        if i == words_before_line_break or s[0] == '-':
            s += u'\n'
            i = 0
    if i > 0:
        s += u'\n'

    if split:
        return s.split('\n')
    else:
        return s

def insert_line_breaks(list_of_str):
    l = ""
    for x in list_of_str:
        l += x + "\n"
    return l

# https://stackoverflow.com/questions/42014195/rendering-text-with-multiple-lines-in-pygame/42015712
def blit_text(surface, text, pos, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text.splitlines()]  
    # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.

# ----------------------------
#   END  FUNCTION DEFINITIONS 
# ----------------------------


# ------------
#  BEGIN MAIN 
# ------------
if __name__ == "__main__":

    pygame.init() 
    display_surface = pygame.display.set_mode(SCREEN_SIZE) 
    pygame.display.set_caption("Oblique Strategies")
#    font = pygame.font.Font('freesansbold.ttf', FONT_SIZE)
    font = pygame.font.Font('OpenSans-Regular-webfont.ttf', FONT_SIZE)

    # Open the file into a list
    with open("oblique.txt", "r") as f:
        oblique = f.readlines()
    # Add line breaks at dashes
    for i in range(len(oblique)):
        # Fit to screen: print only three words per line
        oblique[i] = rewrite_string(oblique[i], False)

    # Clear the screen and print a random message at timed intervals
    while True:
#        text = font.render(random_line(oblique), True, WHITE, BLACK) 
        text = random_line(oblique)
#        textRect = text.get_rect()
#        textRect.center = (SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 2)

        display_surface.fill(BLACK)
#        display_surface.blit(text, textRect) 
        blit_text(display_surface, text, #insert_line_breaks(text), 
            (SCREEN_SIZE[0] // 5, SCREEN_SIZE[1] // 4), font, WHITE)

        for event in pygame.event.get() : 
                if event.type == pygame.QUIT: 
                    pygame.quit() 
                    quit() 
        pygame.display.update()
        time.sleep(SLEEP_TIME)
# ------------
#   END  MAIN 
# ------------