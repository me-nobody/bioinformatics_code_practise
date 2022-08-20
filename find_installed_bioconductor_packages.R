library(dplyr)
library(sessioninfo)
df_installed <- as_tibble(installed.packages())
pkgs <- pull(df_installed,Package)
pkg_details <- lapply(pkgs,utils::packageDescription)
sources<-vapply(pkg_details,sessioninfo:::pkg_source,character(1))
bioc_pkgs <- data_frame(pkgs, sources) %>%
filter(sources == "Bioconductor")
