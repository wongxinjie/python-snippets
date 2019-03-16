import collections


def is_balance_binary_tree(tree):
    BalanceStatusWithHeight = collections.namedtuple(
        'BalanceStatusWithHeight', ('balanced', 'height')
    )

    def check_balanced(tree):
        if not tree:
            return BalanceStatusWithHeight(True, -1)

        left_result = check_balanced(tree.left)
        if not left_result.balanced:
            return BalanceStatusWithHeight(False, 0)

        right_result = check_balanced(tree.right)
        if not right_result.balanced:
            return BalanceStatusWithHeight(False, 0)

        is_balanced = abs(left_result.height - right_result.height)
        height = max(left_result.height, right_result.height)
        return BalanceStatusWithHeight(is_balanced, height)

    return check_balanced(tree).balanced
