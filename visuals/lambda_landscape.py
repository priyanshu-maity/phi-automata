from metrics.lambda_parameter import compute_lambda
import matplotlib.pyplot as plt


def plot_lambda_vs_wolfram_rules() -> None:
    rules = range(256)
    lambdas = [compute_lambda(rule) for rule in rules]

    plt.figure(figsize=(10, 6))
    plt.plot(rules, lambdas, marker='o', linestyle='-', markersize=4)
    plt.title('Lambda Parameter vs. Wolfram Rule Number')
    plt.xlabel('Wolfram Rule Number')
    plt.ylabel('Lambda Parameter')
    plt.xticks(range(0, 256, 15))
    plt.grid()
    plt.show()