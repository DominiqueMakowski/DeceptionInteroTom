# Load dependencies
import os

import matplotlib.pyplot as plt
import neurokit2 as nk
import numpy as np
import pandas as pd

# Set working directory
directory = os.getcwd()
list_participants = os.listdir(directory + "/../../data/data_experimental")
participant = '001'
subdir = directory + "/../../data/data_experimental/" + participant + "/heartbeat/"

# Load data
filename = [i for i in os.listdir(subdir) if i.endswith('.txt')][0]
bio, sampling_rate = nk.read_bitalino(subdir + "/" + filename)

# Clean ecg signal
ecg_cleaned = nk.ecg_clean(bio["ECGBIT"], sampling_rate=sampling_rate)

# Epoching
events = nk.events_find(bio["LUX"], event_conditions=['start', 'stop'] * 8)
event_conditions = np.array(['start', 'stop'] * 8)
events_start = np.array(events["onset"])[event_conditions == 'start']
events_duration = np.array(events["onset"])[event_conditions == 'stop'] - events_start

peaks_total = np.repeat(np.nan, len(events_start[:5]))
for i, start in enumerate(events_start[:5]):
    epoch = ecg_cleaned[start:start+events_duration[i]]
    peaks, info = nk.ecg_peaks(epoch, sampling_rate=sampling_rate)
    peaks_total[i] = len(info["ECG_R_Peaks"])
    print(peaks_total)

# Get behavioural data
