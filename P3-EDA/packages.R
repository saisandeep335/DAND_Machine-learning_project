install.packages('reshape')
install.packages('plyr')
install.packages('dplyr')
install.packages('gridExtra')
install.packages('ggplot2')
install.packages('GGally')
install.packages('knitr')
install.packages('evaluate')
install.packages('stringi')
install.packages('backports')
library(backports)
require(devtools)

install_version("backports", version = '1.1.0')
devtools::install_github("r-pkgs/usethis")
install.packages('devtools')
install.packages('rmarkdown')
install.packages('rprojroot')
