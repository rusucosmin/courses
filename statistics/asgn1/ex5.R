set.seed(20092017)
n <- 1000
X <- runif(n, 0, 1)

quant <- function(X, lambda) {
  -log(1 - X) / lambda
}

Y <- function(lambda) {
  return(function(X) {
    return(quant(X, lambda))
  })
}

E <- function(Y) {
  return(ecdf(Y))
}

Y(1)(X)
Y(2)(X)
Y(4)(X)

E(Y(1)(X))
E(Y(2)(X))
E(Y(4)(X))

par(mfrow=c(1, 3))
plot(E(Y(1)(X)))
plot(E(Y(2)(X)))
plot(E(Y(4)(X)))

