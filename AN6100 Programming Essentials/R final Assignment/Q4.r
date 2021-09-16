### R Final Assignment
### Q4 Solution
### Date:     2021 Jul 28
### Author:   Yuan Liben
### Organisation: Nanyang Business School, NTU
### Program:  MSBA
### Course:   AN6100-Programming Essentials
### --------------------------------------------
library(cluster)
wd = getwd()
setwd(wd)

##read the csv file into dataframe and perform divisive clustering
df = read.csv(file = 'AN6100-Data-3B.csv', header = TRUE)
clusDn = diana(df, metric = 'euclidean')
##cut the dendrogram to make 3 clusters
clusDn2 = cutree(clusDn, k = 3)
table(clusDn2)
#Answer1:Cluster 3 is the smallest.
#Answer2:766 people are in the largest cluster-cluster 1.
#        And 46 people are in the smallest cluster-cluster 3.

##create the BMI column in the dataframe and calculate the mean BMI
df$BMI = df$Weight / (df$Height ^ 2)
mean(df$BMI)
#Answer3:The mean BMI of all is 18.89139.

##make a income vs BMI plot and draw a line where BMI = 18.5
plot(df$Income.Annual, df$BMI, type = 'p', col=clusDn2, 
     xlab = 'Annual Income ($)', ylab = 'BMI')
abline(h = 18.5, col = 'Orange', lty = 2, lwd = 2)
#Answer4:The people in the smallest cluster (cluster 3) are the people who earn the most income and are generally healthier, and in general, the more income they earn, the healthier they are.