#!python3

import os, json
from time import sleep
from argparse import ArgumentParser, ArgumentError
from selenium import webdriver
from tqdm import tqdm
from string import ascii_uppercase
from PyPDF2 import PdfFileMerger
from shutil import rmtree

parser = ArgumentParser(description='Generate problem statements from HDU', )
parser.add_argument('-c', '--webdriver', type=str, help='path of chromedriver', default='chromedriver')
parser.add_argument('-s', '--script', type=str, help='path of javascript used when printing', default='kattis_print.js')
parser.add_argument('-o', '--output', type=str, help='path of output file', default='statements.pdf')
parser.add_argument('--no-add-mark', action='store_true', help='do not add mark to the title')
parser.add_argument('--preserve-single-files', action='store_true', help='preserve single files for each problem printed')
parser.add_argument('problem', type=str, nargs='+', help='problem name at open.kattis.com')
try:
    args = parser.parse_args()
except ArgumentError:
    parser.print_help()
with open(args.script) as f:
    script = f.read()
output_path = os.path.realpath(args.output)
dest_path = os.path.dirname(output_path)
assert os.path.isdir(dest_path), 'destination directory do not exists'
dest_path = os.path.join(dest_path, 'single_pages')
os.makedirs(dest_path, exist_ok=True)
assert all(map(lambda x: x == '.' or x =='..', os.listdir(dest_path))), 'non-empty directory single_pages already in destination directory'
merger = PdfFileMerger()

try:
    print('open chromedriver...', end='')
    chrome_options = webdriver.ChromeOptions()
    settings = {
        "recentDestinations": [{
            "id": "Save as PDF",
            "origin": "local", "account": ""
        }],
        "selectedDestinationId":
        "Save as PDF", "version": 2,
        "isHeaderFooterEnabled": False
    }
    prefs = {
        'savefile.default_directory': dest_path,
        'printing.print_preview_sticky_settings.appState': json.dumps(settings)
    }
    chrome_options.add_experimental_option('prefs', prefs)
    chrome_options.add_argument('--kiosk-printing')
    driver = webdriver.Chrome(executable_path=args.webdriver, options=chrome_options)
    print('Done')

    prange = args.problem
    for mark, problem in tqdm(zip(ascii_uppercase[:len(prange)], prange), ncols=50, total=len(prange), smoothing=1):
        driver.get(f'https://open.kattis.com/problems/{problem}')
        sleep(5 if mark == 'A' else 2)
        if not args.no_add_mark:
            driver.execute_script(f"""
                title = document.querySelector('h1')
                title.innerText = '{mark} - ' + title.innerText
            """)
        file_name = os.path.join(dest_path, f'{driver.title}.pdf')
        driver.execute_script(script)
        sleep(0.5)
        merger.append(file_name)
finally:
    if driver:
        driver.close()

print('writing merged pdf...', end='')
merger.write(output_path)
merger.close()
print('Done')
if not args.preserve_single_files and os.path.isdir(dest_path):
    rmtree(dest_path)
