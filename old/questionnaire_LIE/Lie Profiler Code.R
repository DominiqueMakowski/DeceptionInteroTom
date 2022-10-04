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
install.packages("lavaan")

# Load required packages
library(foreign)
library(psych)
library(GPArotation)
library(Hmisc)
library(tidyverse)
library(ggplot2)
library(bayestestR)
library(see)
library(lavaan)

# Remember to first set your working directory from pull down menu or use the command below by inserting the directory path
setwd("  ")
setwd("~/Desktop/R Testing")
setwd("C:/Users/gen_3/Desktop/R Testing")

#************LIE Profiler Code Processing***********************************
# read SPSS fa_eg.sav
# mydata <- read.spss('fa_eg.sav', to.data.frame = T)
setwd("~/Dropbox/FYP_Jia Rong/R Processing/R Code for LIE Profiler")
library(tidyverse)
mydata <- read.csv('LIE_30.csv', stringsAsFactors = FALSE)[-c(1, 2), -c(1:17)] 

data <- mydata %>% 
  as.data.frame() %>%  
  rename(LIE_10 = Q1_4,
         LIE_9 = Q2_4, 
         LIE_14 = Q3_4,
         LIE_18 = Q4_4,  
         LIE_4 = Q5_4, 
         LIE_5 = Q6_4, 
         LIE_23 = Q7_4, 
         LIE_1 = Q8_4, 
         LIE_41 = Q9_4, 
         LIE_25 = Q10_1, 
         LIE_44 = Q11_1, 
         LIE_34 = Q12_4, 
         LIE_43 = Q13_4, 
         LIE_33 = Q14_4, 
         LIE_42 = Q15_4, 
         LIE_39 = Q16_4, 
       LieDay = Q17,
       LieWeek = Q18)

  cfa_parameters_URL <- "https://github.com/DominiqueMakowski/2020structure/blob/master/statistics/proflier/model_dimensions.rda?raw=true"
  load(url(cfa_parameters_URL))

    ### Convert to doubles
  data <- data %>% 
    mutate_if(is.character,as.numeric) %>% 
    mutate(ID = as.character(ID))

    ### Rescale
  data[stringr::str_detect(names(data), "LIE_")] <- effectsize::change_scale(data[stringr::str_detect(names(data), "LIE_")], from = c(-10, 10), to = c(-5, 5))
  
  cfa <- attributes(cfa_parameters)$model
  scores <- lavaan::lavPredict(cfa, newdata = data) %>% 
    as.data.frame() %>% 
    rename(DS_Frequency = Frequency,
           DS_Ability = Ability,
           DS_Negativity = Negativity,
           DS_Contextuality = Contextuality) %>% 
    mutate(DS_TotalAvg = (DS_Frequency+DS_Ability+DS_Negativity+DS_Contextuality)/4)
  
  
  final <- cbind(data, scores)
  
  finalscore <- final %>% 
    select(c(1, 20:24)) %>% 
    mutate(ID = as.numeric(ID)) %>% 
    arrange(ID) %>% 
    rename(Lie_Freq = DS_Frequency,
           Lie_Ability = DS_Ability,
           Lie_Neg = DS_Negativity,
           Lie_Content = DS_Contextuality,
           Lie_TotalAvg = DS_TotalAvg)
  
  write.csv(finalscore, file = "lieprofiler_30.csv")
  
  #------------------------END---------------------------------------

  
  
  
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
  mutate(PRI = IPM + CA, SEC = ELS + ASB)
  
  

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
       
  
  
  ### Deception and Lying Profile (LIE)
  
  We rescaled the LIE variables, originally scored on a -10 to 10 scale, to -5 to 5, so that the coefficients are more easily interpretable (i.e., refers to a change of 10\% of the scale).
  
  ```{r warning=FALSE, message=FALSE}
  df_raw[stringr::str_detect(names(df_raw), "LIE_")] <- effectsize::change_scale(df_raw[stringr::str_detect(names(df_raw), "LIE_")], from = c(-10, 10), to = c(-5, 5))
  ```
  
  
  
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


