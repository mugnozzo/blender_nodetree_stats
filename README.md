# blender_nodetree_stats

## Disclaimer
This is just a python script to get some stats on nodes in a Blender material nodetree. It counts the nodes, the node types and the max deep level for group nodes.
It's not user friendly but it's not hard to use.

## What's inside
In this folder you'll find:
- the standalone script in the file blender_nodetree_stats.py;
- a blender file for directly testing it (blender_nodetree_stats.blend) with:
    - a Text Editor window with the script;
    - a Text Editor window with some instructions;
    - a Python Console window;
    - a Shader Editor window with a test material with various levels of nodes and group nodes.

## How it works
The script will be improved but at the moment, when executed, it will print the stats in a message box.

You can run it from the text editor:
- by pressing ALT+P when the mouse cursor is inside the text editor window;
- by pressing the play button on the text editor.

Or you can run it from the Python Console:
```
bpy.data.texts['Material Nodetree Stats'].as_module()
```
in this case, if you're using a script in a Blender file other than the text file in this folder, you'll have to replace 'Material Nodetree Stats' with the name of the text data-block you copied the script in.

You'll also have to change the material name (line 8 of code in the script) in order to get stats about a material you want to get info about.

It will print
- a tree-like ASCII representation of the nodes:
	- the elements in the first tree level are the nodes in the main nodetree at level 0;
	- the elements in the second tree level are the nodes inside groups belonging to level 0;
	- the elements in the third tree level are the nodes inside the groups belonging to level1;
	- and so on...
- and some statistics:
	- the total number of nodes;
	- the number of nodes that are not Group nodes;
	- the maximum group level (0 is the first level);
	- the number of nodes of each type.

## Missing (but planned) features
- It works with materials nodetrees only, unless you change that in the code; I planned to make it work also with Geometry Nodes and Compositing nodetrees.
- The nodetree can be selected changing it in the code; I planned to let the user select the nodetree in a dropdown selector.

This script is released under the GNU General Public License v3.0 (see the LICENSE file in the same folder of this file).

For any question, suggestion, etc... related to this script send me an email at info@mugnozzo.net
