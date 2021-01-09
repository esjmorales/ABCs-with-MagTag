import time
from activity import Activity

class ABC(Activity):
    '''
    Handles the ABCs activity
    Buttons:
        1 - Turn on/off lights
        2 - Reset alphabet back to A
        3 - Previous letter (if at A, we go to Z)
        4 - Next letter (if at Z, we go to A)

    When a letter is selected
        Show the letter
        Show a food item
        Show food item w/ the word
        Show the food item w/ the letter
    '''

    def __init__(self):
        super().__init__()

        self._first = True
        self._alphabet_index = 0
        self._color_index = 1
        self._alphabet = [chr(i) for i in range(ord('A'),ord('Z')+1)]
        self._foods = {   'A' : "Apple", 'B': "Banana", 'C': "Cookie", 'D' : "Doughnut", 'E': "Egg",
                    'F' : "Fries", 'G': "Grapes", 'H': "Honey", 'I': "IceCream", 'J': "Juice",
                    'K' : "Kiwi", 'L' : "Lettuce", 'M': "Milk", 'N': "Noodle", 'O' : "Onigiri",
                    'P' : "Pizza", 'Q' : "Quesadilla", 'R' : "Rice", 'S' : "Strawberry",
                    'T' : "Taco", 'U' : "Uni", 'V': "Vanilla", 'W': "Waffle",
                    'X' : "TrailMix", 'Y' : "Yogurt", 'Z': "Zucchini"
                }
        self._colors = [self._red, self._orange, self._yellow, self._blue, self._green, self._indigo, self._pink, self._white]

    def main_menu(self, magtag):
        '''
        input: Magtag object to call set_text
        The first time we show the main menu, we'll also show the letter A
        The following times, only show the main menu
        '''

        if self._first:
            magtag.set_text(self._alphabet[self._alphabet_index], index=0, auto_refresh=False)
            magtag.set_background("images/"+self._alphabet[self._alphabet_index]+"1.bmp")
            magtag.set_text(self.button_text("Lights", "Reset", "Prev", "Next"), index=1, auto_refresh=True)
            self._first = False
        else:
            magtag.set_text(self.button_text("Lights", "Reset", "Prev", "Next"), index=1, auto_refresh=False)

    def action(self, magtag, button_value, num_text_boxes, pwm=None):
        '''
        Handles the ABCs activity
        Buttons:
            1 - Turn on/off lights
            2 - Reset alphabet back to A, show letter
            3 - Previous letter (if at A, we go to Z), show letter
            4 - Next letter (if at Z, we go to A), show letter
        '''

        color = self._colors[self._alphabet_index%len(self._colors)]

        if button_value == 0:
            magtag.peripherals.neopixel_disable = self.button_lights()
            magtag.peripherals.neopixels.fill(color)
            time.sleep(1)
            return None
        elif button_value == 1:
            self.button_reset()
        elif button_value == 2:
            self.button_prev()
        elif button_value == 3:
            self.button_next()

        if not self._lights_off:
            magtag.peripherals.neopixels.fill(color)

        self.show_letter(magtag)

    def button_next(self):
        self._alphabet_index += 1

        if self._alphabet_index >= len(self._alphabet):
            self._alphabet_index = 0


    def button_prev(self):
        self._alphabet_index -= 1

        if self._alphabet_index < 0:
            self._alphabet_index = len(self._alphabet) - 1

    def button_reset(self):
        self._alphabet_index = 0


    def show_letter(self, magtag):
        '''
        Show the letter
        Show a food item
        Show food item w/ the word
        Show the food item w/ the letter
        '''

        magtag.set_background(0xFFFFFF)
        magtag.set_text("", index=1, auto_refresh=False)
        magtag.set_text(self._alphabet[self._alphabet_index], index=0, auto_refresh=True)
        time.sleep(0.1)

        word = self._foods[self._alphabet[self._alphabet_index]]
        index = 2
        if len(word) > 8:
            index = 3

        try:
            magtag.set_text("", index=0, auto_refresh=False)
            image_path = "images/"+self._alphabet[self._alphabet_index]+"1.bmp"
            magtag.set_background(image_path)
            magtag.set_text(word, index=index, auto_refresh=False)
            magtag.refresh()
            time.sleep(0.2)
        except Exception:
            magtag.set_background(0xFFFFFF)

        self.main_menu(magtag)
        magtag.set_text("", index=2, auto_refresh=False)
        magtag.set_text("", index=3, auto_refresh=False)
        magtag.set_text(self._alphabet[self._alphabet_index], index=0, auto_refresh=True)