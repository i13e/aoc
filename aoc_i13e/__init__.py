import importlib
from pathlib import Path


def dynamic_version():
    here = Path(__file__).parent
    years = here.glob("aoc20??")
    max_year = max(years)
    days = max_year.glob("q??.py")
    max_day = max(days)
    year = int(max_year.name[-4:])
    day = int(max_day.name[1:3])
    return f"{year}.{day}"


__version__ = dynamic_version()


def mysolve(year: str, day: str, data: str) -> tuple[str, str]:
    ans_1, ans_2 = "", ""
    try:
        mod_name = f"aoc_i13e.aoc{year}.q{day:02d}"
        mod = importlib.import_module(name=mod_name)

        part_1 = getattr(mod, "part_1")
        ans_1 = str(part_1(data))

        part_2 = getattr(mod, "part_2")
        ans_2 = str(part_2(data))
    except (ModuleNotFoundError, AttributeError):
        pass

    return ans_1, ans_2
