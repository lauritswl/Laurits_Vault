# QQ PLOT
#🥀Missing 

___

## How is QQ plots made?
```{r}

qq_plot_name <- DF_name %>% 
  ggplot(aes(sample = data)) +
    stat_qq() +
    stat_qq_line(colour = "red") +
    labs(x = "Theoretical Quantiles", y = "Sample Quantiles") +
    ggtitle("salient_means, qq plot") +
    theme_bw()

```


## How to use QQ plots?