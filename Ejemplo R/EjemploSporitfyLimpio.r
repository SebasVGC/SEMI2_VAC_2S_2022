#DATASET 1
datasetLimpio <- read.csv(file="C:/Users/SebasVGC/Documents/SEBASTIAN/Github/SEMI2_VAC_2S_2022/Ejemplo R/StreamingHistory2Limpio.csv")

dataCanciones2 <- as.data.frame(datasetLimpio)

#EDA
par(mfrow=c(2,2))

#Histograma de los ms
hist(x=dataCanciones2$msPlayed, xlab = "ms",ylab="Frecuencia",main = "ms time")

#Densidad de los ms
plot(density(dataCanciones2$msPlayed),"Densidad de ms time")

#QPLOT DE MS
qqplot(dataCanciones2$msPlayed,main="QQPlot de preciosms time")
qqnorm(dataCanciones2$msPlayed,main="QQPlot de preciosms time")


#OUTLIERS
boxplot(dataCanciones2$msPlayed,main = "Boxplot de ms time")


#MEDIA, MEDIANA, MODA
#DATASET LIMPIO
mediana<-median(dataCanciones2$msPlayed)
media<-mean(dataCanciones2$msPlayed)
Frecuencia1 <- data.frame(table(dataCanciones2$msPlayed))
moda1 <- Frecuencia1[which.max(Frecuencia1$Freq),1]
paste("Medidas para ms time: MEDIA:",media,"MEDIANA:",mediana,"MODA:",moda1)
