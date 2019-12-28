from pathlib import Path
import re
import datetime

p = Path('C://NullpoMino/replay').glob("**/*")

for file in p:
    if file.suffix == ".rep":
        output = file.read_text()
        if "name.mode=LINE RACE" in output:
            get_timestamp = re.findall(r'timestamp\.date=(.+)', output)[0]
            get_time = re.findall(r'result\.time=(\d+)', output)[0]
            formatted_timestamp = datetime.datetime.strptime(get_timestamp, '%Y/%m/%d')
            formatted_time = datetime.timedelta(seconds=int(get_time))
