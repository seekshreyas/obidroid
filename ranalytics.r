# Android App Analysis 
# Unsupervised learning
# ========================
# code referred from: http://www.statmethods.net/advstats/cluster.html

setwd("~/Documents/_Berkeley/sem3/i219ComputerSecurity/obidroid")

# load data
appData <- read.csv("exports/appFeatures.csv", header=TRUE)
featData <- appData[c(2,3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)]

head(featData)
head(appData)

hist(appData$revSent)
hist(appData$revLength)

# CLUSTERING
# ------------

# K-Means Clustering 

# To determine the number of clusters
wss <- (nrow(featData)-1)*sum(apply(featData,2,var))
for (i in 2:15) wss[i] <- sum(kmeans(featData, centers=i)$withinss)
plot(1:15, wss, type="b", xlab="Number of Clusters", ylab="Within groups sum of squares")


library(cluster)

clus <- kmeans(featData, centers=7)
plotcluster(featData, clus$cluster)
