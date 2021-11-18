import os

import neurokit2 as nk
import numpy as np
import pandas as pd

# Set working directory
directory = os.getcwd()
list_participants = os.listdir(directory + "/data/data_experimental")
list_participants.remove("022")  # only have 133 events
df = pd.DataFrame()
for participant in list_participants[21:]:
    print(participant)
    if participant == "022":
        data = pd.DataFrame({"ID" : participant,
                             "condition" : ["Social"] * 40 + ["Polygraph"] * 40,
                             "trial" : np.arange(1, 81),
                             "ECG_Rate_MeanRaw" : np.repeat(np.nan, 80),
                             "ECG_Rate_Mean" : np.repeat(np.nan, 80)})
    else:
        subdir = directory + "/data/data_experimental/" + participant + "/deception/"
    # Load data
        filename = [i for i in os.listdir(subdir) if i.endswith('.txt')][0]
        bio, sampling_rate = nk.read_bitalino(subdir + "/" + filename)
    # Clean ecg signal
        signal, _ = nk.ecg_process(bio["ECGBIT"], sampling_rate=sampling_rate)
    # Epoching
        events = nk.events_find(bio["LUX"], duration_min=3)
        index = np.arange(1, len(events["onset"]) + 1, 4)
        epochs = nk.epochs_create(signal, events["onset"][index], epochs_end = 2, sampling_rate=sampling_rate)
        data = nk.ecg_analyze(epochs, sampling_rate=sampling_rate)
        data["ECG_Rate_MeanRaw"] = data["ECG_Rate_Mean"] + data["ECG_Rate_Baseline"]
        data["condition"] = ["Social"] * 40 + ["Polygraph"] * 40
        data["trial"] = np.arange(1, len(data) + 1)
        data = data[["ID", "trial", "condition", "ECG_Rate_MeanRaw", "ECG_Rate_Mean"]]
    # Concat
    data["ID"] = participant.lstrip("0")
    df = pd.concat([df, data], axis=0)


data_beh = pd.read_csv(directory + "/data/data_combined.csv")
data_beh["ID"] = data_beh["ID"].astype(str)
data_all = pd.merge(data_beh, df, on = ["ID", "trial"])
assert len(data_beh) == len(data_all)
data_all.to_csv(directory + "/data/data_combined2.csv", index = False)