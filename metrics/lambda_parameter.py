"""
Langton's λ (lambda) parameter.

λ measures the activity density of a cellular automaton rule by calculating
the fraction of rule outputs that are non-quiescent (active).

For elementary cellular automata, the quiescent state is 0 and the active
state is 1. Since each rule contains 8 output states, λ is simply the number
of 1s in the rule table divided by 8.

Examples:
    Rule 0   -> λ = 0.000
    Rule 30  -> λ = 0.500
    Rule 110 -> λ = 0.625
    Rule 255 -> λ = 1.000

References:
    Langton, C. G. (1990). Computation at the edge of chaos.
"""


def compute_lambda(rule: int) -> float:
    """
    Compute Langton's λ for an elementary cellular automaton rule.

    λ is defined as the fraction of active outputs (1s) in the rule's
    8-bit lookup table.

    Args:
       rule: Wolfram rule number in the range [0, 255].

    Returns:
       The λ value as a float in the range [0.0, 1.0].

    Raises:
       ValueError: If the rule number is outside [0, 255].
    """

    if not (0 <= rule <= 255):
        raise ValueError("rule must be an integer between 0 and 255.")

    return rule.bit_count() / 8
