# Load dependencies
import os

import matplotlib.pyplot as plt
import neurokit2 as nk
import numpy as np
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'

### Get psychopy data files ---------------------------------------------------
directory = os.getcwd()
list_participants = os.listdir(directory + "/../../data/data_experimental")

### Utilities -----------------------------------------------------------------
def extract_taps(data, key, rt):
    """keys: column name corresponding to when "space" is entered
    rt: column name corresponding to the cumulative time points when space is entered
    """
    if 'None' in np.array(data[key]):
        return np.array([])  # return empty if no taps
    else:
        # get cumulative time points of taps
        tap_times = pd.DataFrame(data[rt].dropna())
        tap_times = np.array([float(i) for i in tap_times[rt].iloc[0].replace('[', '').replace(']', '').split(',')])

        return tap_times

def align_taps(ecg, start, stop, sampling_rate, taps, task="Guess"):
    """ecg: ecg signal
    start: onset time of the task
    stop: end time of the task
    taps: array of tap timings obtained from `extract_taps()`
    task: name of the task condition (appended to final dataframe)
    """

    # Process ecg signal
    ecg = nk.as_vector(ecg[start:stop])
    ecg_processed, peaks = nk.ecg_process(ecg, sampling_rate=sampling_rate)
    df = ecg_processed[["ECG_Clean", "ECG_R_Peaks"]]  # keep only cleaned and R peaks cols

    # Index periods in which taps are expected
    search = np.repeat(np.nan, len(ecg))
    interval = 0.2 * sampling_rate  # 0.2 milliseconds epoch
    before_beat_interval = np.concatenate([np.arange(peak - interval, peak) for peak in peaks['ECG_R_Peaks']])
    after_beat_interval = np.concatenate([np.arange(peak, peak + interval) for peak in peaks['ECG_R_Peaks']])

    for i, _ in enumerate(search):
        if i in before_beat_interval:
            search[i] = 0  # taps not expected 0.2 ms before beat
        elif i in after_beat_interval:
            search[i] = 1  # taps expected 0.2 ms after beat

    df["Periods"] = search  # append indexes of periods to ecg dataframe

    # Align ecg to taps
    taps = nk.find_closest(taps * sampling_rate, np.array(df.index))
    df["Tap"] = 0
    if isinstance(taps, np.integer):  # if only one tap
        df.loc[taps, "Tap"] = 1
    else:
        for i in taps:
            df.loc[i, "Tap"] = 1
    df["Condition"] = task

    return df


### Loop through participants and extract data --------------------------------
df_all = pd.DataFrame([])

for i, participant in enumerate(list_participants):
#     # Check number of photosensor events per participant (16 expected)  
#     subdir = directory + "/../../data/data_experimental/" + participant + "/heartbeat/"
#     filename = [i for i in os.listdir(subdir) if i.endswith('.txt')][0]
#     bio, sampling_rate = nk.read_bitalino(subdir + "/" + filename)
#     n_events = len(nk.events_find(bio["LUX"])['onset'])
#     print(f"{participant} : {n_events} events detected\n======================")
#     # participants 010: 1 extra
#     # participants 012, 023: 3 extra

    # Directory of where heartbeat data is stored
    subdir = directory + "/../../data/data_experimental/" + participant + "/heartbeat/"

    # Get psychopy data
    print(f"Reading psychopy data for participant: {participant}\n======================")
    data = pd.read_csv(subdir + participant + "_heartbeat.csv")

    data = data[["key_guess.keys", "key_guess.rt", # guessing condition
                 "key_noguess.keys", "key_noguess.rt", # no guessing condition
                 "key_noguess_perturbed.keys", "key_noguess_perturbed.rt"]] # perturbed condition

    # Extract taps from three conditions
    taps_guess = extract_taps(data, "key_guess.keys", "key_guess.rt")
    taps_noguess = extract_taps(data, "key_noguess.keys", "key_noguess.rt")
    taps_noguess_perturbed = extract_taps(data, "key_noguess_perturbed.keys", "key_noguess_perturbed.rt")

    # Read raw ecg signal
    print(f"Reading ecg data for participant: {participant}\n======================")
    filename = [i for i in os.listdir(subdir) if i.endswith('.txt')][0]
    bio, sampling_rate = nk.read_bitalino(subdir + "/" + filename)

    # Find events (events 1 - 10 for heartbeat counting, 11 - 16 for 3 conditions of heartbeat tracking)
    events_all = nk.events_find(bio["LUX"], duration_min=3)
    start_guess, stop_guess = events_all['onset'][10], events_all['onset'][11]
    start_noguess, stop_noguess = events_all['onset'][12], events_all['onset'][13]
    start_noguess_perturbed, stop_noguess_perturbed = events_all['onset'][14], events_all['onset'][15]

    # Align taps to ECG peaks
    if participant == '009':  # no taps for guess and no guess conditions
        df = align_taps(bio["ECGBIT"], start_noguess_perturbed,
                        stop_noguess_perturbed, sampling_rate,
                        taps_noguess_perturbed, task="NoGuess_Perturbed")
    elif participant == '027':  # no taps for noguess_perturbed condition
        df_guess = align_taps(bio["ECGBIT"], start_guess, stop_guess, sampling_rate,
                              taps_guess, task="Guess")
        df_noguess = align_taps(bio["ECGBIT"], start_noguess, stop_noguess, sampling_rate,
                              taps_noguess, task="NoGuess")
        df = pd.concat([df_guess, df_noguess])      
    else:
        df_guess = align_taps(bio["ECGBIT"], start_guess, stop_guess, sampling_rate,
                              taps_guess, task="Guess")
        df_noguess = align_taps(bio["ECGBIT"], start_noguess, stop_noguess, sampling_rate,
                              taps_noguess, task="NoGuess")
        df_noguess_perturbed = align_taps(bio["ECGBIT"], start_noguess_perturbed,
                                          stop_noguess_perturbed, sampling_rate,
                                          taps_noguess_perturbed, task="NoGuess_Perturbed")
        df = pd.concat([df_guess, df_noguess, df_noguess_perturbed])

    df['ID'] = i + 1  # append participant number
    
    # Visualize to see where taps align with ecg signal
    # tap_indices = np.where(df["Tap"] == 1)[0]
    # peaks = np.where(df["ECG_R_Peaks"] == 1)[0]
    # signal = nk.as_vector(df["ECG_Clean"])
    # nk.events_plot(events=[peaks, tap_indices], signal=signal)
    
    df_all = pd.concat([df_all, df])  # combine all participants

df_all.to_csv("HCT_Part2.csv", na_rep="NA", index=False)
