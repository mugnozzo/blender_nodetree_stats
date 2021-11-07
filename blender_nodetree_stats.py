# Author: Alek Mugnozzo
# E-mail: info@mugnozzo.net
# Website: mugnozzo.net
# License: GNU GPLv3.0

import bpy

mat=bpy.data.materials['Material']
nodes=mat.node_tree.nodes
node_struct=[]
stats={
    'nodes':{'tot_nodes':0,'tot_non_group_nodes':0},
    'max_level':0
}

def count_nodes(nodes,lev):
    global stats
    stats['max_level']=max(lev,stats['max_level'])
    for n in nodes:
        for l in range(lev):
            print('-',end='')
        print(n.name)
        try:
            stats['nodes'][n.type]+=1
        except:
            stats['nodes'][n.type]=1
        try:
            new_nodes=n.node_tree.nodes
            count_nodes(new_nodes,lev+1)
        except:
            stats['nodes']['tot_nodes']+=1
            if n.type not in ['GROUP_INPUT','GROUP_OUTPUT','GROUP']:
                stats['nodes']['tot_non_group_nodes']+=1

count_nodes(nodes,0)
print()
print(stats)