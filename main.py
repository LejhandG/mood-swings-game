#Importing the random module which basically helps choose/generate random choices/values
import random
#Importing the time module for the timer
import time
#Importing turtle for the whole graphics part of the game
from turtle import Turtle, Screen

#Setting colors of the ball. Each of them represent a mood
#Red - Angry
#Blue - Sad
#Yellow = Happy
COLORS = ["red", "blue", "yellow"]
#This is the speed of the balls falling from the sky
STARTING_MOVE_DISTANCE = 8
#This is how many pixels forward they will move
MOVE_INCREMENT = 10
#This is the 60 seconds = 1 minute timer
GAME_TIME = 60
#If the sad/angry exceeds this threshold it ends the game
MOOD_THRESHOLD = 80

#We making a class to handle all the falling objects functions/variables
class Moods_Fall:
    #Constructor creation
    def __init__(self):
        #Creating an array which will store each of the object falling from the sky
        self.all_moods = []
        #Setting speed of the objects
        self.move_speed = STARTING_MOVE_DISTANCE
        #Setting the levels i.e mood counter
        self.mood_levels = {
            "angry": 0,
            "sad": 0,
            "happy": 0
        }
        
        #Calling the function which will display the mood meter
        self.setup_mood_meter()
        
        #Calling the function which will set all the displayes
        self.setup_displays()
        
        # Set up the minute timer using the minute moduke
        self.time_left = GAME_TIME
        self.last_time = time.time()
        
        #Updates the time by clearing the old time and updating the new one
        self.update_displays()

#Setting up the mood counter meter
    def setup_mood_meter(self):
        #Create object turtle
        self.mood_meter = Turtle()
        #Hide the turtle for a while so isn't seeing moving
        self.mood_meter.hideturtle()
        #No lines are drawn while moving
        self.mood_meter.penup()
        #The object goes to x=-600, y=300
        self.mood_meter.goto(-600, 300)

    def setup_displays(self):
        # Initializing object for timer
        self.timer_display = Turtle()
        self.timer_display.hideturtle()
        self.timer_display.penup()
        self.timer_display.goto(600, 300)
        
        # Initializing object for score
        self.score_display = Turtle()
        self.score_display.hideturtle()
        self.score_display.penup()
        self.score_display.goto(600, 270)
        #Score counter variable
        self.score = 0


    def update_mood_meter(self):
        #Clears the previous score so that it can update
        self.mood_meter.clear()
        #Starting position of the moods label
        x_pos = -600
        #Loop through all of the mood lable items
        for mood, level in self.mood_levels.items():
            color = {"angry": "red", "sad": "blue", "happy": "yellow"}[mood]
            self.mood_meter.goto(x_pos, 300)
            self.mood_meter.color(color)
            self.mood_meter.write(f"{mood.title()}: {level}%", 
                                font=("Arial", 16, "normal"))
            # Draw mood bar
            self.mood_meter.goto(x_pos, 280)
            self.mood_meter.pendown()
            self.mood_meter.setheading(0)
            self.mood_meter.forward(level)
            self.mood_meter.penup()
            # Increased spacing between moods
            x_pos += 400  

    def update_displays(self):
        #Update the mood meter
        self.update_mood_meter()
        # Update the timer by clearing and rewriting
        self.timer_display.clear()
        #Add timer text
        self.timer_display.write(f"Time Left: {self.time_left}s", 
                               align="right", 
                               font=("Arial", 16, "normal"))
        # Update score
        self.score_display.clear()
        self.score_display.write(f"Score: {self.score}", 
                               align="right", 
                               font=("Arial", 16, "normal"))

#This will create the object which will fall from the sky
    def create_moods(self):
        random_chance = random.randint(1, 8)
        if random_chance == 1:
            mood = Turtle("circle")
            color = random.choice(COLORS)
            mood.color(color)
            mood.penup()
            mood.goto(random.randint(-600, 600), 360)
            mood.setheading(270)
            self.all_moods.append(mood)

#This will move the moods from top to bottom (all of the according to the array)
    def move_moods(self):
        #Loop through all of the objects and move them all
        for mood in self.all_moods[:]:
            mood.forward(self.move_speed)
            #If the object hits the bottom of the screen remove it from the array
            if mood.ycor() < -360:
                mood.hideturtle()
                self.all_moods.remove(mood)

#Checks if the moods are in extreme or limit
    def check_game_over(self):
        return (self.mood_levels["angry"] >= MOOD_THRESHOLD or 
                self.mood_levels["sad"] >= MOOD_THRESHOLD)

#If the moods are in control i.e angry and sad and not crossing the limit
    def check_win(self):
        return (self.mood_levels["angry"] < MOOD_THRESHOLD and 
                self.mood_levels["sad"] < MOOD_THRESHOLD)

#Checks whether the blob has collected the mood or not
    def handle_collision(self, mood, blob):
        color = mood.pencolor()
        
        #If the blob collects red circle the anger level increases by 15
        #And happy level decreases by 5
        if color == "red":  # Angry
            self.mood_levels["angry"] = min(100, self.mood_levels["angry"] + 15)
            self.mood_levels["happy"] = max(0, self.mood_levels["happy"] - 5)
        #If the blob collects blue circle the sad level increases by 15
        #And happy level decreases by 10
        elif color == "blue":  # Sad
            self.mood_levels["sad"] = min(100, self.mood_levels["sad"] + 15)
            self.mood_levels["happy"] = max(0, self.mood_levels["happy"] - 10)
        #If the blob collects yello circle the happy level increases by 15
        #And sad level decreases by 5
        #And the angry level decreases by 5
        elif color == "yellow":  # Happy
            self.mood_levels["happy"] = min(100, self.mood_levels["happy"] + 15)
            self.mood_levels["sad"] = max(0, self.mood_levels["sad"] - 10)
            self.mood_levels["angry"] = max(0, self.mood_levels["angry"] - 5)

        # Update blob appearance based on dominant mood
        dominant_mood = max(self.mood_levels.items(), key=lambda x: x[1])
        if dominant_mood[1] >= 60:
            #If the anger level is more than 60 change to angry emoji
            if dominant_mood[0] == "angry":
                blob.shape(sad_emoji)
            #If the anger sad is more than 60 change to sad emoji
            elif dominant_mood[0] == "sad":
                blob.shape(neutral_emoji)
            #If the happy level is more than 60 change to happy emoji
            elif dominant_mood[0] == "happy":
                blob.shape(happy_emoji)

        # Update score if collected any mood
        self.score += 10
        
        # Remove the collected mood
        mood.hideturtle()
        self.all_moods.remove(mood)
        
        # Update displays
        self.update_displays()

#Keep updating the timer
    def update_timer(self):
        current_time = time.time()
        if current_time - self.last_time >= 1:
            self.time_left -= 1
            self.last_time = current_time
            self.update_displays()
        return self.time_left <= 0

#Displays the label of game over
def display_game_over(screen, win=False):
    game_over = Turtle()
    game_over.hideturtle()
    game_over.penup()
    game_over.goto(0, 0)
    #If you maintain an emotional balance it will display the below message
    if win:
        message = "You Won!\nYou maintained emotional balance!"
        color = "green"
    #If you dont maintain an emotional balance it will display the below message
    else:
        message = "Game Over!\nEmotions got too extreme!"
        color = "red"
    game_over.color(color)
    game_over.write(message, align="center", font=("Arial", 30, "bold"))


#Now calling the main function
def main():
    screen = Screen()
    #Changing the background picture of the scree
    screen.bgpic(picname="background.gif")
    #Setting the screen height and width
    screen.setup(width=1280, height=720)
    #Setting the screen title
    screen.title("Mood Swings")
    #Hides the animations
    screen.tracer(0)

    #Adding the sad, happy and neutral emoji
    global sad_emoji, neutral_emoji, happy_emoji
    sad_emoji = r"C:\Users\bdhru\Downloads\Mood Swings\sad_emoji.gif"
    neutral_emoji = r"C:\Users\bdhru\Downloads\Mood Swings\neutral_emoji.gif"
    happy_emoji = r"C:\Users\bdhru\Downloads\Mood Swings\happy_emoji.gif"

    screen.addshape(sad_emoji)
    screen.addshape(neutral_emoji)
    screen.addshape(happy_emoji)

    blob = Turtle(shape=happy_emoji)
    blob.shapesize(3, 3, 1)
    blob.penup()
    blob.goto(x=0, y=-230)

    #calling the class
    moodManager = Moods_Fall()

    #initializing move left method
    def left_fun():
        new_x = blob.xcor() - 20
        if new_x > -620:
            blob.goto(new_x, blob.ycor())

    #initializing the move right method
    def right_fun():
        new_x = blob.xcor() + 20
        if new_x < 620:
            blob.goto(new_x, blob.ycor())

    #Event listener. Sees which button is clicked
    screen.listen()
    screen.onkey(key="a", fun=left_fun)
    screen.onkey(key="d", fun=right_fun)

    #Is the main loop which keeps the game running
    game_is_on = True
    while game_is_on:
        time.sleep(0.05)
        screen.update()
        
        moodManager.create_moods()
        moodManager.move_moods()

        # Check for collisions. If the blob and object are between 50 pixel range then it updates the mood
        for mood in moodManager.all_moods[:]:
            if mood.distance(blob) < 50:
                moodManager.handle_collision(mood, blob)

        # Check for game over conditions
        if moodManager.check_game_over():
            game_is_on = False
            display_game_over(screen, win=False)
        elif moodManager.update_timer():
            game_is_on = False
            if moodManager.check_win():
                display_game_over(screen, win=True)
            else:
                display_game_over(screen, win=False)

    screen.exitonclick()

#Run the file if the file name is main.py
if __name__ == "__main__":
    main()
