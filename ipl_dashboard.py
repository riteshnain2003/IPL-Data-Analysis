import streamlit as st
import os

# Make sure working dir is the script's folder
os.chdir(os.path.dirname(os.path.abspath(__file__)))

st.set_page_config(page_title="IPL Dashboard", layout="wide")
st.title("🏏 IPL Data Analysis Dashboard")
st.markdown("Select an insight and view its visualization")

# Define relative paths (without drive letters)
team_queries = {
    "Which team has won the most matches?": "team_insights/plots/wining_count.jpg",
    "Which team has the best win percentage?": "team_insights/plots/winning_percentage_plot.png",
    "Which team wins the most tosses?": "team_insights/plots/pietosswinner.jpg",
    "How often does toss winner = match winner?": "team_insights/plots/pietosswinner.jpg",
    "Which team performs best when batting first vs chasing?": "team_insights/plots/batVSchasing.jpg",
    "Season-wise top-performing team (most wins per season)": "team_insights/plots/season_wise_top.jpg",
    "Win distribution across different venues": "team_insights/plots/venues_win.jpg"
}

player_queries = {
    "Top 10 run-scorers of all time": "player_insights/plots/top_ten_batsman.jpg",
    "Top 10 batsmen with most 4s and 6s": "player_insights/plots/topten_boundary.png",
    "Top 10 bowlers with most wickets": "player_insights/plots/top_bowler.jpg",
    "Best finishers (runs in overs 16‑20)": "player_insights/plots/most_run_5_over.jpg",
    "Most ‘Player of the Match’ awards": "player_insights/plots/player_of_match.jpg",
    "Top batsmen vs specific teams": "player_insights/plots/batsmen_against_specific_team.jpg"
}

match_queries = {
    "Average runs scored per match / per over": "match_insights/plots/avg_run_per_match.jpg",
    "Total matches per season": "match_insights/plots/total_matches_per_season.jpg",
    "Highest and lowest team scores": "match_insights/plots/high_low_score.jpg",
    "Super over matches count": "match_insights/plots/Super_over.jpg",
    "Venues with highest win % for specific teams": "match_insights/plots/Venues_with_highest_win.jpg"
}

# Sidebar
st.sidebar.header("Select Insight Category")
insight_type = st.sidebar.radio("", ["Team-Level", "Player-Level", "Match-Level"])

# Choose based on insight category
if insight_type == "Team-Level":
    query_dict = team_queries
elif insight_type == "Player-Level":
    query_dict = player_queries
else:
    query_dict = match_queries

selected_query = st.sidebar.selectbox("Select a query:", list(query_dict.keys()))
image_path = query_dict[selected_query]

# Display query + image side by side
col1, col2 = st.columns([1, 2])
with col1:
    st.subheader("Query")
    st.write(selected_query)
with col2:
    if os.path.exists(image_path):
        st.image(image_path, use_container_width=True)
    else:
        st.error(f"🚫 Plot not found: {image_path}")
        st.write("Working directory:", os.getcwd())
        st.write("Files here:", os.listdir(os.path.dirname(image_path)))
