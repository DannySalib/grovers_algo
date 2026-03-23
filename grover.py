'''
Grover's Algorithm

Overview
"https://en.wikipedia.org/wiki/Grover's_algorithm"
"https://www.youtube.com/watch?v=RQWpF2Gb-gU"
 
this one just gives the answer... but i dont like it
"https://www.geeksforgeeks.org/dsa/introduction-to-grovers-algorithm/"

Reading
"https://www.ryanlarose.com/uploads/1/1/5/8/115879647/quic09-dj-algorithm.pdf"
"https://quantum.cloud.ibm.com/learning/en/courses/fundamentals-of-quantum-algorithms/grover-algorithm/grover-algorithm-description"
"https://www.youtube.com/watch?v=hnpjC8WQVrQ&t=708s"

Quantum Oracles
"https://milvus.io/ai-quick-reference/what-is-a-quantum-oracle-and-how-is-it-used-in-algorithms-like-grovers-search"

Intent
1. No vibe coding 
2. Try to implement using qiskit logic gates 

What I learned:
- grover's algo uses the query model of computation
- phase query gates encode a function f into the qbit's state 
- the oracle in Grover’s algorithm marks the correct solution by inverting its amplitude
- ket(-) = H(X(ket(0)))
'''

import sys
import os
import random 
import numpy as np
from qiskit import QuantumCircuit
import time

random.seed(42)

# being strange 
idx = int 
bits = str 

def _Zf(n_qubits: int, y: int): # -> Gate
    # assert 2**n_qubits >= target 
    qc: QuantumCircuit = QuantumCircuit(n_qubits, n_qubits)

    # Make anc = ket(-) [assuming the last bit is anc]
    anc: idx = n_qubits-1
    qc.reset(anc)
    qc.x(anc)
    qc.h(anc)

    ### below is how we encode the key into the qubits 
    ybits: bits = format(y, f"0{n_qubits}b") # fast bit repr
    def flip():
        for i, b in enumerate(ybits):
            if b == "0": continue
            qc.x(i)

    flip()
    qc.mcx(
        control_qubits  = list(range(n_qubits-1)),
        target_qubit    = n_qubits # ancilla which is ket(-)
    )
    flip()

    return qc.to_gate(label="Zf")

def grov_search(n_qubits: int, xs: list[int], y: int, f = None) -> int:
    if not f: f = lambda x: x == y # the encode function is what i'll call this

    ###* Why do we need classical bits?
    #* When you measure a qubit in a quantum circuit, its superposition collapses to a classical state—either 0 or 1. This outcome must be recorded somewhere,  and that’s where classical bits come in. Without classical bits, you cannot access or use the results of your quantum computation. 

    # num qbits/classical bits needed for this search is...
    n: int = n_qubits+1 # last bit is ancilla 
    qc: QuantumCircuit = QuantumCircuit(n, n)

    #* The only way to get a true quantum speedup for array search is if the array is stored in QRAM (Quantum RAM) — a physical quantum device that can load arr[x] into a quantum register in superposition without classical iteration. Hence how this version is slightly slower than a classic search. As seen below, I have to make the circit classically, which is O(n), making grov_search O(n^3/2)

    for x in xs:
        if not f(x): continue
         # TODO

    # qc.h(range(qr)) # hadamar gate = superpositon 
    
    # What Grover's algorithm does is to search for a string x ∈ Σ^n for which f(x) = 1
    # Needs an oracle to encode this info for each bit 
    
    print(qc)
    return 0

"""
Something important about Grover's search 

Grover's search algo isnt setup like a regular search algo.
Though it's O(N^1/2), it's actually slower than convential search algo (O(N)).
It's setup like this... imagine I asked you for a number between 0 and n-1.
The amount of time for it'd take me to guess all the random nums, would be O(N)
whereas a quantum computer would need O(N^1/2) guesses (it's really good at guessing).
But practically, to interface the quantum computer, it takes O(N^3/2) due to current day's 
hardware constraints.

But, the qsearch is much faster because it needs N^1/2 iterations to encode the key (the number you picked)
into our set of qubits. 
"""
def main(args: list[str]) -> None:
    n_qubits: int = 3
    N: int = 2 ** n_qubits # largest number we can reprsent
    xs: list[int] = [random.randint(0, N-1) for _ in range(N)]
    y: int # target 

    if not args:
        print(f"Usage: python3 {os.path.basename(__file__)} | --random")
        return 

    if args[0] == "--random": 
        y = random.randint(0, N-1)
    else:   
        while True:
            try: y = int(input(f"Pick a number between 0 and {N-1}"))
            except Exception: continue
            if 0 <= y < N: break

    xs[random.randint(0,N-1)] = y # sneak it in randomly 
        
    print(f"Searching for {y} using grover's algorithm in array...") 

    start: float = time.perf_counter()
    yhat: int = grov_search(n_qubits, xs, y)
    end: float = time.perf_counter()
    
    if y == yhat:   print(f"Found your number in {end-start:.2f} seconds")
    else:           print(f"Failed to find your number (took {end-start:.2f} seconds)")

if __name__ == "__main__":
    main(sys.argv[1:])
