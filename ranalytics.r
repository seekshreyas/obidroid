# Android App Analysis 
# Unsupervised learning
# ========================
# code referred from: http://www.statmethods.net/advstats/cluster.html

setwd("~/Documents/_Berkeley/sem3/i219ComputerSecurity/obidroid")

# load data
appData <- read.csv("appFeatures.csv", header=TRUE)
# data preparation
appData <- na.omit(appData)
appData <- scale(appData) # standardize variables
attach(appData)
head(appData)
summary(appData)

hist(appData$revSent)
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
fit <- kmeans(appData, 11) 
fit

plot(fit)
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


# Cluster Plots
require(vegan)
data(dune)

# kmeans
kclus <- kmeans(dune,centers= 4, iter.max=1000, nstart=10000)

# distance matrix
dune_dist <- dist(dune)

# Multidimensional scaling
cmd <- cmdscale(dune_dist)

# plot MDS, with colors by groups from kmeans
groups <- levels(factor(kclus$cluster))
ordiplot(cmd, type = "n")
cols <- c("steelblue", "darkred", "darkgreen", "pink", "blue", "lightgreen", "#bada55", "#666666", "yellow", "orange")
for(i in seq_along(groups)){
  points(cmd[factor(kclus$cluster) == groups[i], ], col = cols[i], pch = 16)
}


ordispider(cmd, factor(kclus$cluster), label = TRUE)
ordihull(cmd, factor(kclus$cluster), lty = "dotted")

hc <- hclust(dist(appData))
plot(hc)
plot(hc, hang=-30)



## tweeking some parameters for plotting a dendrogram
# set background color
op = par(bg="#DDE3CA")
# plot dendrogram
plot(hc, col="#487AA1", col.main="#45ADA8", col.lab="#7C8071", col.axis="#F38630", lwd=3, lty=3, sub='', hang=200, axes=TRUE)
# add axis
axis(side=2, at=seq(0, 400, 100), col="#F38630", labels=TRUE, lwd=2)
# add text in margin
mtext(seq(0, 400, 100), side=2, at=seq(0, 400, 100), line=1, col="#A38630", las=2)




# using dendrogram objects
hcd = as.dendrogram(hc)
# alternative way to get a dendrogram
op = par(mfrow = c(2,1))
plot(hcd)
# triangular dendrogram
plot(hcd, type="triangle")
par(op)

par(op)




# plot dendrogram with some cuts
op = par(mfrow = c(2,1))
plot(cut(hcd, h=75)$upper, main="Upper tree of cut at h=75")
plot(cut(hcd, h=75)$lower[[2]], main="Second branch of lower tree with cut at h=75")
par(op)


# vector of colors
labelColors = c("#CDB380", "#036564", "#EB6841", "#EDC951")
# cut dendrogram in 4 clusters
clusMember = cutree(hc, 4)
# function to get color labels
colLab { if(is.leaf(n)) { a     labCol     attr(n, "nodePar")   } n}
# using dendrapply
clusDendro = dendrapply(hcd, colLab)
# make plot
plot(clusDendro, main = "Cool Dendrogram", type = "triangle")






# load package ape;
# remember to install it: install.packages("ape")
library(ape)
# plot basic tree
plot(as.phylo(hc), cex=0.9, label.offset=1, xlim=x.lim)
# cladogram
plot(as.phylo(hc), type="cladogram", cex=0.9, label.offset=1)
# unrooted
plot(as.phylo(hc), type="unrooted")
# fan
plot(as.phylo(hc), type="fan")
# radial
plot(as.phylo(hc), type="radial")



library(ggplot2)
library(ggdendro)
# basic option
ggdendrogram(hc, theme_dendro=TRUE, rotate=TRUE)
# another option
ggdendrogram(hc, rotate=TRUE, size=100, theme_dendro=TRUE, color="tomato")





# load packages
library(corrgram)

# create correlation matrix
set.seed(707)
R = cor(matrix(rnorm(70), 10, 7))

# vector of colors (purple to orange)
purple_orange = c("#8073AC","#B2ABD2","white","#E08214","#FDB863")

# create correlation matrix
corrgram(appData, order=TRUE, lower.panel=panel.shade, upper.panel=panel.pie,
         text.panel=panel.txt, main="Example",
         col.regions=colorRampPalette(purple_orange))






library(cluster)
library(HSAUR)
data(pottery)
km <- kmeans(appData,10)
dissE <- daisy(appData) 
dE2 <- dissE^2
sk2 <- silhouette(km$cl, dE2)
plot(sk2)


library(cluster)
library(fpc)

data(iris)
dat <- iris[, -5] # without known classification 
# Kmeans clustre analysis
clus <- kmeans(appData, centers=3)
plotcluster(appData, clus$cluster)