# pitchFORK-chia-forks-ports-check
Tool used to check multiple chia and chia forks cfg files for port conflicts.

# High level overview
The tool will parse the configured yaml config files and then scan the data for possible port conflicts.

# Output example

Here is an output example from print_raw_parsed_data()

![alt text](https://raw.githubusercontent.com/ageorge95/pitchFORK-chia-forks-ports-check/main/ReadMe_res/print_raw_data_snapshot.JPG?raw=true)

Here is an output example from print_port_conflicts()

![alt text](https://raw.githubusercontent.com/ageorge95/pitchFORK-chia-forks-ports-check/main/ReadMe_res/print_port_conflicts_snapshot.JPG?raw=true)?raw=true)

# How to use
The tool was tested just in Windows, but should work on every OS where python works.

## Usage scenario 1
DIRECT USAGE - Usefull for a quick overview.
1. Add your fork config.yaml filepaths in "input.json"
2. Execute RUN_ME.py
3. See the scanned data and possible conflicts on your screen

## Usage scenario 1
INTERFACE WITH OTHER PYTHON SCRIPTS - usefull as a sub-module in your python scripts.
1. Prepare a list containing the config filepaths.
2. Directly import the pitchfork() class from _pitchfork.py
3. Call the parse_all_cfgs() methods with the list created at #1
4. Execute as needed print_raw_parsed_data() OR print_port_conflicts()