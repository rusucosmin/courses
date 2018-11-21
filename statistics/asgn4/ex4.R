p <- 0.49
n <- 1000
mu <- 2*p
s2 <- 4*p*(1-p)
t <- 1000
f1 <- function(x) pbinom((x*sqrt(s2/n) + mu)*n/2 , size = n, prob = p)

curve(f1, from=-3, to=3)
curve(pnorm, add=TRUE, col='blue')
