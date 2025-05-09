import importlib
from pathlib import Path

def fetch_a_criterion(criteria):
    criteria = criteria.replace(" ", "_")
    return importlib.import_module(f"src.criteria_to_sort.criteria_to_sort_{criteria}").criteria_to_sort

def fetch_criteria():
    criteria_files = Path("src/criteria_to_sort")
    criteria_options = []

    for file in criteria_files.iterdir():
        if file.suffix == '.py':
            extract_criteria_from_file_name = file.stem[len('criteria_to_sort_'):]
            final_criteria_name = extract_criteria_from_file_name.replace("_", " ")
            criteria_options.append(final_criteria_name)

    return criteria_options
