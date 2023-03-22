import bge
from bge import *

class drone(bge.types.KX_PythonComponent):

    args = {
        'FL_PROP': '',
        'FR_PROP': '',
        'BL_PROP': '',
        'BR_PROP': '',
        'BODY': '',
        'prop_rot': float(),
        'prop_mass': float(),
        'body_mass': float(),
    }

    def start(self, args):

        scene = bge.logic.getCurrentScene()
        prefarbs = scene.objects

        self.FL_PROP = prefarbs[args['FL_PROP']]
        self.FR_PROP = prefarbs[args['FR_PROP']]
        self.BL_PROP = prefarbs[args['BL_PROP']]
        self.BR_PROP = prefarbs[args['BR_PROP']]
        self.BODY    = prefarbs[args['BODY']]

        self.prop_rot = args['prop_rot']
        self.prop_mass = args['prop_mass']
        self.body_mass = args['body_mass']

        # Props container

        props = [
            self.FL_PROP, self.FR_PROP, self.BL_PROP,self.BR_PROP
        ]

        # Game Properties
        self.speed = self.object['speed']
        

    def update(self):
        pass
