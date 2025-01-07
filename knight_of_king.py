def alph_to_num(alph: str):
    alph = alph.upper()
    num = ord(alph) - ord('A') + 1
    return num