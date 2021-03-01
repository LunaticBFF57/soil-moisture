//  Config and other stuff that should not be changed. 
let reading = 0
radio.setTransmitSerialNumber(true)
radio.setGroup(4)
//  ______________________________________________________________
//  You can change all these variables that are in between the lines.
//  Set the 'pause2' variable to set the 'sleep' time of the Micro:Bit to save power.
let pause2 = 500
//  If no pause is desired, simply uncomment the comment, according to your respectable coding language.
//  pause2 = 0 # (for Python)
//  let pause2 = 0 // (for JavaScript)
//  Make sure this a whole number between 0 and 255.
let LED_Light_Level = 255
led.setBrightness(LED_Light_Level)
//  _______________________________________________________________
/** 
Coding across multiple goddamn coding languages in a pain the ass honestly.
Damn Example Below:
pause2 = 500
# pause2 = 0 # (for Python)
# let pause2 = 0 // (for JavaScript)

 */
//  Just the script.
basic.forever(function on_forever() {
    
    pins.analogWritePin(AnalogPin.P1, 1023)
    reading = pins.analogReadPin(AnalogPin.P0)
    radio.sendNumber(reading / 4)
    pins.analogWritePin(AnalogPin.P1, 0)
    led.plotBarGraph(reading, 1023)
    if (input.buttonIsPressed(Button.A)) {
        basic.showNumber(reading)
    }
    
    basic.pause(pause2)
})
