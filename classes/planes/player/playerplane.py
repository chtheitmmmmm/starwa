import pygame
from myGametools import mypoint, mySprite
from ...media.frame import frame
from ..parture import hp
from ..parture.weapon import gun, bullet
from .. import plane
from classes.media.audio import plane_audio


class PlayerPlane(plane.Plane):
    DESTORY = 3

    def update(self):
        super().update()
        self.condition_judge()

    def condition_judge(self):
        stage = self.controlcenter.engine.stage
        thisframe = self.frame.thisframe
        Set = self.frame.set_certain
        e = self.controlcenter.engine
        if not self.destoryed:
            if stage == e.STAGE_RIGHT1 and thisframe != 0:
                Set(0, e.RIGHT, True)
            elif stage == e.STAGE_RIGHT2 and thisframe != 1:
                Set(1, e.RIGHT, True)
            elif stage == e.STAGE_RIGHT3 and thisframe != 2:
                Set(2, e.RIGHT, True)
            elif stage == e.STAGE_LEISURE and self.frame.this_code != e.LEISURE:
                Set(0, e.LEISURE, True)
            elif stage == e.STAGE_LEFT1 and thisframe != 0:
                Set(0, e.LEFT, True)
            elif stage == e.STAGE_LEFT2 and thisframe != 1:
                Set(1, e.LEFT, True)
            elif stage == e.STAGE_LEFT3 and thisframe != 2:
                Set(2, e.LEFT, True)

