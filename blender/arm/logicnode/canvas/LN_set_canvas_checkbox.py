from arm.logicnode.arm_nodes import *

class CanvasSetCheckBoxNode(ArmLogicTreeNode):
    """Sets the state of the given UI checkbox."""
    bl_idname = 'LNCanvasSetCheckBoxNode'
    bl_label = 'Set Canvas Checkbox'
    arm_version = 1

    def init(self, context):
        super(CanvasSetCheckBoxNode, self).init(context)
        self.add_input('ArmNodeSocketAction', 'In')
        self.add_input('NodeSocketString', 'Element')
        self.add_input('NodeSocketBool', 'Check')
        self.add_output('ArmNodeSocketAction', 'Out')
