import time
from activity import Activity

class Colors(Activity):
    '''
    Handles the colors activity

    Helped with colors: https://rgbcolorcode.com/

    Eight colors, 4 buttons, 2 colors each
    Button:
        1 : Green, Red
        2 : Blue, Orange
        3 : Yellow, Indigo
        4 : Pink, White
    '''

    def __init__(self):
        super().__init__()

        # Button-Index
        self._colors = {'00' : self._red,     '01' : self._green,
                        '10' : self._blue,    '11' : self._orange,
                        '20' : self._yellow,  '21' : self._indigo,
                        '30' : self._white,   '31' : self._pink}

        # Keeps track of which color to show, 2 per button_text
        self._colors_index = [0,0,0,0]

    def main_menu(self, magtag):
        magtag.set_text(self.button_text("Red", "Blue", "Yellow", "White"), index=1, auto_refresh=False)
        magtag.set_text(self.button_text("Green", "Orange", "Indigo", "Pink"), index=5, auto_refresh=False)
        magtag.set_text("Select a Color", index=4, auto_refresh=True)

    def action(self, magtag, button_value, num_text_boxes, pwm=None):
        '''
        Button value increments the index
        Button has two possible colors so we use % 2
        Button_value + Index == key
        '''
        if self._lights_off:
            self._lights_off = False
            magtag.peripherals.neopixel_disable = self._lights_off
        self._colors_index[button_value] += 1
        index = self._colors_index[button_value] % 2
        color = str(button_value) + str(index)
        magtag.peripherals.neopixels.fill(self._colors[color])
        time.sleep(0.3)