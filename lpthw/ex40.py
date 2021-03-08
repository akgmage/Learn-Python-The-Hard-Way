class song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics
     
    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = song(["Happy birthday to you", "I don't want to get sued", "So I'll stop right there"])

bulls_on_parade = song(["They rally around the family", "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

my_sen = ["Hey there!", "How are you doing?", "Shut the the the ", "okay! calm down..."]

okay = song(my_sen)
okay.sing_me_a_song()
