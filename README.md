# SJTU-ACM-Scripts

## hdu\_print.js

Remove unnecessary information on a HDU problem description page and print the modified page.

#### Usage:

Execute this script in the console in Chrome DevTools after a HDU problem description page is loaded.

## hdu\_print.py

Execute `hdu_print.js` on several consecutive problem description pages and concatenate the resulting PDFs.
Also mark the problems starting from `A`.

#### Requirements:

`selenium tqdm PyPDF2`

When tested, `Chrome 85.0.4183.102`, `ChromeDriver 85.0.4183.87` and `selenium 3.141.0` are used.

#### Usage:

```
hdu_print.py [-h] [-c WEBDRIVER] [-s SCRIPT] [-o OUTPUT] [--no-add-mark] [--preserve-single-files] from to
```

## kattis\_print.js

Remove unnecessary information on a Kattis problem description page and print the modified page.

#### Usage:

Execute this script in the console in Chrome DevTools after a HDU problem description page is loaded.

## kattis\_print.py

Execute `kattis_print.js` on several problem description pages and concatenate the resulting PDFs.
Also mark the problems starting from `A`.

#### Requirements:

`selenium tqdm PyPDF2`

When tested, `Chrome 85.0.4183.102`, `ChromeDriver 85.0.4183.87` and `selenium 3.141.0` are used.

#### Usage:

```
kattis_print.py [-h] [-c WEBDRIVER] [-s SCRIPT] [-o OUTPUT] [--no-add-mark] [--preserve-single-files] problem [problem ...]
```

## vjudge\_board.py

Crawl standings of one or more vjudge contests and output it in SJTU OJ shadow form.

#### Requirements:

`requests`

`xclip` if clipboard needed on Linux

#### Usage:

```
vjudge_board.py [-h] [-o OUTPUT] [-c {clip.exe,xclip}] contest_id [contest_id ...]
```

## codeforces\_board.py

Crawl standings of one or more codeforces contests or gyms and output it in SJTU OJ shadow form.

#### Requirements:

`requests`

`xclip` if clipboard needed on Linux

#### Usage:

```
codeforces_board.py [-h] [-o OUTPUT] [-c {clip.exe,xclip}] contest_id [contest_id ...]
```
