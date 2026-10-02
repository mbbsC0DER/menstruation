# Alpha-Beta Pruning in Python

MAX = 1000
MIN = -1000

def alpha_beta(depth, node_index, maximizing_player, values, alpha, beta):
    
    # If we reach a leaf node
    if depth == 3:
        return values[node_index]

    if maximizing_player:
        best = MIN

        for i in range(2):
            value = alpha_beta(depth + 1, node_index * 2 + i,
                               False, values, alpha, beta)

            best = max(best, value)
            alpha = max(alpha, best)

            # Alpha-Beta Pruning
            if beta <= alpha:
                break

        return best

    else:
        best = MAX

        for i in range(2):
            value = alpha_beta(depth + 1, node_index * 2 + i,
                               True, values, alpha, beta)

            best = min(best, value)
            beta = min(beta, best)

            # Alpha-Beta Pruning
            if beta <= alpha:
                break

        return best


# Leaf node values
values = [3, 5, 6, 9, 1, 2, 0, -1]

# Initial values of alpha and beta
alpha = MIN
beta = MAX

# Start Alpha-Beta Pruning
result = alpha_beta(0, 0, True, values, alpha, beta)

print("The optimal value is:", result)