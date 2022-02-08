def get_suitable_spn(toponym):
    toponym_upper_corner = [float(x) for x in toponym['boundedBy']['Envelope']['upperCorner'].split()]
    toponym_lower_corner = [float(x) for x in toponym['boundedBy']['Envelope']['lowerCorner'].split()]
    return get_spn_by(toponym_upper_corner, toponym_lower_corner)


def get_spn_by(p1, p2):
    return abs(p1[0] - p2[0]), abs(p1[1] - p2[1])
