### R Final Assignment
### Q3 Solution
### Date:     2021 Jul 28
### Author:   Yuan Liben
### Organisation: Nanyang Business School, NTU
### Program:  MSBA
### Course:   AN6100-Programming Essentials
### --------------------------------------------
library(dplyr)
wd = getwd()
setwd(wd)

##Read csv file into dataframe and then create Hello column according to gender
df = read.csv(file = 'AN6100-Data-3B.csv', header = TRUE)
df$Hello = ifelse(df$Gender == 'M', 
                  paste('Mr', df$Lastname), 
                  paste('Ms', df$Lastname))
##Filter the dataframe by annual income and weight and create a new dataframe
df1 = filter(df, Income.Annual >= 80000 & Weight >= 80)
highincome = data.frame(df1[c('Hello','Income.Annual','Job.Title','Country')])
##Write the new dataframe into csv file
write.csv(highincome, 'highincome.csv', row.names=FALSE)

print(length(unique(df$Country)))
#Answer1: 49 different countries are found in AN6100-Data-3B.csv.

male = length(grep('Mr',highincome$Hello))
female = length(grep('Ms',highincome$Hello))
male
female
#Answer2:There are 5 male and 0 female in 'highincome.csv'.