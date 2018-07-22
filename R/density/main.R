#!/usr/bin/R --vanilla -q -f 
#
#The data is in the following format Value \t Quantity
#

tbl <- read.csv("data.csv",header=FALSE, sep="\t")
dsty <- tbl$V1/tbl$V2

dk <- density(dsty)
dn <- dnorm(dk$x,mean=mean(dsty),sd=sd(dsty))

pdf("out.pdf")
plot(dk,
    col="red",
    main=c("Kernel method vs Gaussian distribution",paste("data sz=", length(dsty),"mean=",as.integer(mean(dsty)),"variance=",as.integer(sd(dsty)))), 
    xlab="density", 
    ylab="probability")
lines(dk$x,dn,col="blue")
legend("topright",
        c("Gaussian","Observed"),text.col=c("blue","red"))
dev.off()