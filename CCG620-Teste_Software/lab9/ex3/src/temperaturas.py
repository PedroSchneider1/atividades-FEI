def maior(temps):
    if not temps:
        raise ValueError("lista vazia")
    m = temps[0]
    for t in temps[1:]:
        if t > m:
            m = t
    return m


def dia_do_maior(temps):
    if not temps:
        raise ValueError("lista vazia")
    pos = 0
    for i in range(1, len(temps)):
        if temps[i] > temps[pos]:
            pos = i
    return pos
