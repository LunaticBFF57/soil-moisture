# Config and other stuff that should not be changed.
reading = 0
radio.set_group(69)
# ███████████████████████████████████████████████████████████████████████████████████████████
# You can change all these variables that are in between the lines.
# Set the 'pause2' variable to set the 'delay' time of the Micro:Bit to save power.
pause2 = 100
# Make sure this a whole number between 0 and 255.
LED_Light_Level = 255
led.set_brightness(LED_Light_Level)
# ███████████████████████████████████████████████████████████████████████████████████████████

# Just the script.
# basic.show_string("Moisture Detector")
def on_forever():
    global reading
    pins.analog_write_pin(AnalogPin.P1, 1023)
    reading = pins.analog_read_pin(AnalogPin.P0)
    pins.analog_write_pin(AnalogPin.P1, 0)
    led.plot_bar_graph(reading, 1023)
    if reading < 500:
        basic.show_icon(IconNames.UMBRELLA)
        pins.servo_write_pin(AnalogPin.P2, 0)
        basic.pause(3000)
        pins.servo_write_pin(AnalogPin.P2, 80)
        basic.pause(3000)
        pins.analog_write_pin(AnalogPin.P2, 0)
    if input.button_is_pressed(Button.A):
        basic.show_number(reading)
basic.forever(on_forever)

def on_forever2():
    radio.send_number(reading)
    basic.pause(pause2)
basic.forever(on_forever2)
