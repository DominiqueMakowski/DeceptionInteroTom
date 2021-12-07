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
#library(rstatix)

#LOAD DATA
Behav <- read.csv('Behaviouraldata.csv', stringsAsFactors = FALSE, header = TRUE)[-c(1)] %>% 
  rename(participant = ID) %>% 
  mutate(Trial = rep(1:80, 30))

Phy <- read.csv('DT.csv', stringsAsFactors = FALSE, header = TRUE) [-c(1),] %>% 
  rename(participant = Participant.number) %>% 
  mutate(Trial = rep(1:80, each = 4, times = 30))

#Phy <- Phy[!(Phy$Participant == 1 & Phy$Label == 3),]

data <- merge(Behav, Phy, by = c("participant" ,"Trial"), all = TRUE) %>% 
  arrange(participant,Trial)

#REMOVE ERROR TRIALS IN PARTICIPANTS


test <- test[!(test$Occupation == "Management" & test$AvgMonthSpend > 59.24 ) | !(test$Occupation == "Manual" & test$AvgMonthSpend > 54.28 ),] 


DTNEW <- DTNEW [, c(7,2,3,4,5,6,1)] %>% 
  rename(ID = participant)
final <- cbind(BES, LIE, MAIA, SRP3, YONI, HCT, Demo)

Finalset <- merge(DTNEW, final, by = "ID")
#Finalset <- merge(HCTPhy, Finalset, by = "ID")


DT - Reaction Time between Truth and lines(DV - left, IV - Truth lies)
- lmer family=binonial 
# DTNEW$condition <- as.factor(ifelse(DTNEW$condition == "TRUTH", 0, 1))
DTNEW$condition <- as.factor(DTNEW$condition)
# contrasts(DTNEW$condition)
DTNEW$condition <- relevel(DTNEW$condition, ref = "TRUTH")

# random variables + (1|participant)

t.test(RT ~ condition, data = DTNEW)

test <- lmer(RT ~ condition/ECG_Rate_Mean + (1|participant), data = DTNEW)




---------------------------------------------------------------------------------
