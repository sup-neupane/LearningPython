import turtle
import pandas

df = pandas.read_csv("50_states.csv")

screen = turtle.Screen()
screen.title("U.S. States Game")

IMG = "blank_states_img.gif"
screen.addshape(IMG)
turtle.shape(IMG)


all_states = df.state.to_list()
guessed_states=[]


while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
            guessed_states.append(answer_state)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = df[df.state == answer_state]
            t.goto(int(state_data.x), int(state_data.y))
            t.write(answer_state)

    
