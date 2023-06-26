def ButtonGame():
    while True:
        if input.button_is_pressed(Button.A):
            if input.button_is_pressed(Button.A):
                basic.show_string("A")
                basic.pause(1000)
                basic.clear_screen()
        if input.button_is_pressed(Button.B):
            if input.button_is_pressed(Button.B):
                basic.show_string("B")
                basic.pause(1000)
                basic.clear_screen()



def ButtoneCaculate():
    A = 0
    B = 0
    basic.show_number(A)
    basic.pause(300)
    basic.show_number(B)
    basic.pause(300)
    basic.clear_screen()
    while True:
        if input.button_is_pressed(Button.A):
            if input.button_is_pressed(Button.A):
                A += 1
                basic.show_string("A=")
                basic.show_number(A)
                basic.pause(20)
                basic.clear_screen()
        if input.button_is_pressed(Button.B):
            if input.button_is_pressed(Button.B):
                B += 1
                basic.show_string("B=")
                basic.show_number(B)
                basic.pause(20)
                basic.clear_screen()
        if on_button_pressed    


ButtoneCaculate()