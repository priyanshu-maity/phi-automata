import numpy as np
from typing import Literal


class ElementaryCA:
    def __init__(self, rule: int):
        if not (0 <= rule <= 255):
            raise ValueError("Rule must be an integer between 0 and 255.")

        self.rule = rule
        self.ruleset = self._generate_ruleset()

    def run(
        self,
        width: int,
        steps: int,
        boundary: Literal['periodic', 'fixed'] = 'periodic',
        seed: Literal['single', 'random'] | int | list | np.ndarray = 'single',
    ) -> np.ndarray:
        ...

    def _generate_ruleset(self) -> dict:
        ruleset = {}
        for i in range(8):
            ruleset[i] = (self.rule >> i) & 1
        return ruleset
