import matplotlib.pyplot as plt
from typing import Literal

from automata.elementary import ElementaryCA


rule: int = 30
boundary: Literal['fixed', 'periodic'] = 'fixed'
seed: Literal['single', 'random'] = 'single'

ca = ElementaryCA(rule=rule)
history = ca.run(width=101, steps=50, boundary=boundary, seed=seed)

plt.imshow(history, cmap='binary', interpolation='nearest')

plt.title(f'Rule: {rule}  |  Boundary: {boundary}  |  Seed: {seed}\n')
plt.axis('off')

plt.savefig(f'outputs/rule_{rule}_{boundary}_{seed}.png', dpi=300, bbox_inches='tight')
plt.show()
