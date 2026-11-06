"""Koda lauzēja dzinējs: binārās meklēšanas loģika."""


def aprekinat_minejumu(apaksa, augsa):
    """Aprēķina viduspunktu binārajai meklēšanai."""
    return (apaksa + augsa) // 2


def atjaunot_robezas(apaksa, augsa, minejums, atbilde):
    """Pārbīda robežas pēc atbildes: l (lielāks) vai m (mazāks)."""
    if atbilde == "l":
        apaksa = minejums + 1
    elif atbilde == "m":
        augsa = minejums - 1
    return apaksa, augsa
