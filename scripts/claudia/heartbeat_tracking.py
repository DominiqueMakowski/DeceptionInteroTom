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

def get_time_to_rpeak(ecg, start, stop, sampling_rate, taps, task="Guess"):
    """ecg: ecg signal
    start: onset time of the task
    stop: end time of the task
    taps: array of tap timings obtained from `extract_taps()`
    task: name of the task condition (appended to final dataframe)
    """

    # Process ecg signal
    ecg = nk.as_vector(ecg[start:stop])
    _, peaks = nk.ecg_process(ecg, sampling_rate=sampling_rate)
    rpeaks = peaks["ECG_R_Peaks"]

    # Get time to closest rpeak
    closest_rpeak = nk.find_closest(taps * sampling_rate, rpeaks)
    
    # positive = in systole
    # negative = in diastole
    time_to_rpeak = (taps * sampling_rate).astype(int) - closest_rpeak  # in samples

    df = pd.DataFrame(time_to_rpeak / sampling_rate)
    df[task] = task
    df.columns = ['Time_to_Rpeak', 'Condition']
    
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

    # Get time to closest Rpeaks
    if participant == '009':  # no taps for guess and no guess conditions
        df = get_time_to_rpeak(bio["ECGBIT"], start_noguess_perturbed, stop_noguess_perturbed,
                               sampling_rate, taps_noguess_perturbed, task="NoGuess_Perturbed")
    elif participant == '027':  # no taps for noguess_perturbed condition
        time_guess = get_time_to_rpeak(bio["ECGBIT"], start_guess, stop_guess, sampling_rate, taps_guess,
                                       task="Guess")
        time_noguess = get_time_to_rpeak(bio["ECGBIT"], start_noguess, stop_noguess, sampling_rate, taps_noguess,
                                         task="NoGuess")
        df = pd.concat([time_guess, time_noguess])
    else:
        time_guess = get_time_to_rpeak(bio["ECGBIT"], start_guess, stop_guess, sampling_rate, taps_guess,
                                       task="Guess")
        time_noguess = get_time_to_rpeak(bio["ECGBIT"], start_noguess, stop_noguess, sampling_rate, taps_noguess,
                                         task="NoGuess")
        time_noguess_perturbed = get_time_to_rpeak(bio["ECGBIT"], start_noguess_perturbed, stop_noguess_perturbed,
                                                   sampling_rate, taps_noguess_perturbed, task="NoGuess_Perturbed")
        df = pd.concat([time_guess, time_noguess, time_noguess_perturbed])

    df['ID'] = i + 1  # append participant number
    df_all = pd.concat([df_all, df])  # combine all participants

df_all.to_csv("HCT_Tracking.csv", na_rep="NA", index=False)
