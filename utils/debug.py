"""Utils for debugging."""
import os, sys

from pprint import pprint

from django.conf import settings
from django.utils.termcolors import colorize

def print_if_local(data):
    """Print data if environment is localhost"""
    try:
        if settings.ENV == "localhost":
            print(data)
    except Exception as exc:
        pass
    
def pprint_bold(text, fg="red"):
    """Print text bold."""
    print(colorize(text, opts=("bold",), fg=fg))

def make_bold(text, fg="red"):
    """Return text as bolded"""
    return colorize(text, opts=("bold",), fg=fg)

def pprint_symbols(symbol="=", symbol_repetition=42, bg="green"):
    """Print colorized symbol repeated."""
    print(colorize(symbol*symbol_repetition, opts=("bold",), fg="white", bg=bg))

def pprint_label(label="DATA", symbol="=", symbol_repetition=20, fg="white", bg="green"):
    "Prints label string, surrounded by repeated symbols, colorized."
    symboled_label = "{} {} {}".format(symbol*symbol_repetition, label, symbol*symbol_repetition)
    print(colorize(symboled_label, opts=("bold",), fg=fg, bg=bg))

def pprint_data(data, label="DATA", fg="white", bg="green"):
    "Pretty print data with label."
    print()
    pprint_label(label, fg=fg, bg=bg)
    pprint(data)
    print()

def pprint_exception(exc, label="Exception Occurred", location=None, bg="red"):
    """Pretty print the string representation of exception exc."""
    try:
        # Header
        print()
        pprint_label(label, bg=bg)

        exc_type, exc_obj, exc_tb = sys.exc_info()
        
        filename = os.path.split(exc_tb.tb_frame.f_code.co_filename)
        if location is None:
            location = filename

        print("Exception Data:", str(exc))
        print("Type:", exc_type) 
        print("Filename:", filename)     
        print("Location:", make_bold(location))
        print("Line:", make_bold(exc_tb.tb_lineno))
        
        # Footer - match header length
        pprint_symbols(symbol_repetition=42 + len(label), bg=bg)  

    except Exception as exc:
        pprint_data(exc, "An exception occurred", bg="red")

def pprint_breakpoint(label="BREAK POINT", symbol="*"):
    """Print a break point line."""
    print()
    pprint_label(label, symbol="*", symbol_repetition=30, bg="red")
    print()

def pprint_locals(local_vars):
    """Pretty print local variables `local_vars` from locals() returned dictionary.
    
    Sample invocation:
        pprint_locals(locals())
    """
    pprint_data(local_vars, label="Local Variables")


def debug_exception(exc, label="Exception Occurred", bg="red"):
    """Debug exception info returned by sys.exc_info().
    
    NOTE: This should be called on the context of an except clause
    SAMPLE invocation:
    ..
    except Exception as exc:
        debug_exception(exc)
    ..

    https://docs.python.org/3/library/sys.html#sys.exc_info
    """
    try:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        exc_frame = exc_tb.tb_frame
        f_code = exc_frame.f_code
        
        code = f_code.co_name
        location = f_code.co_filename.split(settings.BASE_DIR)[1]
        filename = location.split("/")[-1]
        line_no = exc_tb.tb_lineno

        print()
        pprint_label(label, bg=bg)
        print("Exception:", make_bold(str(exc_obj), fg=bg))
        print("Type:", make_bold(exc_type, fg=bg)) 
        print("Function/Method/Caller:", make_bold(code, fg=bg))
        print("Location:", make_bold(location, fg=bg))
        print("Line:", make_bold(line_no, fg=bg))
        print("Filename:", make_bold(filename, fg=bg))
        pprint_symbols(symbol_repetition=42 + len(label), bg=bg)  
     
    except Exception as exc:
        pprint_exception(exc, "An exception occurred", bg="red")

def debugger(message="Paused in debugger"):
    """Stop execution, mimiced from javascript `debugger` statement."""
    raise RuntimeError(message)