import matplotlib.pyplot as plt
from numpy.typing import ArrayLike


def plot_damage_spreading_curve(
    curve: ArrayLike,
    rule: int | None = None,
) -> None:

    plt.plot(curve)

    if rule is not None:
        plt.title(f'Damage-Spreading Curve for Rule {rule}')
    else:
        plt.title('Damage-Spreading Curve')

    plt.xlabel('Timestep')
    plt.ylabel('Average Normalized Divergence')
    plt.grid()
    plt.show()