# ABCs with MagTag
Adafruit's MagTag IoT with learning activities for kids coded in CircuitPython.
<br/>Activities include ABCs, Songs, Colors, and Shapes. 
<br/><br/>After receiving AdaBox 017, I was thinking about a project I could do that was age appropriate for my two year old son. He's learning letters, colors, and shapes. Of course he enjoys music, pressing buttons, and lights. All of which the MagTag was capable of doing. Pictures below.<br/>
### Generating Tones
I did have some difficulty with the music. To generate sounds, the sample code that came preloaded in the MagTag used the function <code>magtag.peripherals.play_tone(frequency, duration)</code><br/>
At the time I wrote my code, using this function, the MagTag would not generate more than 4 unique tones per boot. I reached out the AdaFruit discord channel for some help. A thank you to GastroGeek who pointed me to the CircuitPython MagTag source code where I found the issue.
Let's start from the top layer class "peripherals.py" It initializes the speaker with the following code:
```
import board
from digitalio import DigitalInOut, Direction, Pull

speaker_enable = DigitalInOut(board.SPEAKER_ENABLE)
speaker_enable.direction = Direction.OUTPUT
speaker_enable.value = False
```

The function <code>play_tone(self, frequency, duration)</code> is used to play tones:
```
play_tone(self, frequency, duration):
  self._speaker_enable.value = True
  simpleio.tone(board.SPEAKER, frequency, duration)
```

An error was occuring at this point when more than 4 distinct tones were trying to be played. So I dug into simpleio.<br/>
simpleio's <code>tone(pin, frequency, duration=1, length=100)</code> function is being called to generate the tone using the following code, which errors out when more than 4 distinct frequencies are given
```
with pulseio.PWMOut(pin, frequency=int(frequency), variable_frequency=False) as pwm:
            pwm.duty_cycle = 0x8000
            time.sleep(duration)

Error:
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: No more timers available
```


My work around was initializing a single pulseio.PWMOut object with variable frequency, and changing the frequencies as needed. Enabling / disabling the speaker as needed.
```
import time
import pulseio
import board
from digitalio import DigitalInOut, Direction, Pull

# Enable the speaker
speaker_enable = DigitalInOut(board.SPEAKER_ENABLE)
speaker_enable.direction = Direction.OUTPUT
speaker_enable.value = False
pin = board.SPEAKER
pwm = pulseio.PWMOut(pin, duty_cycle=0x8000, frequency=131, variable_frequency=True)

# Play the frequencies 
for i, freq in enumerate([131, 147, 165, 175, 196, 220, 247]):
    if i == 0:
         speaker_enable.value = True
    pwm.frequency = freq
    time.sleep(0.25)

speaker_enable.value = False
pwm.deinit()
```

### Parts & Documentation
Project parts from AdaBox 017: https://learn.adafruit.com/adabox017
<br/>MagTag Documentation: https://circuitpython.readthedocs.io/projects/magtag/en/latest/api.html#adafruit-magtag-magtag
<br/>Requires CircuitPython: https://learn.adafruit.com/welcome-to-circuitpython/installing-circuitpython
<br/><br/>
### Images
Start up menu:<br/>
![alt text](https://github.com/esjmorales/MagTagBu/blob/main/images_readme/001.jpg?raw=true)
<br/><br/>
ABCs:<br/>
![alt text](https://github.com/esjmorales/MagTagBu/blob/main/images_readme/002.jpg?raw=true)
<br/><br/>
Songs (plays music through MagTag speaker):<br/>
![alt text](https://github.com/esjmorales/MagTagBu/blob/main/images_readme/003.jpg?raw=true)
<br/><br/>
Colors:<br/>
![alt text](https://github.com/esjmorales/MagTagBu/blob/main/images_readme/004.jpg?raw=true)
<br/><br/>
Shapes:<br/>
![alt text](https://github.com/esjmorales/MagTagBu/blob/main/images_readme/005.jpg?raw=true)
