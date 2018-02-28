
stroopdata <- read.csv('stroopdata.csv')
head(stroopdata)

library(ggplot2)
library(gridExtra)

ggplot(aes(Congruent), data = stroopdata)+
  geom_histogram(breaks = c(8,12,16,20,24), color =I('black'),
                 fill = I('#099009'))+
  ggtitle('Congruent Histogram')
  
ggplot(aes(Incongruent), data = stroopdata)+
  geom_histogram(breaks = c(16,20,24,28,32,36), color =I('black'),
                 fill = I('#099009'))+
  ggtitle('Incongruent Histogram')

p1 <- ggplot(aes(y = Congruent, x = 1), data = stroopdata)+
  geom_boxplot(fill = 'green')

p2 <- ggplot(aes(y = Incongruent, x = 1), data = stroopdata)+
  geom_boxplot(fill = 'blue')

grid.arrange(p1,p2,ncol=2)
