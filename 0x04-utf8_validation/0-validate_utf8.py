#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """
    Determines if a given data set represents
    a valid UTF-8 encoding.
    """
    # Number of bytes remaining for the current UTF-8 character
    remaining_bytes = 0

    for num in data:
        # If remaining_bytes is 0, it means we are starting a new character
        if remaining_bytes == 0:
            # Count the number of leading 1s to determine
            # the number of bytes in the character
            mask = 1 << 7
            while mask & num:
                remaining_bytes += 1
                mask >>= 1

            # Edge case: invalid UTF-8 character length
            if remaining_bytes > 4 or remaining_bytes == 1:
                return False

            # For characters of length 1, remaining_bytes will remain 0
            if remaining_bytes == 0:
                continue

        else:
            # Check if the current byte is a valid continuation byte
            if (num >> 6) != 0b10:
                return False

        # Decrement the remaining_bytes count for each byte
        remaining_bytes -= 1

    # All bytes have been checked, and there are no
    # remaining incomplete characters
    return remaining_bytes == 0
