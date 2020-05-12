# Makes blue axis be the forward axis, and green arrow the up axis
# so as to use the Unity standard
#
# To use select objects you want to apply, and find 'Apply for Unity'
# in the context menu (press space by default)
#
# By Nothke

bl_info = {
    "name": "Unity Rotation Fix",
    "category": "Object",
    "blender": (2, 80, 0)
}

import bpy
from math import pi
from mathutils import Vector
from mathutils import Matrix

class ApplyForUnity(bpy.types.Operator):
    """My Object Moving Script"""      # blender will use this as a tooltip for menu items and buttons.
    bl_idname = "object.apply_unity"        # unique identifier for buttons and menu items to reference.
    bl_label = "Apply for Unity"         # display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # enable undo for the operator.
    
    def execute(self, context):        # execute() is called by blender when running the operator.

        # original_active_object = bpy.context.scene.objects.active
        original_active_object = context.view_layer.objects.active

        for obj in bpy.context.selected_objects:
            context.view_layer.objects.active = obj
            
            # Remember original rotation
            rot = bpy.context.object.rotation_euler
            original_rotation = [rot[0], rot[1], rot[2]]
            
            # Unrotate
            bpy.context.object.rotation_euler = [0, 0, 0]
            
            # First, apply rotation so it's 0,0,0
            bpy.ops.object.transform_apply(location=False, rotation=True, scale=False, properties=False)

            # Then rotate the object so it points 'up'
            rot[0] = pi * 90 / 180
            rot[2] = pi * 180 / 180
            
            # Then apply this rotation, now forward is blue and up is green relative to mesh
            context.view_layer.objects.active = obj
            bpy.ops.object.transform_apply(location=False, rotation=True, scale=False, properties=False)
            
            # Finally, return rotation so that it's oriented properly in Blender
            rot[0] = pi * -90 / 180
            rot[1] = pi * -180 / 180
            
            bpy.context.view_layer.update()
            
            rot[0] -= original_rotation[0]
            rot[1] += original_rotation[1]
            rot[2] += original_rotation[2]
            
            bpy.context.view_layer.update()
            
        # You should see no changes in viewport, but blue and green axes have switched and rotations set

        # bpy.context.scene.objects.active = original_active_object
        context.view_layer.objects.active = original_active_object

        return {'FINISHED'}            # this lets blender know the operator finished successfully.

def register():
    bpy.utils.register_class(ApplyForUnity)


def unregister():
    bpy.utils.unregister_class(ApplyForUnity)


# This allows you to run the script directly from blenders text editor
# to test the addon without having to install it.
if __name__ == "__main__":
    register()