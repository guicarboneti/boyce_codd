# execute the code by running 
# > python boyce_codd.py <fds.txt>
# where "fds.txt" is the file storing the functional
# dependencies boyce codd will use to find the relations.

# the FDs in the file should be in the format below:
#       B,D->A
#       A,E->B,D
#       A,C->B,D
#       C,D,E->A,B
#       E->A,D

import functional_dependencies as fd
import sys

def parse_input(input_string):
    pairs = input_string.split('\n')
    result = []
    for pair in pairs:
        values = pair.split('->')
        lhs = values[0]
        rhs = values[1]
        result.append([lhs, rhs])
    return result

def createFDList(output):
    for line in output:
        lhs, rhs = line
        lhs_obj = set()
        rhs_obj = set()
        values = lhs.split(',')
        for el in values:
            lhs_obj.add(el)
        values = rhs.split(',')
        for el in values:
            rhs_obj.add(el)
        fdx = fd.FD(lhs_obj, rhs_obj)
        fds_list.append(fdx)
    return fds_list

def flatten_list(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result

with open(sys.argv[1], 'r') as f:
    input_string = f.read()
output = parse_input(input_string)
fds_list = []
fds_list = createFDList(output)

fds = fd.FDSet(fds_list)
R = []
R = fds.attributes()

def violatesBCNF(r, fun_dep, r_key):
    f_set = fd.FDSet({fun_dep})
    dep_attrs = f_set.attributes()-f_set.key()

    if f_set.key().issubset(r) and f_set.key() != r_key:
        for attr in dep_attrs:
            if attr in r:
                return True     # does violate
    return False    # does not violate

def BCNF(R, fds, key):
    decomp = []
    for f in fds:
        if violatesBCNF(R, f, key):
            fs = fd.FDSet({f})
            S1 = []
            S1 = fs.attributes()
            S1_key = fs.key()
            
            S2 = []
            S2 = R-(fs.attributes()-fs.key())
            S2_key = fd.RelSchema(S2, fds).key()

            decomp.append(BCNF(S1, fds, S1_key))
            decomp.append(BCNF(S2, fds, S2_key))
            break

    if not decomp:
        return R
    else: return decomp

Decomposition = []
Decomposition = BCNF(R, fds, fds.key())

fnl_list = []
for obj in flatten_list(Decomposition):
    if obj not in fnl_list:     # remove duplicates
        fnl_list.append(obj)
for obj in fnl_list:
    print("("+", ".join((item) for item in obj)+")")