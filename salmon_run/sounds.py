import pygame

SONG_END = pygame.USEREVENT + 1 # uh
SFX_END = SONG_END + 1

pygame.mixer.init(48000)

class Main:
    def __init__(self, music):
        self.current_music = music
        self.loopable = False

    def start(self):
        pygame.mixer.music.set_endevent(SONG_END)

        print('loading intro', self.current_music.intro)
        pygame.mixer.music.load(self.current_music.intro)
        pygame.mixer.music.play()
        self.loopable = True

    def switch(self, new_music):
        return

        self.current_music = new_music

        self.loopable = False
        pygame.mixer.music.fadeout(250)
        self.start()

    def on_music_end(self):
        pygame.mixer.music.load(self.current_music.loop)
        pygame.mixer.music.play(-1)
        pass
        # if not self.loopable: return

        # print('looping', self.current_music.loop, self.loopable)
        # pygame.mixer.music.load(self.current_music.loop)
        # pygame.mixer.music.play(100)

    def on_sfx_end(self):
        pygame.mixer.music.set_volume(1.0)

    def fadeout(self):
        pygame.mixer.music.fadeout()

class Music:
    def __init__(self, intro, loop):
        self.intro = intro
        self.loop = loop

class Sound:
    def __init__(self, fname):
        self.effect = pygame.mixer.Sound(fname)

    def play(self):
        pygame.mixer.music.set_volume(0.75)
        channel = self.effect.play()
        channel.set_endevent(SFX_END)

menu_music = Music('./assets/wav/menu-intro.wav', './assets/wav/menu-loop.wav')
level_music = Music('./assets/wav/flowing-intro.wav', './assets/wav/flowing-loop.wav')

pop_fx = Sound('./assets/wav/pop.wav')

testy = Music('./assets/wav/move-fixed.wav', './assets/wav/next-stage-fixed.wav')

music = Main(level_music)
