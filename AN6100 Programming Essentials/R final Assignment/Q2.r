### R Final Assignment
### Q2 Solution
### Date:     2021 Jul 28
### Author:   Yuan Liben
### Organisation: Nanyang Business School, NTU
### Program:  MSBA
### Course:   AN6100-Programming Essentials
### --------------------------------------------
##set seed value
set.seed(6226)

bigSmall = function() {
  ##generates a vector of 5,000 uniformly distributed rounded off numbers 
  ##from 20 to 80.
  randB = round(runif(5000, 20, 80))
  for (i in (1:5000)){
    if (randB[i] >= 65){
      randB[i] = 'BIG'
    } else {
      randB[i] = 'small'
    }
  }
  return(randB)
}

randB = bigSmall()
table(randB)
#Answer1: 1332 BIG numbers were generated. 3668 small numbers were generated.
probability = (64-20+1) / (80-20+1)
print(probability)
#Answer2: Because these numbers are uniformly distributed, so the probability 
#         of getting a 'small' integer is 0.7377049.