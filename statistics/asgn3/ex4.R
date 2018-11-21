vals <- matrix(0, nrow=1000,ncol=2)
n <- 100
for(i in 1:1000) {
  set.seed(i + 04102017)
  X <- rnorm(n)
  vals[i,1] <- mean(X)
  vals[i,2] <- var(X)
}

plot(vals[,1], vals[,2], xlab=expression(bar(X)), ylab=expression(S^2))
abline(v=0, col='red')
abline(h=1, col='red')
