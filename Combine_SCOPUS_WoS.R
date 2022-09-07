setwd("D:/pasta")
getwd()
library(bibliometrix)

scopus_files <- c("scopus.bib")
S=convert2df(scopus_files, dbsource = "scopus", format = "bibtex")
View(S)

wos_files <- c("savedrecs.bib", "savedrecs(1).bib", "savedrecs(2).bib")
W<-convert2df(wos_files, dbsource = "wos", format = "bibtex")
View(W)

Database=mergeDbSources(W, S, remove.duplicated = TRUE)
View(Database)
dim(Database)

write.table(Database, file = "database.txt", sep = "\t", row.names = FALSE)


