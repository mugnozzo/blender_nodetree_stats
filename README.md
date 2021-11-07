# blender_nodetree_stats
This is just a python script to get some stats on nodes in a Blender material nodetree. It counts the nodes, the node types and the max deep level for group nodes.

In this folder you'll find:
- the standalone script in the file blender_nodetree_stats.py;
- a blender file for directly testing it (blender_nodetree_stats.blend) with:
	- a Text Editor window with the script;
	- a Text Editor window with some instructions;
	- a Python Console window;
	- a Shader Editor window with a test material with various levels of nodes and group nodes.

The script will be improved but I wanted to publish it just as it is now.
When executed it will print the stats in the console, so if you ran Blender in a console (eg Bash, Windows Command Prompt, Mac Terminal) the stats will appear there.
Otherwise you'd run the script from the Python Console window within Blender:

	bpy.data.texts['Material Nodetree Stats'].as_module()

If you're using a script in a Blender file other than the test file in this folder, you'll have to replace 'Material Nodetree Stats with the name of the text data-block you copied the script in.

You'll also have to change the material name (3rd line of code in the script) in order to get stats about a material you want to get info about.

It will print a tree-like ASCII representation of the nodes and a python dictionary with all the statistics.

This script is released under the GNU General Public License v3.0 (see the LICENSE file in the same folder of this file).

For any question, suggestion, etc... related to this script you can write to me: info@mugnozzo.net
