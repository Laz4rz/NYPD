from typing import Dict


def save_csv(d: Dict, filename: str) -> None:
    with open(filename, 'w') as f:
        for key in d.keys():
            f.write("%s,%s\n" % (key, d[key]))
