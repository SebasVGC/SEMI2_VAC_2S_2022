#DATASET 1
dataset <- read.csv(file="C:/Users/SebasVGC/Documents/SEBASTIAN/Github/SEMI2_VAC_2S_2022/Ejemplo R/StreamingHistory2Original.csv")

dataCanciones1 <- as.data.frame(dataset)

#EDA
par(mfrow=c(2,2))

#Histograma de los ms
hist(x=dataCanciones1$msPlayed, xlab = "ms",ylab="Frecuencia",main = "ms time")

#Densidad de los ms
plot(density(dataCanciones1$msPlayed),"Densidad de ms time")

#QPLOT de los ms
qqplot(dataCanciones1$msPlayed,main="QQPlot de preciosms time")
qqnorm(dataCanciones1$msPlayed,main="QQPlot de preciosms time")


#OUTLIERS
boxplot(dataCanciones1$msPlayed,main = "Boxplot de ms time")


#MEDIA, MEDIANA, MODA
#DATASET 1 original

#MS
mediana<-median(dataCanciones1$msPlayed)
media<-mean(dataCanciones1$msPlayed)
Frecuencia1 <- data.frame(table(dataCanciones1$msPlayed))
moda1 <- Frecuencia1[which.max(Frecuencia1$Freq),1]
paste("Medidas para ms time: MEDIA:",media,"MEDIANA:",mediana,"MODA:",moda1)
