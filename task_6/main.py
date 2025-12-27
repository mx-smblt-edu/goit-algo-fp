def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    selected_items = []
    total_calories = 0
    total_cost = 0

    for item, details in sorted_items:
        if total_cost + details['cost'] <= budget:
            selected_items.append(item)
            total_cost += details['cost']
            total_calories += details['calories']

    return selected_items, total_calories, total_cost


def dynamic_programming(items, budget):
    n = len(items)
    table = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]
    item_list = list(items.items())

    for i in range(1, n + 1):
        for w in range(budget + 1):
            prev = i - 1
            cost = item_list[prev][1]['cost']
            if cost <= w:
                calories = item_list[prev][1]['calories']
                table[i][w] = max(calories + table[prev][w - cost], table[prev][w])
            else:
                table[i][w] = table[prev][w]

    b = budget
    selected_items = []
    total_cost = 0
    for i in range(n, 0, -1):
        prev = i - 1
        if table[i][b] != table[prev][b]:
            name = item_list[prev][0]
            selected_items.append(name)
            cost = item_list[prev][1]["cost"]
            b -= cost
            total_cost += cost

    total_calories = table[n][budget]

    return selected_items, total_calories, total_cost


def main():
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 20, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }
    budget = int(input("Введіть бюджет: "))

    selected_items_greedy, total_calories_greedy, total_cost_greedy = greedy_algorithm(items, budget)
    print(
        f"Greedy Algorithm: {selected_items_greedy}, "
        f"total Calories: {total_calories_greedy}, "
        f"total Cost: {total_cost_greedy}"
    )

    selected_items_dp, total_calories_dp, total_cost_dp = dynamic_programming(items, budget)
    print(
        f"Dynamic Programming: {selected_items_dp}, "
        f"total Calories: {total_calories_dp}, "
        f"total Cost: {total_cost_dp}"
    )


if __name__ == "__main__":
    main()
