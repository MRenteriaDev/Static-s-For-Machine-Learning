survey = read.csv('../Data/survey.csv', header=TRUE)

tbl = table(survey$Smoke,survey$Exer)
p_val = chisq.test(tbl)
