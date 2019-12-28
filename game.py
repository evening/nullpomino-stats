# Game Object

from enum import Enum
from pathlib import Path
from datetime import datetime

class GameMode(Enum):
    marathon = 1
    line_race = 2

class Game:
    timestamp = datetime.min
    mode = 0
    score = 0
    time = 0
    directory = Path()

    def __init__(self, replay_dir):
        self.directory = Path(replay_dir)
        if self.directory.suffix != ".rep":
            raise SystemExit("not a replay file")

        replay_data = self.directory.read_text()

        timestamp_date = re.findall(r'timestamp\.date=(.+)', output)[0]
        timestamp_time = re.findall(r'timestamp\.time=(.+)', output)[0]
        # TODO create datetime

        self.score = re.findall(r'statistics\.score=(.+)', output)[0]

        # TODO time type
        self.time = re.findall(r'result\.time=(\d+)', output)[0]
