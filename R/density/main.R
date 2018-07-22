#The data is in the following format Value \t Quantity
values <- read.csv("data.csv",header=FALSE, sep="\t")
pm2 <- values$V1/values$V2
dk <- density(pm2)
dn <- dnorm(dk$x,mean=mean(pm2),sd=sd(pm2))
pdf("out.pdf")
plot(dk,col="red", main=c("Kernel method vs Gaussian distribution",paste("data sz=", length(pm2),"mean=",as.integer(mean(pm2)),"variance=",as.integer(sd(pm2)))), xlab="density", ylab="probability")
lines(dk$x,dn,col="blue")
legend("topright",c("Gaussian","Observed"),text.col=c("blue","red"))
dev.off()