import streamlit as st
import pickle
import pandas as pd


teams = ['Royal Challengers Bangalore',
    'Punjab Kings',
    'Delhi Capitals',
    'Mumbai Indians', 
    'Kolkata Knight Riders',
    'Rajasthan Royals', 
    'Chennai Super Kings',
    'Sunrisers Hyderabad',
    'Lucknow Super Giants', 
    'Gujarat Titans']

cities = ['Bangalore', 'Chandigarh', 'Delhi', 'Mumbai', 'Kolkata', 'Jaipur',
       'Hyderabad', 'Chennai', 'Cape Town', 'Port Elizabeth', 'Durban',
       'Centurion', 'East London', 'Johannesburg', 'Kimberley',
       'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
       'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
       'Rajkot', 'Kanpur', 'Bengaluru', 'Indore', 'Dubai', 'Sharjah',
       'Navi Mumbai', 'Lucknow', 'Guwahati', 'Mohali']

pipe = pickle.load(open('pipe_lr.pkl','rb'))
st.markdown("<h3 style='text-align: center;'>IPL Match Winning Probability Predictor</h3>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Select the batting team',sorted(teams))
    bowling_team_options = [team for team in teams if team != batting_team]
with col2:
    bowling_team = st.selectbox('Select the bowling team',sorted(bowling_team_options))

selected_city = st.selectbox('Select host city',sorted(cities))

target = st.number_input('Target', min_value=0, step=1, format="%d")

col3,col4,col5 = st.columns(3)

with col3:
    score = st.number_input('Score', min_value=0, step=1, format="%d")
with col4:
    overs = st.number_input('Overs completed',min_value=0.0, max_value=20.0, step=0.1,format="%.1f")
with col5:
    wickets = st.number_input('Wickets fallen',min_value=0, max_value=10, step=1, format="%d")

if st.button('Predict Probability'):
    if overs - int(overs) > 0.5:
        st.error("Invalid input for overs. Please enter a value up to .5 for partial overs (e.g., 2.3, 2.5, 19.5).")
    else:
        runs_left = target - score
        overs_completed = int(overs)
        balls_completed = round((overs - overs_completed) * 10)
        total_balls_completed = (overs_completed * 6) + balls_completed
        balls_left = 120 - total_balls_completed

        wickets_left = 10 - wickets
        if total_balls_completed == 0:
            current_run_rate = 0
        else:
            current_run_rate = score * 6 / total_balls_completed
        required_run_rate = (runs_left * 6) / balls_left

        input_df = pd.DataFrame({'batting_team':[batting_team],'bowling_team':[bowling_team],'city':[selected_city],'runs_left':[runs_left],'balls_left':[balls_left],'wickets':[wickets_left],'total_runs_x':[target],'current_run_rate':[current_run_rate],'required_run_rate':[required_run_rate]})

        result = pipe.predict_proba(input_df)
        loss = result[0][0]
        win = result[0][1]
        st.header(batting_team + "- " + str(round(win*100)) + "%")
        st.header(bowling_team + "- " + str(round(loss*100)) + "%")