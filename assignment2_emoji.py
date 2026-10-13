# Assignment 2: Personalized Greeting (emoji)
import emoji

name = input("Enter your name: ")
print("Hello", name, emoji.emojize(":grinning_face_with_big_eyes:"))

activity = input("What is your favorite activity? ")
print("Wow,", activity, "sounds amazing!", emoji.emojize(":star-struck:"))
print("Keep learning Python!", emoji.emojize(":thumbs_up:"))
