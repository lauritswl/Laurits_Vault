#Personality Test for CogSci 2021
setwd("C:/Users/lauri/Desktop/CogNotes/Working Directories/Personality_Test")
install.packages("tidyverse")
library(tidyverse)
df <- read.csv("personality_data_cleaned_2021.csv")
view(df)

#Excersice 1: filter(), find student(s) that:
#1.1 - Have shoesize 39 or bigger
filter(df,shoesize>39)

#1.2 - Able to touch the floor
df %>% 
  filter(touch_floor=="Yes"|touch_floor=="Yes of course") %>% 
  select(c("name","birth_day","touch_floor")) %>% 
  arrange(birth_day)
#1.2.2 - How many people of each gender is able to touch the floor

df %>% 
  filter(touch_floor=="Yes"|touch_floor=="Yes of course") %>% 
  group_by(gender) %>%
  summarise(gender_count=n())



#1.3 - Wereable to hold breath longer than average
df %>% 
  filter(breathhold>mean(breathhold)) %>% 
  select(c("name","breathhold")) %>% 
  arrange(desc(breathhold))

#1.4 Could balance a balloon between 13 and 60 seconds

df %>% 
  filter(balloon_balance<60 & balloon_balance>13)%>% 
  select(c("name","balloon_balance"))%>% 
  arrange(desc(balloon_balance))

#1.5 All of the above in on pipeline
df %>% 
  filter(shoesize>39) %>% 
  filter(touch_floor=="Yes"|touch_floor=="Yes of course") %>% 
  filter(breathhold>mean(breathhold)) %>% 
  filter(balloon_balance<60 & balloon_balance>13) %>% 
  select(c("name","birth_day","shoesize","touch_floor","breathhold","balloon_balance"))

#2 Exersice 2: arrange()
#2.1 Sort data so it starts with the slowest tongue twister person
df %>% 
  select(c("name","tongue_twist")) %>% 
  arrange(desc(tongue_twist))
#2.2 Sort data by one argument to find the student who performed best at the
#Romberg task (you define best)
df %>% 
  mutate(romberg_avg=(romberg_open+romberg_closed)/2) %>% 
  select(c("name","romberg_avg")) %>% 
  arrange(desc(romberg_avg))

#3 Exersice 3: select()
#3.1 What happens if you select the same column multiple times? 
select(df,c("name","name","birth_day","birth_day"))
#If you select a column multiple times, it only shows it once

#3.1 Make the following vector cols <- c("name","shoesize","touch_floor")
cols <- c("name","shoesize","touch_floor")

#3.2 What happens when you select with this vector?
select(df,cols)

#3.3 Rearrange the columns of the dataframe with gender and shoesize first

new_df <- df %>%
  select(gender,shoesize,everything()) %>% 
  view

#4 Exercise 4: mutate()
#4.1 The tongue twister had 99 words. Make a new column called "words_per_sec"
#where you calculate how many words each student said per second.

df %>% 
  mutate(words_per_sec=99/tongue_twist) %>% 
  select(c("name","words_per_sec")) %>% 
  arrange(desc(words_per_sec))

#4.2.1 Currently breath_hold is in seconds. Convert it into two new columns called
# "breath_min" and "breath_sec" containing the number of whole minutes
# (achieved by dividing using %/%) and remaining seconds respectively

df %>% 
  mutate(breath_min=breathhold%/%60) %>% 
  mutate(breath_sec=breathhold/60-breath_min) %>% 
  select(c("name","breathhold","breath_min","breath_sec")) %>% 
  arrange(desc(breathhold))

#4.2.2 BONUS: create a new column calculating how far is from the average
#breath_hold

df %>% 
  mutate(breath_min=breathhold%/%60) %>% 
  mutate(breath_sec=breathhold/60-breath_min) %>% 
  mutate(from_avg_breath=abs(breathhold-mean(breathhold))) %>% 
  select(c("name","breathhold","breath_min","breath_sec","from_avg_breath")) %>% 
  arrange(desc(breathhold))

#5 Exercise 5: summarise()
#5.1 Is there a gender difference when it comes to balloon balancing? 
#(hint: group_by and %>% are your friends!) 

#Finding mean of a collumn
df %>% 
  summarize(balloon_balance=mean(balloon_balance))

#Mean grouped be gender
df %>% 
  group_by(gender) %>% 
  summarize(balloon_balance=mean(balloon_balance))

#5.2. Is there a relation between sound level preference and which cola was chosen? 
#mean(x,na.rm = TRUE), used to ignore NA cases
df %>% 
  group_by(taste_cola) %>%
  summarize(sound_level_pref=mean(sound_level_pref,na.rm = TRUE))

#Result:
#mean of Option L = 10.4
#mean of Option S = 12.6


#5.3 Does handedness influence tongue twisting speed? 
df %>% 
  group_by(handedness) %>%
  summarize(tongue_twist=mean(tongue_twist)) %>% 
  view

#Results
#mean of Left-handed =  50.7 sec
#mean of Right-handed =   47.7 sec


#5.3.1 Add a column to the summary which contains number of people in each group 
#(e.g. number of right handed people). Hint: look at the n()-function
df %>% 
  group_by(handedness) %>%
  summarise(handedness_count=n()) %>% 
  view

# Number of Left-handed = 4
# Number of Right-handed = 44

#5.3.2 Does this tell us something about the reliability?
#It's not very reliable, as the data-set of left-handen people is a tenth of the size of
#the right-handed data-set.



