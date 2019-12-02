#!/usr/bin/python3.6

#################################################
# filename: path2graph.py
# Author: Juan Carlos Gomez (jcki)
# Creation date : 01-12-2019
# Last modification date: 01-12-2019
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

a = ''' 
digraph G {

	subgraph cluster_0 {
		style=filled;
		color=lightgrey;
		node [style=filled,color=white];
		a0 -> a1 -> a2 -> a3;
		label = "process #1";
	}

	subgraph cluster_1 {
		node [style=filled];
		b0 -> b1 -> b2 -> b3;
		label = "process #2";
		color=blue
	}
	start -> a0;
	start -> b0;
	a1 -> b3;
	b2 -> a3;
	a3 -> a0;
	a3 -> end;
	b3 -> end;

	start [shape=Mdiamond];
	end [shape=Msquare];
}'''

def line2graph(line):
    cost = float(line.split(' ')[0])
    path = line.split(' ')[1]
    # Using `O` as the Origin
    subpaths = path.split('O')
    sp_counter = 0

    ''' n90[label = "O",style=filled];
        n91[label = "O",style=filled];
        n92[label = "O",style=filled];'''
    initOs = 'n0[label = "0"]\n'
    clusters = ''
    connections = ''
    for sp in subpaths:
        if len(sp) != 0:
            subgraph,first,last = subpath2subgraph(sp_counter,sp)
            clusters += subgraph
            
            sp_counter +=1
            initOs += 'n{}[label = "0"];\n'.format(sp_counter)
            connections += 'n{} -> {};\n{} -> n{}\n;'.format(sp_counter-1,first,last,sp_counter)

    return 'digraph G {\n' + initOs + clusters + connections + '\n}\n'

        
    
def subpath2subgraph(index,subpath):
    elements = subpath.split('->')
    elements = elements[1:-1]
    basic = '''
        subgraph cluster_{} {{
                style=filled;
                color=lightgrey;
                node [style=filled,color=white];
                {};
                label = "process #1";
        }}\n'''.format(index,' -> '.join(elements))
    return basic,elements[0],elements[-1]



while input_file.readable():
    line = input_file.readline().strip()
    if len(line) == 0:
        break
    # print('Analyzing :',line)
    graph = line2graph(line)
    output_file.write(graph)



