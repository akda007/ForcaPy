ESC = "\033"

def printf(formatter, *values):
    print(formatter.format(*values), end='')

def cursor_home():
    printf(ESC + "[H")

def cursor_to(x, y):
    printf(ESC + "[{};{}H", x, y)

def cursor_up(x):
    printf(ESC + "[{}A", x)

def cursor_down(x):
    printf(ESC + "[{}B", x)

def cursor_right(x):
    printf(ESC + "[{}C", x)

def cursor_left(x):
    printf(ESC + "[{}D", x)

def cursor_save():
    printf(ESC + "7")

def cursor_load():
    printf(ESC + "8")

def screen_clear():
    printf(ESC + "[2J")

def screen_clear_end():
    printf(ESC + "[0J")

def screen_clear_start():
    printf(ESC + "[1J")

def line_clear_end():
    printf(ESC + "[0K")

def line_clear_start():
    printf(ESC + "[1K")

def line_clear():
    printf(ESC + "[2K")

def clear_home():
    screen_clear()
    cursor_home()