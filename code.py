'''
https://github.com/esjmorales/MagTagBu/

MagTag Documentation: https://circuitpython.readthedocs.io/projects/magtag/en/latest/api.html#adafruit-magtag-magtag
'''

import time
import random
import board
import pulseio
from adafruit_magtag.magtag import MagTag
from activity import Activity
import songs
import abc
import colors
import shapes
####################################################

####################################################
if __name__ == "__main__":
    #################
    # Initialize
    magtag = MagTag()
    pwm = pulseio.PWMOut(board.SPEAKER, duty_cycle=0x8000, frequency=100, variable_frequency=True)
    magtag.peripherals.neopixel_disable = True
    #################

    #################
    # Intro
    '''
    magtag.set_background(0xFFFFFF)
    image_path = 'images/logo.bmp'
    magtag.set_background('C3.bmp')
    magtag.refresh()
    time.sleep(1)
    magtag.set_background(0xFFFFFF)
    '''
    #################

    #################
    # add_text
    # Large single letter
    magtag.add_text(
        text_position=(magtag.graphics.display.width // 2 - 10,(magtag.graphics.display.height // 2) - 10),
        text_scale=7,
    )

    # Bottom Menu
    magtag.add_text(
        text_position=(1,magtag.graphics.display.height - 8),
        text_scale=1,
    )

    # Word
    magtag.add_text(
        text_position=(128,(magtag.graphics.display.height // 2) - 5),
        text_scale=3,
    )

    # Long Word
    magtag.add_text(
        text_position=(128,(magtag.graphics.display.height // 2) - 5),
        text_scale=2.5,
    )

    # Middle Large text
    magtag.add_text(
        text_position=(20,(magtag.graphics.display.height // 2) - 5),
        text_scale=2.5,
    )

    # Bottom Menu Upper
    magtag.add_text(
        text_position=(1,magtag.graphics.display.height - 18),
        text_scale=1,
    )

    num_text_boxes = 6
    #################

    #################
    # Main menu selection
    activities = Activity()
    magtag.set_text(activities.button_text("ABCs", "Songs", "Colors", "Shapes"), index=1, auto_refresh=False)
    magtag.set_text("Select an Activity", index=4, auto_refresh=True)
    current_activity = None

    while current_activity is None:
        for i, b in enumerate(magtag.peripherals.buttons):
            if not b.value:
                if i == 0:
                    current_activity = abc.ABC()
                elif i == 1:
                    current_activity = songs.Songs()
                elif i == 2:
                    current_activity = colors.Colors()
                elif i == 3:
                    current_activity = shapes.Shapes()
    #################

    #################
    # Activity runs indefinitely
    current_activity.clear_text_boxes(magtag, num_text_boxes)
    current_activity.main_menu(magtag)

    while True:
        for i, b in enumerate(magtag.peripherals.buttons):
            if not b.value:
                current_activity.action(magtag, i, num_text_boxes, pwm)

    #################