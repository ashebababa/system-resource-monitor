# System Resource Monitor
This application monitors and reports the usage of system resources on your device, including storage space and memory usage. There are options to view the reports live or to save a current snapshot of the report to your logs.

## Menu Option Features
- Display current system status with CPU, RAM, and disk usage information
- Display a live updating monitor of CPU, RAM, and disk usage in perentages
- Display a report of the 5 top processes on your device by greatest memory percentage
- Save a current snapshot of system status
- Display device system information, including os name, computer name, processor, and python version
- No optional features added yet

![Main Menu](screenshots/main%20menu.png)

## Technologies used
- **Python**, **psutil**, and standard-library modules **platfrom**, **socket**, **os**, **time**, **csv**, and **datetime**.

## Project Structure
**snapshots.csv** - Where system status snapshots get saved
**.gitignore** - A List of files and folders to NOT be tracked by github
**logger.py** - The code that appears as text in snapshots.csv
**main.py** - The code for the main features of the application
**monitor.py** - The code for the live systems monitor
**requirements.txt** - What you need installed to run the application

## How to Install and run
To clone repo and install requirements:
`git clone https://github.com/YOUR-USERNAME/tb-system-resource-monitor.git`
`cd tb-system-resource-monitor`
`python -m pip install -r requirements.txt`

To run: `python main.py`

## Known Limitations
2 second delay in the live monitoring. Only testeed on Windows operating system. Percents monitor to only 1 decimal place while GB values monitor to 2 decimal places.

## What I learned
I learned so much about not just python, but computer systems. Before this project I barely knew what RAM was and now I feel so much more confindetn navigating my own device. I practiced my critical thinking skills the most during this project.
