# Name:         Blender Nodetree Stats
# Author:       Alek Mugnozzo
# Version:      1.0.0
# E-mail:       info@mugnozzo.net
# Website:      mugnozzo.net
# License:      GNU GPLv3.0
# Hosted at:    https://github.com/mugnozzo/blender_nodetree_stats

import bpy

# Replace the material name inside square brackets
# with the material you want to get stats from.
mat=bpy.data.materials['Material']
nodes=mat.node_tree.nodes
node_struct=[]
stats={
    'nodes':{'tot_nodes':0,'tot_non_group_nodes':0},
    'node_types':{},
    'max_level':0
}
lines=[]

def count_nodes(nodes,lev):
    global stats
    stats['max_level']=max(lev,stats['max_level'])
    for n in nodes:
        f=True
        for l in range(lev):
            print('-',end='')
            if f:
                lines.append('-')
                f=False
            else:
                lines[-1]+='-'
        print(n.name)
        if lev>0:
            lines[-1]+=n.name
        else:
            lines.append(n.name)
        try:
            stats['node_types'][n.type]+=1
        except:
            stats['node_types'][n.type]=1
        try:
            new_nodes=n.node_tree.nodes
            count_nodes(new_nodes,lev+1)
        except:
            stats['nodes']['tot_nodes']+=1
            if n.type not in ['GROUP_INPUT','GROUP_OUTPUT','GROUP']:
                stats['nodes']['tot_non_group_nodes']+=1

count_nodes(nodes,0)

def ShowMessageBox(title = "Message Box", icon = 'INFO', lines=""):
    myLines=lines
    def draw(self, context):
        for n in myLines:
            self.layout.label(text=n)
    bpy.context.window_manager.popup_menu(draw, title = title, icon = icon)

lines.append("")
lines.append("NODES: "+str(stats['nodes']['tot_nodes']))
lines.append("NON GROUP NODES: "+str(stats['nodes']['tot_non_group_nodes']))
lines.append("MAX LEVEL: "+str(stats['max_level']))
lines.append("")
lines.append("NUMBER OF NODES grouped by NODE TYPE")
for k,v in stats['node_types'].items():
    lines.append(k+": "+str(v))
lines.append(str(stats))

ShowMessageBox("Nodes stats",lines=lines,icon="INFO")
