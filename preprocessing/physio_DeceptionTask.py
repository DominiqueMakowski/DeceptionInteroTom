import os

import neurokit2 as nk
import numpy as np
import pandas as pd

# Set working directory
list_participants = os.listdir("../data/data_experimental")
df = pd.DataFrame()
df_signal = pd.DataFrame()
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
        subdir = "../data/data_experimental/" + participant + "/deception/"
        # Load data
        filename = [i for i in os.listdir(subdir) if i.endswith(".txt")][0]
        bio, sampling_rate = nk.read_bitalino(subdir + "/" + filename)
        # Clean ecg signal
        signal, _ = nk.ecg_process(bio["ECGBIT"], sampling_rate=sampling_rate)
        # Initialize data
        data = pd.DataFrame(
            {
                "condition": ["Social"] * 40 + ["Polygraph"] * 40,
                "trial": np.arange(1, 81),
                "ID": [participant.lstrip("0")] * 80,
            }
        )
        # Epoching
        events = nk.events_find(bio["LUX"], duration_min=3)
        index = np.arange(1, len(events["onset"]) + 1, 4)
        for window in [3.5, 3, 2.5, 2]:
            epochs = nk.epochs_create(
                signal,
                events["onset"][index],
                epochs_start=-0.5,
                epochs_end=window,
                sampling_rate=sampling_rate,
            )
            if window == 3.5:  # Store rate signal for the longest epoch
                rate_signal = pd.DataFrame([epochs[i]["ECG_Rate"].values for i in epochs.keys()])
                data[f"ECG_Rate_MeanRaw_2_3s"] = rate_signal.loc[:, 2500:3500].mean(axis=1)
                data[f"ECG_Rate_Mean_2_3s"] = data[f"ECG_Rate_MeanRaw_2_3s"] - rate_signal[500]
                data[f"ECG_Rate_MeanRaw_1.5_2.5s"] = rate_signal.loc[:, 2000:3000].mean(axis=1)
                data[f"ECG_Rate_Mean_1.5_2.5s"] = (
                    data[f"ECG_Rate_MeanRaw_1.5_2.5s"] - rate_signal[500]
                )
                data[f"ECG_Rate_MeanRaw_1.5_3s"] = rate_signal.loc[:, 2000:3500].mean(axis=1)
                data[f"ECG_Rate_Mean_1.5_3s"] = data[f"ECG_Rate_MeanRaw_1.5_3s"] - rate_signal[500]
                rate_signal = pd.concat([data, rate_signal], axis=1)
                df_signal = pd.concat([df_signal, rate_signal], axis=0)
            temp = nk.ecg_analyze(epochs, sampling_rate=sampling_rate).reset_index(drop=True)
            data[f"ECG_Rate_MeanRaw_{window}s"] = temp["ECG_Rate_Mean"] + temp["ECG_Rate_Baseline"]
            data[f"ECG_Rate_Mean_{window}s"] = temp["ECG_Rate_Mean"]

    # Concat
    df = pd.concat([df, data], axis=0)

# Load behavioural
data_beh = pd.read_csv("../data/data_combined.csv")
data_beh["ID"] = data_beh["ID"].astype(str)

# Merge features
data_all = pd.merge(df, data_beh)
assert len(data_beh) == len(data_all)
data_all.to_csv("../data/data_combined_wPhysio.csv", index=False)

# Merge signals
df_signal = pd.merge(df_signal, data_beh)
df_signal.groupby(["ID", "condition", "instruction"])[np.arange(4000)].mean().to_csv(
    "../data/data_physio_DeceptionTask.csv"
)
