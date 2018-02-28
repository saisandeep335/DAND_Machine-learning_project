setwd('C:/Users/Saisandeep/Documents/Udacity Data Analyst/EDA')
statesInfo <- read.csv('stateData.csv')
subset(statesInfo,state.region == 1)
statesInfo[statesInfo$state.region==1,]


reddit<-read.csv('reddit.csv')
table(reddit$employment.status)
summary(reddit)
str(reddit)
levels(reddit$age.range)
reddit$age.range <-ordered(reddit$age.range, levels = c("Under 18", "18-24", "25-34", "35-44", "45-54", "55-64", "65 or Above"))
library(ggplot2)
qplot(data = reddit,x = age.range)

install.packages('devtools', dependencies = T)
library(devtools)
install_version("colorspace","1.2-4")

list.files()
pf <- read.csv("pseudo_facebook.tsv",sep = '\t')
names(pf)
install.packages('ggthemes', dependencies = TRUE)
library(ggthemes)
qplot(x = dob_day, data = pf)+
  scale_x_discrete(breaks = 1:31)

ggplot(aes(x = dob_day), data = pf) +
  geom_histogram(binwidth = 1) +
  scale_x_continuous(breaks = 1:31)+
  facet_wrap(~dob_month, ncol = 3)

ggplot(data = pf, aes(x = dob_day)) +
  geom_histogram(binwidth = 1) +
  scale_x_continuous(breaks = 1:31) +
  facet_wrap(~dob_month)


qplot(x = friend_count, data = pf, binwidth = 25)+
  scale_x_continuous(limits = c(0,1000),breaks = seq(0,1000,50))+
  facet_wrap(~gender,ncol = 2)

qplot(x = friend_count, data = subset(pf,!is.na(gender)), binwidth = 10)+
  scale_x_continuous(limits = c(0,1000),breaks = seq(0,1000,50))+
  facet_wrap(~gender,ncol = 2)

by(pf$friend_count, pf$gender, summary)

qplot(x = friend_count, data = subset(pf,!is.na(gender)), binwidth = 10)+
  scale_x_continuous(limits = c(0,1000),breaks = seq(0,1000,50))+
  facet_wrap(~gender,ncol = 2)


qplot(x = pf$tenure/365, data = pf, binwidth = .25,
      xlab = 'Number of years using Facebook',
      ylab = 'Number of users in Sample',
      color = I('black'),fill = I('#099009'))+
  scale_x_continuous(breaks = seq(1,7,1), limits = c(0,7))


qplot(x = pf$age, data = pf, binwidth = 5,
      xlab = 'Age of Users', ylab = 'Number of Users',
      color = I('black'), fill = I('#5760AB'))

summary(pf$friend_count)
summary(log10(pf$friend_count+1))
summary(sqrt(pf$friend_count))

install.packages("gridExtra")
library(gridExtra)

p1 = qplot(pf$friend_count, data = pf)
p2 = qplot(log10(pf$friend_count+1), data = pf)
p3 = qplot(sqrt(pf$friend_count),  data = pf)

p1 <- ggplot(aes(x = pf$friend_count), data = pf) + geom_histogram()
p2 <- p1 + scale_x_log10()
p3 <- p1 + scale_x_sqrt()

grid.arrange(p1,p2,p3, ncol = 1)

qplot(x = pf$friend_count, data = subset(pf,!is.na(pf$gender)))

head(!is.na(pf$gender))

qplot(x = friend_count, data = subset(pf,!is.na(gender)), binwidth = 10, geom = 'freqpoly',
      color = gender)+
  scale_x_continuous(breaks = seq(0,1000,50), lim = c(0,1000))
  
qplot(x = friend_count, y = ..count../sum(..count..),
      data = subset(pf,!is.na(gender)), 
      xlab = 'Number of friends for User',
      ylab = 'Proportions of users with that friend count',
      binwidth = 10, geom = 'freqpoly',
      color = gender)+
  scale_x_continuous(breaks = seq(200,1000,50), lim = c(600,1000))

qplot(x = www_likes,
      data = subset(pf,!is.na(gender)), 
      xlab = 'Number of Likes for User',
      ylab = 'Number of users with that Likes',
      binwidth = 10, geom = 'freqpoly',
      color = gender)+
  scale_x_continuous(breaks = seq(20,500,20), lim = c(20,500))


qplot(x = www_likes,
      data = subset(pf,!is.na(gender)), 
      xlab = 'Number of Likes for User',
      ylab = 'Number of users with that Likes',
      binwidth = 10, geom = 'freqpoly',
      color = gender)+
  scale_x_continuous(breaks = seq(0,20,1), lim = c(0,20))


sum(subset(pf, pf$gender == 'male')$www_likes)
head(subset(pf, pf$gender == 'male'))


qplot(x = gender, y = friend_count, 
      data = subset(pf,!is.na(gender)),
      geom = 'boxplot')+
  scale_y_continuous(lim = c(0,150), breaks = seq(0,150,25))

qplot(x = gender, y = friend_count, 
      data = subset(pf,!is.na(gender)),
      geom = 'boxplot')+
  coord_cartesian(ylim = c(0,1000))

by(pf$friend_count, pf$gender, summary)

qplot(x = gender, y = friendships_initiated, 
      data = subset(pf,!is.na(gender)),
      geom = 'boxplot')+
  coord_cartesian(ylim = c(0,250))

by(pf$friendships_initiated, pf$gender, summary)


summary(pf$mobile_likes)
summary(pf$mobile_likes>0)
mobile_check_in <- NA
pf$mobile_check_in <- ifelse(pf$mobile_likes>0, 1, 0)
pf$mobile_check_in <- factor(pf$mobile_check_in)
summary(pf$mobile_check_in)
head(pf$mobile_check_in)

63947/(63947+35056)
sum(pf$mobile_check_in==1)/length(pf$mobile_check_in)

data("diamonds")
summary(diamonds)
?diamonds
qplot(price, data = diamonds)
summary(diamonds$price)
d500below <- subset(diamonds, diamonds$price<500)
d250below <- subset(diamonds, diamonds$price<250)
d15kabv <- subset(diamonds, diamonds$price>=15000)

qplot(price, data = diamonds)+
  scale_x_log10()

qplot(price, data = diamonds, binwidth = 1)+
  scale_x_continuous(lim = c(0,2000), breaks = seq(0,2000,50))

qplot(price, data = diamonds, binwidth = 1)+
  scale_x_continuous(lim = c(2000,15000), breaks = seq(0,2000,250))

qplot(price,data=diamonds)+
  facet_wrap(~cut, ncol = 3)

summary(subset(diamonds$price, diamonds$cut == 'Fair'))
summary(subset(diamonds$price, diamonds$cut == 'Good'))
summary(subset(diamonds$price, diamonds$cut == 'Very Good'))
summary(subset(diamonds$price, diamonds$cut == 'Premium'))
summary(subset(diamonds$price, diamonds$cut == 'Ideal'))

max(subset(diamonds$price, diamonds$cut == 'Premium'))
max(subset(diamonds$price, diamonds$cut == 'Very Good'))
min(subset(diamonds$price, diamonds$cut == 'Ideal'))
min(subset(diamonds$price, diamonds$cut == 'Premium'))

qplot(x = price, data = diamonds) + facet_wrap(~cut)

qplot(x = price, data = diamonds) + facet_wrap(~cut, scales = 'free_y')

qplot(x = price/carat, data = diamonds)+
  facet_wrap(~cut)+
  scale_x_log10()

qplot(x = color, y = price, data = diamonds, geom = 'boxplot')+
  coord_cartesian(ylim = c(0,10000))

summary(subset(diamonds$price, diamonds$color == 'D'))
summary(subset(diamonds$price, diamonds$color == 'J'))
?diamonds

qplot(x = color, y = price/carat, data = diamonds, geom = 'boxplot')

qplot(x = carat, data = diamonds, geom = 'freqpoly', binwidth = 0.1)
install.packages('xlsx')

library(xlsx)
emp_data <- read.xlsx('indicator_t 15-24 employ.xlsx', sheetName = 'Data', header = TRUE)
head(emp_data)
colnames(emp_data)
colnames(emp_data)[1] <- "country"
colnames(emp_data)[19]
emp_data$NA. <- NULL
qplot(X2007, data =emp_data, binwidth = 10)
qplot(X2007, data =emp_data, binwidth = 10, geom = 'freqpoly')
head(emp_data)

emp_data_t <- t(emp_data)
head(emp_data_t)
colnames(emp_data_t)
emp_data_t[1,]
colnames(emp_data_t) <- emp_data_t[1,]
head(emp_data_t)
emp_data_t <- emp_data_t[-1,]
colnames(emp_data_t)


birthdays <- read.csv('birthdaysExample.csv')
head(birthdays)
fb_birthdays <- read.csv('birthdays.csv', header = FALSE)
head(fb_birthdays)
colnames(fb_birthdays) <- c('year', 'month','date','name')
qplot(month, data = fb_birthdays, binwidth = 0.5,
      color = 'black', fill = '#099009')+
  scale_x_continuous(lim = c(0,13),breaks = seq(1,12,1))
  
qplot(date, data = fb_birthdays, binwidth = 0.5,
      color = 'black', fill = '#099009')+
  scale_x_continuous(lim = c(0,32),breaks = seq(1,31,1))

summary(fb_birthdays$month)
summary(fb_birthdays$date)

ftable(fb_birthdays$month)
ftable(fb_birthdays$date)

qplot(date, data = fb_birthdays, binwidth = 0.5,
      color = 'black', fill = '#099009')+
  scale_x_continuous(lim = c(0,32),breaks = seq(1,31,1))+
  facet_wrap(~month)