diamonds
ggplot(aes(x = price, fill = cut), data = diamonds)+
  geom_histogram()+
  facet_wrap(~color)+
  scale_fill_brewer(type = 'qual')

ggplot(aes(x=table, y =price, color = cut), data= diamonds)+
  geom_point()+
  scale_fill_brewer(type = 'qual')

idealdia <- subset(diamonds, diamonds$cut=='Ideal')
summary(idealdia$table)
predia <- subset(diamonds, diamonds$cut=='Premium')
summary(predia$table)

diamonds$volume <- diamonds$x * diamonds$y * diamonds$z
ggplot(aes(x = volume, y = price, color = clarity), data =diamonds)+
  geom_point()+
  scale_y_log10()+
  coord_cartesian(xlim = c(0, quantile(diamonds$volume, 0.99)))+
  scale_fill_brewer(type = 'div')

head(pf)
pf$prop_initiated <- pf$friendships_initiated/pf$friend_count

ggplot(aes(color = year_joined.bucket, x = tenure, y = prop_initiated), data= pf)+
  geom_line(stat = 'summary', fun.y = median)+
  scale_fill_brewer(type = 'qual')+
  geom_smooth()


ggplot(aes(color = year_joined.bucket, x = 40*(round(tenure/40)), y = prop_initiated), data= pf)+
  geom_line(stat = 'summary', fun.y = median)+
  scale_fill_brewer(type = 'qual')+
  geom_smooth()

pf.high_bucket <- subset(pf, !is.na(pf$prop_initiated))
pf.high_bucket <- subset(pf.high_bucket, year_joined.bucet = '(2012,2014]' )
summary(pf.high_bucket$prop_initiated)
head(pf.high_bucket)


ggplot(aes(y = price/carat, x = cut, color = color), data = diamonds)+
  geom_point()+
  scale_fill_brewer(type = 'qual')+
  facet_wrap(~clarity)

ggplot(aes(y = price/carat, x = cut, color = color), data = diamonds)+
  geom_jitter()+
  scale_fill_brewer(type = 'qual')+
  facet_wrap(~clarity)

ggplot(aes(y = price, x = carat), data = diamonds)+
  geom_point()
  