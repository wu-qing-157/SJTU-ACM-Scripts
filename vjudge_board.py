#!python3

import requests, json
from os import system
from argparse import ArgumentParser, ArgumentError
from string import ascii_uppercase

parser = ArgumentParser()
parser.add_argument('contest_id', nargs='+', help='contest id(s) requested')
parser.add_argument('-o', '--output', default='', type=str, help='path of the output json')
parser.add_argument('-c', '--clip', type=str, choices=['clip.exe', 'xclip'], help='also store to the system clipboard')
try:
    args = parser.parse_args()
except ArgumentError:
    parser.print_help()

if args.output == '':
    args.output = f'{"_".join(args.contest_id)}.json'

result = []
for contest in args.contest_id:
    info = json.loads(requests.get(f'https://vjudge.net/contest/rank/single/{contest}', timeout=5).text)
    for submission in info['submissions']:
        result.append({
            'user': info['participants'][str(submission[0])][0],
            'problem': ascii_uppercase[submission[1]],
            'is_accepted': submission[2] == 1,
            'time': submission[3]
        })

with open(args.output, 'w') as f:
    f.write(json.dumps(result))

if args.clip == 'clip.exe':
    system(f'clip.exe < {args.output}')
elif args.clip == 'xclip':
    system(f'xclip -selection clipboard < {args.output}')