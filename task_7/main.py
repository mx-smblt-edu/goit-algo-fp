import random

import matplotlib.pyplot as plt
import rich
from rich.table import Table


def simulate_dice_rolls(num_rolls):
    frequency = {i: 0 for i in range(2, 13)}
    for _ in range(num_rolls):
        first_cube = random.randint(1, 6)
        second_cube = random.randint(1, 6)
        total = first_cube + second_cube
        frequency[total] += 1

    probabilities = {total: round((count / num_rolls) * 100, 5) for total, count in frequency.items()}
    return probabilities


def plot_probabilities(probabilities):
    sums = list(probabilities.keys())
    probabilities = list(probabilities.values())

    plt.bar(sums, probabilities, tick_label=sums)
    plt.xlabel('Sum')
    plt.ylabel('Probability %')
    plt.title('Probabilities of Sums of Two Dice Rolls')
    plt.show()


def print_plot_probabilities(probabilities):
    table = Table(show_header=True)
    table.add_column("Sum", justify="center", no_wrap=True)
    table.add_column("Probability", justify="center", no_wrap=True)
    for s in sorted(probabilities.keys()):
        table.add_row(str(s), f"{probabilities[s]:.2f}%")
    rich.print(table)


def main():
    num_rolls = 1000000
    probabilities = simulate_dice_rolls(num_rolls)

    plot_probabilities(probabilities)
    print_plot_probabilities(probabilities)


if __name__ == "__main__":
    main()
