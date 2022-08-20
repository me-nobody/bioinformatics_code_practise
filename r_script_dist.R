library(ggplot2)
plot_clust<-function(df){
  # standardizing the data
  df<-scale(df)
  # find the distances
  dist_manhhtn<-dist(df,method="manhattan")
  dist_eucln<-dist(df,method="euclidian")
  dist_corr<-as.dist(1-cor(t(df)))
  
  # cluster on distances using hierarchical clustering method complete
  clust_manhhtn_cmp<-hclust(dist_manhhtn,method="complete")
  clust_eucln_cmp<-hclust(dist_eucln,method="complete")
  clust_corr_cmp<-hclust(dist_corr,method="complete")
  
  # cluster on distances using hierarchical clustering method single
  clust_manhhtn_sg<-hclust(dist_manhhtn,method="single")
  clust_eucln_sg<-hclust(dist_eucln,method="single")
  clust_corr_sg<-hclust(dist_corr,method="single")
  
  # cluster on distances using hierarchical clustering method average
  clust_manhhtn_upgma<-hclust(dist_manhhtn,method="average")
  clust_eucln_upgma<-hclust(dist_eucln,method="average")
  clust_corr_upgma<-hclust(dist_corr,method="average")
  
  # create a plotting frame of 3 rows and 1 column using par(mfrow) function
  par(mfrow=c(3,3))
  plot(clust_manhhtn_cmp)
  plot(clust_eucln_cmp)
  plot(clust_corr_cmp)
  plot(clust_manhhtn_sg)
  plot(clust_eucln_sg)
  plot(clust_corr_sg)
  plot(clust_manhhtn_upgma)
  plot(clust_eucln_upgma)
  plot(clust_corr_upgma)
  
  
}
