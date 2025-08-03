import streamlit as st
import os

st.set_page_config(page_title="IPL Dashboard", layout="wide")

st.title("🏏 IPL Data Analysis Dashboard")

# 📁 Define plot paths
team_queries = {
    "Which team has won the most matches?": "R:/projects/IPL-DATA-ANALYSIS/team_insights/plots/wining_count.jpg",
    "Which team has the best win percentage?": "R:/projects/IPL-DATA-ANALYSIS/team_insights/plots/winning_percentage_plot.png",
    "Which team wins the most tosses?": "R:/projects/IPL-DATA-ANALYSIS/team_insights/plots/pietosswinner.jpg",
    "How often does toss winner = match winner?": "R:/projects/IPL-DATA-ANALYSIS/team_insights/plots/pietosswinner.jpg",
    "Which team performs best when batting first vs chasing?": "R:/projects/IPL-DATA-ANALYSIS/team_insights/plots/batVSchasing.jpg",
    "Season-wise top-performing team (most wins per season)": "R:/projects/IPL-DATA-ANALYSIS/team_insights/plots/season_wise_top.jpg",
    "Win distribution across different venues": "R:/projects/IPL-DATA-ANALYSIS/team_insights/plots/venues_win.jpg"
}

player_queries = {
    "Top 10 run-scorers of all time": "R:/projects/IPL-DATA-ANALYSIS/player_insights/plots/top_ten_batsman.jpg",
    "Top 10 batsmen with most 4s and 6s": "R:/projects/IPL-DATA-ANALYSIS/player_insights/plots/topten_boundary.png",
    "Top 10 bowlers with most wickets": "R:/projects/IPL-DATA-ANALYSIS/player_insights/plots/top_bowler.jpg",
    "Best finishers (most runs in last 5 overs: over 16-20)": "R:/projects/IPL-DATA-ANALYSIS/player_insights/plots/most_run_5_over.jpg",
    "Most ‘Player of the Match’ awards": "R:/projects/IPL-DATA-ANALYSIS/player_insights/plots/player_of_match.jpg",
    "Top performing batsmen against specific teams": "R:/projects/IPL-DATA-ANALYSIS/player_insights/plots/batsmen_against_specific_team.jpg"
}

match_queries = {
    "Average runs scored per match / per over": "R:/projects/IPL-DATA-ANALYSIS/match_insights/plots/avg_run_per_match.jpg",
    "Total matches per season": "R:/projects/IPL-DATA-ANALYSIS/match_insights/plots/total_matches_per_season.jpg",
    "Highest and lowest team scores": "R:/projects/IPL-DATA-ANALYSIS/match_insights/plots/high_low_score.jpg", 
    "Super over matches count":"R:\projects\IPL-DATA-ANALYSIS\match_insights\plots\Super_over_%.jpg",  
    "Venues with highest win % for specific teams":"R:\projects\IPL-DATA-ANALYSIS\match_insights\plots\Venues_with_highest_win%.jpg"  
}


# 🎛 Sidebar controls
st.sidebar.title("📂 Select Insight Type")
insight_type = st.sidebar.radio("Insight Category", ["Team-Level", "Player-Level", "Match-Level"])

if insight_type == "Team-Level":
    selected_query = st.sidebar.selectbox("🔹 Team-Level Insights", list(team_queries.keys()))
    image_path = team_queries[selected_query]

elif insight_type == "Player-Level":
    selected_query = st.sidebar.selectbox("🔹 Player-Level Insights", list(player_queries.keys()))
    image_path = player_queries[selected_query]

elif insight_type == "Match-Level":
    selected_query = st.sidebar.selectbox("🔹 Match-Level Insights", list(match_queries.keys()))
    image_path = match_queries[selected_query]

# 📊 Display query and plot side by side
col1, col2 = st.columns([1, 2])
with col1:
    st.subheader("Query:")
    st.markdown(f"**{selected_query}**")

with col2:
    if os.path.exists(image_path):
        st.image(image_path, use_container_width=True)
    else:
        st.error("🚫 Plot not found. Please check the file path.")
