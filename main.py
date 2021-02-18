pause2 = 0
reading = 0

def on_forever():
    global pause2, reading
    # Set this to set the "sleep" time to whatever time you desire.
    pause2 = 1000
    pins.analog_write_pin(AnalogPin.P1, 1023)
    reading = pins.analog_read_pin(AnalogPin.P0)
    pins.analog_write_pin(AnalogPin.P1, 0)
    led.plot_bar_graph(reading, 1023)
    if input.button_is_pressed(Button.A):
        basic.show_number(reading)
    basic.pause(pause2)
basic.forever(on_forever)
