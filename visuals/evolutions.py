import matplotlib.pyplot as plt
from numpy.typing import NDArray


def plot_evolution(
        history: NDArray,
        title: str = '',
) -> None:
    plt.figure(figsize=(8, 8))
    plt.imshow(history, cmap='binary', interpolation='nearest', aspect='auto')

    if title:
        plt.title(title)

    plt.axis('off')
    plt.show()
