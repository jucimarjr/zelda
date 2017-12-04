from amplifier import Amplifier
from cdplayer import CdPlayer
from dvdplayer import DvdPlayer
from hometheatherfacade import HomeTheatherFacade
from popcornpopper import PopcornPopper
from projector import Projector 
from screen import Screen
from theterlights import TheaterLights
from tuner import Tuner


if __name__ == '__main__':
    # Home Theater Test Drive
    AMP = Amplifier("Top-O-Line Amplifier")
    TUNER = Tuner("Top-O-Line AM/FM Tuner", AMP)
    DVD = DvdPlayer("Top-O-Line DVD Player", AMP)
    CD = CdPlayer("Top-O-Line CD Player", AMP)
    PROJECTOR = Projector("Top-O-Line Projector", DVD)
    LIGHTS = TheaterLights("Theater Ceiling Lights")
    SCREEN = Screen("Theater Screen")
    POPPER = PopcornPopper("Popcorn Popper")

    HOME_THEATER = HomeTheatherFacade(AMP, TUNER, DVD, CD, PROJECTOR, SCREEN,
                                      LIGHTS, POPPER)

    HOME_THEATER.watch_movie("Raiders of the Lost Ark")
    HOME_THEATER.end_movie()