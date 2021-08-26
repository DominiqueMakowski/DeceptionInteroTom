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
setwd("C:/Users/gen_3/Desktop/R Testing")


#*****BES CODE PROCESSING****
# read SPSS fa_eg.sav
# mydata <- read.spss('fa_eg.sav', to.data.frame = T)
setwd("~/Dropbox/FYP_Jia Rong/R Processing/R Code for BES")
library(tidyverse)
mydata <- read.csv('BES_30.csv', stringsAsFactors = FALSE)[-c(1, 2), -c(1:17)] 

data <- mydata %>% 
  as.data.frame() %>%  
  rename(Q1 = Q3_1,
       Q2 = Q3_2,
       Q3 = Q3_3,
       Q4 = Q3_4,
       Q5 = Q3_5,
       Q6 = Q3_6,
       Q7 = Q3_7,
       Q8 = Q3_8,
       Q9 = Q3_9,
       Q10 = Q3_10,
       Q11 = Q3_11,
       Q12 = Q3_12,
       Q13 = Q3_13,
       Q14 = Q3_14,
       Q15 = Q3_15,
       Q16 = Q3_16,
       Q17 = Q3_17,
       Q18 = Q3_18,
       Q19 = Q3_19,
       Q20 = Q3_20,
       ID = Q2) %>% 
  mutate(Q1 = recode(Q1, "1" = "5", "2" = "4", "4" = "2", "5" = "1"),
    Q6 = recode(Q6, "1" = "5", "2" = "4", "4" = "2", "5" = "1"),
    Q7 = recode(Q7, "1" = "5", "2" = "4", "4" = "2", "5" = "1"),
    Q8 = recode(Q8, "1" = "5", "2" = "4", "4" = "2", "5" = "1"),
    Q13 = recode(Q13, "1" = "5", "2" = "4", "4" = "2", "5" = "1"),
    Q18 = recode(Q18, "1" = "5", "2" = "4", "4" = "2", "5" = "1"),
    Q19 = recode(Q19, "1" = "5", "2" = "4", "4" = "2", "5" = "1"),
    Q20 = recode(Q20, "1" = "5", "2" = "4", "4" = "2", "5" = "1"))
   
data <- data %>% 
  mutate(Q1 = as.numeric(Q1), Q2 = as.numeric(Q2), Q3 = as.numeric(Q3), Q4 = as.numeric(Q5),
         Q5 = as.numeric(Q5), Q6 = as.numeric(Q6), Q7 = as.numeric(Q7), Q8 = as.numeric(Q8),
          Q9 = as.numeric(Q9), Q10 = as.numeric(Q10), Q11 = as.numeric(Q11), Q12 = as.numeric(Q12),
          Q13 = as.numeric(Q13), Q14 = as.numeric(Q14), Q15 = as.numeric(Q15), Q16 = as.numeric(Q16),
          Q17 = as.numeric(Q17), Q18 = as.numeric(Q18), Q19 = as.numeric(Q19), Q20 = as.numeric(Q20)) %>% 
  mutate(BES_Cognitive = Q3+Q6+Q9+Q10+Q12+Q14+Q16+Q19+Q20) %>% 
  mutate(BES_Affective = Q1+Q2+Q4+Q5+Q7+Q8+Q11+Q13+Q15+Q17+Q18) %>% 
  mutate(BES_Total = BES_Cognitive+BES_Affective)

finaldata <- data %>% 
  select(c(1, 22:24)) %>% 
  arrange(ID)

#raw data + final
write.csv(data, file = "BES_processed.csv")

#final data with only calculated scores
write.csv(finaldata, file = "BES_30processed.csv")

#------END-------------------------------------------------------------------------------



as.data.frame() %>% 
  mutate(Empathy_Type = ifelse(str_detect(Question, paste(c("Q3","Q6","Q9","Q10","Q12","Q14","Q16","Q19","Q20"),collapse = '|')),
                               "Cognitive", "Affective")) 
  results <- data %>%
    mutate(Score = as.numeric(Score)) %>%
    group_by(Empathy_Type) %>% 
    summarise(total = sum(Score))

  
  
  #pivot_longer(cols = starts_with("Q"), names_to="Question", values_to="Score")
  
  #9 items assess cognitive empathy (Items 3, 6, 9, 10, 12, 14, 16, 19, 20)
  #11 items assess affective empathy (Items 1, 2, 4, 5, 7, 8, 11, 13, 15, 17, 18). 
  


#total score of affective, cognitive and physical
#affective = 49, cognitive = 37, physical = 15
total_score <- results %>% 
  group_by(condition) %>% 
  summarise(total = sum(answer))

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


