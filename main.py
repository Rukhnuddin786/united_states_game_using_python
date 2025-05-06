import turtle
import pandas

screen = turtle.Screen()
screen.title("Us States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
df = pandas.read_csv("50_states.csv")
all_states = df.state.to_list()
guess_states = []

while len(guess_states) < 50:
    answer_states = screen.textinput(title=f"{len(guess_states)}/50 is correct", prompt="What is the another statae ?").title()
    if answer_states == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guess_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        #print(missing_states)
        break
    if answer_states in all_states:
        guess_states.append(answer_states)
        t = turtle.Turtle()
        t.hideturtle()
        #t.penup()
        state_data = df[df.state == answer_states]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_states)

    '''def get_mouse_on_click_cor(x, y):
        print(x, y)
    
    turtle.onscreenclick(get_mouse_on_click_cor)
    turtle.mainloop()'''





screen.exitonclick()

