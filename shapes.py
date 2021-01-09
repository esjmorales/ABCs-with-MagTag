import time
from activity import Activity

class Shapes(Activity):
    '''
    Handles the shapes activity

    Button:
        1 : Square, Rectangle, Trapezoid, Rhombus
        2 : Circle, Oval, Triangle, Diamond
        3 : Heart, Pentagon, Hexagon, Octagon
        4 : Sun, Cresent (Moon), Star, Cloud
    '''

    def __init__(self):
        self._shapes = ['images//shapes1.bmp', 'images//shapes2.bmp', 'images//shapes3.bmp', 'images//shapes4.bmp']
        self._first = True

    def main_menu(self, magtag):
        magtag.set_text(self.button_text("Set 1", "Set 2", "Set 3", "Set 4"), index=1, auto_refresh=False)
        magtag.set_text("Select a Shape", index=4, auto_refresh=True)

    def action(self, magtag, button_value, num_text_boxes, pwm=None):
        '''
        Button value used for the array index
        We only need to clear the 'Select a Shape' text once
        '''
        if self._first:
            magtag.set_text("", index=4, auto_refresh=True)
            self._first = False

        magtag.set_background(self._shapes[button_value])
        magtag.refresh()