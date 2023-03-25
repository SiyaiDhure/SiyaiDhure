import bge
from bge import *
from mathutils import *

class drone(bge.types.KX_PythonComponent):

    args = {
        'FL_PROP': '',
        'FR_PROP': '',
        'BL_PROP': '',
        'BR_PROP': '',
        'FL_Controller': '',
        'FR_Controller': '',
        'BL_Controller': '',
        'BR_Controller': '',
        'BODY': '',
        'prop_mass': float(),
        'body_mass': float(),
        'Prop speed': float(),
        'Force' : float()
    }

    def start(self, args):

        scene = bge.logic.getCurrentScene()
        prefarbs = scene.objects

        self.BODY    = prefarbs[args['BODY']]

        self.prop_mass = args['prop_mass']
        self.body_mass = args['body_mass']
        self.prop_rotation_speed = args['Prop speed']
        self.force = args['Force']

        self.props = [
            prefarbs[args['FL_PROP']],
            prefarbs[args['FR_PROP']],
            prefarbs[args['BL_PROP']],
            prefarbs[args['BR_PROP']]
        ]

        self.prop_controller = [
            prefarbs[args['FL_Controller']],
            prefarbs[args['FR_Controller']],
            prefarbs[args['BL_Controller']],
            prefarbs[args['BR_Controller']]
        ]

        self.physicsId = [

            self.props[0].getPhysicsId(),
            self.props[1].getPhysicsId(),
            self.props[2].getPhysicsId(),
            self.props[3].getPhysicsId(),

        ]

#.................DRONE LOGIC(don't modify !!!)......................................

    def drop(self):
        pass

    def forward(self):
        pass

    def backward():
        pass

    def yaw_clock_wise(self):
        pass

    def yaw_anti_clock_wise(self):
        pass
#....................................................................................
    def update(self):
        p_or_mZ = float(0.02)
        keyboard = logic.keyboard

        up = keyboard.inputs[bge.events.UPARROWKEY]


        active = logic.KX_INPUT_ACTIVE


        rot = self.prop_rotation_speed*logic.deltaTime()
        for p in self.props:
            if p in self.props:
                p.applyRotation([0,0,rot], True)

        
        class assemble_parts():

            global default_parent

            def default_parent(self):
                self.prop_controller[0].worldPosition = self.props[0].worldPosition
                self.prop_controller[1].worldPosition = self.props[1].worldPosition
                self.prop_controller[2].worldPosition = self.props[2].worldPosition
                self.prop_controller[3].worldPosition = self.props[3].worldPosition

                for cont in self.prop_controller:
                    if cont in self.prop_controller:
                        cont.worldPosition.z += p_or_mZ
            default_parent(self)
    

        class drive():
            subZ = 0.02

            global parent
            def parent(self):
                self.props[0].worldPosition = self.prop_controller[0].worldPosition
                self.props[1].worldPosition = self.prop_controller[1].worldPosition
                self.props[2].worldPosition = self.prop_controller[2].worldPosition
                self.props[3].worldPosition = self.prop_controller[3].worldPosition
                

            def lift(self):
                contr = self.prop_controller
                props = self.props
                for _ in contr:
                    if _ in contr:
                        _.applyForce([0,0,self.force], True)
                    for __ in props:
                        if __ in props:
                            parent(self)
                            
            if active in up.status:
                lift(self)
            else:
                default_parent(self)

