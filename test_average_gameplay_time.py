import json
from decimal import Decimal

from click.testing import CliRunner

from average_gameplay_time import analyze, average_seconds, filtered_targets

runner = CliRunner()

with open('test_data.json') as infile:
    test_data = json.load(infile)


def test_command_exists():

    result = runner.invoke(analyze, ['test_data.json'])
    assert result.exit_code == 0


def test_command_returns_number():

    result = runner.invoke(analyze, ['test_data.json'])
    Decimal(result.output)


def test_command_returns_two_digits():

    result = runner.invoke(analyze, ['test_data.json'])
    (before, after) = result.output.split('.')
    assert len(after.strip()) == 2


def test_filtered_targets():
    'Verify that the correct number of target are filtered'
    targets = list(filtered_targets(test_data))
    assert len(targets) == 2


def test_average_seconds():
    '''Verify that the correct targets pass filter

    Undesired targets have been given elapsed times of >= 1 second'''

    result = average_seconds(test_data)
    assert result == 0.25
