'''
Grover's Algorithm

Overview
"https://en.wikipedia.org/wiki/Grover's_algorithm"
"https://www.youtube.com/watch?v=RQWpF2Gb-gU"
 
this one just gives the answer... 
"https://www.geeksforgeeks.org/dsa/introduction-to-grovers-algorithm/"

Reading
"https://www.ryanlarose.com/uploads/1/1/5/8/115879647/quic09-dj-algorithm.pdf"
"https://quantum.cloud.ibm.com/learning/en/courses/fundamentals-of-quantum-algorithms/grover-algorithm/grover-algorithm-description"

Quantum Oracles
"https://milvus.io/ai-quick-reference/what-is-a-quantum-oracle-and-how-is-it-used-in-algorithms-like-grovers-search"

Intent
1. No vibe coding 
2. Try to implement using qiskit logic gates 

What I learned:
- grover's algo uses the query model of computation
- phase query gates encode a function f into the qbit's state 
- the oracle in Grover’s algorithm marks the correct solution by inverting its amplitude
'''

import sys
import os
import random 
import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister

random.seed(42)

RAN_VALS_SIZE: int = 11

def oracle(qc: QuantumCircuit, i: int) -> None:
    # last bit is ancilla 
    Uf = QuantumCircuit(3)
    pass 

def grov_search(arr: list[int], x: int) -> int:

    # num qbits/classical bits needed for this search is...
    n = int(np.floor(np.log2(len(arr))) + 1)
    print(f'{n = }')

    ###* Why do we need classical bits?
    #* When you measure a qubit in a quantum circuit, its superposition collapses 
    #* to a classical state—either 0 or 1. This outcome must be recorded somewhere, 
    #* and that’s where classical bits come in. Without classical bits, 
    #* you cannot access or use the results of your quantum computation. 

    qr  : QuantumRegister   = QuantumRegister(n)
    cr  : ClassicalRegister = ClassicalRegister(n)
    qc  : QuantumCircuit    = QuantumCircuit(qr, cr)
    [qc.reset(qb) for qb in qc.qubits]
    
    qc.h(qr) # hadamar gate = superpositon 
    
    # What Grover's algorithm does is to search for a string x ∈ Σ^n for which f(x) = 1
    f = lambda xhat: x == xhat
    print(qc)
    
    # TODO create an oracle to encode each bit 


    return 0

def main(args: list[str]) -> None:
    values  : list[int]
    val     : int

    if not args:
        print(f"Usage: python3 {os.path.basename(__file__)} random | <x> <item1> <item2> ...")
        return 
    
    if args[0] == "random": 
        values = [random.randint(0,10000) for _ in range(RAN_VALS_SIZE)]
        val    = values[random.randint(0, len(values)-1)]
    else:                   
        try:
            values = list(map(int, args[1:]))
            val    = int(args[0])
        except Exception:
            print("Could not read search values")
            print(f"Usage: python3 {os.path.basename(__file__)} <val> <item1> <item2> ...")
            return

    print(f"Searching for {val} using grover's algorithm in array...") 
    i: int = grov_search(values, val)

    return

if __name__ == "__main__":
    main(sys.argv[1:])
