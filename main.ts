//  Config and other stuff that should not be changed.
let reading = 0
radio.setGroup(69)
//  ███████████████████████████████████████████████████████████████████████████████
//  You can change all these variables that are in between the lines.
//  Set the 'pause2' variable to set the 'delay' time of the Micro:Bit to save power.
let pause2 = 100
//  Make sure this a whole number between 0 and 255.
let LED_Light_Level = 255
led.setBrightness(LED_Light_Level)
//  ███████████████████████████████████████████████████████████████████████████████
//  Just the script.
//  basic.show_string("Moisture Detector")
basic.forever(function on_forever() {
    
    pins.analogWritePin(AnalogPin.P1, 1023)
    reading = pins.analogReadPin(AnalogPin.P0)
    pins.analogWritePin(AnalogPin.P1, 0)
    led.plotBarGraph(reading, 1023)
    if (reading < 500) {
        basic.showIcon(IconNames.Umbrella)
        pins.servoWritePin(AnalogPin.P2, 0)
        basic.pause(3000)
        pins.servoWritePin(AnalogPin.P2, 80)
        basic.pause(3000)
        pins.analogWritePin(AnalogPin.P2, 0)
    }
    
    if (input.buttonIsPressed(Button.A)) {
        basic.showNumber(reading)
    }
    
})
basic.forever(function on_forever2() {
    radio.sendNumber(reading)
    basic.pause(pause2)
})
