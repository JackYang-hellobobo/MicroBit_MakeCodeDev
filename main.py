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
ButtonGame()