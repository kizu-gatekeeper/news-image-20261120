# The World Today — Friday, 20 November 2026

[![news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/kizu-gatekeeper/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/kizu-gatekeeper/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120)

A one-page newspaper poster that sums up the world news of Friday,
20 November 2026 — drawn entirely in code with PIL, no photos and no
downloaded artwork.

The front page leads with Russia's overnight missile and drone attack
on Kyiv, hours after the Trump–Putin–Xi meeting in Shenzhen, and
carries four more stories from the same day: the International Court
of Justice ruling that Myanmar committed genocide against the
Rohingya, Anthropic's stock-market debut as the first purely AI
company to list publicly, President Trump's posthumous pardon of
baseball legend Pete Rose, and the UK's pledge of more than 1,000
drones for Ukraine.

## How to run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` (standard library only) copies `entry.png` into the output
directory and verifies the copy's byte size matches the original.

The poster itself is produced by `../build/draw_news.py`, a PIL script
that draws the whole front page — masthead, dateline, headlines and
pictograms — and saves it as `entry.png`.
