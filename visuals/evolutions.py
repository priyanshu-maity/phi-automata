import matplotlib.pyplot as plt
from numpy.typing import NDArray


def plot_evolution(
        history: NDArray,
        title: str = '',
) -> None:
    plt.imshow(history, cmap='binary', interpolation='nearest', aspect='equal')

    if title:
        plt.title(title)

    plt.axis('off')
    plt.show()
