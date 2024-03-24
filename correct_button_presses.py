from init_pins import blueLEDPin, yellowLEDPin
from random import randint



def get_correct_button_presses(was_last_attempt_correct: bool, last_led_blink_pattern_length = 3) -> list:

    if was_last_attempt_correct:
        last_led_blink_pattern_length = last_led_blink_pattern_length + 1
    
    correct_button_presses = list()

    while len(correct_button_presses) != last_led_blink_pattern_length:
        this_random_num = randint(0, 1)
        if this_random_num == 0:
            correct_button_presses.append(blueLEDPin)
        else:
            correct_button_presses.append(yellowLEDPin)

    return correct_button_presses