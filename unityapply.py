# Makes blue axis be the forward axis, and green arrow the up axis
# so as to use the Unity standard
#
# By Nothke

bl_info = {
    "name": "Unity Rotation Fix",
    "description": "Swaps Y and Z axes to fix rotations for Blender hiararchies and Unity export",
    "author": "Nothke",
    "category": "Object",
    "blender": (2, 80, 0),
    "location": "Object > Apply > Unity Rotation Fix",
}

import bpy
from math import pi
from mathutils import Vector
from mathutils import Matrix

class NOTHKE_OT_unity_rotation_fix(bpy.types.Operator):
    """Fixes rotation (swaps Y and Z axes) for exporting to Unity"""
    bl_idname = "object.unity_rotation_fix"
    bl_label = "Apply Unity Rotation Fix"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):

        original_active_object = context.view_layer.objects.active

        layer = context.view_layer

        for obj in bpy.context.selected_objects:
            layer.objects.active = obj
            
            # Remember original rotation
            rot = obj.rotation_euler
            original_rotation = [rot[0], rot[1], rot[2]]
            
            # Unrotate
            bpy.context.object.rotation_euler = [0, 0, 0]
            
            # First, apply rotation so it's 0,0,0
            bpy.ops.object.transform_apply(location=False, rotation=True, scale=False, properties=False)

            # Then rotate the object so it points 'up'
            rot[0] = pi * 90 / 180
            rot[2] = pi * 180 / 180
            
            # Then apply this rotation, now forward is blue and up is green relative to mesh
            layer.objects.active = obj
            bpy.ops.object.transform_apply(location=False, rotation=True, scale=False, properties=False)
            
            # Finally, return rotation so that it's oriented properly in Blender
            rot[0] = pi * -90 / 180
            rot[1] = pi * -180 / 180
            
            # Apply original rotation
            rot[0] -= original_rotation[0]
            rot[1] += original_rotation[1]
            rot[2] += original_rotation[2]
            
            # Update model matrix
            bpy.context.view_layer.update()
            
            layer.objects.active = None
            
        # You should see no changes in viewport, but blue and green axes have switched and rotations set

        context.view_layer.objects.active = original_active_object

        return {'FINISHED'}

def menu_draw(self, context):
    layout = self.layout
    layout.operator("object.unity_rotation_fix", text="Unity Rotation Fix")

def register():
    bpy.utils.register_class(NOTHKE_OT_unity_rotation_fix)
    bpy.types.VIEW3D_MT_object_apply.append(menu_draw)

def unregister():
    bpy.utils.unregister_class(NOTHKE_OT_unity_rotation_fix)
    bpy.types.VIEW3D_MT_object_apply.remove(menu_draw)

if __name__ == "__main__":
    register()