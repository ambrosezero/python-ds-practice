def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}

        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    phrase_lower = phrase.lower()
    rtn_value = dict()
    # for i in phrase:
    #     if i in ['a', 'e', 'i', 'o', 'u']:
    #         rtn_value[i] = rtn_value[i] + 1
    for letter in phrase_lower:
        if letter in ['a', 'e', 'i', 'o', 'u']:
            rtn_value[letter] = phrase_lower.count(letter)
    return rtn_value

    # for vowell in ['a', 'e', 'i', 'o', 'u']:
    #     if vowell in phrase:
    #         rtn_value[vowell] = phrase.count(vowell)
    # return rtn_value
