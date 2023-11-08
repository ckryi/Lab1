transactions = [(1001, 2), (1001, 1), (1003, 2), (1005, 2), (1001, 3), (1007, 1), (1007, 2), (1100, 2), (1003, 2), (1001, 1)]

stats = {}

for id, type in transactions:
    if id not in stats:
        stats[id] = {1: 0, 2: 0, 3: 0, 'mft': None, 'lft': None}

    stats[id][type] += 1

for id, user_stats in stats.items():
    most_frequent = max(user_stats, key=lambda k: user_stats[k] if k != 'mft' and k != 'lft' else -1)
    least_frequent = min(user_stats, key=lambda k: user_stats[k] if k != 'mft' and k != 'lft' else 1)

    user_stats['mft'] = most_frequent
    user_stats['lft'] = least_frequent

print("stats =", stats)
