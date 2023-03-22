import bge
from bge import *

class drone(bge.types.KX_PythonComponent):

    args = {
        'FL_Prop': '',
        'FR_Prop': '',
        'BL_Prop': '',
        'FR_Prop': '',
        'Body': '',
        'prop_rot': float(),
        'prop_mass': float(),

    }

    def start(self, args):

        scene = bge.logic.getCurrentScene()
        prefarbs = scene.objects

        self.FL_Prop = prefarbs[args['FL_Prop']]


    def update(self):
        self.FL_Prop.applyMovement([0.02,0,0], True)
