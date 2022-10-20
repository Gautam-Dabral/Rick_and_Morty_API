# importing modules

import requests
import random
from tkinter import *
from PIL import Image, ImageTk
from character import character
from Scrollable import ScrollableFrame
from url import url


def load_data():
    url_ = random.choice(url)                              # goes to a random page in rickandMorty api

    response = requests.get(url_)                          #recieves response from server
    json_response = response.json()                       #converts into json (equivalent to a dict)
    json_response_result = json_response['results']

    characters = []                                       # initializing characters

    for items in json_response_result:
        name = items['name']
        gender = items['gender']
        species = items['species']
        origin = items['origin']['name']
        status = items['status']
        image_url = items['image']
        number_episodes = len(items['episode'])

        char1 = character(name, gender, species, origin, status, image_url, number_episodes)
        
        characters.append(char1)

    return characters 

characters = load_data()                  # returns characters in the form of a list containing a character object

# creating UI

root = Tk()
root.title('Rick and Morty\nCharacter Data')
root.geometry('600x750')
root.update()
root.resizable()                   # cannot resize len or wid of window 'root'

scroll_bar = ScrollableFrame(root)                  # creating window 'root' to be a scrollable frame
scroll_bar.pack(fill= BOTH, expand= True )

for char in characters:

    # main items frame for each of the characters
    list_item_frame = Frame(scroll_bar.scrollable_frame, border= 4,  relief=GROOVE)

    #left frame
    left_frame = Frame(list_item_frame)
    #load image
    photo = ImageTk.PhotoImage(char.get_image())
    image_label = Label(left_frame, image=photo)
    image_label.image = photo
    image_label.pack(fill= BOTH, expand = True)
    left_frame.grid(row=0, column=0, padx = 7.5, pady = 15)

    #right_frame
    right_frame = Frame(list_item_frame)

    #lables in the right frame

    #name label
    Label(right_frame, text= 'Name: '+char.name, font=('Arial', 11), padx=7.5).pack(anchor = 'w', expand=True)
    #species label
    Label(right_frame, text= 'Species: '+char.species, font=('Arial', 11), padx=7.5).pack(anchor = 'w', expand=True)
    #gender label
    Label(right_frame, text= 'Gender: '+char.gender, font=('Arial', 11), padx=7.5).pack(anchor = 'w', expand=True)
    #origin label
    Label(right_frame, text= 'Origin: '+ char.origin, font=('Arial', 11), padx=7.5).pack(anchor = 'w', expand=True)
    #status label
    Label(right_frame, text= 'Status: '+char.status, font=('Arial', 11), padx=7.5).pack(anchor = 'w', expand=True)
    #episodes label
    Label(right_frame, text= str(char.number_episodes)+ 'Episodes', font=('Arial', 11), padx=7.5).pack(anchor = 'w', expand=True)

    right_frame.grid(row=0, column=1, sticky ='we')

    list_item_frame.pack(fill=X, padx= 7.5)


root.mainloop()               # main loop of UI window , named = root