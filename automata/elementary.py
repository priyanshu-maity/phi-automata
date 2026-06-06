import numpy as np
from typing import Literal


class ElementaryCA:
    def __init__(self, rule: int):
        if not (0 <= rule <= 255):
            raise ValueError("rule must be an integer between 0 and 255.")

        self.rule = rule
        self.rule_lookup = self._generate_rule_lookup()

    def run(
        self,
        width: int,
        steps: int,
        boundary: Literal['periodic', 'fixed'] = 'fixed',
        seed: Literal['single', 'random'] = 'single',
    ) -> np.ndarray:

        if width <= 0:
            raise ValueError("width must be positive")
        if steps <= 0:
            raise ValueError("steps must be positive")

        if seed == 'single':
            state = np.zeros(width, dtype=np.uint8)
            state[width // 2] = 1
        elif seed == 'random':
            state = np.random.randint(0, 2, size=width, dtype=np.uint8)
        else:
            raise ValueError("seed can be either 'single' or 'random'.")

        history = np.empty((steps + 1, width), dtype=state.dtype)
        history[0] = state

        for step in range(1, steps + 1):
            if boundary == 'fixed':
                left = np.zeros_like(state)
                right = np.zeros_like(state)

                left[1:] = state[:-1]
                right[:-1] = state[1:]

            elif boundary == 'periodic':
                left = np.roll(state, 1)
                right = np.roll(state, -1)

            else:
                raise ValueError("boundary can be either 'fixed' or 'periodic'.")

            neighborhood_codes = 4 * left + 2 * state + right
            state = self.rule_lookup[neighborhood_codes]

            history[step] = state

        return history

    def _generate_rule_lookup(self) -> np.ndarray:
        rule_lookup = np.zeros(8, dtype=np.uint8)
        for i in range(8):
            rule_lookup[i] = (self.rule >> i) & 1

        return rule_lookup
