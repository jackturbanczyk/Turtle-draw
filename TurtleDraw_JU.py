import turtle
import math


screen = turtle.Screen()
screen.title("Turtle Drawing Application")
screen.setup(width=450, height=450)


draw_turtle = turtle.Turtle()
draw_turtle.speed(9) 
draw_turtle.penup() 

total_distance = 0.0
previous_point = None  

def calculate_distance(point1, point2):
    """Calculate Euclidean distance between two points."""
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

def display_total_distance():
    """Display the total distance at the bottom right corner of the screen."""
    draw_turtle.penup()
    draw_turtle.goto(250, -350)  
    draw_turtle.color("blue")
    draw_turtle.write(f"Total distance = {total_distance:.2f}", align="left", font=("Arial", 10, "normal"))
    draw_turtle.color("black")  

file_name = input("Enter the name of the input file: ")

try:
    with open(file_name, "r") as file:
        for line in file:
            line = line.strip() 
            if line.lower() == "stop":
                # Lift pen on stop 
                draw_turtle.penup()
                previous_point = None  
            else:
                
                parts = line.split()
                if len(parts) < 2:
                    continue  
                
               #color
                try:
                    x, y = int(parts[1]), int(parts[2])
                    color = parts[0]
                except ValueError:
                    continue #skiping bad cordanates
                
             
                draw_turtle.pencolor(color)
                draw_turtle.goto(x, y)
                
                if previous_point:
                    draw_turtle.pendown()
                    total_distance += calculate_distance(previous_point, (x, y))
                else:
                    draw_turtle.penup()  
                previous_point = (x, y)
    
    display_total_distance()

    #exit instruction 
    draw_turtle.penup()
    draw_turtle.goto(-220, -220)
    draw_turtle.color("red")
    draw_turtle.write("Click the X button to exit.", align="left", font=("Arial", 12, "bold"))
    screen.mainloop()

except FileNotFoundError:
    print(f"Error: File '{file_name}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")


turtle.done()
