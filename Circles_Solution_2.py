from graphics import Canvas
import random

CANVAS_WIDTH = 300
CANVAS_HEIGHT = 300
CIRCLE_SIZE = random.randint(10, 20)
N_CIRCLES = 200
FRAME_THICKNESS = 60.



def main():
    
    random_number = random.randint(1, CANVAS_WIDTH)
    
    my_lovely_painting = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    draw_random_circles(my_lovely_painting)    

def draw_random_circles(some_input_painting):

    for i in range(N_CIRCLES):
        left = random.randint(FRAME_THICKNESS, CANVAS_WIDTH - CIRCLE_SIZE - FRAME_THICKNESS)
        right = left + CIRCLE_SIZE
        top = random.randint(FRAME_THICKNESS, CANVAS_HEIGHT - CIRCLE_SIZE - FRAME_THICKNESS)
        bottom = top + CIRCLE_SIZE
        some_input_painting.create_oval(left, top, right, bottom, color = random_color())


















def random_color():
    """
    This is a function to use to get a random color for each circle. We have
    defined this for you and there is no need to edit code in this function,
    but feel free to read it over if you are interested. 
    """
    colors = ['blue', 'purple', 'salmon', 'lightblue', 'cyan', 'forestgreen']
    return random.choice(colors)



































if __name__ == '__main__':
    main()
