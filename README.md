# blender_unity_rotation_fix
Rotation fix for exporting from Blender to Unity

This plugin basically swaps Y and Z axes to be compatible with Unity's orientation, while taking hierarchies and already present rotations into account. This plugin has been created out of need for reliable deeply nested hierarchy fbx exporting, which with standard "Apply Transform" option gets broken at 2nd child. This plugin only deals with rotations and not positions nor scales.

### How to use

This plugin is only compatible with Blender 2.8+ versions.

Warning: This plugin is supposed to also work with multi-selection, but right now it seems to be broken (instead of rotating and unrotating the object, it just applies the rotation in-place). To be safe, perform this action with ONLY ONE active object at a time. This will be fixed in a future update.

Add it through Edit > Preferences > Add-ons. When you install it, it will appear in Object > Apply > Unity Rotation Fix menu. Alternatively you can use the search bar and look for "Apply Unity Rotation Fix".

Important: When exporting fbx, make sure "Apply Transforms" option is OFF, and Apply Scalings is set to "FBX All" (otherwise the root object will have scale of 100x).
