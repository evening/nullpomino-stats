# Game Object
import re
from enum import Enum
from pathlib import Path
from datetime import datetime, timedelta

class GameMode(Enum):
    MARATHON = 1
    LINE_RACE = 2

class Game:
    timestamp = datetime.min
    mode = 0
    score = 0
    time = timedelta()
    directory = Path()

    def __init__(self, replay_dir):
        self.directory = Path(replay_dir)
        if self.directory.suffix != ".rep":
            raise SystemExit("not a replay file")

        replay_data = self.directory.read_text()

        timestamp_raw_date = re.findall(r'timestamp\.date=(.+)', replay_data)[0]
        timestamp_raw_time = re.findall(r'timestamp\.time=(.+)', replay_data)[0].replace("\\","")
        timestamp_date = datetime.strptime(timestamp_raw_date, '%Y/%m/%d')
        timestamp_time = datetime.strptime(timestamp_raw_time,"%H:%M:%S").time()
        self.timestamp = datetime.combine(timestamp_date,timestamp_time)

        self.score = re.findall(r'statistics\.score=(.+)', replay_data)[0]
        self.time = timedelta(seconds=int(re.findall(r'result\.time=(\d+)', replay_data)[0]))

        mode = re.findall(r'name\.mode=(.+)', replay_data)[0].replace(" ","_")
        self.mode = getattr(GameMode, mode)
