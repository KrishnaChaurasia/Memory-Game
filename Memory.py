# implementation of card game - Memory

import simplegui
import random


# helper function to initialize globals
def new_game():
    global cards, face_down, turns, state
    turns = 0
    state = 0
    face_down = []
    label.set_text("Turns = "+str(turns))
    face_down = []
    i = 0
    while i < 16:
        face_down.append(True)
        i += 1
    cards = [i % 8 for i in range(16)]
    random.shuffle(cards)
    
# define event handlers
def mouseclick(pos):
    global state, turns, first_move, second_move, face_down
    i = 0
    for card in cards:
        x = i%16
        y = int(i/16)
        if(50*x < pos[0] < 50*(x+1) and 100*y < pos[1] < 100*(y+1)):
            if(face_down[i]):
                face_down[i] = False
                if state == 0:
                    first_move = i
                elif state == 1:
                    second_move = i
                    turns += 1
                    label.set_text("Turns = "+str(turns))
                elif state == 2:
                    if cards[first_move] == cards[second_move]:
                        pass
                    else:
                        face_down[first_move] = True
                        face_down[second_move] = True
                    first_move = i
                    state = 0
                state += 1
        else:
            pass
        i += 1

# cards are logically 50x100 pixels in size    
def draw(canvas):
    global cards
    i = 0
    for card in cards:
        x = i%16
        y = int(i/16)
        if not face_down[i]:
            canvas.draw_text(str(card+1), [x*50+20, y*100+60], 26, "White")
        elif face_down[i]:
            canvas.draw_polygon([(x*50, y*100), ((x+1)*50, y*100), ((x+1)*50, (y+1)*100), (x*50,(y+1)*100)], 2, "White", "Green")
        i+=1

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()

# Always remember to review the grading rubric
