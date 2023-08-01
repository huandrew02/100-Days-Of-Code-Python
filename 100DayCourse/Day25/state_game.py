import turtle
import pandas

def state_location():
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    state_data = data[data.state == guess_state]
    t.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
    t.write(guess_state)

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=725, height=491)
image = "100DayCourse/Day25/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

state_guessed = []
score = 0
data = pandas.read_csv("100DayCourse/Day25/50_states.csv") # type: ignore
states = data.state.to_list()

while len(state_guessed) < 50:
    guess_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?")
    if guess_state == "exit":
        missing_states = [state for state in states if state not in state_guessed]
        new_data = pandas.DataFrame(missing_states).to_csv("100DayCourse/Day25/states_to_learn.csv")
        break    
    if guess_state is not None:
        guess_state = guess_state.title()
        if guess_state in states:
            state_location()
            state_guessed.append(guess_state)
            score += 1













screen.exitonclick()
