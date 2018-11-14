from random import *
from ex_11 import is_inside

shapes = [
    {
        'text': 'blue',
        'color': '#3F51B5',
        'rect': [20, 60, 100, 100]
    },
    {
        'text': 'red',
        'color': '#C62828',
        'rect': [140, 60, 100, 100]
    },
    {
        'text': 'yellow',
        'color': '#FFD600',
        'rect': [20, 180, 100, 100]
    },
    {
        'text': 'green',
        'color': '#4CAF50',
        'rect': [140, 180, 100, 100]
    }
]


def get_shapes():
    return shapes


def generate_quiz():
    text_list = []
    color_list = []
    for i in shapes:
        text_list.append(i["text"])
        color_list.append(i["color"])
    return [
                choice(text_list),
                choice(color_list),
                randint(0, 1) # 0 : meaning, 1: color
            ]

def mouse_press(x, y, text, color, quiz_type):  
    if quiz_type == 0:
        for i in shapes:
            if i["text"] == text:                
                if is_inside([x, y], i["rect"]) == True:
                    return True
                else:
                    return False
    if quiz_type == 1:
        for i in shapes:
            if i["color"] == color:
                if is_inside([x, y], i["rect"]) == True:
                    return True
                else:
                    return False

