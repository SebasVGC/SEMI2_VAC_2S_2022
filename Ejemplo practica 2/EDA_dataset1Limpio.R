#DATASET 1
dataset <- read.csv(file="C:/Users/SebasVGC/Documents/SEBASTIAN/Github/SEMI2_VAC_2S_2022/Ejemplo practica 2/Dataset 1/datasetViajes.csv")

dataViajes <- as.data.frame(dataset)

#EDA
par(mfrow=c(2,2))

#Histograma sobre los precios de los vuelos
hist(x=dataViajes$price, xlab = "ms",ylab="Frecuencia",main = "Precios de vuelos")
hist(x=dataViajes$time, xlab = "ms",ylab="Frecuencia",main = "Tiempo de vuelos")
hist(x=dataViajes$distance, xlab = "ms",ylab="Frecuencia",main = "Distancia de vuelos")

#Densidad de los campos de los vuelos
plot(density(dataViajes$price),"Densidad del precio de vuelos")
plot(density(dataViajes$time),"Densidad del tiempo de vuelos")
plot(density(dataViajes$distance),"Densidad de la distancia de vuelos")

#QPLOT DE VUELOS
qqnorm(dataViajes$price,main="QQPlot de precios de vuelos")
qqnorm(dataViajes$time,main="QQPlot de tiempo de vuelos")
qqnorm(dataViajes$distance,main="QQPlot de tiempo de vuelos")

#OUTLIERS
boxplot(dataViajes$time,main = "Boxplot del tiempo de vuelo")
boxplot(dataViajes$price,main = "Boxplot del precio de vuelo")
boxplot(dataViajes$distance,main = "Boxplot de la distancia de vuelo")

#MEDIA, MEDIANA, MODA
#precio
mediana<-median(dataViajes$price)
media<-mean(dataViajes$price)
Frecuencia1 <- data.frame(table(dataViajes$price))
moda1 <- Frecuencia1[which.max(Frecuencia1$Freq),1]
paste("Medidas para precio de vuelos: MEDIA:",media,"MEDIANA:",mediana,"MODA:",moda1)


#tiempo
mediana2<-median(dataViajes$time)
media2<-mean(dataViajes$time)
Frecuencia2 <- data.frame(table(dataViajes$time))
moda2 <- Frecuencia2[which.max(Frecuencia2$Freq),1]
paste("Medidas para tiempo de vuelos: MEDIA:",media2,"MEDIANA:",mediana2,"MODA:",moda2)



#distancia
mediana3<-median(dataViajes$time)
media3<-mean(dataViajes$time)
Frecuencia3 <- data.frame(table(dataViajes$time))
moda3 <- Frecuencia3[which.max(Frecuencia3$Freq),1]
paste("Medidas para distancia de vuelos: MEDIA:",media3,"MEDIANA:",mediana3,"MODA:",moda3)

