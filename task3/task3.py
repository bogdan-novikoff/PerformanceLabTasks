import sys
from typing import List, Dict
import json


def upgrade_values(tests: List[Dict], ids: List[int], values: List[str]):
    for test in tests:
        if test['id'] in ids:
            test['value'] = values[ids.index(test['id'])]
        if 'values' in test:
            upgrade_values(test['values'], ids, values)


def main():
    file1, file2, file3 = sys.argv[1:]
    with open(file1, 'r') as f1:
        with open(file2, 'r') as f2:
            values: List[Dict] = json.load(f1)['values']
            tests: List[Dict] = json.load(f2)['tests']

    ids: List[int] = [d['id'] for d in values]
    values: List[str] = [d['value'] for d in values]

    upgrade_values(tests, ids, values)

    with open(file3, 'w') as f3:
        json.dump(tests, f3)


if __name__ == '__main__':
    main()
