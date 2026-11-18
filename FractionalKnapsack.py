
def knapsack(weights, profits, capacity):
    items = []

    for i in range(len(weights)):
        ratio = profits[i] / weights[i]
        items.append((ratio, weights[i], profits[i], i))

    items.sort(reverse=True)
    total = 0

    print("\nParcel Selection:")

    for ratio, weight, profit, i in items:
        if capacity == 0:
            print("Parcel", i+1, ": Not Taken")
            continue

        if weight <= capacity:
            taken = weight
            total += profit
            capacity -= weight
        else:
            taken = capacity
            total += ratio * taken
            capacity = 0

        print("Parcel", i+1, ":", taken, "/", weight,
              "kg taken")

    return total


n = int(input("Enter number of parcels: "))
weights = list(map(int, input("Enter weights: ").split()))
profits = list(map(int, input("Enter profits: ").split()))
capacity = int(input("Enter capacity: "))

if (len(weights) != n or len(profits) != n or
    any(w <= 0 for w in weights) or capacity < 0):
    print("Invalid parcel details")
else:
    print("\nMaximum Profit:", knapsack(weights, profits, capacity))
