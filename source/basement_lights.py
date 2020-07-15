#Basement Lights Control
#RPi3B+
#from gpiozero import OutputDevice, PWMOutputDevice
#from gpiozero.pins.pigpio import PiGPIOFactory
from kivy.app import App
from kivy.uix.slider import Slider
from kivy.uix.button import Button
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget

#BasementLightsPi = PiGPIOFactory(host='192.168.1.40')
#
#Light1Relay = OutputDevice(5, initial_value=None, pin_factory=BasementLightsPi)
#Light1Dim = PWMOutputDevice(12, initial_value=1, pin_factory=BasementLightsPi)
#Light2Relay = OutputDevice(6, initial_value=None, pin_factory=BasementLightsPi)
#Light2Dim = PWMOutputDevice(16, initial_value=1, pin_factory=BasementLightsPi)

class BasementLights(App):
    def build(self):
        return SwitchLayout()

if __name__ == "__main__":
    BasementLights().run()