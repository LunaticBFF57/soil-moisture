# Config and other stuff that should not be changed.
reading = 0
radio.set_group(4)

# ______________________________________________________________
# You can change all these variables that are in between the lines.
# Set the 'pause2' variable to set the 'sleep' time of the Micro:Bit to save power.
pause2 = 0
# If no pause is desired, simply uncomment the comment, according to your respectable coding language.
# pause2 = 0 # (for Python)
# let pause2 = 0 // (for JavaScript)
# Make sure this a whole number between 0 and 255.
LED_Light_Level = 255
led.set_brightness(LED_Light_Level)
# _______________________________________________________________


"""
Coding across multiple goddamn coding languages in a pain the ass honestly.
Damn Example Below:
pause2 = 500
# pause2 = 0 # (for Python)
# let pause2 = 0 // (for JavaScript)
"""

# Just the script.
def on_forever():
    global reading
    pins.analog_write_pin(AnalogPin.P1, 1023)
    reading = pins.analog_read_pin(AnalogPin.P0)
    pins.analog_write_pin(AnalogPin.P1, 0)
    led.plot_bar_graph(reading, 1023)
    if reading < 750:
        basic.show_icon(IconNames.UMBRELLA)
        pins.servo_write_pin(AnalogPin.P2, 0)
        basic.pause(3000)
        pins.servo_write_pin(AnalogPin.P2, 80)
        basic.pause(3000)
        pins.analog_write_pin(AnalogPin.P2, 0)
    if input.button_is_pressed(Button.A):
        basic.show_number(reading)
    '''
    # Sends the number to the PC (must be connected to the PC via USB).
    serial.write_value("Water Wetness", reading)
    '''
    basic.pause(pause2)
basic.forever(on_forever)

