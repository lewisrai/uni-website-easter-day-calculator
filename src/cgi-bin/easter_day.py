#!/usr/bin/python3
import cgi
import datetime

# Source: Stuart Allen's Lecture
def easter_day(year):
    a = year % 19
    b = year // 100
    c = year % 100
    d = b // 4
    e = b % 4
    g = (8 * b + 13) // 25
    h = (19 * a + b - d - g + 15) % 30
    j = c // 4
    k = c % 4
    m = (a + 11 * h) // 319
    r = (2 * e + 2 * j - k - h + m + 32) % 7
    n = (h - m + r + 90) // 25
    p = (h - m + r + n + 19) % 32

    return datetime.date(year=year, month=n, day=p)


def format_date(date, date_type):
    date_string = "<p>"

    if date.day % 10 == 1:
        date_superscript = "<sup>st</sup>"
    elif date.day % 10 == 2:
        date_superscript = "<sup>nd</sup>"
    elif date.day % 10 == 3:
        date_superscript = "<sup>rd</sup>"
    else:
        date_superscript = "<sup>th</sup>"

    if date_type == "numerically":
        date_string += date.strftime("%d/%m/%Y")
    elif date_type == "verbosely":
        date_string += date.strftime(f'%d{date_superscript} %B %Y')
    else:
        date_string += date.strftime("%d/%m/%Y")
        date_string += "</p>\n<p>"
        date_string += date.strftime(f'%d{date_superscript} %B %Y')

    date_string += "</p>"

    return date_string


form_data = cgi.FieldStorage()

date = easter_day(int(form_data["year"].value))

date_type = form_data["date_type"].value

date_formatted = format_date(date, date_type)


print('content-type: text/html')
print('')
print('<!DOCTYPE html>')
print('<html lang="en">')
print('    <head>')
print('        <meta charset="utf-8">')
print('        <meta name="viewport" content="width=device-width, initial-scale=1">')
print('        <title>Easter Day Calculator</title>')
print('        <link rel="stylesheet" href="../styles/global.css" type="text/css">')
print('    </head>')
print('    <body>')
print('        <div class="container">')
print('            <div class="box center-text">')
print('                <h1>Easter Day Calculator</h1>')
print('            </div>')
print('        </div>')
print('')
print('        <div class="container">')
print('            <div class="box">')
print('                <p>Dates:</p>')
print(date_formatted)
print('                <p>Return back <a href="../index.html">here.</a></p>')
print('            </div>')
print('        </div>')
print('    </body>')
print('</html>')
