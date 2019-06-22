#!/usr/bin/env python
import psutil
import time
import configparser
import json
import os
from datetime import datetime


class ScriptClass:
    """Systeminfo script ver.1"""
    cpu = psutil.cpu_percent(interval=1, percpu=False)

    @staticmethod
    def func():
        print('Script finished successfully')


print(ScriptClass.__doc__)

end = ScriptClass()

vm = psutil.virtual_memory().total
sw = psutil.swap_memory().total
io = psutil.disk_io_counters().busy_time
net = psutil.net_io_counters().bytes_sent

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
            "CPU_load_info,%": ScriptClass.cpu,
            "Memory_info": sw,
            "Virtual_memory_info": vm,
            "IO_info": io,
            "Network_info": net
        }, indent=4)
        f.write(prints)
        time.sleep(int(interval))
    elif outputformat == "txt":
        prints = "SNAPSHOT :" + str(i) + " " + \
                 timestamp + ":" + \
                 "CPU_load_info,%:" + str(ScriptClass.cpu) + " " + \
                 "Memory_info:" + str(vm) + " " + \
                 "Virtual_memory_info:" + str(sw) + " " + \
                 "IO_info:" + str(io) + " " + \
                 "Network_info:" + str(net) + "\n"
        f.write(prints)
        time.sleep(int(interval))

end.func()
