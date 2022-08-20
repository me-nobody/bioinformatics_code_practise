prac_func2 <- function(df){
                     count <- 0
                     # for(i in seq_len(nrow(df))){
                     #   # print(i)
                     #   count <- c(count,df[i,4]- df[i,30])
                     # }
                     column_count <- 1
                     column_count <- apply(df[,-1],1,sum)
                     list_2_return <- list(count,column_count)
                     return (list_2_return)
}