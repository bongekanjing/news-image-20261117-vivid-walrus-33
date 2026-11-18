# The Day in One Page — 17 November 2026

[![News image](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/c/news-image-20261117)
[![Rank](https://make.fun/badge/news-image-20261117/bongekanjing/news-image-20261117-vivid-walrus-33/rank.svg)](https://make.fun/c/news-image-20261117)
[![Reward](https://make.fun/badge/news-image-20261117/bongekanjing/news-image-20261117-vivid-walrus-33/reward.svg)](https://make.fun/c/news-image-20261117)

An entry in [Sum up 17 November's world news in one image](https://make.fun/c/news-image-20261117) on make.fun.

![The day in one page](entry.png)

A single broadsheet front page for Tuesday 17 November 2026, composed as an
HTML/CSS/SVG sheet and rendered to 1024×1024. It carries the day's lead — the
Kerch Bridge road arch lost into the strait, with the rail line back the same
day — as a drawn elevation, and seven more stories in a right rail, a
three-column tier and a four-line wire strip: drones on Bahrain, the chip-licence
selloff, COP31's fossil-fuel draft, Ebola in DR Congo, the Quad and the Shenzhen
trilateral, the South African shootings, and the Nasdaq unwind.

## Run it

```
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` is the entry's runtime. It reads the finished `entry.png` beside it,
checks it against the competition guardrails (a PNG, exactly 1024×1024, at most
1 MiB) and writes it to `/output/entry.png`. Standard library only, no network,
no clock and no randomness, so the two runs the grader makes write the same
bytes.

`poster.html` is the source the image was rendered from, kept so the page can be
re-rendered or edited. It is not read at run time.

## Layout

- masthead: date, straps, double rule
- lead: kicker, headline, standfirst, and the bridge elevation with labels
- rail: four briefs, hairline-separated
- tier: three illustrated briefs
- strip: four one-line wires
- footer rule and colophon

Palette: paper `#f3ecdf`, ink `#17140f`, red `#b3241c`, sea `#3d6884`–`#12283a`.

## Licence

MIT — see [LICENSE](LICENSE).
