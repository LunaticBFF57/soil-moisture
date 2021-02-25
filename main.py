reading = 0
# _______________________________________________________________________________________
# You change all these variables that are in between the lines.
# Set this variable to set the 'sleep' time of the Micro:Bit to save power.
pause2 = 1000
# Make sure this a whole number between 0 and 255.
LED_Light_Level = 255
led.set_brightness(LED_Light_Level)
# _______________________________________________________________________________________

def on_forever():
    global reading
    pins.analog_write_pin(AnalogPin.P1, 1023)
    reading = pins.analog_read_pin(AnalogPin.P0)
    pins.analog_write_pin(AnalogPin.P1, 0)
    led.plot_bar_graph(reading, 1023)
    if input.button_is_pressed(Button.A):
        basic.show_number(reading)
    basic.pause(pause2)
basic.forever(on_forever)
