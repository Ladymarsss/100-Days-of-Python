import turtle as t
import random as ra

#USED THIS TO EXTRACT COLORS FROM AN IMAGE (IMAGE.JPG)

# import colorgram

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r 
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

extracted_colors = [(207, 160, 83), (55, 89, 131), (145, 91, 40), (139, 27, 49), (222, 206, 108), (132, 176, 202), (157, 47, 83), (46, 55, 103), (168, 160, 40), (128, 188, 142), (83, 20, 43), (36, 43, 68), (186, 93, 105), (186, 140, 171), (84, 122, 180), (59, 39, 31), (79, 152, 164), (87, 156, 91), (194, 79, 73), (80, 73, 43), (161, 201, 219), (45, 74, 77), (61, 124, 117), (218, 175, 187), (167, 207, 162), (220, 181, 168)]
t.colormode(255)
t.shape("turtle")
t.color("pink")
t.title("Hirst Painting")
t.bgcolor("black")

def random_color():
    color = ra.choice(extracted_colors)
    return color



def random_color():
    color = ra.choice(extracted_colors)
    return color

# Start position (bottom left)
t.penup()
t.setpos(-225, -225)  # Adjust starting position as needed

# Draw 10 rows of 10 dots each
for row in range(10):
    for col in range(10):
        t.color(random_color())
        t.dot(20)
        t.forward(50)
    
    # Move to start of next row
    t.setpos(-225, -225 + (row + 1) * 50)

t.exitonclick()