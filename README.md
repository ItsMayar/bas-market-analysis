# BAS Market Landscape Analysis

A small Python analysis of the Saudi/GCC business development, training and freelance ecosystem, done to support BAS Innovations' positioning.

**About the data:** `landscape.csv` is built from desk research on seven players (Marn, Ureed, Freelance Yard / Shift, Jadah 30, HUB1006, traditional consulting, and BAS). Each capability is scored 1 (clearly offered), 0.5 (partial or emerging) or 0 (not a focus). These scores are my own judgements from public descriptions, not measured data, and the sample is small, so the results are directional only.

## What it does
- Calculates how many players cover each capability and what share of the market that is
- Counts how many capabilities each player combines
- Produces `landscape_heatmap.png` and `gap_summary.csv`

## Run
pip install pandas matplotlib
python analyze.py

## Findings
- Freelancer marketplaces are the most crowded area (3 of 6 players). AI/data-led positioning is the least covered: no player leads with it, and only one is partial.
- No player combines more than 2 of the 5 capabilities, while BAS plans to combine 4. That combination is the main differentiator.

## Limits
Seven players is a small sample, the scoring is subjective, and the list is not exhaustive. A next step would be to add more players and verify each score against the player's own materials.
