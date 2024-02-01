from pytest_html import __version__
from pkg_resources import parse_version

PHTML_VER_MAJ = parse_version(__version__).major

if PHTML_VER_MAJ < 4:
    from py.xml import html


def th(value):
    return f"<th>{value}</th>" if PHTML_VER_MAJ >= 4 else html.th(value)


def td(value):
    return f"<td>{value}</td>" if PHTML_VER_MAJ >= 4 else html.td(value)


def pytest_html_results_table_header(cells):
    cells.insert(2, th("Special Header"))


def pytest_html_results_table_row(report, cells):
    cells.insert(2, td("Special Value"))
