#!/usr/bin/env python
import psutil
import time
import configparser
import json
import os
from datetime import datetime


class SystemInfo:
    """Systeminfo script ver.1"""

    def __init__(self):
        self.cpu = str(psutil.cpu_percent(interval=1, percpu=False))
        self.vm = str(psutil.virtual_memory().total)
        self.sw = str(psutil.swap_memory().total)
        self.io = str(psutil.disk_io_counters().busy_time)
        self.net = str(psutil.net_io_counters().bytes_sent)

    @staticmethod
    def func():
        print('Script finished successfully')


print(SystemInfo.__doc__)


config = configparser.ConfigParser()
config.read(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'config.ini'))

interval = config.get('common', 'interval')
outputformat = config.get('common', 'output')
snap = config.get('common', 'snapshots')

timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

f = open("syslog." + outputformat, "w")

for i in range(1, int(snap) + 1):
    if outputformat == "json":
        prints = json.dumps({
            "SNAPSHOT": str(i),
            "Timestamp": timestamp,
            "CPU_load_info,%": SystemInfo().cpu,
            "Memory_info": SystemInfo().sw,
            "Virtual_memory_info": SystemInfo().vm,
            "IO_info": SystemInfo().io,
            "Network_info": SystemInfo().net
        }, indent=4)
        f.write(prints)
        time.sleep(int(interval))
    elif outputformat == "txt":
        prints = "SNAPSHOT :" + str(i) + " " + \
                 timestamp + ":" + \
                 "CPU_load_info,%:" + SystemInfo().cpu + " " + \
                 "Memory_info:" + SystemInfo().vm + " " + \
                 "Virtual_memory_info:" + SystemInfo().sw + " " + \
                 "IO_info:" + SystemInfo().io + " " + \
                 "Network_info:" + SystemInfo().net + "\n"
        f.write(prints)
        time.sleep(int(interval))

SystemInfo().func()
