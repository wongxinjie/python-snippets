import collections


def binary_tree_depth_order(tree):
    result, current_depth_nodes = [], collections.deque([tree])
    while current_depth_nodes:
        next_depth_nodes, this_level = current_depth_nodes.deque([]), []

        while current_depth_nodes:
            curr = current_depth_nodes.popleft()
            if curr:
                this_level.append(curr.data)
                next_depth_nodes += [curr.left, curr.right]

        if this_level:
            result.append(this_level)

        current_depth_nodes = next_depth_nodes
    return result
