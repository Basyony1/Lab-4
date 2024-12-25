from itertools import combinations

# Данные задачи
items = {
    'r': {'size': 3, 'points': 25},  # винтовка
    'p': {'size': 2, 'points': 15},  # пистолет
    'a': {'size': 2, 'points': 15},  # боекомплект
    'm': {'size': 2, 'points': 20},  # аптечка
    'i': {'size': 1, 'points': 5},   # ингалятор
    'k': {'size': 1, 'points': 15},  # нож
    'x': {'size': 3, 'points': 20},  # топор
    't': {'size': 1, 'points': 25},  # оберег
    'f': {'size': 1, 'points': 15},  # фляжка
    'd': {'size': 1, 'points': 10},  # антидот
    's': {'size': 2, 'points': 20},  # еда
    'c': {'size': 2, 'points': 20}   # арбалет
}

# Input parameters
inventory_size = 9  # ячеек (3x3)
base_points = 15     # начальные очки выживания
disease = None       # болезнь (None, "asthma" или "infection")

# Mandatory subjects depending on the disease
mandatory_items = []
if disease == "asthma":
    mandatory_items.append('i')
if disease == "infection":
    mandatory_items.append('d')

# Find all combinations of items that fit into inventory
def find_best_combination(items, inventory_size, base_points, mandatory_items):
    valid_combinations = []
    for r in range(1, len(items) + 1):
        for combination in combinations(items.keys(), r):
            total_size = sum(items[item]['size'] for item in combination)
            total_points = sum(items[item]['points'] for item in combination) + base_points
            if total_size <= inventory_size and all(m in combination for m in mandatory_items):
                valid_combinations.append((combination, total_points))
    # Find the combination with maximum points
    best_combination = max(valid_combinations, key=lambda x: x[1], default=None)
    return best_combination

# Solution to the problem
result = find_best_combination(items, inventory_size, base_points, mandatory_items)

# Formation of two-dimensional inventory
def create_inventory_grid(combination, items, grid_size):
    grid = [["" for _ in range(grid_size)] for _ in range(grid_size)]
    flat_grid = [item for item in combination for _ in range(items[item]['size'])]
    for i, item in enumerate(flat_grid):
        grid[i // grid_size][i % grid_size] = f"[{item}]"
    return grid

if result:
    best_combination, final_points = result
    inventory_grid = create_inventory_grid(best_combination, items, int(inventory_size**0.5))
    for row in inventory_grid:
        print(" ".join(row))
    print(f"\nИтоговые очки выживания: {final_points}")
else:
    print("Нет возможных решений.")
