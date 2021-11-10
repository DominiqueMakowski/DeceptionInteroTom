import os

import matplotlib.pyplot as plt
import neurokit2 as nk
import numpy as np
import pandas as pd

### Get psychopy data files
directory = os.getcwd()
list_participants = os.listdir(directory + "/../../data/data_experimental")

### Utilities

def extract_taps(key, rt, started, task="Guess"):
    """keys: column name corresponding to when "space" is entered
    rt: column name corresponding to the cumulative time points when space is entered
    started: onset of trial wrt beginning of experiment
    """
    taps_n = len(data[key].dropna().iloc[0].split(','))
    taps = np.arange(1, taps_n + 1)

    start_task_time = data[started].dropna().iloc[0]
    tap_times = pd.DataFrame(data[rt].dropna())
    tap_times = np.array([start_task_time + float(i) for i in tap_times[rt].iloc[0].replace('[', '').replace(']', '').split(',')])

    df = pd.DataFrame([taps, tap_times]).T
    df.columns = ['Tap_Number', 'Tap_Times']
    df['Condition'] = task

    return df

df_all = pd.DataFrame()
### Loop through participants and extract data
for i, participant in enumerate(list_participants):
    data = pd.read_csv(directory + "/../../data/data_experimental/" + participant + "/heartbeat/" + participant + "_heartbeat.csv")

    data = data[["key_guess.keys", "key_guess.rt", "key_guess.started", # guessing condition
                 "key_noguess.keys", "key_noguess.rt", "key_noguess.started", # no guessing condition
                 "key_noguess_perturbed.keys", "key_noguess_perturbed.rt", "key_noguess_perturbed.started"]] # perturbed condition

    # Format data from three conditions
    if 'None' in np.array(data['key_guess.keys']):
        df_guess = pd.DataFrame([])
    else:
        df_guess = extract_taps("key_guess.keys", "key_guess.rt", "key_guess.started", task="Guess")

    if 'None' in np.array(data['key_noguess.keys']):
        df_noguess = pd.DataFrame([])
    else:
        df_noguess = extract_taps("key_noguess.keys", "key_noguess.rt", "key_noguess.started", task="NoGuess")

    if 'None' in np.array(data['key_noguess_perturbed.keys']):
        df_noguess_perturbed = pd.DataFrame([])
    else:
        df_noguess_perturbed = extract_taps("key_noguess_perturbed.keys", "key_noguess_perturbed.rt", "key_noguess_perturbed.started", task="NoGuess_Perturbed")

    # Merge dataframes from all 3 conditions
    df = pd.concat([df_guess, df_noguess, df_noguess_perturbed])
    df["ID"] = i + 1  # append participant number

    df_all = pd.concat([df_all, df])

df_all.to_csv("HCT_Part2.csv", index=False)
