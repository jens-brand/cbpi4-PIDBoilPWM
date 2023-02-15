# Craftbeerpi4 Kettle Logic Plugin

## PID Logic with boil threshold and output via PWM

If the target Temperature is above a configurable threshold the PID will be ignored and heater is switched on to the max output value. This is helpful if you use the same kettle for mashing and boiling.

Once the boil threshold temperature is reached, the boil will be done with the max boil output power

This is a fork of cbpi4-PIDBoil[https://github.com/avollkopf/cbpi4-PIDBoil], but this plugin instead calculates the heating and waiting time and directly turns the heater on and off.
Additionally the sampletime can be set to 2, 5, 10, 20 or 30 seconds.

### Installation:

You can install it directly via pypi.org:	
- sudo pip3 install cbpi4-PIDBoilPWM (not yet implemented!) 

Alternativeley you can install (or clone) it from the GIT Repo. In case of updates, you will find them here first:
- sudo pip3 install https://github.com/jens-brand/cbpi4-PIDBoilPWM/archive/main.zip


### Parameters

![PIDBoil Settings](https://github.com/jens-brand/cbpi4-PIDBoilPWM/blob/main/cbpi4-PIDBoil-logic.png?raw=true)

- P - proportional value
- I - integral value
- D - derivative value
- SampleTime - 2, 5, 10, 20 or 30 seconds -> how often the logic calculates the power setting
- max output - heater power which is set above boil threshold
- Boil Threshold - Above this temperature the heater will be set to Max Boil Output Power (default: 98°C / 208F)
- Max Boil Output - Power (%) that is used above Boil Threshold Temperature (default: 100%)

### Changelog

- 15.02.23: (0.0.2) Reintegrated bugfix version 0.0.9 from avollkopf
- 08.09.22: (0.0.1) Initial fork from [https://github.com/avollkopf/cbpi4-PIDBoil]
