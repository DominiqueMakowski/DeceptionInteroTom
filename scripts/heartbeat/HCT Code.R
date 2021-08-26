#### HP3804 EFA in RStudio =====================================  (stats generated factors)
# install the following 4 packages before you can run the commands below:
#foreign is for reading spss
#psych is for efa
#gpa rotation is for factor rotation
#hmisc is for some factor analysis
install.packages("foreign")
install.packages("psych")
install.packages("GPArotation")
install.packages("Hmisc")
install.packages("tidyverse")
install.packages("ggplot2")
install.packages("bayestestR")
install.packages("see")
install.packages("stringr")

# Load required packages
library(foreign)
library(psych)
library(GPArotation)
library(Hmisc)
library(tidyverse)
library(ggplot2)
library(bayestestR)
library(see)
library(stringr)

# Remember to first set your working directory from pull down menu or use the command below by inserting the directory path
setwd("  ")
setwd("~/Desktop/R Testing")



#**********YONI TASK Code Processing************************************
# read SPSS fa_eg.sav
# mydata <- read.spss('fa_eg.sav', to.data.frame = T)
setwd("~/Dropbox/FYP_Jia Rong/R Processing/heartbeat task processing in R")
library(tidyverse)
library(stringr)



mydata <- data.frame()
for (participant in list.files("../../data/")) {
  df_sub <- read.csv(paste0("../../data/", participant, "/heartbeat/", participant, "_heartbeat.csv"))[-c(6:9), -c(1, 3:8, 12:31, 33:38)]  
    mydata <- rbind(mydata, df_sub)
}


mydata <- mydata %>% 
rename(hbcount = heartbeatresponse.text,
       confidence = confidenceslider.response,
       confidenceRT = confidenceslider.rt)
      # guess = key_guess.keys,
      # guessRT = key_guess.rt,
      # noguess = key_noguess.keys,
     #  noguessRT = key_noguess.rt,
     #  onebreath = key_noguess_perturbed.keys,
      # onebreathRT = key_noguess_perturbed.rt) 

#partone <- mydata %>% 
  #drop_na() %>% 
 # select(c(1:4, 11))

partone <- mydata %>% 
  mutate(hbcount = str_remove_all(hbcount, "Enter Number")) %>% 
  mutate(hbcount = as.numeric(hbcount)) %>% 
  mutate(confidence = str_replace_all(confidence, "None", "0")) %>% 
  mutate(confidenceRT = str_replace_all(confidenceRT, "None", "0")) %>% 
  rename(HCT_timeframe = time,
         HCT_hbcount = hbcount,
         HCT_confidence = confidence,
         HCT_confidenceRT = confidenceRT,
         ID = participant) %>% 
  arrange(ID) 
  #arrange(ID,HCT_hbcount) %>% 
test <- partone %>% 
  pivot_wider(names_from = HCT_timeframe, values_from = c(HCT_hbcount, HCT_confidence, HCT_confidenceRT))

HCT <- read.csv("HCT.csv", stringsAsFactors = FALSE)[-c(2,8:10)] %>% 
  rename(participant = Participant.number)
  
HCT <- HCT %>% 
  pivot_longer(!participant, names_to = "hbcount", values_to = "value")

HCTfinal <- cbind(partone, HCT)


#HCTfinal <- HCTfinal %>% 
 # mutate(HCT_Accuracy = 1-(value - HCT_hbcount)/((value + HCT_hbcount)/2)) %>% #value = actual, HCT_hbcount = reported
 # select(c(1,3,6,9)) 

HCTfinal <-HCTfinal %>% 
  mutate(numerator = value - HCT_hbcount) %>% 
  mutate(numerator = abs(numerator)) %>% 
  mutate(HCT_Accuracy = 1-numerator/(value + HCT_hbcount)/2) %>% 
  select(1,3,6,10)
  


HCTfinal <- HCTfinal[, c(3,1,2,4)] %>% 
  arrange(participant, HCT_timeframe) %>% 
  mutate(HCT_confidence = as.numeric(HCT_confidence)) 

df_awarness <- data.frame()
for(participant in unique(HCTfinal$participant)) {
  conf <- HCTfinal[HCTfinal$participant == participant, "HCT_confidence"]
  acc <- HCTfinal[HCTfinal$participant == participant, "HCT_Accuracy"]
  awa <- cor(conf, acc, use = "pairwise.complete.obs")
  df_awarness <- rbind(df_awarness,
                       data.frame(participant = participant,
                                  HCT_Awareness = awa))
  
}

HCTfinal <- merge(HCTfinal, df_awarness, by = "participant") %>% 
  group_by(participant) %>% 
  summarise_all(mean, na.rm = TRUE) %>% 
  rename(HCT_Confidence = HCT_confidence)

HCTdata <- HCTfinal %>% 
  select(-c(2))

write.csv(HCTdata, file = "HCTdata.csv")



#cor(HCTfinal$HCT_confidence, HCTfinal$HCT_Accuracy, use = "pairwise.complete.obs", method = "pearson")

  



write.csv(partone, file = "HCT_30_partone.csv")

#PART 2
parttwo <- data.frame()
for (participant in list.files("../../data/")) {
  df_sub2 <- read.csv(paste0("../../data/", participant, "/heartbeat/", participant, "_heartbeat.csv"))[-c(1:5, 9), -c(1:13, 16:19, 22:25, 28:31, 33:38)]  
  parttwo <- rbind(parttwo, df_sub2)
}
  
parttwo <- parttwo %>% 
  rename(guess = key_guess.keys,
         guessRT = key_guess.rt,
         noguess = key_noguess.keys,
         noguessRT = key_noguess.rt,
         onebreath = key_noguess_perturbed.keys,
         onebreathRT = key_noguess_perturbed.rt) 

parttwo <- parttwo %>% 
  mutate(guesstotal = str_count(parttwo$guess, "space")) %>% 
  mutate(noguesstotal = str_count(parttwo$noguess, "space")) %>% 
  mutate(onebreathtotal = str_count(parttwo$onebreath, "space"))

parttwo <- parttwo %>% 
  select(c(7:10)) %>% 
  rename(ID = participant,
         HCT_guess = guesstotal,
         HCT_noguess = noguesstotal,
         HCT_onebreath = onebreathtotal)

write.csv(parttwo, file = "HCT_30_parttwo.csv")

--------------------------------------------------------------------------------
  mutate(guessRT = as.numeric(guessRT)) %>% 
  mutate(noguessRT = as.numeric(noguessRT)) %>% 
  mutate(onebreathRT = as.numeric(onebreathRT))
 

total_score <- mydata %>% 
  group_by(participant, condition) %>% 
  summarise(SubAvg = mean(subresp), RTAvg = mean(RT))
  #pivot_wider(names_from = condition, values_from = SubAvg, RTAvg) 

subscore <- mydata %>% 
  group_by(participant, condition, style) %>% 
  summarise(SubAvg = mean(subresp), RTAvg = mean(RT)) %>% 
  group_by(participant, condition) %>% 
 # mutate(Con_SubAvg = mean(SubAvg))

write.csv(total_score, file = "deceptiontask_processed.csv")
#-------------END---------------------------------------------------------------



mydata <- read.csv('raw001.csv', stringsAsFactors = FALSE)[-c(1:10), -c(5:34, 37:46, 48:53)] 
mydata2 <- read.csv('raw002.csv', stringsAsFactors = FALSE, row.names = NULL)[-c(1:10), -c(5:34, 37:46, 48:54)] 
  

#total score of affective, cognitive and physical
#affective = 49, cognitive = 37, physical = 15
  total_score <- results %>% 
    group_by(condition) %>% 
  summarise(total = sum(answer))





  


data_response <- mydata %>% 
  select(ends_with("_1")) %>% 
  as.data.frame() %>%  
  pivot_longer(cols = starts_with("Q"), names_to="Question", values_to="Ranking")

  
data_response %>% 
  ggplot(aes(x = reorder(Question, Ranking), y = Ranking, fill = Ranking)) +
  geom_bar(stat="identity") +
  see::theme_modern() +
  coord_flip()


  ylab("Number of Responses") +
  xlab("Question") +
  ggtitle("Plot of Question Response Rate")





### WHETHER QUESTIONS ARE ANSWERED OR NOT
data_response <- mydata %>% 
  select(ends_with(".1")) %>% 
  mutate(X34.1 = recode(X34.1, "I stay on a landed property" = "Answer")) %>% 
  mutate(X35.1 = recode(X35.1, No = "Answer")) %>% 
  mutate(X35.1 = recode(X35.1, Yes = "Answer")) %>%
  mutate(X35.1 = recode(X35.1, "I am not from NTU / I have graduated from NTU" = "Answer")) %>%
  mutate(X36.1 = recode(X36.1, Morning = "Answer")) %>% 
  mutate(X36.1 = recode(X36.1, NIght = "Answer")) %>% 
  mutate(X36.1 = recode(X36.1, "Both, I am active during the morning and night" = "Answer")) %>%
  mutate(X37.1 = recode(X37.1, "I drink both frequently" = "Answer")) %>% 
  mutate(X37.1 = recode(X37.1, "I do not drink both coffee and tea" = "Answer")) %>% 
  mutate(X38.1 = recode(X38.1, Both = "Answer")) %>% 
  mutate(X39.1 = recode(X39.1, "I am/was not from NTU" = "Answer")) %>% 
  mutate(X40.1 = recode(X40.1, "I am not from NTU" = "Answer")) %>% 
  mutate(X40.1 = recode(X40.1, "I have graduated from NTU" = "Answer")) %>% 
  mutate(X45.1 = recode(X45.1, No = "Answer")) %>% 
  mutate(X45.1 = recode(X45.1, Yes = "Answer")) %>% 
  mutate(X46.1 = recode(X46.1, No = "Answer")) %>% 
  mutate(X46.1 = recode(X46.1, Yes = "Answer")) %>% 
  mutate(X47.1 = recode(X47.1, No = "Answer")) %>% 
  mutate(X47.1 = recode(X47.1, Yes = "Answer")) %>% 
  mutate(X48.1 = recode(X48.1, "Light Sleeper" = "Answer")) %>% 
  mutate(X48.1 = recode(X48.1, "Heavy Sleeper" = "Answer")) %>% 
  mutate(X49.1 = recode(X49.1, "I do not smoke" = "Answer")) %>% 
  mutate(X49.1 = recode(X49.1, Socially = "Answer")) %>% 
  mutate(X49.1 = recode(X49.1, "Once in a while" = "Answer")) %>%
  mutate(X50.1 = recode(X50.1, "I do not drink alcohol at all" = "Answer")) %>% 
  mutate(X50.1 = recode(X50.1, "I rarely drink alcohol" = "Answer")) %>% 
  mutate(X50.1 = recode(X50.1, "I drink alcohol frequently (on a regular basis)" = "Answer")) %>% 
  mutate(X50.1 = recode(X50.1, "I drink alcohol socially (when situation or occasion requires it)" = "Answer")) %>%
  mutate(X51.1 = recode(X51.1, "Free-thinker" = "Answer")) %>% 
  mutate(X51.1 = recode(X51.1, "Buddhism" = "Answer")) %>%
  mutate(X51.1 = recode(X51.1, "Taoism" = "Answer")) %>% 
  mutate(X51.1 = recode(X51.1, "Christianity" = "Answer")) %>%
  mutate(X51.1 = recode(X51.1, "Islam" = "Answer")) %>%
  mutate(X51.1 = recode(X51.1, "Catholicism" = "Answer")) %>%
  mutate(X51.1 = recode(X51.1, "Hinduism" = "Answer")) %>%
  mutate(X51.1 = recode(X51.1, "Others" = "Answer")) %>%
  mutate(X52.1 = recode(X52.1, Yes = "Answer")) %>%
  mutate(X52.1 = recode(X52.1, No = "Answer")) %>%
  mutate(X53.1 = recode(X53.1, "Light On" = "Answer")) %>%
  mutate(X53.1 = recode(X53.1, "Light Off" = "Answer")) %>%
  mutate(X54.1 = recode(X54.1, "Apple" = "Answer")) %>%
  mutate(X54.1 = recode(X54.1, "Huawei" = "Answer")) %>%
  mutate(X54.1 = recode(X54.1, "Samsung" = "Answer")) %>%
  mutate(X54.1 = recode(X54.1, "Xiaomi" = "Answer")) %>%
  mutate(X54.1 = recode(X54.1, 'OPPO' = "Answer")) %>%
  mutate(X55.1 = recode(X55.1, "Apple" = "Answer")) %>%
  mutate(X55.1 = recode(X55.1, "HP" = "Answer")) %>%
  mutate(X55.1 = recode(X55.1, "Lenovo" = "Answer")) %>%
  mutate(X55.1 = recode(X55.1, "Asus" = "Answer")) %>%
  mutate(X55.1 = recode(X55.1, "Acer" = "Answer")) %>%
  mutate(X55.1 = recode(X55.1, "Dell" = "Answer")) %>%
  mutate(X55.1 = recode(X55.1, "Others" = "Answer")) %>% 
  sapply(function(x) ifelse(x == "Answer", 1, 0)) %>% 
  as.data.frame() %>%  
  mutate(Participant = seq(from = 1, to = nrow(mydata))) %>%
  mutate(Participant = paste0("Subject_", Participant)) %>% 
  pivot_longer(cols=starts_with("X"), names_to="Question", values_to="Answer") %>% 
  group_by(Question) %>% 
  summarise(total = sum(Answer))

data_response %>% 
  ggplot(aes(x = reorder(Question, total), y = total, fill = total)) +
  geom_bar(stat="identity") +
  see::theme_modern() +
  scale_fill_viridis_b() +
  ylab("Number of Responses") +
  xlab("Question") +
  coord_flip() +
  ggtitle("Plot of Question Response Rate")

           
  
  
### EASINESS OF QUESTIONS
#sort(increaasing),rank them,  

data_easy <- mydata %>% 
  select(ends_with(".3")) %>%  # selecting all the columns ends with _1  
  mutate_all(as.numeric) %>%  # change all columns to numeric
  drop_na() %>% 
  mutate(Participant = seq(from = 1, to = 45)) %>%
  mutate(Participant = paste0("Subject_", Participant)) %>%
  pivot_longer(cols=starts_with("X"), names_to="Question", values_to="Rating") %>% 
  mutate(Question = as.factor(Question)) %>% 
  group_by(Question) %>% 
  summarize(Mean = mean(Rating),
            CI_low = bayestestR::ci(Rating, ci=0.95)$CI_low,
            CI_high = bayestestR::ci(Rating, ci=0.95)$CI_high) 


# Plot easiness of questions
data_easy %>% 
  ggplot(aes(x = reorder(Question, Mean), y = Mean)) +
  geom_point(aes(y = Mean, color = Mean), size = 6) +
  see::theme_modern() +
  scale_color_viridis_c() +
  ylab("Average easiness rating of Questions") +
  xlab("Question") +
  coord_flip() +
  ggtitle("Plot of Question Difficulty")




# ggplots

# ggplot(data = mydata) + geom_bar(mapping = aes(x = Q5))

ggplot(data = mydata) + geom_bar(mapping = aes(x = X1, fill = X1))
ggplot(data = mydata) + geom_bar(mapping = aes(x = Q5, fill = Q5))

ggplot(data = mydata) + 
  geom_bar(mapping = aes(x = cut, fill = clarity), position = "dodge")


