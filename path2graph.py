#!/usr/bin/python3.6
#################################################
# filename: path2graph.py
# Author: Juan Carlos Gomez (jcki)
# Creation date : 01-12-2019
# Last modification date: 02-12-2019
#################################################


#################################################
# purpose: 
#################################################


import argparse
import sys

parser = argparse.ArgumentParser(description='Process some integers.')

parser.add_argument("-i", "--input", action='store', 
        type=argparse.FileType('r'), dest='input',
        help="Directs the input to a name of your choice",
        default=sys.stdin)

parser.add_argument("-o", "--output", action='store', 
        type=argparse.FileType('w'), dest='output',
        help="Directs the output to a name of your choice",
        default=sys.stdout)

args = parser.parse_args()

input_file = args.input
output_file = args.output


def getColor(path):
    h = hash(path)
    hx = hex(h)
    return hx[-6:]



def line2graph(line):
    cost = float(line.split(' ')[0])
    path = line.split(' ')[1]
    # Using `O` as the Origin
    subpaths = path.split('O')
    sp_counter = 0

    ''' n90[label = "O",style=filled];
        n91[label = "O",style=filled];
        n92[label = "O",style=filled];'''
    initOs = 'n0[label = "O",style=filled]\n'
    clusters = ''
    connections = ''
    for sp in subpaths:
        if len(sp) != 0:
            subgraph,first,last = subpath2subgraph(sp_counter,sp)
            clusters += subgraph
            
            sp_counter +=1
            initOs += 'n{}[label = "O",style=filled];\n'.format(sp_counter)
            connections += 'n{} -> {};\n{} -> n{};\n'.format(sp_counter-1,first,last,sp_counter)

    header = 'digraph G {\nnode[shape=record];\nrankdir="LR"' 
    return header + initOs + clusters + connections + '\n}\n'

        
    
def subpath2subgraph(index,subpath):
    elements = subpath.split('->')
    elements = elements[1:-1]
    basic = '''
        subgraph cluster_{0} {{
                style=filled;
                color="#{2}";
                node [style=filled,color=white];
                {1};
        }}\n'''.format(index,' -> '.join(elements),getColor(subpath))
    return basic,elements[0],elements[-1]



ind = output_file.name.rfind('.')
original_name = output_file.name[:ind]
files = 0
while input_file.readable():
    line = input_file.readline().strip()
    if len(line) == 0:
        break
    # print('Analyzing :',line)
    graph = line2graph(line)
    output_file.write(graph)
    files += 1
    args = parser.parse_args(('-o',original_name+str(files)+'.dot'))
    output_file = args.output




