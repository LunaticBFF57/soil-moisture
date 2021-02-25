let reading = 0
//  _______________________________________________________________________________________
//  You change all these variables that are in between the lines.
//  Set this variable to set the 'sleep' time of the Micro:Bit to save power.
let pause2 = 1000
//  Make sure this a whole number between 0 and 255.
let LED_Light_Level = 255
led.setBrightness(LED_Light_Level)
//  _______________________________________________________________________________________
basic.forever(function on_forever() {
    
    pins.analogWritePin(AnalogPin.P1, 1023)
    reading = pins.analogReadPin(AnalogPin.P0)
    pins.analogWritePin(AnalogPin.P1, 0)
    led.plotBarGraph(reading, 1023)
    if (input.buttonIsPressed(Button.A)) {
        basic.showNumber(reading)
    }
    
    basic.pause(pause2)
})
