
setwd("C:/Users/Jennifer/Desktop")
commits_data <- read.csv('testFile.csv', header=TRUE)
plot(commits_data$Day, commits_data$Author)
summary(commits_data)

plot(commits_data$Author, commits_data$Day)

pairs(commits_data)

