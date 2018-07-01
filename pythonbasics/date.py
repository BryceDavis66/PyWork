from datetime import datetime


def datecalc(x, y, z):
    hehe = datetime.now() - datetime(x, y, z)
    print(hehe.days)


datecalc(1999, 7, 16)
