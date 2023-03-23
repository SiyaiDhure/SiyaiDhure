import bge
from bge import *
from mathutils import *

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
        'pivot': Vector(),
        'axis': Vector(),
        'balance': float()
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

        self.pivot = args['pivot']
        self.axis  = args['axis']
        self.balance = args['balance']

        self.props = [
            self.FL_PROP, self.FR_PROP, self.BL_PROP,self.BR_PROP
        ]

        self.physicsId = [

            self.BODY.getPhysicsId(),
            self.props[0].getPhysicsId(),
            self.props[1].getPhysicsId(),
            self.props[2].getPhysicsId(),
            self.props[3].getPhysicsId(),

        ]

        class droneParts_assemple():
            
            const = int(1)
            FL_pos   = self.props[0].worldPosition
            FR_pos   = self.props[1].worldPosition
            BL_pos   = self.props[2].worldPosition
            BR_pos   = self.props[3].worldPosition
            
            bge.constraints.createConstraint(
                self.physicsId[0] , self.physicsId[1] , constraint_type = const,
                pivot_x = self.pivot.x , pivot_y = self.pivot.y , pivot_z = self.pivot.z,
                axis_x = self.axis.x , axis_y = self.axis.y , axis_z = self.axis.z, flag = 0
                
                )
            
            bge.constraints.createConstraint(
                self.physicsId[0] , self.physicsId[2] , constraint_type = const,
                pivot_x = self.pivot.x, pivot_y = self.pivot.y, pivot_z = self.pivot.z,
                axis_x = self.axis.x, axis_y = self.axis.y, axis_z = self.axis.z, flag = 0
                )
            
            bge.constraints.createConstraint(
                self.physicsId[0], self.physicsId[3] , constraint_type = const,
                pivot_x = -self.pivot.x, pivot_y = -self.pivot.y, pivot_z = -self.pivot.z,
                axis_x = -self.axis.x, axis_y = -self.axis.y, axis_z = -self.axis.z, flag = 0
                )
            
            bge.constraints.createConstraint(
                self.physicsId[0], self.physicsId[4], constraint_type = const,
                pivot_x = -self.pivot.x, pivot_y = -self.pivot.y, pivot_z = -self.pivot.z,
                axis_x = -self.axis.x, axis_y = -self.axis.y, axis_z = -self.axis.z, flag = 0
                )
            
    def update(self):

        class balance(self):
            self.props[0].applyForce([0,0,self.balance], True)
            self.props[1].applyForce([0,0,self.balance], True)
            self.props[2].applyForce([0,0,self.balance], True)
            self.props[3].applyForce([0,0,self.balance], True)
            bge.constraints.setGravity(0,0,self.body_mass)
