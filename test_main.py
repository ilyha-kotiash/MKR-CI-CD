import pytest
from main import read_population_data, sort_by_area, sort_by_population

@pytest.fixture
def sample_data():
    return [
        {"country": "Ukraine", "area": 603500, "population": 41000000},
        {"country": "France", "area": 551695, "population": 68000000},
        {"country": "Germany", "area": 357022, "population": 83000000}
    ]

@pytest.mark.parametrize("key, expected", [
    ("area", ["Ukraine", "France", "Germany"]),
    ("population", ["Germany", "France", "Ukraine"])
])
def test_sorting(sample_data, key, expected):
    sorted_data = sort_by_area(sample_data) if key == "area" else sort_by_population(sample_data)
    assert [item["country"] for item in sorted_data] == expected
