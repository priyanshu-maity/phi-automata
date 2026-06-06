import numpy as np
from typing import Literal


class ElementaryCA:
    def __init__(self, rule: int):
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
        ...
