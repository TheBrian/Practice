""" fix_csv.py
    1. Change pipe-delimited file into comma-delmited file
    2. Allow user to define delimiter for change > Bonus 1
    3. Automatically detect de-limiter if one is not defined ( Don't assume pipe and quote ) > Bonus 2 """
import csv
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('old_filename')
parser.add_argument('new_filename')
parser.add_argument('--in-delimiter', dest='delim')
parser.add_argument('--in-quote', dest='quote')
args = parser.parse_args()

with open(args.old_filename, newline='') as old_file:
    arguments = {}
    """if delimiter argument is given"""
    if args.delim:
        arguments['delimiter'] = args.delim
    """if quotechar argument is given"""
    if args.quote:
        arguments['quotechar'] = args.quote
    """if delimiter and quotechar arguments aren't given"""
    if not args.delim and not args.quote:
        """ sniffer sniffs the file for a dialect, or a delimiter and quotechar, that is passed into the argments"""
        arguments['dialect'] = csv.Sniffer().sniff(old_file.read())
        old_file.seek(0) """ Seek is where the read process begins, defaulting to 0 """
    """ Pass the file and arguments through the csv reader, then return the fixed csv through a list """
    reader = csv.reader(old_file, **arguments)
    rows = list(reader)

""" Writing of the new file. Pass the rows into the new file, as they would have been fixed already """
with open(args.new_filename, mode='wt', newline='') as new_file:
    writer = csv.writer(new_file)
    writer.writerows(rows)
