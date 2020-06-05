import pandas as pd
from pandas.testing import assert_frame_equal
import hw_4_test_gen as h4tg

def generate_test_dict():
    print("Fetching test data...")
    test_list = [h4tg.create_standard_teams_test(),
                 h4tg.create_nba_teams_test(),
                 h4tg.create_standard_players_test(),
                 h4tg.create_nba_players_test(),
                 h4tg.count_nba_player_nationalities_test()
    ]
    test_dict = dict()
    for i, df in enumerate(test_list):
        dict_k = "question_{}".format(i + 1)
        dict_v = df
        test_dict[dict_k] = dict_v
    return test_dict

def generate_answer_dict(answer_list):
    print("Fetching our answers...")
    answer_dict = dict()
    for i, df in enumerate(answer_list):
        dict_k = "question_{}".format(i + 1)
        dict_v = df
        answer_dict[dict_k] = dict_v
    return answer_dict

def run_tests(test_dict, answer_dict):
    summary = {
        'Question 1': 0,
        'Question 2': 0,
        'Question 3': 0,
        'Question 4': 0,
        'Question 5': 0
    }
    print("###### TESTING STARTS ######")
    for i in range(1, 6):
        dict_key = "question_{}".format(i)
        answer_df = answer_dict[dict_key]
        test_df = test_dict[dict_key]
        try:
            answer_df_str = answer_df.astype(str)
            test_df_str = test_df.astype(str)
            answer_df.columns = test_df.columns
            answer_df.index = test_df.index
            assert_frame_equal(test_df, answer_df)
            summary["Question {}".format(i)] = 2
            print("Congrats! answer {} passed!".format(i))
        except:
            print("Unfortunately, answer {} did not pass, try again!".format(i))
    print("###### TESTING ENDS ######")
    print("Submission Summary")
    for k, v in summary.items():
        print("{}: {}".format(k, v))
    print("Total Points on Homework 4: {}".format(sum(summary.values())))