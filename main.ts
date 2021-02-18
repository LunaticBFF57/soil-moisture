let pause2 = 0
let reading = 0
basic.forever(function () {
    // Set this variable to set the 'sleep' time of the Micro:Bit to save power.
    pause2 = 1000
    pins.analogWritePin(AnalogPin.P1, 1023)
    reading = pins.analogReadPin(AnalogPin.P0)
    pins.analogWritePin(AnalogPin.P1, 0)
    led.plotBarGraph(
    reading,
    1023
    )
    if (input.buttonIsPressed(Button.A)) {
        basic.showNumber(reading)
    }
    basic.pause(pause2)
})
