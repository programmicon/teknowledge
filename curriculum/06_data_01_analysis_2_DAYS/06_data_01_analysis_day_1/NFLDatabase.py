# Contains data for 10 teams with the best offense, defense, or passing Statistics
# for the 2016-17 football season, from: http://www.nfl.com/stats/team
NFLData = {
    "New England Patriots": {
        "Points": 27.6,
        "Yards": 386.2,
        "Pass Yards": 269.2,
        "Rush Yards": 117.0,
        "Passing Statistics": {  # Post-Season
            "Quarterback Name": "Tom Brady",
            "Attempted": 142,
            "Completed": 93,
            "Yards": 1137,
            "Completion Percent": 65.5,
            "Yards Per Attempt": 8.0,
            "Touchdown": 7,
            "Touchdown Percent": 4.9,
            "Interception": 3,
            "Interception Percent": 2.1,
            "Long": 48,
            "Sack": 9,
            "Sack Per Lost": 42,
            "Rating": 97.7,
        },
    },
    "Dallas Cowboys": {
        "Points": 26.3,
        "Yards": 376.7,
        "Pass Yards": 226.9,
        "Rush Yards": 149.8,
        "Passing Statistics": {  # Post-Season
            "Quarterback Name": "Dak Prescott",
            "Attempted": 38,
            "Completed": 24,
            "Yards": 302,
            "Completion Percent": 63.2,
            "Yards Per Attempt": 7.9,
            "Touchdown": 3,
            "Touchdown Percent": 7.9,
            "Interception": 1,
            "Interception Percent": 2.6,
            "Long": 40,
            "Sack": 2,
            "Sack Per Lost": 11,
            "Rating": 103.2,
        },
    },
    "Atlanta Falcons": {
        "Points": 33.8,
        "Yards": 415.8,
        "Pass Yards": 295.3,
        "Rush Yards": 120.5,
        "Passing Statistics": {  # Post-Season
            "Quarterback Name": "Matt Ryan",
            "Attempted": 98,
            "Completed": 70,
            "Yards": 1014,
            "Completion Percent": 71.4,
            "Yards Per Attempt": 10.3,
            "Touchdown": 9,
            "Touchdown Percent": 9.2,
            "Interception": 0,
            "Interception Percent": 0.0,
            "Long": 73,
            "Sack": 8,
            "Sack Per Lost": 59,
            "Rating": 135.3,
        },
    },
    "Green Bay Packers": {
        "Points": 27.0,
        "Yards": 368.8,
        "Pass Yards": 262.4,
        "Rush Yards": 106.3,
        "Passing Statistics": {  # Post-Season
            "Quarterback Name": "Aaron Rodgers",
            "Attempted": 128,
            "Completed": 80,
            "Yards": 1004,
            "Completion Percent": 62.5,
            "Yards Per Attempt": 7.8,
            "Touchdown": 9,
            "Touchdown Percent": 7.0,
            "Interception": 2,
            "Interception Percent": 1.6,
            "Long": 42,
            "Sack": 10,
            "Sack Per Lost": 79,
            "Rating": 103.8,
        },
    },
    "Pittsburgh Steelers": {
        "Points": 24.9,
        "Yards": 372.6,
        "Pass Yards": 262.6,
        "Rush Yards": 110.0,
        "Passing Statistics": {  # Post-Season
            "Quarterback Name": "Ben Roethlisberger",
            "Attempted": 96,
            "Completed": 64,
            "Yards": 745,
            "Completion Percent": 66.7,
            "Yards Per Attempt": 7.7,
            "Touchdown": 3,
            "Touchdown Percent": 3.1,
            "Interception": 4,
            "Interception Percent": 4.2,
            "Long": 62,
            "Sack": 2,
            "Sack Per Lost": 15,
            "Rating": 82.6,
        },
    },
    "Houston Texans": {
        "Points": 17.4,
        "Yards": 314.7,
        "Pass Yards": 198.5,
        "Rush Yards": 116.2,
        "Passing Statistics": {  # Post-Season
            "Quarterback Name": "Brock Osweiler",
            "Attempted": 25,
            "Completed": 14,
            "Yards": 168,
            "Completion Percent": 56.0,
            "Yards Per Attempt": 6.7,
            "Touchdown": 1,
            "Touchdown Percent": 4.0,
            "Interception": 0,
            "Interception Percent": 0.0,
            "Long": 38,
            "Sack": 0,
            "Sack Per Lost": 0,
            "Rating": 90.1,
        },
    },
    "Oakland Raiders": {
        "Points": 26.0,
        "Yards": 373.3,
        "Pass Yards": 253.2,
        "Rush Yards": 120.1,
        "Passing Statistics": {  # Post-Season
            "Quarterback Name": "Connor Cook",
            "Attempted": 45,
            "Completed": 18,
            "Yards": 161,
            "Completion Percent": 40.0,
            "Yards Per Attempt": 3.6,
            "Touchdown": 1,
            "Touchdown Percent": 2.2,
            "Interception": 3,
            "Interception Percent": 6.7,
            "Long": 20,
            "Sack": 3,
            "Sack Per Lost": 22,
            "Rating": 30.0,
        },
    },
    "Seattle Seahawks": {
        "Points": 22.1,
        "Yards": 357.2,
        "Pass Yards": 257.8,
        "Rush Yards": 99.4,
        "Passing Statistics": {  # Post-Season
            "Quarterback Name": "Russel Wilson",
            "Attempted": 60,
            "Completed": 40,
            "Yards": 449,
            "Completion Percent": 66.7,
            "Yards Per Attempt": 7.5,
            "Touchdown": 4,
            "Touchdown Percent": 6.7,
            "Interception": 2,
            "Interception Percent": 3.3,
            "Long": 42,
            "Sack": 6,
            "Sack Per Lost": 31,
            "Rating": 97.2,
        },
    },
    "New York Giants": {
        "Points": 19.4,
        "Yards": 330.7,
        "Pass Yards": 242.4,
        "Rush Yards": 88.2,
        "Passing Statistics": {  # Post-Season
            "Quarterback Name": "Eli Manning",
            "Attempted": 44,
            "Completed": 23,
            "Yards": 229,
            "Completion Percent": 52.3,
            "Yards Per Attempt": 6.8,
            "Touchdown": 1,
            "Touchdown Percent": 2.3,
            "Interception": 1,
            "Interception Percent": 2.3,
            "Long": 51,
            "Sack": 2,
            "Sack Per Lost": 4,
            "Rating": 72.1,
        },
    },
    "Miami Dolphins": {
        "Points": 22.7,
        "Yards": 332.8,
        "Pass Yards": 218.8,
        "Rush Yards": 114.0,
        "Passing Statistics": {  # Post-Season
            "Quarterback Name": "Matt Moore",
            "Attempted": 36,
            "Completed": 29,
            "Yards": 289,
            "Completion Percent": 80.6,
            "Yards Per Attempt": 8.0,
            "Touchdown": 1,
            "Touchdown Percent": 2.8,
            "Interception": 1,
            "Interception Percent": 2.8,
            "Long": 37,
            "Sack": 5,
            "Sack Per Lost": 36,
            "Rating": 97.8,
        },
    },
}
