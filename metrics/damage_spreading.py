"""
Damage-spreading analysis for elementary cellular automata.

Damage spreading measures the sensitivity of a cellular automaton to
small perturbations in its initial conditions. The experiment begins
with two nearly identical states that differ by a small amount,
typically a single flipped cell. Both states are evolved under the
same rule, and their divergence is measured over time using the
normalized Hamming distance.

Interpretation:

    Ordered systems:
        Perturbations disappear and divergence approaches zero.

    Chaotic systems:
        Perturbations spread rapidly and divergence grows toward a
        non-zero value.

    Critical systems:
        Perturbations neither vanish nor spread uncontrollably,
        producing long-lived intermediate divergence.

Damage-spreading curves provide a simple way to study information
propagation, robustness, and sensitivity to initial conditions in
cellular automata.
"""


import numpy as np
from numpy.typing import NDArray
from typing import Literal

from automata.elementary import ElementaryCA


def compute_damage_spreading_curve(
        rule: int,
        width: int,
        steps: int,
        boundary: Literal['fixed', 'periodic'] = 'periodic',
        trials: int = 100
) -> NDArray:
    """
    Compute the average damage-spreading curve for an elementary
    cellular automaton.

    The experiment begins with a randomly generated state and a
    perturbed copy that differs by a single cell. Both states are
    evolved under the same rule, and the normalized Hamming distance
    between them is measured at every timestep.

    The procedure is repeated across multiple trials, and the
    resulting divergence curves are averaged to reduce the effects
    of random initial conditions.

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
        A one-dimensional NumPy array of length (steps + 1)
        containing the average normalized divergence at each
        timestep.

    Notes:
        The first value of the returned curve corresponds to the
        initial perturbation. For a single flipped cell, this value
        is approximately 1 / width.

        Damage-spreading curves characterize how perturbations evolve
        through time and should not be confused with classical
        Derrida plots, which compare initial and post-update
        divergences across many perturbation sizes.
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
