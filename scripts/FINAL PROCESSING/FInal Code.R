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
install.packages("psycho")
install.packages("lme4")
install.packages("rstatix")
install.packages("glmer")

# Load required packages
library(foreign)
library(psych)
library(GPArotation)
library(Hmisc)
library(tidyverse)
library(ggplot2)
library(bayestestR)
library(see)

# Remember to first set your working directory from pull down menu or use the command below by inserting the directory path
setwd("  ")
setwd("~/Desktop/R Testing")



#**********YONI TASK Code Processing************************************
# read SPSS fa_eg.sav
# mydata <- read.spss('fa_eg.sav', to.data.frame = T)
setwd("~/Dropbox/FYP_Jia Rong/R Processing/FINAL PROCESSING")
library(tidyverse)
library(lme4)
library(rstatix)

BES <- read.csv('BES_30processed.csv', stringsAsFactors = FALSE, header = TRUE)[-c(1)]
LIE <- read.csv('lieprofiler_30.csv', stringsAsFactors = FALSE, header = TRUE)[-c(1,2)]
MAIA <- read.csv('MAIA2_30processed.csv', stringsAsFactors = FALSE, header = TRUE)[-c(1,2)]
SRP3 <- read.csv('SRP3_30processed.csv', stringsAsFactors = FALSE, header = TRUE)[-c(1,2)]
YONI <- read.csv('yonitask_30processed.csv', stringsAsFactors = FALSE, header = TRUE)[-c(1,2)]
HCT <- read.csv('HCTdata.csv', stringsAsFactors = FALSE, header = TRUE)[-c(1,2)]
#DT <- read.csv('deceptiontask_30processed.csv', stringsAsFactors = FALSE, header = TRUE)[-c(1,2)]
DTNEW <- read.csv('deceptiontask_30_full80items.csv', stringsAsFactors = FALSE, header = TRUE)[-c(1)]
Demo <- read.csv('demo_30.csv', stringsAsFactors = FALSE, header = TRUE)[-c(1,2,3,4:6,9,11,12,18)]
Errors <- read.csv('Errors.csv', stringsAsFactors = FALSE, header = TRUE)[-c(1)]


#Physio data load
#Phy <- read.csv('DT.csv', stringsAsFactors = FALSE, header = TRUE) [-c(1),] %>% 
  rename(participant = Participant.number)

#HCTphy <- read.csv('HCT.csv', stringsAsFactors = FALSE, header = TRUE) %>% 
  rename(participant = Participant.number,
         HC1 = X0,
         HC2 = X1,
         HC3 = X2,
         HC4 = X3,
         HC5 = X4,
         HCT_guess = X5,
         HCT_noguess = X6,
         HCT_onebreath = X7)
#RSTphy <- read.csv('RST.csv', stringsAsFactors = FALSE, header = TRUE) %>% 
#  rename(participant = Participant.number)

#test <- test[!(test$Occupation == "Management" & test$AvgMonthSpend > 59.24 ) | !(test$Occupation == "Manual" & test$AvgMonthSpend > 54.28 ),] 


DTNEW <- DTNEW [, c(7,2,3,4,5,6,1)] %>% 
  rename(ID = participant)
final <- cbind(BES, LIE, MAIA, SRP3, YONI, HCT, Demo)

Finalset <- merge(DTNEW, final, by = "ID")

Finaldata <- cbind(Errors, Finalset)

#Finalset <- merge(HCTPhy, Finalset, by = "ID")

write.csv(Finaldata, file = "BehaviouraldataNEW.csv")



#------------------------------------------------------------------------------
New <- merge(Phy, DTNEW, by = "participant")

write.csv(Finalset, file = "fullset.csv")




---------------------------------------------------------------------------------

  
  
  
  mydata <- data.frame()
for (participant in list.files("../../data/")) {
  df_sub <- read.csv(paste0("../../data/", participant, "/deception/", participant, "_deceptiontask.csv"), header = FALSE)[-c(1:11), -c(5:34, 37:46, 48:54)]  
    mydata <- rbind(mydata, df_sub)
}




mydata <- mydata %>% 
rename(item = V1,
       style = V2,
       condition = V3,
       question = V4,
       subresp = V35,
       RT = V36,
       participant = V47) %>% 
  mutate(subresp = str_replace_all(subresp, "None", "0")) %>% 
  mutate(RT = str_replace_all(RT, "None", "0"))
 
  mydata <- mydata %>% 
  mutate(subresp = as.numeric(subresp)) %>% 
  mutate(RT = as.numeric(RT))
 

#total_score <- mydata %>% 
  group_by(participant, condition) %>% 
  summarise(SubAvg = mean(subresp), RTAvg = mean(RT))
  #pivot_wider(names_from = condition, values_from = SubAvg, RTAvg) 

subscore <- mydata %>% 
  group_by(participant, condition, style) %>% 
  summarise(DT_SubjAvg = mean(subresp), DT_RTAvg = mean(RT)) %>% 
  group_by(participant, condition) %>% 
  mutate(DT_TotalAvg = mean(DT_SubjAvg), TotalRT = mean(DT_RTAvg)) %>% 
  rename(ID = participant,
         DT_condition = condition,
         DT_style = style)
 # mutate(Con_SubAvg = mean(SubAvg))

write.csv(subscore, file = "deceptiontask_30processed.csv")
#-------------END---------------------------------------------------------------

mydata2 <- data.frame()
for (participant in list.files("../../data/")) {
  df_sub2 <- read.csv(paste0("../../data/", participant, "/deception/", participant, "_deceptiontask.csv"), header = FALSE)[-c(1:11), -c(5:28, 30, 32:34, 37:42, 44, 46, 48:54)]  
  mydata2 <- rbind(mydata2, df_sub2)
}

mydata2 <- mydata2 %>% 
  rename(item = V1,
         style = V2,
         condition = V3,
         question = V4,
         subresp = V35,
         subrespRT = V36,
         participant = V47,
         SRstart = V29,
         SRend = V31,
         PRstart = V43,
         PRend = V45) %>% 
  mutate(subresp = as.numeric(subresp)) %>% 
  mutate(subrespRT = as.numeric(subrespRT)) %>% 
  mutate(SRstart = as.numeric(SRstart)) %>% 
  mutate(SRend = as.numeric(SRend)) %>% 
  mutate(PRstart = as.numeric(PRstart)) %>% 
  mutate(PRend = as.numeric(PRend)) %>% 
  mutate(Social_RT = SRend-SRstart) %>% 
  mutate(Poly_RT = PRend-PRstart)


write.csv(total_score, file = "deceptiontask_reactiontimes.csv")

#---------------END-------------------------------------------------------------

mydata4 <- read.csv('raw001.csv', stringsAsFactors = FALSE, header = FALSE)[-c(1:11), -c(5:28, 30, 32:34, 37:42, 44, 46, 48:54)] 
mydata3 <- read.csv('raw002.csv', stringsAsFactors = FALSE, header = FALSE)[-c(1:11), -c(5:28, 30, 32:34, 37:42, 44, 46, 48:54)] 
  

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


