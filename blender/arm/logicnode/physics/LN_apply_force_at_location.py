from arm.logicnode.arm_nodes import *

class ApplyForceAtLocationNode(ArmLogicTreeNode):
    """Applies force in the given rigid body at the given position.

    @seeNode Apply Force
    @seeNode Apply Impulse
    @seeNode Apply Impulse At Location

    @input Force: the force vector
    @input Force On Local Axis: if `true`, interpret the force vector as in
        object space
    @input Location: the location where to apply the force
    @input Location On Local Axis: if `true`, use the location relative
        to the objects location, otherwise use world coordinates
    """
    bl_idname = 'LNApplyForceAtLocationNode'
    bl_label = 'Apply Force At Location'
    arm_section = 'force'
    arm_version = 1

    def init(self, context):
        super(ApplyForceAtLocationNode, self).init(context)
        self.add_input('ArmNodeSocketAction', 'In')
        self.add_input('ArmNodeSocketObject', 'RB')
        self.add_input('NodeSocketVector', 'Force')
        self.add_input('NodeSocketBool', 'Force On Local Axis')
        self.add_input('NodeSocketVector', 'Location')
        self.add_input('NodeSocketBool', 'Location On Local Axis')
        self.add_output('ArmNodeSocketAction', 'Out')
