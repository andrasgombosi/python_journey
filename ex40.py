class Song(object):

    def __init__(self,lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

lyrics = ["Happy line1 ", "To youuu", "Line 3 and cake"]

happy_bday = Song(lyrics)


happy_bday.sing_me_a_song()
