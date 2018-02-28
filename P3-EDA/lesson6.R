data("diamonds")
head(diamonds)
ggplot(aes(x=x, y = price), data = diamonds)+
  geom_point()+
  coord_cartesian(xlim = c(quantile(diamonds$x,0.01),quantile(diamonds$x,0.99)))

summary(diamonds$x)

cor.test(diamonds$price,diamonds$x)
cor.test(diamonds$price,diamonds$y)
cor.test(diamonds$price,diamonds$z)

ggplot(aes(x=depth, y = price), data = diamonds)+
  geom_point()+
  coord_cartesian(xlim = c(50,75))
#coord_cartesian(xlim = c(quantile(diamonds$depth,0.01), quantile(diamonds$depth,0.99)))

summary(diamonds$depth)
cor.test(diamonds$price, diamonds$depth)

ggplot(aes(x=carat, y = price), data = diamonds)+
  geom_point()+
  coord_cartesian(xlim = c(0, quantile(diamonds$carat,0.99)), 
                  ylim = c(0, quantile(diamonds$price,0.99)))

diamonds$volume <- (diamonds$x * diamonds$y * diamonds$z)
head(diamonds)
3.95*3.98*2.43

ggplot(aes(x=volume, y = price), data = diamonds)+
  geom_point()

library(plyr)
count(diamonds$volume == 0)
detach("package:plyr", unload=TRUE)

diasub <- subset(diamonds, diamonds$volume > 0)
diasub <- subset(diasub, diasub$volume < 800)

diasub <- subset(diamonds, diamonds$volume > 0 & diamonds$volume<800)
summary(diasub$volume)

cor.test(diasub$price, diasub$volume)

ggplot(aes(x=volume, y = price), data = diasub)+
  geom_point(alpha = 0.15)+
  geom_smooth(method = 'lm', color='red')

suppressMessages(library(ggplot2))
suppressMessages(library(dplyr))
data(diamonds)

clarity_groups <- group_by(diamonds,clarity)
diamondsByClarity <- summarise(clarity_groups,
                               mean_price = mean(price),
                               median_price = median(price),
                               min_price = min(price),
                               max_price = max(price),
                               n = n())
diamondsByClarity <- arrange(diamondsByClarity, clarity)

head(diamondsByClarity)

diamonds_by_clarity <- group_by(diamonds, clarity)
diamonds_mp_by_clarity <- summarise(diamonds_by_clarity, mean_price = mean(price))
head(diamonds_mp_by_clarity)

diamonds_by_color <- group_by(diamonds, color)
diamonds_mp_by_color <- summarise(diamonds_by_color, mean_price = mean(price))
head(diamonds_mp_by_color)

p1 <- ggplot(aes(x = clarity, y = mean_price), data = diamonds_mp_by_clarity)+
  geom_bar(stat = "identity")

p2 <- ggplot(aes(x = color, y = mean_price), data = diamonds_mp_by_color)+
  geom_bar(stat = "identity")

grid.arrange(p1,p2,ncol = 1)

?diamonds

emp_data <- read.xlsx('indicator_t 15-24 employ.xlsx', sheetName = 'Data', header = TRUE)
head(emp_data)
colnames(emp_data)
colnames(emp_data)[1] <- "country"
colnames(emp_data)[19]
emp_data$NA. <- NULL

ggplot(aes(x = country, y = X2007), data = emp_data)+
  geom_bar(stat = 'Identity')+
  theme(axis.text.x = element_text(angle = 90, hjust = 1))

emp_data$avg <- mean(emp_data[2], emp_data[3])

ggplot()
