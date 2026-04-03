import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned data (adjust file path to your saved CSV)
# Assuming you saved df_outfield_clean and df_gk_clean as CSV files
df_outfield = pd.read_csv('df_outfield_clean.csv')
df_gk = pd.read_csv('df_gk_clean.csv')

st.title("FIFA 22 EDA: What Predicts Player Wage?")
st.markdown("Outfield players vs. Goalkeepers – correlation analysis and data quality audit.")

# Sidebar filter
position = st.radio("Select player type", ("Outfield", "Goalkeeper"))

if position == "Outfield":
    df_show = df_outfield
    attrs = ['pace', 'shooting', 'passing', 'dribbling', 'defending', 'physic']
    target = 'wage_eur'
    st.subheader("Outfield Players: Correlation with Wage")
else:
    df_show = df_gk
    attrs = ['goalkeeping_diving', 'goalkeeping_handling', 'goalkeeping_kicking',
             'goalkeeping_positioning', 'goalkeeping_reflexes', 'goalkeeping_speed']
    target = 'wage_eur'
    st.subheader("Goalkeepers: Correlation with Wage")

# Correlation heatmap
corr = df_show[attrs + [target]].corr()
fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(corr[[target]].sort_values(by=target, ascending=False), annot=True, cmap='coolwarm', ax=ax)
st.pyplot(fig)

# Scatter plot: highest correlated attribute vs wage
top_attr = corr[target].drop(target).idxmax()
st.subheader(f"Scatter: {top_attr} vs Wage")
fig2, ax2 = plt.subplots(figsize=(8, 5))
ax2.scatter(df_show[top_attr], df_show[target], alpha=0.4)
ax2.set_yscale('log')
ax2.set_xlabel(top_attr)
ax2.set_ylabel("Wage (EUR, log scale)")
st.pyplot(fig2)

# Cleanlab flagged players (if you saved the flagged indices)
st.subheader("Potential Label Issues (Cleanlab)")
# Load flagged players
flagged_players = pd.read_csv('flagged_players.csv')
st.dataframe(flagged_players[['short_name', 'wage_eur', 'wage_category']].head(5))
