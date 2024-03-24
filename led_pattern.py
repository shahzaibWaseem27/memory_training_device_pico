from utime import sleep_ms

def blink_led_pattern(correct_button_presses, each_led_on_duration_ms):

    for led in correct_button_presses:
        led.on()
        sleep_ms(each_led_on_duration_ms)
        led.off()
        sleep_ms(each_led_on_duration_ms)