# Makes blue axis be the forward axis, and green arrow the up axis
# so as to use the Unity standard
#
# To use select objects you want to apply, and find 'Apply for Unity'
# in the context menu (press space by default)
#
# By Nothke

bl_info = {
    "name": "Apply for Unity",
    "category": "Object",
}

import bpy
from math import pi
from mathutils import Vector
from mathutils import Matrix

def test_test():
    print("WTF")
    
def look_at(obj, direction):
    rot_quat = direction.to_track_quat('Z', 'Y')

    # assume we're using euler rotation
    obj.rotation_euler = rot_quat.to_euler()
    
    print("Look!")

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
            
            # Remember axes for later
            forward_dir = (obj.matrix_world @ Vector((0,1,0)))
            forward_dir.normalize()
            up_dir = (obj.matrix_world @ Vector((0,0,1)))
            up_dir.normalize()
            right_dir = (obj.matrix_world @ Vector((1,0,0)))
            up_dir.normalize()
            
            print("forward ",forward_dir)
            
            print(obj.rotation_euler)
            
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
            
            rot_mat = Matrix.Rotation(-original_rotation[0], 4, 'X') \
                    @ Matrix.Rotation(original_rotation[1], 4, 'Z') \
                    @ Matrix.Rotation(original_rotation[2], 4, 'Y')
                    
            
                
            #rot_mat = Matrix.
                
                
            #obj.matrix_world = obj.matrix_world @ rot_mat
            #obj.rotation_euler = rot_mat.to_euler()
            
            #forward_dir[1], forward_dir[2] = forward_dir[2], forward_dir[1]
            
            print("forward: ", forward_dir)
            #look_at(obj, forward_dir)
            
            #bpy.ops.transform.rotate(value=0.2, orient_axis='X')
            #bpy.ops.transform.rotate(value=0.2, orient_axis='Y', orient_type='GLOBAL')

            bpy.context.view_layer.update()
            
            #newrot = Matrix.Rotation(-original_rotation[0], 4, (1,0,0))
            #obj.matrix_world @= newrot
            #bpy.context.view_layer.update()
            #obj.matrix_world @= Matrix.Rotation(-original_rotation[1], 4, (0,0,1))
            
            rot[0] -= original_rotation[0]
            rot[1] += original_rotation[1]
            rot[2] += original_rotation[2]
            
            #newrot @= Matrix.Rotation(-original_rotation[1], 4, (0,0,1))
            
            bpy.context.view_layer.update()
            #obj.matrix_world @= Matrix.Rotation(-0.5, 4, 'X')
            #obj.matrix_world @= Matrix.Rotation(-0.5, 4, 'Z')
            #obj.matrix_world @= rot_mat
            
            #rot[0] = pi * original_rotation[0]
            #rot[1] = pi * original_rotation[1]
            #rot[2] = pi * original_rotation[2]
                    
            #bpy.context.object.rotation_euler[0] = 1
            #bpy.context.object.rotation_euler[2] = pi * original_rotation[2]
            
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