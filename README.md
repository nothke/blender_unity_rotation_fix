# blender_unity_rotation_fix

This plugin basically swaps Y and Z axes to be compatible with Unity's Y-up Z-forward orientation, while taking hierarchies and already present rotations into account.

This plugin has been created out of need for reliable deeply nested hierarchy fbx exporting, which with standard "Apply Transform" option gets broken at 2nd child, while without "Apply Transform" it doesn't swap Y and Z axes.

It also supports multiselection, so you can easily select all objects and apply the fix at once, while not breaking hiararchies. This plugin only deals with rotations and not positions nor scales.

### How to use

This plugin is only compatible with Blender 2.8+ versions.

Add the plugin through Edit > Preferences > Add-ons. When you install it, "Unity Rotation Fix" option will appear in Object > Apply menu (default hotkey: CTRL + A). Alternatively you can also use the search bar and look for "Apply Unity Rotation Fix".

Important: When exporting fbx, make sure that:
- "Apply Scalings" is set to "FBX All" (otherwise the root object will have scale of 100 in Unity), and
- "Apply Transform" option is OFF

![image](docs/fbx_export_properties.png)
