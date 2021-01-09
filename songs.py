import time
from activity import Activity

tones = {'C3': 131, 'D3': 147, 'E3': 165, 'F3': 175, 'G3': 196, 'A3': 220, 'B3': 247,
         'C4': 262, 'D4': 294, 'E4': 330, 'F4': 349, 'G4': 392, 'A4': 440, 'B4': 494,
         'C5': 523, 'D5': 587, 'E5': 659, 'F5': 698, 'G5': 784, 'A5': 880, 'B5': 988}
notes = {'W': 1, 'WD': 1.5, 'H': 0.5, 'HD': 0.75, 'Q': 0.25, 'QD': 0.375, 'E': 0.125, 'ED': 0.1875}


class Songs(Activity):
    '''
    Handles the songs activity
    User can selects 1 of 4 songs:
        Twinkle Twinkle Little Star
        Itsy Bitsy Spider
        Row Row Row Your Boat
        Wheels on the Bus

    Each song is stored in a function which returns a tuple of the song, the pace, and the image location
    for the song

    Once the song is finished, the image is left on the screen. The menu is not shown again

    TO DO: Lower volume
    '''

    def __init__(self):
        super().__init__()

    def main_menu(self, magtag):
        magtag.set_text(self.button_text("Twinkle", "Itsy-Bitsy", "Row-Row", "Wheels"), index=1, auto_refresh=False)
        magtag.set_text("Select a song", index=4, auto_refresh=True)

    def action(self, magtag, button_value, num_text_boxes, pwm=None):
        song, pace, img = self.song_selector(button_value)

        if not song == None:
            magtag.set_background(0xFFFFFF)
            self.clear_text_boxes(magtag, num_text_boxes)
            magtag.set_background(img)
            magtag.refresh()
            time.sleep(1.5)

            for notepair in song:
                pwm.frequency = notepair[0]
                magtag.peripherals.speaker_disable = False
                time.sleep(notepair[1] * pace)
                magtag.peripherals.speaker_disable = True

    def song_selector(self, button_value):
        if button_value == 0:
            return self.twinkle_twinkle()
        elif button_value == 1:
            return self.itsy_bitsy()
        elif button_value == 2:
            return self.row_row()
        elif button_value == 3:
            return self.wheels()
        else:
            return (None, None, None)

    def twinkle_twinkle(self):
        song =  (   # Twinkle Twinkle Little Star
                (tones['C3'], notes['Q']), (tones['C3'], notes['Q']), (tones['G3'], notes['Q']), (tones['G3'], notes['Q']),
                (tones['A3'], notes['Q']), (tones['A3'], notes['Q']), (tones['G3'], notes['H']),
                # How I wonder what you are
                (tones['F3'], notes['Q']), (tones['F3'], notes['Q']), (tones['E3'], notes['Q']), (tones['E3'], notes['Q']),
                (tones['D3'], notes['Q']), (tones['D3'], notes['Q']),(tones['C3'], notes['H']),
                # Up above the world so high
                (tones['G3'], notes['Q']), (tones['G3'], notes['Q']), (tones['F3'], notes['Q']), (tones['F3'], notes['Q']),
                (tones['E3'], notes['Q']), (tones['E3'], notes['Q']),(tones['D3'], notes['H']),
                # Like a diamond in the sky
                (tones['G3'], notes['Q']), (tones['G3'], notes['Q']), (tones['F3'], notes['Q']), (tones['F3'], notes['Q']),
                (tones['E3'], notes['Q']), (tones['E3'], notes['Q']),(tones['D3'], notes['H']),
                # Twinkle Twinkle Little Star
                (tones['C3'], notes['Q']), (tones['C3'], notes['Q']), (tones['G3'], notes['Q']), (tones['G3'], notes['Q']),
                (tones['A3'], notes['Q']), (tones['A3'], notes['Q']), (tones['G3'], notes['H']),
                # How I wonder what you are
                (tones['F3'], notes['Q']), (tones['F3'], notes['Q']), (tones['E3'], notes['Q']), (tones['E3'], notes['Q']),
                (tones['D3'], notes['Q']), (tones['D3'], notes['Q']),(tones['C3'], notes['H'])
                )
        return song, 2, 'images\\twinkle.bmp'

    def itsy_bitsy(self):
        song =  (
                #The itsy-bitsy spider
                (tones['G3'], notes['E']), (tones['C4'], notes['Q']), (tones['C4'], notes['E']), (tones['C4'], notes['Q']),
                (tones['D4'], notes['E']), (tones['E4'], notes['QD']), (tones['E4'], notes['Q']),
                # Climbed up the water spout
                (tones['E4'], notes['E']), (tones['D4'], notes['Q']), (tones['C4'], notes['E']), (tones['D4'], notes['Q']),
                (tones['E4'], notes['E']), (tones['C4'], notes['HD']),
                # Down came the rain
                (tones['E4'], notes['QD']), (tones['E4'], notes['Q']), (tones['F4'], notes['E']), (tones['G4'], notes['QD']),
                # And washed the spider out
                (tones['G4'], notes['QD']), (tones['F4'], notes['Q']), (tones['E4'], notes['E']), (tones['F4'], notes['Q']),
                (tones['G4'], notes['E']), (tones['E4'], notes['HD']),
                # Out came the sun
                (tones['C4'], notes['QD']), (tones['C4'], notes['Q']), (tones['D4'], notes['E']), (tones['E4'], notes['QD']),
                # And dried up all the rain
                (tones['E4'], notes['QD']), (tones['D4'], notes['Q']), (tones['C4'], notes['E']), (tones['D4'], notes['Q']),
                (tones['E4'], notes['E']),  (tones['C4'], notes['QD']),
                # And the itsy-bitsy spider
                (tones['G3'], notes['Q']),
                (tones['G3'], notes['E']), (tones['C4'], notes['Q']), (tones['C4'], notes['E']), (tones['C4'], notes['Q']),
                (tones['D4'], notes['E']), (tones['E4'], notes['QD']), (tones['E4'], notes['Q']),
                # Climbed up the spout again
                (tones['E4'], notes['E']), (tones['D4'], notes['Q']), (tones['C4'], notes['E']), (tones['D4'], notes['Q']),
                (tones['E4'], notes['E']), (tones['C4'], notes['QD'])
                )
        return song, 1.5, 'images\\spider.bmp'

    def row_row(self):
        song =  [
                # Row row row your boat
                (tones['C4'], notes['QD']), (tones['C4'], notes['QD']), (tones['C4'], notes['Q']), (tones['D4'], notes['E']),
                (tones['E4'], notes['QD']),
                # Gently down the stream
                (tones['E4'], notes['Q']), (tones['D4'], notes['E']), (tones['E4'], notes['Q']), (tones['F4'], notes['E']),
                (tones['G4'], notes['HD']),
                # Merily merily merily merily
                (tones['C5'], notes['E']), (tones['C5'], notes['E']), (tones['C5'], notes['E']),
                (tones['G4'], notes['E']), (tones['G4'], notes['E']), (tones['G4'], notes['E']),
                (tones['E4'], notes['E']), (tones['E4'], notes['E']), (tones['E4'], notes['E']),
                (tones['C4'], notes['E']), (tones['C4'], notes['E']), (tones['C4'], notes['E']),
                # Life is but a dream
                (tones['G4'], notes['Q']), (tones['F4'], notes['E']), (tones['E4'], notes['Q']),
                (tones['D4'], notes['E']), (tones['C4'], notes['HD']),
                ]
        song.extend(song)
        return song, 1.5, 'images\\row.bmp'

    def wheels(self):
        song =  (
                # The wheels on the bus go
                (tones['C3'], notes['Q']), (tones['F3'], notes['Q']), (tones['F3'], notes['E']), (tones['F3'], notes['E']),
                (tones['F3'], notes['Q']), (tones['A3'], notes['Q']),
                # Round and round
                (tones['C4'], notes['Q']), (tones['A3'], notes['Q']), (tones['F3'], notes['H']),
                # Round and round
                (tones['G3'], notes['Q']), (tones['E3'], notes['Q']), (tones['C3'], notes['H']),
                # Round and round
                (tones['C4'], notes['Q']), (tones['A3'], notes['Q']), (tones['F3'], notes['Q']),
                # The wheels on the bus go
                (tones['C3'], notes['Q']), (tones['F3'], notes['Q']), (tones['F3'], notes['E']), (tones['F3'], notes['E']),
                (tones['F3'], notes['Q']), (tones['A3'], notes['Q']),
                # Round and round
                (tones['C4'], notes['Q']), (tones['A3'], notes['Q']), (tones['F3'], notes['H']),
                # All  through the town
                (tones['G3'], notes['H']), (tones['C3'], notes['QD']), (tones['C3'], notes['E']), (tones['F3'], notes['HD'])
                )

        return song, 1.6, 'images\\schoolbus.bmp'