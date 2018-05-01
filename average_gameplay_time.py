import json
import statistics

import click


@click.command()
@click.argument('filename')
def analyze(filename):
    with open(filename) as infile:
        data = json.load(infile)
    average_sec = average_seconds(data)
    rounded = '{:.2f}'.format(average_sec)
    click.echo(rounded)


def average_seconds(data):
    '''Yields average duration (ms) for targets of trials with "Result": "Complete" and "levelType": "Gameplay". '''

    average_milliseconds = statistics.mean(filtered_milliseconds(data))
    return average_milliseconds / 1000


def filtered_milliseconds(data):
    '''Yields milliseconds elapsed for trials with "Result": "Complete" and "levelType": "Gameplay". '''

    for target in filtered_targets(data):
        yield target['finishTime'] - target['showTime']


def filtered_targets(data):
    '''Yields "CorrectUnfriendly" targets of trials with "Result": "Complete" and "levelType": "Gameplay". '''

    # Alternately, this could be implemented with jq.

    return [target
            for module in data['modules'] for level in module['levels']
            if level['levelType'] == 'Gameplay' and level[
                'result'] == 'Complete' for trial in level['trials']
            for target in trial['targets']
            if target['result'] == 'CorrectUnfriendly']


if __name__ == '__main__':
    analyze()
