"""Executes pylint"""
from pylint.lint import Run
def main():
    """Executes pylint and validates score"""

    try:
        results = Run(['oi'], exit=False)
    except TypeError:
        results = Run(['oi'], do_exit=False)
    if results.linter.stats['global_note'] <= 9:
        exit('pylint score must be greater than 9')

main()
