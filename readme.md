# nullpomino stats

quickly view [nullpomino](https://github.com/nullpomino/nullpomino) replay information. Developed so I can view progress for the line race mode.

usage:
```
g = Game("C:\\NullpoMino\\replay\\2019_12_20_20_09_39.rep")
g.timestamp

>  datetime.datetime(2019, 12, 20, 20, 9, 39)


u = Replays("C:\\NullpoMino\\replay")
u.load()
u.line_race_over_time()

> [ line graph here ]

```
