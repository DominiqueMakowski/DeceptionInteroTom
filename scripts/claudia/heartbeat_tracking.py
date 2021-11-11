# Load dependencies
import os

import matplotlib.pyplot as plt
import neurokit2 as nk
import numpy as np
import pandas as pd
from opensignalsreader import OpenSignalsReader

### Get psychopy data files ---------------------------------------------------
directory = os.getcwd()
list_participants = os.listdir(directory + "/../../data/data_experimental")

### Utilities -----------------------------------------------------------------
def extract_taps(data, key, rt, started, task="Guess"):
    """keys: column name corresponding to when "space" is entered
    rt: column name corresponding to the cumulative time points when space is entered
    started: onset of trial wrt beginning of experiment
    task: can be "Guess", "NoGuess", or "NoGuess_Perturbed"
    """
    if 'None' in np.array(data[key]):
        return pd.DataFrame([])  # return empty if no taps
    else:
        taps_n = len(data[key].dropna().iloc[0].split(','))
        taps = np.arange(1, taps_n + 1)

        # '.started' corresponds to timing of last tap of the condition
        last_tap_time = data[started].dropna().iloc[0]

        # get cumulative time points of taps
        tap_times = pd.DataFrame(data[rt].dropna())
        tap_times = np.array([float(i) for i in tap_times[rt].iloc[0].replace('[', '').replace(']', '').split(',')])
        lapsed = last_tap_time - tap_times[-1]
        tap_times = np.array([i + lapsed for i in tap_times])

        # Tidy df
        df = pd.DataFrame([taps, tap_times]).T
        df.columns = ['Tap_Number', 'Tap_Times']
        df['Condition'] = task
        return df

def align_taps(df, epochs, sampling_rate):
    # Align ecg to taps
    tap_times = np.array(df['Tap_Times'] * sampling_rate)
    taps = nk.find_closest(tap_times, np.array(epochs.index))
    epochs["Tap"] = 0
    for i in taps:
        epochs.loc[i, "Tap"] = 1

    # Condition column
    epochs["Condition"] = np.unique(df['Condition'])[0]

    return epochs


### Loop through participants and extract data --------------------------------
df_psychopy = pd.DataFrame()
df_bio = pd.DataFrame()

for i, participant in enumerate(list_participants):
    # i = 29
    # participant = '030'
    subdir = directory + "/../../data/data_experimental/" + participant + "/heartbeat/"

    # Get psychopy data
    data = pd.read_csv(subdir + participant + "_heartbeat.csv")

    data = data[["key_guess.keys", "key_guess.rt", "key_guess.started", # guessing condition
                 "key_noguess.keys", "key_noguess.rt", "key_noguess.started", # no guessing condition
                 "key_noguess_perturbed.keys", "key_noguess_perturbed.rt", "key_noguess_perturbed.started"]] # perturbed condition

    # Format data from three conditions
    df_guess = extract_taps(data, "key_guess.keys", "key_guess.rt", "key_guess.started", task="Guess")
    df_noguess = extract_taps(data, "key_noguess.keys", "key_noguess.rt", "key_noguess.started", task="NoGuess")
    df_noguess_perturbed = extract_taps(data, "key_noguess_perturbed.keys", "key_noguess_perturbed.rt", "key_noguess_perturbed.started", task="NoGuess_Perturbed")

    # Merge dataframes from all 3 conditions
    df = pd.concat([df_guess, df_noguess, df_noguess_perturbed])
    df["ID"] = i + 1  # append participant number
    df_psychopy = pd.concat([df_psychopy, df])

    # Raw ecg signal
    filename = [i for i in os.listdir(subdir) if i.endswith('.txt')][0]
    bio, sampling_rate = nk.read_bitalino(subdir + "/" + filename)

    # Find events
    # nk.events_find(bio["LUX"])

    # Get R-peaks
    _, peaks = nk.ecg_peaks(bio["ECGBIT"], sampling_rate=sampling_rate)

    # Epoch around R-peaks
    epochs = nk.epochs_create(ecg, sampling_rate=sampling_rate, events=peaks["ECG_R_Peaks"], epochs_start=-0.5, epochs_end=0.5)
    epochs_df = nk.epochs_to_df(epochs)

    # Segment according to conditions
    task_end_times = np.floor(np.array(df.groupby(['Condition']).max()['Tap_Times']) * sampling_rate).astype(int)
    start = np.floor(df['Tap_Times'].iloc[0] * sampling_rate).astype(int)

    if participant == '009':  # no taps for guess and noguess conditions
        epoched = epochs_df[start:task_end_times[0]]

        # Align ecg to taps
        epoched = align_taps(df_noguess_perturbed, epoched, sampling_rate)
    else:
        epochs_guess = epochs_df[start:task_end_times[0]]
        epochs_noguess = epochs_df[task_end_times[0]:task_end_times[1]]
        epochs_noguess_perturbed = epochs_df[task_end_times[1]:task_end_times[2]]

        # Align ecg to taps
        epochs_guess = align_taps(df_guess, epochs_guess, sampling_rate)
        epochs_noguess = align_taps(df_noguess, epochs_noguess, sampling_rate)
        epochs_noguess_perturbed = align_taps(df_noguess_perturbed, epochs_noguess_perturbed, sampling_rate)
        epoched = pd.concat([epochs_guess, epochs_noguess, epochs_noguess_perturbed])

    epoched['ID'] = i + 1  # append participant number
    df_bio = pd.concat([df_bio, epoched])

    # Compute number of taps in diastole/systole
    # n_diastole = epochs_guess[epochs_guess['Time'] < 0]['Tap'].sum()
    # n_systole = epochs_guess[epochs_guess['Time'] > 0]['Tap'].sum()

df_all.to_csv("HCT_Part2.csv", index=False)
df_bio.to_csv("HCT_Epoched.csv", index=False])
