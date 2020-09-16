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
parser.add_argument('-i', '--id', type=str, required=True, help='from-to, [from, to), ids of statement')
parser.add_argument('-c', '--webdriver', type=str, required=True, help='path of chromedriver')
parser.add_argument('-s', '--script', type=str, help='path of javascript used when printing', default='hdu_print.js')
parser.add_argument('-o', '--output', type=str, help='path of output file', default='statements.pdf')
parser.add_argument('--no-add-mark', action='store_true', help='do not add mark to the title')
parser.add_argument('--preserve-single-files', action='store_true', help='preserve single files for each problem printed')
try:
    args = parser.parse_args()
except ArgumentError:
    parser.print_help()
ids, driver_path, script_path, output_path, add_mark, preserve_single = args.id, args.webdriver, args.script, args.output, not args.no_add_mark, args.preserve_single_files
with open(script_path) as f:
    script = f.read()
output_path = os.path.realpath(output_path)
dest_path = os.path.dirname(output_path)
assert os.path.isdir(dest_path), 'destination directory do not exists'
dest_path = os.path.join(dest_path, 'single_pages')
os.makedirs(dest_path, exist_ok=True)
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
    driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)
    print('Done')

    prange = range(*map(int, ids.split('-')))
    for mark, problem in tqdm(zip(ascii_uppercase[:len(prange)], prange), ncols=50, total=len(prange), smoothing=1):
        driver.get(f'http://acm.hdu.edu.cn/showproblem.php?pid={problem}')
        sleep(5 if mark == 'A' else 2)
        if add_mark:
            driver.execute_script(f"""
                title = document.querySelector('h1')
                title.innerText = '{mark} - ' + title.innerText
            """)
        file_name = os.path.join(dest_path, f'{driver.title}.pdf')
        if os.path.isfile(file_name):
            os.remove(file_name)
        if os.path.isdir(file_name):
            rmtree(file_name)
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
if not preserve_single and os.path.isdir(dest_path):
    rmtree(dest_path)