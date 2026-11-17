
def knapsack(weights, profits, capacity):
    items = []

    for i in range(len(weights)):
        ratio = profits[i] / weights[i]
        items.append((ratio, weights[i], profits[i]))

    items.sort(reverse=True)
    total = 0

    for ratio, weight, profit in items:
        if capacity == 0:
            break

        if weight <= capacity:
            total += profit
            capacity -= weight
        else:
            total += ratio * capacity
            capacity = 0

    return total


n = int(input("Enter number of parcels: "))
weights = list(map(int, input("Enter weights: ").split()))
profits = list(map(int, input("Enter profits: ").split()))
capacity = int(input("Enter capacity: "))

if len(weights) != n or len(profits) != n or any(w <= 0 for w in weights):
    print("Invalid parcel details")
else:
    print("Maximum Profit:", knapsack(weights, profits, capacity))
