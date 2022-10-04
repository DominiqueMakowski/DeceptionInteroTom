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


#********SRP3 CODE PROCESSING*************
# read SPSS fa_eg.sav
# mydata <- read.spss('fa_eg.sav', to.data.frame = T)
setwd("~/Dropbox/FYP_Jia Rong/R Processing/R Code for SRP3")
library(tidyverse)
mydata <- read.csv('SRP3_30.csv', stringsAsFactors = FALSE)[-c(1, 2), -c(1:17)] 

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
       Q21 = Q3_21,
       Q22 = Q3_22,
       Q23 = Q3_23,
       Q24 = Q3_24,
       Q25 = Q3_25,
       Q26 = Q3_26,
       Q27 = Q3_27,
       Q28 = Q3_28,
       Q29 = Q3_29,
       Q30 = Q3_30,
       Q31 = Q3_31,
       Q32 = Q3_32,
       Q33 = Q4_1,
       Q34 = Q4_2,
       Q35 = Q4_3,
       Q36 = Q4_4,
       Q37 = Q4_5,
       Q38 = Q4_6,
       Q39 = Q4_7,
       Q40 = Q4_8,
       Q41 = Q4_9,
       Q42 = Q4_10,
       Q43 = Q4_11,
       Q44 = Q4_12,
       Q45 = Q4_13,
       Q46 = Q4_14,
       Q47 = Q4_15,
       Q48 = Q4_16,
       Q49 = Q4_17,
       Q50 = Q4_18,
       Q51 = Q4_19,
       Q52 = Q4_20,
       Q53 = Q4_21,
       Q54 = Q4_22,
       Q55 = Q4_23,
       Q56 = Q4_24,
       Q57 = Q4_25,
       Q58 = Q4_26,
       Q59 = Q4_27,
       Q60 = Q4_28,
       Q61 = Q4_29,
       Q62 = Q4_30,
       Q63 = Q4_31,
       Q64 = Q4_32,
       ID = Q2) %>% 
  mutate(Q5 = recode(Q5, "1" = "5", "2" = "4", "4" = "2", "5" = "1"),
         Q6 = recode(Q6, "1" = "5", "2" = "4", "4" = "2", "5" = "1"),
         Q11 = recode(Q11, "1" = "5", "2" = "4", "4" = "2", "5" = "1"),
         Q14 = recode(Q14, "1" = "5", "2" = "4", "4" = "2", "5" = "1"),
         Q16 = recode(Q16, "1" = "5", "2" = "4", "4" = "2", "5" = "1"),
         Q18 = recode(Q18, "1" = "5", "2" = "4", "4" = "2", "5" = "1"),
         Q19 = recode(Q19, "1" = "5", "2" = "4", "4" = "2", "5" = "1"),
         Q21 = recode(Q21, "1" = "5", "2" = "4", "4" = "2", "5" = "1"),
         Q22 = recode(Q22, "1" = "5", "2" = "4", "4" = "2", "5" = "1"),
         Q23 = recode(Q23, "1" = "5", "2" = "4", "4" = "2", "5" = "1"),
         Q24 = recode(Q24, "1" = "5", "2" = "4", "4" = "2", "5" = "1"),
         Q25 = recode(Q25, "1" = "5", "2" = "4", "4" = "2", "5" = "1"),
         Q26 = recode(Q26, "1" = "5", "2" = "4", "4" = "2", "5" = "1"),
         Q31 = recode(Q31, "1" = "5", "2" = "4", "4" = "2", "5" = "1"),
         Q34 = recode(Q34, "1" = "5", "2" = "4", "4" = "2", "5" = "1"),
         Q36 = recode(Q36, "1" = "5", "2" = "4", "4" = "2", "5" = "1"),
         Q38 = recode(Q38, "1" = "5", "2" = "4", "4" = "2", "5" = "1"),
         Q44 = recode(Q44, "1" = "5", "2" = "4", "4" = "2", "5" = "1"),
         Q46 = recode(Q46, "1" = "5", "2" = "4", "4" = "2", "5" = "1"),
         Q47 = recode(Q47, "1" = "5", "2" = "4", "4" = "2", "5" = "1"),
         Q61 = recode(Q61, "1" = "5", "2" = "4", "4" = "2", "5" = "1")) 

data <- data %>% 
  mutate(Q1 = as.numeric(Q1), Q2 = as.numeric(Q2), Q3 = as.numeric(Q3), Q4 = as.numeric(Q5),
         Q5 = as.numeric(Q5), Q6 = as.numeric(Q6), Q7 = as.numeric(Q7), Q8 = as.numeric(Q8),
         Q9 = as.numeric(Q9), Q10 = as.numeric(Q10), Q11 = as.numeric(Q11), Q12 = as.numeric(Q12),
         Q13 = as.numeric(Q13), Q14 = as.numeric(Q14), Q15 = as.numeric(Q15), Q16 = as.numeric(Q16),
         Q17 = as.numeric(Q17), Q18 = as.numeric(Q18), Q19 = as.numeric(Q19), Q20 = as.numeric(Q20),
         Q21 = as.numeric(Q21), Q22 = as.numeric(Q22), Q23 = as.numeric(Q23), Q24 = as.numeric(Q24),
         Q25 = as.numeric(Q25), Q26 = as.numeric(Q26), Q27 = as.numeric(Q27), Q28 = as.numeric(Q28),
         Q29 = as.numeric(Q29), Q30 = as.numeric(Q30), Q31 = as.numeric(Q31), Q32 = as.numeric(Q32),
         Q33 = as.numeric(Q33), Q34 = as.numeric(Q34), Q35 = as.numeric(Q35), Q36 = as.numeric(Q36),
         Q37 = as.numeric(Q37), Q38 = as.numeric(Q38), Q39 = as.numeric(Q39), Q40 = as.numeric(Q40),
         Q41 = as.numeric(Q41), Q42 = as.numeric(Q42), Q43 = as.numeric(Q43), Q44 = as.numeric(Q44),
         Q45 = as.numeric(Q45), Q46 = as.numeric(Q46), Q47 = as.numeric(Q47), Q48 = as.numeric(Q48),
         Q49 = as.numeric(Q49), Q50 = as.numeric(Q50), Q51 = as.numeric(Q51), Q52 = as.numeric(Q52),
         Q53 = as.numeric(Q53), Q54 = as.numeric(Q54), Q55 = as.numeric(Q55), Q56 = as.numeric(Q56),
         Q57 = as.numeric(Q57), Q58 = as.numeric(Q58), Q59 = as.numeric(Q59), Q60 = as.numeric(Q60),
         Q61 = as.numeric(Q61), Q62 = as.numeric(Q62), Q63 = as.numeric(Q63), Q64 = as.numeric(Q64)) %>% 
  mutate(IPM = Q3+Q8+Q13+Q16+Q20+Q24+Q27+Q31+Q35+Q38+Q41+Q45+Q50+Q54+Q58+Q61, CA = Q2+Q7+Q11+Q15+Q19+Q23+Q26+Q30+Q33+Q37+Q40+Q44+Q48+Q53+Q56+Q60,
         ELS = Q1+Q4+Q9+Q14+Q17+Q22+Q25+Q28+Q32+Q36+Q39+Q42+Q47+Q51+Q55+Q59, ASB = Q5+Q6+Q10+Q12+Q18+Q21+Q29+Q34+Q43+Q46+Q49+Q52+Q57+Q62+Q63+Q64) %>% 
  mutate(PRI = IPM + CA, SEC = ELS + ASB) %>% 
  mutate(SRP3_Total = PRI + SEC)
  
finalscore <- data %>% 
  select(c(1, 66:72)) %>% 
  rename(SRP3_IPM = IPM,
         SRP3_CA = CA,
         SRP3_ELS = ELS,
         SRP3_ASB = ASB,
         SRP3_PRI = PRI,
         SRP3_SEC = SEC) %>% 
  arrange(ID)

write.csv(finalscore, file = "SRP3_30processed.csv")

#---------END----------------------------------------------------------------------------

  data2 <- data %>% 
    mutate(category = case_when(question == "Q3" | question == "Q8" | question == "Q13" | question == "Q16" | question == "Q20" |
                                  question == "Q24" | question == "Q27" | question == "Q31" | question == "Q35" | question == "Q38" |
                                  question == "Q41" | question == "Q45" | question == "Q50" | question == "Q54" | question == "Q58" |
                                  question == "Q61"~ "IPM",
                                question == "Q2" | question == "Q7" | question == "Q11" | question == "Q15" | question == "Q19" |
                                  question == "Q23" | question == "Q26" | question == "Q30" | question == "Q33" | question == "Q37" |
                                  question == "Q40" | question == "Q44" | question == "Q48" | question == "Q53" | question == "Q56" |
                                  question == "Q60" ~ "CA",
                                question == "Q1" | question == "Q4" | question == "Q9" | question == "Q14" | question == "Q17" |
                                  question == "Q22" | question == "Q25" | question == "Q28" | question == "Q32" | question == "Q36" |
                                  question == "Q39" | question == "Q42" | question == "Q47" | question == "Q51" | question == "Q55" |
                                  question == "Q59" ~ "ELS",
                                question == "Q5" | question == "Q6" | question == "Q10" | question == "Q12" | question == "Q18" |
                                  question == "Q21" | question == "Q29" | question == "Q34" | question == "Q43" | question == "Q46" |
                                  question == "Q49" | question == "Q52" | question == "Q57" | question == "Q62" | question == "Q63" |
                                  question == "Q64" ~ "ASB"))

  results <- data2 %>%
    mutate(score = as.numeric(score)) %>%
    group_by(category) %>% 
    summarise(total = sum(score))
       
  
  
#total score of affective, cognitive and physical
#affective = 49, cognitive = 37, physical = 15
total_score <- results %>% 
  group_by(condition) %>% 
  summarise(total = sum(answer))

#Nine items assess cognitive empathy (Items 3, 6, 9, 10, 12, 14, 16, 19, 20)
#11 items assess affective empathy (Items 1, 2, 4, 5, 7, 8, 11, 13, 15, 17, 18). 


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


