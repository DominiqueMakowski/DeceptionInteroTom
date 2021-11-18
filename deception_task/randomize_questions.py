import numpy as np
import pandas as pd

# THINGS TO CHANGE

participant = "030"  # participant ID

# THINGS DO NOT NEED TO CHANGE

master_list = pd.read_excel(participant + "_master_list.xlsx")  # list of 20 questions

video_list = master_list["video"][:40].sample(frac=1).reset_index(drop=True)

bitalino_list = master_list["bitalino"][:40].sample(frac=1).reset_index(drop=True)

# list of all item dataframes
item_list = np.array_split(master_list.iloc[:, :4], 20)  ## change this to 20 later

# RANDOMIZE AND PARITION QUESTIONS INTO 2 SETS FOR 2 CONDITIONS
# loop through item_list to pick 2 questions for each condition
list_social = []
list_polygraph = []
for i in range(len(item_list)):
    # shuffle the truth and lie items
    truth = item_list[i][0:2].sample(frac=1)
    lie = item_list[i][2:4].sample(frac=1)
    # extend list of questions
    list_social.extend([truth.iloc[:1, :], lie.iloc[:1, :]])
    list_polygraph.extend([truth.iloc[1:2, :], lie.iloc[1:2, :]])

df_social = pd.concat(list_social).reset_index(drop=True)
df_social = pd.concat([df_social, video_list], axis=1).sample(frac=1).reset_index(drop=True)

df_poly = pd.concat(list_polygraph).reset_index(drop=True)
df_poly = pd.concat([df_poly, bitalino_list], axis=1).sample(frac=1).reset_index(drop=True)

# SAVE TO FILES

df_social.to_csv(participant + '_social_questions.csv', index = False, header = True)

df_poly.to_csv(participant + '_poly_questions.csv', index = False, header = True)



