def are_almost_equal(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    permitted_disposition = 2

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            permitted_disposition -= 1
        if permitted_disposition < 0:
            return False

    return True
