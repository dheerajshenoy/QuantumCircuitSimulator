from qiskit import *
from qiskit.visualization import *
from qiskit.quantum_info import *
import matplotlib.pyplot as plt
import numpy as np

sim = Aer.get_backend('aer_simulator')
qc = QuantumCircuit(1)

init_state = [1, 0]
qc.initialize(init_state, 0)

plot1 = plot_bloch_multivector(Statevector(qc))
plot1.suptitle("Input")
print(qc.draw())

# Quantum Logic Circuit
qc.x(0) # Not gate

qc.save_statevector()
qobj = assemble(qc)
result = sim.run(qobj).result()

plot2 = plot_bloch_multivector(result.get_statevector())
plot2.suptitle("Output")

# statevec = Statevector(qc)
# iplot = plot_state_qsphere(statevec)
# iplot.suptitle("Input")

# qc.y(0)
# statevec = Statevector(qc)
# fplot = plot_state_qsphere(statevec)
# fplot.suptitle("Output")

plt.show()
