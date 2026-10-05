# BAS Market Landscape Analysis

A small Python analysis of the Saudi/GCC market for business development, training and freelancing. I did it while researching the market for BAS Innovations, to see where the gaps are.

## The data
I researched six players from their public descriptions: Marn, Ureed, Freelance Yard / Shift, Jadah 30, HUB1006 and traditional consulting firms. For each one, I scored five capabilities: growth strategy, training, freelancer marketplace, managed services, and AI/data positioning. 1 means clearly offered, 0.5 means partly, and 0 means not a focus.

These scores are my own judgement, not measured data. The sample is small, and I didn't check every player's website in depth.

## What the code does
- Counts how many players cover each capability
- Counts how many capabilities each player combines
- Draws a heatmap (`landscape_heatmap.png`) and saves a summary (`gap_summary.csv`)

## Run it
```
pip install pandas matplotlib
python analyze.py
```

## What I found
- Freelancer marketplaces are the most crowded area, with 3 of the 6 players.
- Nobody leads with AI or data. Only Marn comes close, with its AI skill assessment.
- No player covers more than 2 of the 5 capabilities, so combining several of them in one offer is rare.

## Limits
Only a few players, subjective scoring, and the list isn't complete. Next, I'd add more players and check each score against the company's own materials.
