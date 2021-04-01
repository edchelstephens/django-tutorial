"""Console printing/debugging utils."""

import os
import sys

from pprint import pprint
from django.utils.termcolors import colorize

def pprint_symbols(symbol="=", symbol_repetition=42, bg="green"):
	"""Print colorized symbols repeated."""
	print(colorize(symbol*symbol_repetition, opts=("bold",), fg="white", bg=bg))

def pprint_bold(text, fg="red"):
    """Print text bold."""
    print(colorize(text, opts=("bold",), fg=fg))

def make_bold(text, fg="red"):
    """Return text as bolded"""
    return colorize(text, opts=("bold",), fg=fg)

def pprint_label(label="DATA", symbol="=", symbol_repetition=20, fg="white", bg="green"):
    "Prints label string, surrounded by repeated symbols, colorized."
    symboled_label = "{} {} {}".format(symbol*symbol_repetition, label, symbol*symbol_repetition)
    print(colorize(symboled_label, opts=("bold",), fg=fg, bg=bg))

def pprint_data(data, label="DATA", fg="white", bg="green", with_footer=True, footer_text=None):
    "Pretty print data with label."
    print()
    pprint_label(label, fg=fg, bg=bg)
    print()
    pprint(data)
    print()
    if with_footer:
        if footer_text:
            print(footer_text)
        pprint_symbols(symbol_repetition=42 + len(label), bg=bg)
        print()

def pprint_exception(exc, label="Exception Occurred", location=None, bg="red"):
    """Pretty print the string representation of exception exc."""
    # Exception header
    print()
    pprint_label(label, bg=bg)

    exc_type, exc_obj, exc_tb = sys.exc_info()
    filename = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]

    print("Exception Data:", str(exc))
    print("Exception Type:", exc_type) 
    print("Filename:", filename)     
    print("Location:", location if location else filename)
    print("Line:", exc_tb.tb_lineno)
    
    # Match exception header length
    pprint_symbols(symbol_repetition=42 + len(label), bg=bg)  

def pprint_breakpoint(label="BREAK POINT", symbol="*", bg="red"):
    """Print a break point line."""
    print()
    pprint_label(label, symbol="*", symbol_repetition=30, bg=bg)
    print()

def pprint_local_vars(local_vars, label="Local Variables", location=None):
    """Pretty print local variables from locals() returned dictionary as local_vars.
    
    Sample invocation:
        pprint_local_vars(locals())
        pprint_local_vars(locals(), label="Local variables at scope", location=__name__)
    """
    footer_text = make_bold("Location: {}".format(location), fg="green") \
        if location is not None else None

    data = dict(
        data=local_vars,
        label=label,
        footer_text=footer_text
    )

    pprint_data(**data)

