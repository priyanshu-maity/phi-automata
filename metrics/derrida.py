"""
Derrida plots and damage-spreading analysis.

A Derrida plot measures the sensitivity of a cellular automaton to small
perturbations in its initial conditions.

The experiment begins with two nearly identical states that differ by a
small amount, typically a single flipped cell. Both states are evolved
using the same cellular automaton rule, and their divergence is measured
over time using the normalized Hamming distance.

Interpretation:

    Ordered systems:
        Perturbations disappear and divergence approaches zero.

    Chaotic systems:
        Perturbations spread rapidly and divergence grows toward one.

    Critical systems:
        Perturbations neither vanish nor explode completely, producing
        intermediate divergence and long-lived structure.

Derrida analysis is commonly used to identify regimes of order, chaos,
and criticality in cellular automata and related dynamical systems.
"""


import numpy as np
from numpy.typing import NDArray
from typing import Literal

from automata.elementary import ElementaryCA


def compute_derrida_curve(
        rule: int,
        width: int,
        steps: int,
        boundary: Literal['fixed', 'periodic'] = 'periodic',
        trials: int = 100
) -> NDArray:
    """
    Compute a Derrida curve for an elementary cellular automaton.

    The Derrida experiment evolves two nearly identical initial states
    under the same rule and measures how their divergence changes over
    time. Divergence is computed as the normalized Hamming distance
    between the two states at each timestep.

    Args:
        rule:
            Wolfram rule number in the range [0, 255].

        width:
            Number of cells in the automaton.

        steps:
            Number of timesteps to evolve.

        boundary:
            Boundary condition ('fixed' or 'periodic').

        trials:
            Number of independent perturbation experiments to average.

    Returns:
        A sequence of normalized divergence values, one for each timestep.

    Notes:
        Low divergence indicates ordered behavior, high divergence
        indicates chaotic behavior, and intermediate divergence may
        indicate critical dynamics near the edge of chaos.
    """

    eca = ElementaryCA(rule=rule, boundary=boundary)
    rng = np.random.default_rng()
    accumulated_divergence = np.zeros(shape=steps + 1, dtype=float)

    for trial in range(trials):
        initial_state = eca.generate_state(width=width, seed='random')
        perturbed_state = initial_state.copy()

        perturbation_index = rng.integers(width)
        perturbed_state[perturbation_index] ^= 1

        history = eca.evolve(initial_state, steps=steps)
        pert_history = eca.evolve(perturbed_state, steps=steps)

        accumulated_divergence += np.mean(history != pert_history, axis=1)

    mean_divergence = accumulated_divergence / trials

    return mean_divergence
