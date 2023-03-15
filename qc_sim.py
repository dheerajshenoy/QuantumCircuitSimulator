from qiskit import *
from qiskit.tools.visualization import plot_bloch_multivector
from qiskit.tools.visualization import plot_histogram

# Creating a circuit with 2 quantum bits and one classical bit
qc = QuantumCircuit(2,1)

# Preparing inputs
qc.x(0) # Comment this line to make Qbit0 = |0>
qc.x(1) # Comment this line to make Qbit1 = |0>
qc.barrier()

# Applying the CNOT gate
qc.cx(0,1)
qc.barrier()

# Measuring Qbit1 and put result to classical bit
qc.measure(1,0)

# Drawing the circuit diagram
qc.draw(output='mpl')

# Run the experimient 1024 times and get stats
counts = execute(qc,Aer.get_backend('qasm_simulator')).result().get_counts()
plot_histogram(counts)
