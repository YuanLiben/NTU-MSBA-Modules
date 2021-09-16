### R Final Assignment
### Q1 Solution
### Date:     2021 Jul 28
### Author:   Yuan Liben
### Organisation: Nanyang Business School, NTU
### Program:  MSBA
### Course:   AN6100-Programming Essentials
### --------------------------------------------
# Sample A
##Generate 1000 random normally distributed numbers
##with mean 500 and sd 75.
set.seed(3993)
normVals = round(rnorm(1000, 500, 75))
##Randomly sample 15 numbers from normVals with replacement
sampleA = sample(x = normVals,size = 15, replace = T)
avgA = mean(sampleA)
sdA = sd(sampleA)
print('The mean of sample A is')
avgA
print('The standard deviation of sample A is')
sdA
#Answer1:The mean of sample A is 530.2, the sd is 66.07053.

#Sample B
sampleB = sample(x = normVals,size = 30, replace = T)
avgB = mean(sampleB)
sdB = sd(sampleB)
print('The mean of sample B is')
avgB
print('The standard deviation of sample B is')
sdB
#Answer2:The mean of sample B is 504.7333, the sd is 65.76758.

#Sample C
sampleC = sample(x = normVals,size = 60, replace = T)
avgC = mean(sampleC)
sdC = sd(sampleC)
print('The mean of sample C is')
avgC
print('The standard deviation of sample C is')
sdC
#Answer3:The mean of sample C is 508.3, the sd is 72.4745.

print('Sample B gives the smallest sampled standard deviation.')
#Answer4: Sample B gives the smallest sampled standard deviation.