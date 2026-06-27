import turtle
import pandas
correct_states=0
correct_guesses=[]
screen = turtle.Screen()
screen.title("U.S States Game")


image="blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
data=pandas.read_csv("50_states.csv")
states=data.state.to_list()

game_on=True
while game_on:


    answer_state=screen.textinput(title =f"{correct_states}/50 Guess the State",prompt="What's another state's name?").title()
    if  answer_state.lower() == "exit":
        game_on = False
        missing_states=[state for state in states if state not in  correct_guesses]
        # missing_states=[]
        # for state in states:
        #     if state not in correct_guesses:
        #         missing_states.append(state)
        new_data=pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")

        break

    if answer_state in states:
        if answer_state not in correct_guesses:
            correct_states+=1
        correct_guesses.append(answer_state)


        turtle_state=turtle.Turtle()
        turtle_state.hideturtle()

        new_state=data[data.state == answer_state]


        turtle_state.penup()


        turtle_state.goto(new_state.x.item(),new_state.y.item())
        turtle_state.write(answer_state)

    if correct_states == 49:
        game_on = False



