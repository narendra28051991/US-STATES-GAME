import turtle
import pandas

image = "blank_states_img.gif"
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()
all_states = []

while len(all_states) < 50:
    answer_state = screen.textinput(title=f"{len(all_states)}/50 States correct", prompt="Guess the state: ").title()

    if answer_state == "Exit":
        missing_states = [state for state in states_list if state not in all_states]
        '''
        missing_states = []
        for state in states_list:
            if state not in all_states:
                missing_states.append(state)
        '''
        missing_states_frame = pandas.DataFrame(missing_states)
        missing_states_frame.to_csv("states_to_learn")
        break

    if answer_state in states_list:
        all_states.append(answer_state)
        new_state = data[data.state == answer_state]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(new_state.x), int(new_state.y))
        t.write(answer_state)