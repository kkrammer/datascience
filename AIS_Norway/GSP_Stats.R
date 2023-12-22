install.packages("gapminder")
library(gapminder)
data(gapminder)
View(data)
summary(gapminder)
x <- mean(gapminder$gdpPercap)
x
attach(gapminder)
median(pop)
hist(lifeExp)
hist(log(pop))
boxplot(lifeExp, continent)     
plot(lifeExp, log(pop))
     
     
install.packages("dplyr")
library(dplyr)
df1 <- gapminder %>%
  select(country, lifeExp) %>%
  filter(country == "South Africa" | country == "Ireland")
t.test(data = df1, lifeExp ~ country)
install.packages("ggplot2")
library(ggplot2)

gapminder %>%
  filter(gdpPercap < 50000) %>%
  ggplot(aes(x=log(gdpPercap), y=lifeExp, col=year, size=pop))+
  geom_point(alpha=.3)+
  geom_smooth(method = lm)+
  facet_wrap(~continent)

summary(lm(lifeExp ~ gdpPercap+pop ))
