"""
monitor.py

System information, resource monitoring, warnings, live monitor,
and process information for the TB System Resource Monitor.
"""

import os
import platform
import socket
import time

import psutil

BYTES_PER_GB = 1024 ** 3

THRESHOLDS = {
    "cpu": 80,
    "memory": 80,
    "disk": 90,
}

REFRESH_SECONDS = 2

def get_system_info():
    """
    Return a dictionary of basic information about this computer.
    """

    info = {
        "os_name": platform.system(),

        "os_release": platform.release(),

        "hostname": socket.gethostname(),

        "processor": platform.processor(),

        "python_version": platform.python_version(),
    }

    if info["processor"] == "":
        info["processor"] = "Not available"

    return info

def display_system_info():
    """
    Print the system information in a readable format.
    """

    # TODO: Call get_system_info() and store the dictionary it returns.
    info = get_system_info()

    print()
    print("System Information")
    print("-" * 30)

    # TODO: Fill in the dictionary keys from get_system_info().
    print(f"Operating System: {info['os_name']} {info['os_release']}")
    print(f"Computer Name:    {info['hostname']}")
    print(f"Processor:        {info['processor']}")
    print(f"Python Version:   {info['python_version']}")

def bytes_to_gb(num_bytes):
    """
    Convert a number of bytes to gigabytes, rounded to 2 decimal places.
    """

    gigabytes = num_bytes / BYTES_PER_GB

    return round(gigabytes, 2)

def get_cpu_usage():
    """
    Return the current CPU usage percentage.
    """

    cpu_usage = psutil.cpu_percent(interval=1)

    return cpu_usage

def get_memory_usage():
    """
    Return a dictionary with memory (RAM) percent, used GB, and total GB.
    """

    # TODO: Call psutil.virtual_memory() and store the result.
    memory = psutil.virtual_memory()

    memory_info = {
        "percent": memory.percent,
        "used_gb": bytes_to_gb(memory.used),
        "total_gb": bytes_to_gb(memory.total),
    }

    return memory_info

def get_disk_path():
    """
    Return the path of the main disk for this operating system.
    """

    system_name = platform.system()
    if system_name == "Windows":
        return "C:\\"
    elif system_name == "Darwin" and os.path.exists("/System/Volumes/Data"):
        return "/System/Volumes/Data"
    else:
        return "/"

def get_disk_usage():
    """
    Return a dictionary with disk percent, used GB, and total GB.
    """

    disk = psutil.disk_usage(get_disk_path())

    disk_info = {
        "percent": disk.percent,
        "used_gb": bytes_to_gb(disk.used),
        "total_gb": bytes_to_gb(disk.total),
    }

    return disk_info


def get_resource_summary():
    """
    Gather CPU, memory, and disk information into ONE dictionary.
    """

    memory = get_memory_usage()
    disk = get_disk_usage()

    summary = {
        "cpu_percent": get_cpu_usage(),
        "memory_percent": memory["percent"],
        "memory_used_gb": memory["used_gb"],
        "memory_total_gb": memory["total_gb"],
        "disk_percent": disk["percent"],
        "disk_used_gb": disk["used_gb"],
        "disk_total_gb": disk["total_gb"],
    }

    return summary

def display_resource_summary(summary):
    """
    Print a resource summary dictionary in a readable format.
    """

    print()
    print("Current System Status")
    print("-" * 30)
    print(f"CPU Usage:    {summary['cpu_percent']}%")

    print(f"Memory Usage: {summary['memory_percent']}%")
    print(f"Used Memory:  {summary['memory_used_gb']:.2f} GB")
    print(f"Total Memory: {summary['memory_total_gb']:.2f} GB")
    print(f"Disk Usage:   {summary['disk_percent']}%")
    print(f"Used Disk:    {summary['disk_used_gb']:.2f} GB")
    print(f"Total Disk:   {summary['disk_total_gb']:.2f} GB")


def check_status(value, threshold):
    """
    Return "HIGH" if value is above threshold, otherwise "OK".
    """

    if value > threshold:
        return "HIGH"
    return "OK"

def get_statuses(summary):
    """
    Return a dictionary with the status ("OK" or "HIGH") of each resource.
    """

    statuses = {
        "cpu": check_status(summary["cpu_percent"], THRESHOLDS["cpu"]),

        "memory": check_status(summary["memory_percent"], THRESHOLDS["memory"]),

        "disk": check_status(summary["disk_percent"], THRESHOLDS["disk"]),
    }

    return statuses

def get_warnings(summary):
    """
    Return a list of warning messages for any resource that is HIGH.
    """

    warnings = []
    statuses = get_statuses(summary)

    if statuses["cpu"] == "HIGH":
        warnings.append("WARNING: CPU usage is high!")
    if statuses["memory"] == "HIGH":
        warnings.append("WARNING: Memory usage is high!")
    if statuses["disk"] == "HIGH":
        warnings.append("WARNING: Disk usage is high!")

    return warnings

def display_warnings(summary):
    """
    Print each warning, or a friendly message if there are none.
    """

    warnings = get_warnings(summary)

    if len(warnings) == 0:
        print("All resources are within normal limits.")
    else:
        for warning in get_warnings(summary):
            print(warning)

# -------------------------------------------------------------------
# Part 8.2: Unclear. Why strikethrough? Why line 232 = dead code?
# -------------------------------------------------------------------

def clear_screen():
    """
    Clear the terminal window.
    """

    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
# -----------------
def display_live_screen(summary):
    """
    Print one "frame" of the live monitor.
    """

    statuses = get_statuses(summary)

    print("=" * 30)
    print("   TB System Resource Monitor")
    print("=" * 30)
    print()
    print(f"CPU Usage:      {summary['cpu_percent']}%")
    print(f"Memory Usage:   {summary['memory_percent']}%")
    print(f"Disk Usage:     {summary['disk_percent']}%")
    print()
    print("Status:")
    print(f"CPU:    {statuses['cpu']}")
    print(f"Memory: {statuses['memory']}")
    print(f"Disk:   {statuses['disk']}")
    print()
    print("Press Ctrl+C to stop monitoring.")

def start_live_monitor():
    """
    Keep refreshing the screen until the user presses Ctrl+C.
    """

    try:
        # TODO: Start a loop that runs forever.
        while True:
            # TODO: Gather a fresh resource summary.
            summary = get_resource_summary()

            clear_screen()

            # TODO: Display this summary on the screen.
            display_live_screen(summary)

            # TODO: Wait REFRESH_SECONDS seconds before the next refresh.
            time.sleep(REFRESH_SECONDS)

    except KeyboardInterrupt:
        print()
        print("Live monitor stopped. Returning to the menu...")