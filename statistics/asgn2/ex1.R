set.seed(27092017)
x=rnorm(10000)
x2=x^2
y=cbind(x, x2)
cov(y)
cor(y)
plot(x, x2)
