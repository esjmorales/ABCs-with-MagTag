class Activity:
    '''
    Parent class to all activities to use polymorphism on main loop
    '''

    def __init__(self):
        self._red = (255,0,0)
        self._orange = (255,165,0)
        self._yellow = (255,255,0)
        self._blue = (0,0,255)
        self._green = (0,255,0)
        self._indigo = (111,0,255)
        self._pink = (255,0,127)
        self._white = (255,255,255)
        self._lights_off = True

    def button_text(self, a="", b="", c="", d=""):
        '''
        Used to write text above the buttons
        Assuming the text_scale=1
        '''
        text = " "*2 + a
        text = text + " " * (14-len(text)) + b
        text = text + " " * (26-len(text)) + c
        text = text + " " * (38-len(text)) + d
        text = text + " " * (49-len(text))
        return text

    def clear_text_boxes(self, magtag, num_text_boxes):
        for i in range(0, num_text_boxes):
            magtag.set_text("", index=i, auto_refresh=False)

    def button_lights(self):
        if self._lights_off:
            self._lights_off = False
        else:
            self._lights_off = True

        return self._lights_off

    def main_menu(self, magtag):
        '''
        Display the main menu
        Each activity will have it's own main menu
        '''
        pass

    def action(self, magtag, button_value, num_text_boxes, pwm=None):
        '''
        Corresponding action to each activity
        '''
        pass