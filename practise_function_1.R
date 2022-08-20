library(dplyr)
my_func1 <- function(data_frame){
            data_frame <- data_frame %>% group_by(group) %>% summarise(mean(values))
            return (data_frame)
  }