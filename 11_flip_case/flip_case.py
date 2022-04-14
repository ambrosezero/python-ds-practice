from cv2 import phase


def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    rtn_phrase = []
    to_swap = to_swap.lower()
    phrase_list = list(phrase)
    for letter in phrase_list:
        if str(letter) == to_swap:
            rtn_phrase.append(letter.upper())
        elif str(letter).lower() == to_swap:
            rtn_phrase.append(letter.lower())
        else:
            rtn_phrase.append(letter)
    return "".join(rtn_phrase[0:len(rtn_phrase)])
    # return phase
