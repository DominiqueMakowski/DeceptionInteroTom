import os

import neurokit2 as nk
import numpy as np
import pandas as pd

# Set working directory
list_participants = os.listdir("../../data/data_experimental")
df = pd.DataFrame()
for participant in list_participants:
    print(participant)
    if participant == "022":
        data = pd.DataFrame(
            {
                "ID": "22",
                "trial": np.arange(1, 81),
                "condition": ["Social"] * 40 + ["Polygraph"] * 40,
                "ECG_Rate_MeanRaw": np.repeat(np.nan, 80),
                "ECG_Rate_Mean": np.repeat(np.nan, 80),
            }
        )
    else:
        subdir = "../../data/data_experimental/" + participant + "/deception/"
        # Load data
        filename = [i for i in os.listdir(subdir) if i.endswith(".txt")][0]
        bio, sampling_rate = nk.read_bitalino(subdir + "/" + filename)
        # Clean ecg signal
        signal, _ = nk.ecg_process(bio["ECGBIT"], sampling_rate=sampling_rate)
        # Epoching
        events = nk.events_find(bio["LUX"], duration_min=3)
        index = np.arange(1, len(events["onset"]) + 1, 4)
        epochs = nk.epochs_create(
            signal, events["onset"][index], epochs_end=2, sampling_rate=sampling_rate
        )
        data = nk.ecg_analyze(epochs, sampling_rate=sampling_rate)
        data["ECG_Rate_MeanRaw"] = data["ECG_Rate_Mean"] + data["ECG_Rate_Baseline"]
        data["condition"] = ["Social"] * 40 + ["Polygraph"] * 40
        data["trial"] = np.arange(1, len(data) + 1)
        data["ID"] = participant.lstrip("0")
        data = data[["ID", "trial", "condition", "ECG_Rate_MeanRaw", "ECG_Rate_Mean"]]
    # Concat
    df = pd.concat([df, data], axis=0)


data_beh = pd.read_csv("../../data/data_combined.csv")
data_beh["ID"] = data_beh["ID"].astype(str)
data_all = pd.merge(df, data_beh)
assert len(data_beh) == len(data_all)
data_all.to_csv("../../data/data_combined_wPhysio.csv", index=False)
