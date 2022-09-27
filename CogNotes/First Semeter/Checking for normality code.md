Written by: Laurits Lyngbæk
Source of information:
Association links: [[Normal Distrubution]]
Tags: #🖥️Code
___
##  Checking for normality
```r
#Data Description
round(pastecs::stat.desc(
  cbind(df$x1,df$x2),
  basic = FALSE, norm = TRUE,desc = FALSE), 
  digits = 2)

#Smooth historgram
ggplot(df, aes(x1)) + 
  geom_density(alpha=.5,fill="pink")

#QQ-plot
ggplot(df, aes(sample = x1))+
  stat_qq()+
  stat_qq_line(color="red")+
   labs(x = "Theoretical Quantiles",
        y = "Sample Quantiles",
        title = "QQ-plot of breathhold")+
  theme_bw()
```

### Transformation of data:
```r
#Transforming Data
trans_df <- df %>% 
  mutate(
    logx1 = log(x1), 
    sqrtx1 = sqrt(x1),
    recipx1 = 1/(x1))

round(pastecs::stat.desc(
  cbind(x1 = trans_df$x1,
        logx1 = trans_df$logx1,
        sqrtx1 = trans_df$sqrtx1,
        - recix1 = trans_df$recipx1
        ),
  basic = FALSE, norm = TRUE,desc = F), 
  digits = 2)

```
  
  



