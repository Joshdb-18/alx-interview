#!/usr/bin/python3
"""
Prime number
"""


def isWinner(x, nums):
    """
    Determine the winner of each game based on the given rules.

    Args:
        x (int): The number of rounds.
        nums (list): An array of n, where n may be different for each round.

    Returns:
        str or None: The name of the player that won the most rounds.
                     If the winner cannot be determined, returns None.
    """

    def is_prime(num):
        """
        Check if a number is prime.

        Args:
            num (int): The number to check.

        Returns:
            bool: True if the number is prime, False otherwise.
        """
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def get_next_prime(nums):
        """
        Get the next prime number from the list of numbers.

        Args:
            nums (list): The list of numbers.

        Returns:
            int or None: The next prime number,
            or None if no prime number is found.
        """
        for num in nums:
            if is_prime(num):
                return num
        return None

    def remove_multiples(nums, prime):
        """
        Remove multiples of a prime number from the list of numbers.

        Args:
            nums (list): The list of numbers.
            prime (int): The prime number.

        Returns:
            list: The list of numbers with multiples of the
            prime number removed.
        """
        return [num for num in nums if num % prime != 0]

    winner_counts = {"Maria": 0, "Ben": 0}

    for n in nums:
        current_player = "Maria"  # Maria always goes first
        current_nums = list(range(1, n + 1))

        while True:
            prime = get_next_prime(current_nums)
            if prime is None:
                break
            current_player = "Ben" if current_player == "Maria" else "Maria"
            current_nums = remove_multiples(current_nums, prime)

        if current_player in winner_counts:
            winner_counts[current_player] += 1

    if winner_counts["Maria"] == winner_counts["Ben"]:
        return None
    return "Maria" if winner_counts["Maria"] < winner_counts["Ben"] else "Ben"
