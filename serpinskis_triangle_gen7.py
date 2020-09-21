"""This draws Serpinski's Triangle up to generation 8 with a tricolor gradient."""

__author__ = "730239946"

from turtle import Turtle, tracer, update, colormode, done

colormode(255)

SQRT2: float = (2 ** (1 / 2))
SQRT3: float = (3 ** (1 / 2))
ROOT2OVER2: float = SQRT2 / 2
ROOT3OVERROOT4: float = (3 / 4) ** (1 / 2)
INITIAL_HUE: int = 80
BLUE_CONSTANT: int = 255
COLOR_INCREMENT: int = 40
COLOR_INCREMENT_2: int = 20
INITIAL_X: float = -325
INITIAL_Y: float = -300
ANGLE: int = 120


def main() -> None:
    """Draws a Serpinski's Triangle of generation 7 with a tricolor gradient."""
    me: Turtle = Turtle()
    tracer(0, 0)
    me.speed(100)
    me.hideturtle()
    size: int = 20
    height: float = SQRT3 * size / 2
    x: float = INITIAL_X
    y: float = INITIAL_Y
    red_hue: int = INITIAL_HUE
    green_hue: int = INITIAL_HUE
    reposition(me, x, y)
    me.pencolor(red_hue, green_hue, BLUE_CONSTANT)
    serpinskis_triangle(me, x, y, size)
    i: int = 0
    while i < 3:
        red_hue += COLOR_INCREMENT
        me.pencolor(red_hue, green_hue, BLUE_CONSTANT)
        x += size * 8
        serpinskis_triangle(me, x, y, size)
        i += 1
    i = 0
    while i < 3:
        green_hue += COLOR_INCREMENT
        red_hue -= COLOR_INCREMENT_2
        me.pencolor(red_hue, green_hue, BLUE_CONSTANT)
        y += height * 8
        x -= size * 4
        serpinskis_triangle(me, x, y, size)
        i += 1
    i = 0
    while i < 2:
        green_hue -= COLOR_INCREMENT
        red_hue += COLOR_INCREMENT_2 - COLOR_INCREMENT
        me.pencolor(red_hue, green_hue, BLUE_CONSTANT)
        x -= size * 4
        y -= height * 8
        serpinskis_triangle(me, x, y, size)
        i += 1
    update()
    done()


def reposition(turt: Turtle, x: float, y: float) -> None:
    """Picks up and moves the turtle to a starting point."""
    turt.penup()
    turt.goto(x, y)
    turt.pendown()


def draw_triangle(turt: Turtle, x: float, y: float, size: float, direction: str) -> None:
    """Draws generation 0 of Serpinski's triangle."""
    reposition(turt, x, y)
    i: int = 0
    while i < 3:
        turt.forward(size)
        if direction == "up":
            turt.left(ANGLE)
        if direction == "down":
            turt.left(-ANGLE)
        i += 1


def draw_filled_triangle(turt: Turtle, x: float, y: float, size: float) -> None:
    """Draws a filled upside down equilateral triangle, which we use to for generation 2."""
    turt.begin_fill()
    reposition(turt, x, y)
    i: int = 0
    while i < 3:
        turt.forward(size)
        turt.left(-ANGLE)
        i += 1
    turt.end_fill()


def split_triangle(turt: Turtle, x: float, y: float, size: float) -> None:
    """Draws the change from generation 1 to generation 2 of Serpinski's triangle."""
    height: float = SQRT3 * size / 2
    x += (size / 2)
    y += height
    draw_filled_triangle(turt, x, y, size)
    x -= size
    y -= 2 * height
    draw_filled_triangle(turt, x, y, size)
    x += 2 * size
    draw_filled_triangle(turt, x, y, size)

    
def draw_embedded_triangles(turt: Turtle, x: float, y: float, size: float) -> None:
    """This function draws generations 0, 1 and 2 of Serpinski's Triangle."""
    draw_triangle(turt, x, y, size, "up")
    x += size / 4
    y += (ROOT3OVERROOT4 * size) / 2
    size /= 2
    draw_triangle(turt, x, y, size, "down")
    size /= 2
    split_triangle(turt, x, y, size)
    

def midstep(turt: Turtle, x: float, y: float, size: float) -> None:
    """Draws a Serpinski's Triangle of generation 4."""
    height: float = SQRT3 * size / 2
    i: int = 0
    while i < 4:
        x += size
        draw_embedded_triangles(turt, x, y, size)
        i += 1
    i = 0
    while i < 3:
        x -= size / 2
        y += height
        draw_embedded_triangles(turt, x, y, size)
        i += 1
    i = 0
    while i < 2:
        x -= size / 2
        y -= height
        draw_embedded_triangles(turt, x, y, size,)
        i += 1
   

def serpinskis_triangle(turt: Turtle, x: float, y: float, size: float) -> None:
    """Draws a Serpinski's Triangle of generation 5."""
    height: float = SQRT3 * size / 2
    j: int = 0
    while j < 3:
        if j % 3 == 1:
            x += 4 * size
        if j % 3 == 2:
            x -= 2 * size
            y += 4 * height
        midstep(turt, x, y, size)
        j += 1


if __name__ == "__main__":
    main()
