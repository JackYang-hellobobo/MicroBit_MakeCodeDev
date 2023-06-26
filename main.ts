function ButtonGame() {
    while (true) {
        if (input.buttonIsPressed(Button.A)) {
            if (input.buttonIsPressed(Button.A)) {
                basic.showString("A")
                basic.pause(1000)
                basic.clearScreen()
            }
            
        }
        
        if (input.buttonIsPressed(Button.B)) {
            if (input.buttonIsPressed(Button.B)) {
                basic.showString("B")
                basic.pause(1000)
                basic.clearScreen()
            }
            
        }
        
    }
}

function ButtoneCaculate() {
    let A = 0
    let B = 0
    basic.showNumber(A)
    basic.pause(300)
    basic.showNumber(B)
    basic.pause(300)
    basic.clearScreen()
    while (true) {
        if (input.buttonIsPressed(Button.A)) {
            if (input.buttonIsPressed(Button.A)) {
                A += 1
                basic.showString("A=")
                basic.showNumber(A)
                basic.pause(20)
                basic.clearScreen()
            }
            
        }
        
        if (input.buttonIsPressed(Button.B)) {
            if (input.buttonIsPressed(Button.B)) {
                B += 1
                basic.showString("B=")
                basic.showNumber(B)
                basic.pause(20)
                basic.clearScreen()
            }
            
        }
        
    }
}

ButtoneCaculate()
