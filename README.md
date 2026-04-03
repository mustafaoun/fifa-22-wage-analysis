# FIFA 22 Player Wage Analysis

Which attributes drive weekly wages? (Outfield vs. Goalkeepers)

Live demo: [Streamlit app link][https://fifa-22-wage-analysis-ihqiw9m8jsappywhqytznpe.streamlit.app/]

GitHub repo: https://github.com/mustafaoun/fifa-22-wage-analysis

Data source: FIFA 22 complete player dataset (19,239 players, 110 attributes) – Kaggle

## Problem statement

A football club's recruitment team needs to understand which player attributes are most strongly associated with weekly wages. This helps them:

- Identify over‑ or under‑valued players before contract negotiations.
- Allocate salary budget efficiently across positions.

Using only EDA (no modelling), we answer:
"Which attributes – pace, shooting, passing, dribbling, defending, physic – best correlate with wage for outfield players? And which goalkeeper attributes matter most?"

## Quantified business impact (simulated)

If a club used this analysis to adjust wage offers for 50 new signings per year:

**Outfield players**: Focusing negotiations on passing & dribbling (r=0.44, 0.42) rather than pace (r=0.13) could avoid €2.1M annual overspend (estimated 15% of misdirected wage budget).

**Goalkeepers**: Shifting budget from speed (r=0.28) to handling/diving/reflexes (r≈0.55) would improve salary‑to‑performance efficiency by 22%, equivalent to €850K yearly savings.

Assumptions based on median wage differences between attribute tiers; methodology available in notebook.

## Key findings (plain English)

**Outfield players (n=17,107)**

- Passing and dribbling have the strongest correlation with wage (r=0.44 and 0.42). Playmakers earn more.
- Pace correlates weakly (r=0.13). Speed alone does not drive high wages.
- The relationship is exponential – a player with passing 90 can earn 10× more than a player with passing 70 (scatter plot with log scale).

**Goalkeepers (n=2,132)**

- Handling, diving, and reflexes dominate (r≈0.55 each). These are the salary drivers.
- Goalkeeping speed has low correlation (r=0.28). Clubs overpay for fast keepers relative to its impact.

**Wage tiers**

- Low wages show horizontal bands – FIFA uses fixed salary steps (€1k, €2k, €3k…).
- High wages are continuous, suggesting individual negotiation.

## Cleanlab data quality audit

We ran Cleanlab (classification proxy, target = wage_eur binned into low/medium/high) to flag potential label errors.

- 6,264 rows (37%) flagged – largely due to quantile binning boundaries, not genuine data errors.
- Example flagged player: Duirval Diniz – wage €13k (labelled "high") but attributes suggest a mid‑tier player. Possible over‑valuation.
- Action: No rows were removed; the audit shows that quantile‑based binning inflates flags. For real‑world salary models, we recommend manual review of boundary cases.

## Out‑of‑distribution (OOD) note

"In three years, player wages will likely increase due to inflation and transfer market growth. Attribute distributions may shift as the game evolves (e.g., pace becoming more important for all positions). My correlation analysis might change if the relationship between passing and wage weakens over time, so the insights are not permanent."

Mitigation: Refresh the analysis annually with new FIFA data; consider Spearman correlation to handle non‑linear wage jumps.

## Technical approach (summary)

- **Data cleaning**: Dropped rows missing wage_eur (53 rows, 0.3%) – MCAR assumption. Separated outfield (non‑null pace, shooting, passing, dribbling, defending, physic) from goalkeepers (null on those six).
- **Correlations**: Pearson (linear) – limitation noted. Spearman would better capture exponential wage jumps.
- **Visualisation**: Scatter plot with log scale (passing vs wage), correlation heatmaps.
- **Cleanlab**: Used RandomForest with cross‑validation to find label inconsistencies.
- **Deployment**: Streamlit app with radio button to toggle outfield/GK, interactive heatmap and scatter.

## Live demo & code

Streamlit app: [Insert your deployed URL]

Jupyter notebook: fifa_wage_eda.ipynb

Run locally:

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Limitations & future work

- **Pearson vs. Spearman**: Our correlations assume linearity; future work will use Spearman for monotonic relationships.
- **Temporal drift**: Wages and attribute importance change yearly – analysis is a snapshot.
- **Cleanlab binning**: The 37% flag rate is an artefact; use fewer or continuous targets for real error detection.
