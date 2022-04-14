def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """

    # ????? why does the following worK...
    return phrase[(len(phrase))::-1]
    # ????? but this doesnt?
    # return phrase[(len(phrase)):-1:-1]
    # ????? shouldn't it function the same?
