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
    for sp in subpaths:
        if len(sp) != 0:
            subgraph = subpath2subgraph(sp_counter,sp)

            sp_counter +=1
        
    
def subpath2subgraph(subpath):
    elements = subpath.split('->')
    elements = elements[1:-1]
    print('\t',elements)



while input_file.readable():
    line = input_file.readline()
    if len(line) == 0:
        break
    print('Analyzing :',line)
    line2graph(line.strip())
    output_file.write(line)



