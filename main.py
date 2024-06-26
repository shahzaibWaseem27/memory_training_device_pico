from utime import ticks_ms, sleep_ms
from machine import Pin
from led_pattern import blink_led_pattern
from init_pins import blueLEDPin, blue_LED_button_pin, yellowLEDPin, yellow_LED_button_pin, greenLEDPin, redLEDPin
from correct_button_presses import get_correct_button_presses


user_button_presses = []
user_pressed_correctly = True


blue_LED_button_debounce_time = 0
is_blue_LED_button_pressed = False

yellow_LED_button_debounce_time = 0
is_yellow_LED_button_pressed = False

def handle_blue_led_button_press(pin):
    global blue_LED_button_debounce_time, is_blue_LED_button_pressed
    if(ticks_ms() - blue_LED_button_debounce_time > 500):
        blue_LED_button_debounce_time = ticks_ms()
        is_blue_LED_button_pressed = True

def handle_yellow_led_button_press(pin):
    global yellow_LED_button_debounce_time, is_yellow_LED_button_pressed
    if(ticks_ms() - yellow_LED_button_debounce_time > 500):
        yellow_LED_button_debounce_time = ticks_ms()
        is_yellow_LED_button_pressed = True


blue_LED_button_pin.irq(trigger=Pin.IRQ_RISING, handler=handle_blue_led_button_press)
yellow_LED_button_pin.irq(trigger=Pin.IRQ_RISING, handler=handle_yellow_led_button_press)


led_on_duration_ms = 700

last_attempt_result = False

correct_button_presses = get_correct_button_presses(last_attempt_result)

while True:
    
    blink_led_pattern(correct_button_presses, led_on_duration_ms, last_attempt_result)

    while(len(user_button_presses) != len(correct_button_presses)):

        if is_blue_LED_button_pressed:
            blueLEDPin.on()
            sleep_ms(led_on_duration_ms)
            blueLEDPin.off()
            user_button_presses.append(blueLEDPin)
            is_blue_LED_button_pressed = False
    
        if is_yellow_LED_button_pressed:
            yellowLEDPin.on()
            sleep_ms(led_on_duration_ms)
            yellowLEDPin.off()
            user_button_presses.append(yellowLEDPin)
            is_yellow_LED_button_pressed = False

    
    for i in range(len(correct_button_presses)):
        if user_button_presses[i] != correct_button_presses[i]:
            user_pressed_correctly = False
            last_attempt_result = False
        
    if user_pressed_correctly:
        last_attempt_result = True
        greenLEDPin.on()
        sleep_ms(3000)
        greenLEDPin.off()
    else:
        redLEDPin.on()
        sleep_ms(3000)
        redLEDPin.off()

    user_button_presses.clear()
    user_pressed_correctly = True

    correct_button_presses = get_correct_button_presses(last_attempt_result, len(correct_button_presses))
    
    led_on_duration_ms = int(0.8 * led_on_duration_ms) if last_attempt_result == True else 700

    sleep_ms(4000)



        
    
    

