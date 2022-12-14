#DATASET 1
dataset <- read.csv(file="C:/Users/SebasVGC/Documents/SEBASTIAN/Github/SEMI2_VAC_2S_2022/Ejemplo practica 2/Dataset 1/datasetFlights.csv")

dataVuelos <- as.data.frame(dataset)

#EDA
par(mfrow=c(2,2))

#Histograma sobre los precios de los vuelos
hist(x=dataVuelos$price, xlab = "ms",ylab="Frecuencia",main = "Precios de vuelos")
hist(x=dataVuelos$time, xlab = "ms",ylab="Frecuencia",main = "Time de vuelos")
hist(x=dataVuelos$distance, xlab = "ms",ylab="Frecuencia",main = "Distancia de vuelos")

#Densidad de las distancias de los vuelos
plot(density(dataVuelos$price),"Densidad del precio de vuelos")
plot(density(dataVuelos$time),"Densidad del tiempo de vuelos")
plot(density(dataVuelos$distance),"Densidad de la distancia de vuelos")

#QPLOT SOBRE PRECIOS DE VUELOS
qqplot(dataVuelos$price,main="QQPlot de precios de vuelos")
qqnorm(dataVuelos$price,main="QQPlot de precios de vuelos")
qqnorm(dataVuelos$time,main="QQPlot de tiempo de vuelos")
qqnorm(dataVuelos$distance,main="QQPlot de distancia de vuelos")


qqPlot(dataHotel$total,main="QQPlot del hotal de dataHotel")

#OUTLIERS
boxplot(dataVuelos$time,main = "Boxplot del tiempo de vuelo")
boxplot(dataVuelos$price,main = "Boxplot del precio de vuelo")
boxplot(dataVuelos$distance,main = "Boxplot de la distancia de vuelo")


#MEDIA, MEDIANA, MODA
#DATASET 1

#VUELOS
mediana<-median(dataVuelos$price)
media<-mean(dataVuelos$price)
Frecuencia1 <- data.frame(table(dataVuelos$price))
moda1 <- Frecuencia1[which.max(Frecuencia1$Freq),1]
paste("Medidas para precio de vuelos: MEDIA:",media,"MEDIANA:",mediana,"MODA:",moda1)

mediana<-median(dataVuelos$distance)
media<-mean(dataVuelos$distance)
Frecuencia1 <- data.frame(table(dataVuelos$distance))
moda1 <- Frecuencia1[which.max(Frecuencia1$Freq),1]
paste("Medidas para distancia de vuelos: MEDIA:",media,"MEDIANA:",mediana,"MODA:",moda1)

mediana<-median(dataVuelos$time)
media<-mean(dataVuelos$time)
Frecuencia1 <- data.frame(table(dataVuelos$time))
moda1 <- Frecuencia1[which.max(Frecuencia1$Freq),1]
paste("Medidas para distancia de vuelos: MEDIA:",media,"MEDIANA:",mediana,"MODA:",moda1)

