
#Regression models
##Subjective Response Comparison
df <- data %>% 
  mutate(participant = as.factor(participant),
         ConditionSP = as.factor(ConditionSP)) %>% 
  filter(truthfulness == "LIE") %>% 
  filter(participant != "3",
         participant != "15",
         participant != "19",
         participant != "23")

#report(model)
#summary(model)

#subresp = ConditionSP(X1) + Yoni_Task(X2) + HCT_Accuracy(X3) (3-way interaction)
model_sub1 <- lme4::lmer(subresp ~ ConditionSP * yoni_total * HCT_Accuracy + (1|participant), data = df)
parameters::parameters(model_sub1)
plot_model(model_sub1, type = "pred", terms = c("HCT_Accuracy", "yoni_total", "ConditionSP"))

#subresp = ConditionSP(X1) + Yoni_Task(X2) + HCT_Accuracy(X3) (3-way interaction)
model_sub2 <- lme4::lmer(subresp ~ ConditionSP * (yoni_total + HCT_Accuracy) + (1|participant), data = df)
parameters::parameters(model_sub2)
plot_model(model_sub2, type = "pred", terms = c("yoni_total", "HCT_Accuracy", "ConditionSP"))

#Interoception (HCT)
#subresp = ConditionSP(X1) + HCT_Accuracy(X2) (Interaction)
model_sub3 <- lme4::lmer(subresp ~ ConditionSP * HCT_Accuracy + (1|participant), data = df)
parameters::parameters(model_sub3)
plot_model(model_sub3, type = "pred", terms = c("HCT_Accuracy", "ConditionSP"))

model_sub4 <- lme4::lmer(subresp ~ ConditionSP * MAIA_Total + (1|participant), data = df)
parameters::parameters(model_sub4)
plot_model(model_sub4, type = "pred", terms = c("MAIA_Total", "ConditionSP"))

model_sub5 <- lme4::lmer(subresp ~ (ConditionSP * HCT_Accuracy) + HCT_Confidence + HCT_Awareness + MAIA_Total + (1|participant), data = df)
parameters::parameters(model_sub5)
plot_model(model_sub5, type = "pred", terms = c("HCT_Accuracy", "ConditionSP"))

model_sub6 <- lme4::lmer(subresp ~ (ConditionSP * HCT_Accuracy) + HCT_Confidence + (1|participant), data = df)
parameters::parameters(model_sub6)
plot_model(model_sub6, type = "pred", terms = c("HCT_Accuracy", "ConditionSP"))


#TOM (YONI)
model_sub7 <- lme4::lmer(subresp ~ ConditionSP * yoni_total + (1|participant), data = df)
parameters::parameters(model_sub7)
plot_model(model_sub7, type = "pred", terms = c("yoni_total", "ConditionSP"))

model_sub8 <- lme4::lmer(subresp ~ ConditionSP * BES_Total + (1|participant), data = df)
parameters::parameters(model_sub8)
plot_model(model_sub8, type = "pred", terms = c("BES_Total", "ConditionSP"))

model_sub9 <- lme4::lmer(subresp ~ (ConditionSP * yoni_total) + BES_Total + (1|participant), data = df)
parameters::parameters(model_sub9)
plot_model(model_sub9, type = "pred", terms = c("yoni_total", "ConditionSP", "BES_Total"))

-------
  
#Physio scores comparison
df2 <- data %>% 
  mutate(participant = as.factor(participant),
         ConditionSP = as.factor(ConditionSP)) %>% 
  filter(truthfulness == "LIE") %>% 
  filter(Inclusion2 != "0") %>% 
  filter(participant != "22") %>% 
#  filter(participant != "23") %>% 
  filter(participant != "30") %>% 
  filter(participant != "12",
         participant != "15") 
#15
#mutate(MAIA_NEW = (MAIA1 + MAIA5 +  MAIA7)/3)

#ECG_RATE_MAX

#subresp = ConditionSP(X1) + Yoni_Task(X2) + HCT_Accuracy(X3) (3-way interaction)
model_ecg1 <- lme4::lmer(ECG_Rate_Max ~ ConditionSP * yoni_total * HCT_Accuracy + (1|participant), data = df2)
parameters::parameters(model_ecg1)
plot_model(model_ecg1, type = "pred", terms = c("HCT_Accuracy", "yoni_total", "ConditionSP"))

#subresp = ConditionSP(X1) + Yoni_Task(X2) + HCT_Accuracy(X3) (3-way interaction)
model_ecg2 <- lme4::lmer(ECG_Rate_Max ~ ConditionSP * (yoni_total + HCT_Accuracy) + (1|participant), data = df2)
parameters::parameters(model_ecg2)
plot_model(model_ecg2, type = "pred", terms = c("yoni_total", "HCT_Accuracy", "ConditionSP"))

#Interoception (HCT)
#subresp = ConditionSP(X1) + HCT_Accuracy(X2) (Interaction)
model_ecg3 <- lme4::lmer(ECG_Rate_Max ~ ConditionSP * HCT_Accuracy + (1|participant), data = df2)
parameters::parameters(model_ecg3)
plot_model(model_ecg3, type = "pred", terms = c("HCT_Accuracy", "ConditionSP"))

model_ecg4 <- lme4::lmer(ECG_Rate_Max ~ ConditionSP * MAIA3 + (1|participant), data = df2)
parameters::parameters(model_ecg4)
plot_model(model_ecg4, type = "pred", terms = c("MAIA3", "ConditionSP"))

model_ecg5 <- lme4::lmer(ECG_Rate_Max ~ (ConditionSP * HCT_Accuracy) + HCT_Confidence + HCT_Awareness + MAIA3 + (1|participant), data = df2)
parameters::parameters(model_ecg5)
plot_model(model_ecg5, type = "pred", terms = c("HCT_Accuracy", "ConditionSP"))

model_ecg6 <- lme4::lmer(ECG_Rate_Max ~ (ConditionSP * HCT_Accuracy) + HCT_Confidence + MAIA3 + (1|participant), data = df2)
parameters::parameters(model_ecg6)
plot_model(model_ecg6, type = "pred", terms = c("HCT_Accuracy", "ConditionSP"))


#TOM (YONI)
model_ecg7 <- lme4::lmer(ECG_Rate_Max ~ ConditionSP * yoni_affective + (1|participant), data = df2)
parameters::parameters(model_ecg7)
plot_model(model_ecg7, type = "pred", terms = c("yoni_affective", "ConditionSP"))

model_ecg8 <- lme4::lmer(ECG_Rate_Max ~ ConditionSP * BES_Total + (1|participant), data = df2)
parameters::parameters(model_ecg8)
plot_model(model_ecg8, type = "pred", terms = c("BES_Total", "ConditionSP"))

model_ecg9 <- lme4::lmer(ECG_Rate_Max ~ (ConditionSP * yoni_total) + BES_Total + (1|participant), data = df2)
parameters::parameters(model_ecg9)
plot_model(model_ecg9, type = "pred", terms = c("yoni_total", "ConditionSP", "BES_Total"))


model_ecg10 <- lme4::lmer(subresp ~ (ConditionSP * SRP3_CA) + (1|participant), data = df2)
parameters::parameters(model_ecg10)
plot_model(model_ecg10, type = "pred", terms = c("SRP3_CA", "ConditionSP"))

-----
  
#ECG_RATE_MIN
#Interoception (HCT)
#subresp = ConditionSP(X1) + HCT_Accuracy(X2) (Interaction)
model_ecg3a <- lme4::lmer(ECG_Rate_Min ~ ConditionSP * HCT_Accuracy + (1|participant), data = df2)
parameters::parameters(model_ecg3a)
plot_model(model_ecg3a, type = "pred", terms = c("HCT_Accuracy", "ConditionSP"))

model_ecg4a <- lme4::lmer(ECG_Rate_Min ~ ConditionSP * MAIA3 + (1|participant), data = df2)
parameters::parameters(model_ecg4a)
plot_model(model_ecg4a, type = "pred", terms = c("MAIA3", "ConditionSP"))

model_ecg5a <- lme4::lmer(ECG_Rate_Min ~ (ConditionSP * HCT_Accuracy) + HCT_Confidence + HCT_Awareness + MAIA_Total + (1|participant), data = df2)
parameters::parameters(model_ecg5a)
plot_model(model_ecg5a, type = "pred", terms = c("HCT_Accuracy", "ConditionSP"))

model_ecg6a <- lme4::lmer(ECG_Rate_Min ~ (ConditionSP * HCT_Accuracy) + HCT_Confidence + (1|participant), data = df2)
parameters::parameters(model_ecg6a)
plot_model(model_ecg6a, type = "pred", terms = c("HCT_Accuracy", "ConditionSP"))


#TOM (YONI)
model_ecg7a <- lme4::lmer(ECG_Rate_Min ~ ConditionSP * yoni_total + (1|participant), data = df2)
parameters::parameters(model_ecg7a)
plot_model(model_ecg7a, type = "pred", terms = c("yoni_total", "ConditionSP"))

model_ecg8a <- lme4::lmer(ECG_Rate_Min ~ ConditionSP * BES_Total + (1|participant), data = df2)
parameters::parameters(model_ecg8a)
plot_model(model_ecg8a, type = "pred", terms = c("BES_Total", "ConditionSP"))

model_ecg9a <- lme4::lmer(ECG_Rate_Min ~ (ConditionSP * yoni_total) + BES_Total + (1|participant), data = df2)
parameters::parameters(model_ecg9a)
plot_model(model_ecg9a, type = "pred", terms = c("yoni_total", "ConditionSP", "BES_Total"))


-----
  
#RSP_Amplitude_Max
#Interoception (HCT)
#subresp = ConditionSP(X1) + HCT_Accuracy(X2) (Interaction)
model_ecg3b <- lme4::lmer(RSP_Amplitude_Max ~ ConditionSP * HCT_Accuracy + (1|participant), data = df2)
parameters::parameters(model_ecg3b)
plot_model(model_ecg3b, type = "pred", terms = c("HCT_Accuracy", "ConditionSP"))

model_ecg4b <- lme4::lmer(RSP_Amplitude_Max ~ ConditionSP * MAIA3 + (1|participant), data = df2)
parameters::parameters(model_ecg4b)
plot_model(model_ecg4b, type = "pred", terms = c("MAIA3", "ConditionSP"))

model_ecg5b <- lme4::lmer(RSP_Amplitude_Max ~ (ConditionSP * HCT_Accuracy) + HCT_Confidence + HCT_Awareness + MAIA_Total + (1|participant), data = df2)
parameters::parameters(model_ecg5b)
plot_model(model_ecg5b, type = "pred", terms = c("HCT_Accuracy", "ConditionSP"))

model_ecg6b <- lme4::lmer(RSP_Amplitude_Max ~ (ConditionSP * HCT_Accuracy) + HCT_Confidence + (1|participant), data = df2)
parameters::parameters(model_ecg6b)
plot_model(model_ecg6b, type = "pred", terms = c("HCT_Accuracy", "ConditionSP"))


#TOM (YONI)
model_ecg7b <- lme4::lmer(RSP_Amplitude_Max ~ ConditionSP * yoni_total + (1|participant), data = df2)
parameters::parameters(model_ecg7b)
plot_model(model_ecg7b, type = "pred", terms = c("yoni_total", "ConditionSP"))

model_ecg8b <- lme4::lmer(RSP_Amplitude_Max ~ ConditionSP * BES_Total + (1|participant), data = df2)
parameters::parameters(model_ecg8b)
plot_model(model_ecg8b, type = "pred", terms = c("BES_Total", "ConditionSP"))

model_ecg9b <- lme4::lmer(RSP_Amplitude_Max ~ (ConditionSP * yoni_total) + BES_Total + (1|participant), data = df2)
parameters::parameters(model_ecg9b)
plot_model(model_ecg9b, type = "pred", terms = c("yoni_total", "ConditionSP", "BES_Total"))


-----
  df2a <- data %>% 
  mutate(participant = as.factor(participant),
         ConditionSP = as.factor(ConditionSP)) %>% 
  filter(truthfulness == "LIE") %>% 
  filter(Inclusion2 != "0") %>% 
  filter(participant != "22") %>% 
  #  filter(participant != "23") %>% 
  #  filter(participant != "30") %>% 
  filter(participant != "4",
         participant != "5",
         participant != "10",
         participant != "12",
         participant != "16",
         participant != "23",
         participant != "27",
         participant != "29")

#EDA_SCR
#Interoception (HCT)
#subresp = ConditionSP(X1) + HCT_Accuracy(X2) (Interaction)
model_ecg3c <- lme4::lmer(EDA_SCR ~ ConditionSP * HCT_Accuracy + (1|participant), data = df2a)
parameters::parameters(model_ecg3c)
plot_model(model_ecg3c, type = "pred", terms = c("HCT_Accuracy", "ConditionSP"))

model_ecg4c <- lme4::lmer(EDA_SCR ~ ConditionSP * MAIA3 + (1|participant), data = df2a)
parameters::parameters(model_ecg4c)
plot_model(model_ecg4c, type = "pred", terms = c("MAIA3", "ConditionSP"))

model_ecg5c <- lme4::lmer(EDA_SCR ~ (ConditionSP * HCT_Accuracy) + HCT_Confidence + HCT_Awareness + MAIA_Total + (1|participant), data = df2a)
parameters::parameters(model_ecg5c)
plot_model(model_ecg5c, type = "pred", terms = c("HCT_Accuracy", "ConditionSP"))

model_ecg6c <- lme4::lmer(EDA_SCR ~ (ConditionSP * HCT_Accuracy) + HCT_Confidence + (1|participant), data = df2a)
parameters::parameters(model_ecg6c)
plot_model(model_ecg6c, type = "pred", terms = c("HCT_Accuracy", "ConditionSP"))


#TOM (YONI)
model_ecg7c <- lme4::lmer(EDA_SCR ~ ConditionSP * yoni_total + (1|participant), data = df2a)
parameters::parameters(model_ecg7c)
plot_model(model_ecg7c, type = "pred", terms = c("yoni_total", "ConditionSP"))

model_ecg8c <- lme4::lmer(EDA_SCR ~ ConditionSP * BES_Total + (1|participant), data = df2a)
parameters::parameters(model_ecg8c)
plot_model(model_ecg8c, type = "pred", terms = c("BES_Total", "ConditionSP"))

model_ecg9c <- lme4::lmer(EDA_SCR ~ (ConditionSP * yoni_total) + BES_Total + (1|participant), data = df2a)
parameters::parameters(model_ecg9c)
plot_model(model_ecg9c, type = "pred", terms = c("yoni_total", "ConditionSP", "BES_Total"))


#An interaction is present when the effects of one IV on DV change at the different levels of the second IV.
#the +ve effect of the HCT_Accuracy on the subjective response varies on the different level of the ConditionSP. The rate of change of HCT_Accuracy on the subjective response in the polygraph condition is larger than the rate of change of HCT_Accuracy on the subjective response in the social condition.

Interaction EXPLANATION
- ConditionSP - differences between social and poly condition when HCTACCuracy is 0
- HCTAccuracy (poly condition as 0) - only in polygraph condition, there is a positive effect of HCT_Accuracy on sub resp but not significant
- interaction - participants who have a better HCTAccur (interoceptive ability) have better confidence on their lies in the poly condition compared to social condition



#Hypothesis 1
ECG_Rate_Max, ECG_Rate_Min, RSP_Amplitude_Max, EDA_SCR

df3 <- data %>% 
  mutate(participant = as.factor(participant),
         ConditionSP = as.factor(ConditionSP)) %>% 
  filter(truthfulness == "LIE") %>% 
  filter(Inclusion2 != "0") %>% 
  filter(participant != "22") %>% 
  #  filter(participant != "23") %>% 
  filter(participant != "30") %>% 
  #  filter(participant != "12") %>% 
  #  filter(participant != "15") %>% 
  filter(ConditionSP != "polygraph") %>% 
  filter(Condition != "R") %>% 
  filter(Condition != "D") %>% 
  filter(Condition != "Q") 

#Hypothesis 1a
##ECG_RATE_MAX
Hone.a <- lme4::lmer(ECG_Rate_Max ~  yoni_total * BES_Total + (1|participant), data = df3)
parameters::parameters(Hone.a)
plot_model(Hone.a, type = "pred", terms = c("yoni_total", "BES_Total"))

Hone.b <- lme4::lmer(ECG_Rate_Max ~ yoni_cognitive + yoni_affective + yoni_physical + (1|participant), data = df3)
parameters::parameters(Hone.b)
plot_model(Hone.b, type = "pred")
plot_model(Hone.b, type = "pred")

Hone.c <- lme4::lmer(ECG_Rate_Max ~  BES_Affective + BES_Cognitive + (1|participant), data = df3)
parameters::parameters(Hone.c)
plot_model(Hone.c, type = "pred")


#ECG_RATE_MIN
Hone.a1 <- lme4::lmer(ECG_Rate_Min ~  yoni_total * BES_Total + (1|participant), data = df3)
parameters::parameters(Hone.a1)
plot_model(Hone.a1, type = "pred", terms = c("yoni_total", "BES_Total"))

Hone.b1 <- lme4::lmer(ECG_Rate_Min ~  yoni_cognitive + yoni_affective + yoni_physical + (1|participant), data = df3)
parameters::parameters(Hone.b1)
plot_model(Hone.b1, type = "pred")

Hone.c1 <- lme4::lmer(ECG_Rate_Min ~  BES_Affective + BES_Cognitive + (1|participant), data = df3)
parameters::parameters(Hone.c1)
plot_model(Hone.c1, type = "pred")

#RSP_Amplitude_Max

Hone.a2 <- lme4::lmer(RSP_Amplitude_Max ~  yoni_total * BES_Total + (1|participant), data = df3)
parameters::parameters(Hone.a2)
plot_model(Hone.a2, type = "pred", terms = c("yoni_total", "BES_Total"))

Hone.b2 <- lme4::lmer(RSP_Amplitude_Max ~  yoni_cognitive + yoni_affective + yoni_physical + (1|participant), data = df3)
parameters::parameters(Hone.b2)
plot_model(Hone.b2, type = "pred")

Hone.c2 <- lme4::lmer(RSP_Amplitude_Max ~  BES_Affective + BES_Cognitive + (1|participant), data = df3)
parameters::parameters(Hone.c2)
plot_model(Hone.c2, type = "pred")

-----
  
#1a: DV: Subjective rating, IV: TOM
# Hone.a4 <- lme4::lmer(subresp ~  yoni_total * BES_Total + (1|participant), data = df3)
# parameters::parameters(Hone.a4)
# plot_model(Hone.a4, type = "pred", terms = c("yoni_total", "BES_Total"))

Hone.b4 <- lme4::lmer(subresp ~ yoni_cognitive + yoni_affective + yoni_physical + (1|participant), data = df3)
parameters::parameters(Hone.b4)
plot_model(Hone.b4, type = "pred")
plot_model(Hone.b4, type = "pred")

Hone.c4 <- lme4::lmer(subresp ~  BES_Affective + BES_Cognitive + (1|participant), data = df3)
parameters::parameters(Hone.c4)
plot_model(Hone.c4, type = "pred")


df3a <- data %>% 
  mutate(participant = as.factor(participant),
         ConditionSP = as.factor(ConditionSP)) %>% 
  filter(truthfulness == "LIE") %>% 
  filter(Inclusion2 != "0") %>% 
  filter(participant != "22") %>% 
  #  filter(participant != "23") %>% 
  filter(participant != "30") %>% 
  filter(participant != "4",
         participant != "5",
         participant != "10",
         participant != "12",
         participant != "16",
         participant != "23",
         participant != "27",
         participant != "29") %>% 
  filter(ConditionSP != "polygraph") %>% 
  filter(Condition != "R") %>% 
  filter(Condition != "D") %>% 
  filter(Condition != "C")

Hone.a3 <- lme4::lmer(EDA_SCR ~  yoni_total * BES_Total + (1|participant), data = df3)
parameters::parameters(Hone.a3)
plot_model(Hone.a3, type = "pred", terms = c("yoni_total", "BES_Total"))

Hone.b3 <- lme4::lmer(EDA_SCR ~  yoni_total + (1|participant), data = df3)
parameters::parameters(Hone.b3)
plot_model(Hone.b3, type = "pred")

Hone.c3 <- lme4::lmer(EDA_SCR ~  BES_Total + (1|participant), data = df3)
parameters::parameters(Hone.c3)
plot_model(Hone.c3, type = "pred")

-------

#Hypothesis 1b  
Hone.d <- lm(yoni_physical ~  SRP3_Total, data = des_stat)
parameters::parameters(Hone.d)
plot_model(Hone.d, type = "pred")

Hone.da <- lm::lmer(BES_Affective ~  SRP3_Total + (1|participant), data = df3)
parameters::parameters(Hone.da)
plot_model(Hone.da, type = "pred")

-------
  

#Hypothesis 1c
Hone.e <- lme4::lmer(ECG_Rate_Max ~ SRP3_SEC + SRP3_PRI + (1|participant), data = df3)
parameters::parameters(Hone.e)
plot_model(Hone.e, type = "pred")

Hone.f <- lme4::lmer(ECG_Rate_Min ~  SRP3_Total + (1|participant), data = df3)
parameters::parameters(Hone.f)
plot_model(Hone.f, type = "pred")

Hone.g <- lme4::lmer(RSP_Amplitude_Max ~  SRP3_Total + (1|participant), data = df3)
parameters::parameters(Hone.g)
plot_model(Hone.g, type = "pred")

Hone.h <- lme4::lmer(EDA_SCR ~  SRP3_Total + (1|participant), data = df3a)
parameters::parameters(Hone.h)
plot_model(Hone.h, type = "pred")  

Hone.i <- lme4::lmer(subresp ~  SRP3_Total + (1|participant), data = df3a)
parameters::parameters(Hone.i)
plot_model(Hone.i, type = "pred")  


#Hypothesis 2
ECG_Rate_Max, ECG_Rate_Min, RSP_Amplitude_Max, EDA_SCR

df4 <- data %>% 
  mutate(participant = as.factor(participant),
         ConditionSP = as.factor(ConditionSP)) %>% 
  filter(truthfulness == "LIE") %>% 
  filter(Inclusion2 != "0") %>% 
  filter(participant != "22") %>% 
  #  filter(participant != "23") %>% 
  filter(participant != "30") %>% 
  filter(participant != "12") %>% 
  filter(participant != "15") %>% 
  filter(ConditionSP != "social") %>% 
  filter(Condition != "R") %>% 
  filter(Condition != "D") %>%  
  filter(Condition != "Q")

#Hypothesis 2a
#ECG_Rate_Max
Htwo.a <- lme4::lmer(ECG_Rate_Max ~ HCT_Accuracy + MAIA3 + (1|participant), data = df4)
parameters::parameters(Htwo.a)
plot_model(Htwo.a, type = "pred", terms = c("HCT_Accuracy", "MAIA3"))

Htwo.b <- lme4::lmer(ECG_Rate_Max ~  HCT_Accuracy + (1|participant), data = df4)
parameters::parameters(Htwo.b)
plot_model(Htwo.b, type = "pred")

Htwo.c <- lme4::lmer(ECG_Rate_Max ~  MAIA3 + (1|participant), data = df4)
parameters::parameters(Htwo.c)
plot_model(Htwo.c, type = "pred")

#ECG_Rate_Min
Htwo.a1 <- lme4::lmer(ECG_Rate_Min ~ HCT_Accuracy + MAIA3 + (1|participant), data = df4)
parameters::parameters(Htwo.a1)
plot_model(Htwo.a1, type = "pred", terms = c("HCT_Accuracy", "MAIA3"))

Htwo.b1 <- lme4::lmer(ECG_Rate_Min ~  HCT_Accuracy + (1|participant), data = df4)
parameters::parameters(Htwo.b1)
plot_model(Htwo.b1, type = "pred")

Htwo.c1 <- lme4::lmer(ECG_Rate_Min ~  MAIA3 + (1|participant), data = df4)
parameters::parameters(Htwo.c1)
plot_model(Htwo.c1, type = "pred")

#RSP_Amplitude_Max
Htwo.a2 <- lme4::lmer(RSP_Amplitude_Max ~ HCT_Accuracy + MAIA3 + (1|participant), data = df4)
parameters::parameters(Htwo.a2)
plot_model(Htwo.a2, type = "pred", terms = c("HCT_Accuracy", "MAIA3"))

Htwo.b2 <- lme4::lmer(RSP_Amplitude_Max ~  HCT_Accuracy + (1|participant), data = df4)
parameters::parameters(Htwo.b2)
plot_model(Htwo.b2, type = "pred")

Htwo.c2 <- lme4::lmer(RSP_Amplitude_Max ~  MAIA3 + (1|participant), data = df4)
parameters::parameters(Htwo.c2)
plot_model(Htwo.c2, type = "pred")

df4a <- data %>% 
  mutate(participant = as.factor(participant),
         ConditionSP = as.factor(ConditionSP)) %>% 
  filter(truthfulness == "LIE") %>% 
  filter(Inclusion2 != "0") %>% 
  filter(participant != "22") %>% 
  #  filter(participant != "23") %>% 
  filter(participant != "30") %>% 
  filter(participant != "4",
         participant != "5",
         participant != "10",
         participant != "12",
         participant != "16",
         participant != "23",
         participant != "27",
         participant != "29") %>% 
  filter(ConditionSP != "social") %>% 
  filter(Condition != "R") %>% 
  filter(Condition != "D") 
filter(Condition != "C")

#EDA_SCR
Htwo.a3 <- lme4::lmer(EDA_SCR ~ HCT_Accuracy + MAIA3 + (1|participant), data = df4)
parameters::parameters(Htwo.a3)
plot_model(Htwo.a3, type = "pred", terms = c("HCT_Accuracy", "MAIA3"))

Htwo.b3 <- lme4::lmer(EDA_SCR ~  HCT_Accuracy + (1|participant), data = df4)
parameters::parameters(Htwo.b3)
plot_model(Htwo.b3, type = "pred")

Htwo.c3 <- lme4::lmer(EDA_SCR ~  MAIA3 + (1|participant), data = df4)
parameters::parameters(Htwo.c3)
plot_model(Htwo.c3, type = "pred")


#subresp
Htwo.a4 <- lme4::lmer(subresp ~ HCT_Accuracy + MAIA3 + (1|participant), data = df4)
parameters::parameters(Htwo.a4)
plot_model(Htwo.a4, type = "pred", terms = c("HCT_Accuracy", "MAIA3"))

Htwo.b4 <- lme4::lmer(subresp ~  HCT_Accuracy + (1|participant), data = df4)
parameters::parameters(Htwo.b4)
plot_model(Htwo.b4, type = "pred")

Htwo.c4 <- lme4::lmer(subresp ~  MAIA3 + (1|participant), data = df4)
parameters::parameters(Htwo.c4)
plot_model(Htwo.c4, type = "pred")


----------
  
#Hypothesis 2b  
Htwo.d <- lme4::lmer(HCT_Accuracy ~  SRP3_PRI + (1|participant), data = df3)
parameters::parameters(Htwo.d)
plot_model(Htwo.d, type = "pred")

Htwo.d <- lm(HCT_Accuracy ~  SRP3_PRI, data = des_stat)
parameters::parameters(Htwo.d)
plot_model(Htwo.d, type = "pred")

Htwo.da <- lme4::lmer(MAIA3 ~  SRP3_PRI + (1|participant), data = df3)
parameters::parameters(Htwo.da)
plot_model(Htwo.da, type = "pred")

-------
  
#Hypothesis 2c
Htwo.e <- lme4::lmer(ECG_Rate_Max ~ SRP3_PRI + (1|participant), data = df4)
parameters::parameters(Hone.e)
plot_model(Hone.e, type = "pred")

Htwo.f <- lme4::lmer(ECG_Rate_Min ~  SRP3_PRI + (1|participant), data = df4)
parameters::parameters(Hone.f)
plot_model(Hone.f, type = "pred")

Htwo.g <- lme4::lmer(RSP_Amplitude_Max ~  SRP3_PRI + (1|participant), data = df4)
parameters::parameters(Hone.g)
plot_model(Hone.g, type = "pred")

Htwo.h <- lme4::lmer(EDA_SCR ~  SRP3_PRI + (1|participant), data = df4a)
parameters::parameters(Hone.h)
plot_model(Hone.h, type = "pred")  

Htwo.i <- lme4::lmer(subresp ~  SRP3_PRI + (1|participant), data = df4)
parameters::parameters(Htwo.i)
plot_model(Htwo.i, type = "pred")  



Others

cor(Corr$subresp, Corr$ECG_Rate_Mean, method = "pearson")
cor.test(Hone$yoni_total, Hone$ECG_Rate_Mean, 
         method = "pearson")
Hone %>% 
  ggscatter(x = "yoni_total", y = "ECG_Rate_Mean", 
            add = "reg.line", conf.int = TRUE, 
            cor.coef = TRUE, cor.method = "pearson",
            xlab = "Yoni Task", ylab = "ECG Rate Mean") +
  ggtitle("Plot of Yoni Task vs ECG Rate Mean for Lies")  + 
  theme(plot.title = element_text(size=10))


##T-test (TO REMOVE)

#T-test of average subjective responses for lies between two conditions
t.test(df_descriptive$polygraph, df_descriptive$social, var.equal = TRUE)



#1a: DV: Subjective rating, IV: TOM
Hone.a4 <- lme4::lmer(subresp ~  yoni_total * BES_Total + (1|participant), data = df3)
parameters::parameters(Hone.a4)
plot_model(Hone.a4, type = "pred", terms = c("yoni_total", "BES_Total"))

Hone.b4 <- lme4::lmer(subresp ~ yoni_cognitive + yoni_affective + yoni_physical + (1|participant), data = df3)
parameters::parameters(Hone.b4)
plot_model(Hone.b4, type = "pred", terms = c("yoni_cognitive"  + "yoni_affective", "yoni_physical"))

Hone.c4 <- lme4::lmer(subresp ~  BES_Affective + BES_Cognitive + (1|participant), data = df3)
parameters::parameters(Hone.c4)
plot_model(Hone.c4, type = "pred")


#Hypothesis 1b
Hone.d <- lm(yoni_physical ~  SRP3_Total, data = des_stat)
parameters::parameters(Hone.d)
plot_model(Hone.d, type = "pred")

Hone.da <- lm::lmer(BES_Affective ~  SRP3_Total + (1|participant), data = df3)
parameters::parameters(Hone.da)
plot_model(Hone.da, type = "pred")


#Hypothesis 2
#Hypothesis 2b
Htwo.d <- lme4::lmer(HCT_Accuracy ~  SRP3_PRI + (1|participant), data = df3)
parameters::parameters(Htwo.d)
plot_model(Htwo.d, type = "pred")

Htwo.d <- lm(HCT_Accuracy ~  SRP3_PRI, data = des_stat)
parameters::parameters(Htwo.d)
plot_model(Htwo.d, type = "pred")

Htwo.da <- lme4::lmer(MAIA3 ~  SRP3_PRI + (1|participant), data = df3)
parameters::parameters(Htwo.da)
plot_model(Htwo.da, type = "pred")
