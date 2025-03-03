import my_oled
import time

state = 0

while True:
    state += 1
    if state >= 4:
        state = 0

    print("Current State:", state)

    if state == 0:
        text = "This is ground control to Major Tom"
        text_width = len(text) * 6  # Estimate width (6 pixels per character)
        
        for i in range(128,-text_width, -1):  # Scroll left to right
            my_oled.oled.fill(0)  # Clear the screen
            my_oled.print_text(text, i, 0)  # Move text dynamically
            my_oled.oled.show()
            time.sleep(0.00001)  # Adjust scrolling speed

    elif state == 1:
        my_oled.print_text("I'm stepping through the door", 0, 48)  # Bottom row

    elif state == 2:
        my_oled.oled.fill(0)  # Clear the screen
        my_oled.oled.line(0, 63, 127, 0, 1)  # Bottom-left to top-right
        my_oled.oled.show()

    elif state == 3:
        my_oled.oled.fill(0)  # Clear the screen
        my_oled.graphics.fill_rect(64, 32, 64, 32, 1)  # Bottom-right quadrant
        my_oled.oled.show()

    time.sleep(1)

