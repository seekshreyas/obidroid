# Android App Analysis 
# Unsupervised learning
# ========================
# code referred from: http://www.statmethods.net/advstats/cluster.html

# load data
appData <- read.csv("appFeatures.csv", header=TRUE)
# data preparation
appData <- na.omit(appData)
appData <- scale(appData) # standardize variables
attach(appData)
head(appData)
summary(appData)



# Data Inspection
boxplot(appData)
pairs(appData)


# CLUSTERING
# ------------

# K-Means Clustering 

# To determine the number of clusters
wss <- (nrow(appData)-1)*sum(apply(appData,2,var))
for (i in 2:15) wss[i] <- sum(kmeans(appData, centers=i)$withinss)
plot(1:15, wss, type="b", xlab="Number of Clusters", ylab="Within groups sum of squares")

# K-Means Cluster Analysis
fit <- kmeans(appData, 10) 
# get cluster means 
aggregate(appData,by=list(fit$cluster),FUN=mean)
# append cluster assignment
appData <- data.frame(appData, fit$cluster)


# Hierarchical Clustering
d <- dist(appData, method = "euclidean") # distance matrix
fit <- hclust(d, method="ward") 
plot(fit) # display dendogram
groups <- cutree(fit, k=10) # cut tree into 5 clusters
# draw dendogram with red borders around the 5 clusters 
rect.hclust(fit, k=10, border="red")

# Ward Hierarchical Clustering with Bootstrapped p values
library(pvclust)
fit <- pvclust(appData, method.hclust="ward", method.dist="euclidean")
plot(fit) # dendogram with p values
# add rectangles around groups highly supported by the data
pvrect(fit, alpha=.95)


# Model Based Clustering
library(mclust)
fit <- Mclust(appData)
plot(fit) # plot results 
summary(fit) # display the best model

# Plotting Cluster Solutions
# K-Means Clustering with 5 clusters
fit <- kmeans(appData, 10)

# Cluster Plot against 1st 2 principal components

# vary parameters for most readable graph
library(cluster) 
clusplot(appData, fit$cluster, color=TRUE, shade=TRUE, labels=2, lines=0)

# Centroid Plot against 1st 2 discriminant functions
library(fpc)
plotcluster(appData, fit$cluster)


