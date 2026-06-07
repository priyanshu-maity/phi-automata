import numpy as np
from numpy.typing import NDArray
from typing import Literal

from metrics.lambda_parameter import compute_lambda


class ElementaryCA:
    def __init__(self, rule: int, boundary: Literal['periodic', 'fixed'] = 'fixed'):
        if not (0 <= rule <= 255):
            raise ValueError("rule must be an integer between 0 and 255.")
        if boundary not in ('periodic', 'fixed'):
            raise ValueError("boundary can be either 'fixed' or 'periodic'.")

        self.rule = rule
        self.boundary = boundary
        self.rule_lookup = self._generate_rule_lookup()
        self.lambda_ = compute_lambda(self.rule)

    def run(self, width: int, steps: int, seed: Literal['single', 'random'] = 'single') -> NDArray:
        """
        Simulate an elementary cellular automaton.

        Args:
            width: Number of cells in each generation.
            steps: Number of generations to evolve.
            boundary: Boundary condition ('fixed' or 'periodic').
            seed: Initial state ('single' or 'random').

        Returns:
            A NumPy array of shape (steps + 1, width) containing the
            complete state history, including the initial state.
        """

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
            if self.boundary == 'fixed':
                left = np.zeros_like(state)
                right = np.zeros_like(state)

                left[1:] = state[:-1]
                right[:-1] = state[1:]
            else:
                left = np.roll(state, 1)
                right = np.roll(state, -1)

            neighborhood_codes = 4 * left + 2 * state + right
            state = self.rule_lookup[neighborhood_codes]

            history[step] = state

        return history

    def _generate_rule_lookup(self) -> NDArray:
        rule_lookup = np.zeros(8, dtype=np.uint8)
        for i in range(8):
            rule_lookup[i] = (self.rule >> i) & 1

        return rule_lookup
