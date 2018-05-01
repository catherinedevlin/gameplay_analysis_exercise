# Gameplay Analysis

## Summary

A command-line tool that calculates the average completion time from a
JSON file of gameplay statistics.

## Usage

    python average_gameplay_time.py data.json

(Replace `data.json` with path to your own data file)

Results are displayed in seconds.

The gameplay statistics file should have the format demonstrated in
[data.json](data.json).

The only times that will be factored into the average are "CorrectUnfriendly"
targets of trials with "Result": "Complete" and "levelType": "Gameplay".

## Installing Requirements


[Install Python3](http://docs.python-guide.org/en/latest/starting/installation/)

[Install Pipenv](https://docs.pipenv.org/)

At a terminal window, `cd` into the directory you have cloned or copied the code into.  For instance,

    git clone https://github.com/catherinedevlin/gameplay_analysis_exercise.git
    cd gameplay_analysis_exercise
    pipenv shell

Now run `python average_gameplay_time.py` from within that `pipenv shell` session.

## Testing

To run the test suite, from the project directory,

    pipenv shell
    pytest
