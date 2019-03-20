data <- read.table("apple.txt",
                   sep="",
                   col.names=c("Variety", "FusariumStrain", "Days", "AppleWeight",
                               "Radius", "FungalRadialAdvance", "RateOfAdvance"))

data.fit <- lm(FungalRadialAdvance ~ Variety, data)
FRA_V = summary(data.fit)

data.fit <- lm(FungalRadialAdvance ~ FusariumStrain, data)
FRA_FS = summary(data.fit)

data.fit <- lm(FungalRadialAdvance ~ Days, data)
FRA_D = summary(data.fit)

data.fit <- lm(FungalRadialAdvance ~ AppleWeight, data)
FRA_AW = summary(data.fit)

data.fit <- lm(FungalRadialAdvance ~ Radius, data)
FRA_R = summary(data.fit)

data.fit <- lm(FungalRadialAdvance ~ RateOfAdvance, data)
FRA_ROA = summary(data.fit)

i = 9 #adjusted R sq

FRA_adj_R = c(FRA_V[i],FRA_FS[i],FRA_D[i],FRA_AW[i],FRA_R[i],FRA_ROA[i])

'''
for (i in x) {
if(val %% 2 == 0)  count = count+1
}
'''



data.fit <- lm(RateOfAdvance ~ Variety, data)
ROA_V = summary(data.fit)

data.fit <- lm(RateOfAdvance ~ FusariumStrain, data)
ROA_FS =summary(data.fit)

data.fit <- lm(RateOfAdvance ~ Days, data)
ROA_D = summary(data.fit)

data.fit <- lm(RateOfAdvance ~ AppleWeight, data)
ROA_AW = summary(data.fit)

data.fit <- lm(RateOfAdvance ~ Radius, data)
ROA_R = summary(data.fit)

ROA_adj_R = c(ROA_V[i],ROA_FS[i],ROA_D[i],ROA_AW[i],ROA_R[i],FRA_ROA[i])

name = c('Variety', 'FusariumStrain', 'Days', 'AppleWeight','Radius', 'FungalRadialAdvance/RateOfAdvance')



plot(factor(name), FRA_adj_R, col = "red")
par(new=TRUE)
plot(factor(name), ROA_adj_R, col = "green")