"""

this is an example
further work is still necessary in order for this code to work!!!

"""

from random import *
from math import *

class Neuron:
    def __init__(self, nI=0):
        self.noInputs=nI
        #MIN_W = -1, MAX_W = 1
        self.weights=[(random()*2-1) for k in range(self.noInputs)]
        self.output=0
        self.err=0
    
    def activate(self, info):
        net = 0.0
        for i in range(self.noInputs):
            net += info[i] * self.weights[i]
        self.output = net		#for linear activation
        #self.output = 1 / (1.0 + exp(-net));	#for sigmoidal activation

    def setErr(val):
        self.err = val				#for linear activation
        #self.err = self.output * (1 – self.output) * val 	
            #for sigmoidal activation

class Layer:
    def __init__(self, noN=0, noIn=0):
        self.noNeurons=noN
        self.neurons=[Neuron(noIn) for k in range(self.noNeurons)]


class Network:
    def __init__(self, m=0, r=0, p=0, h=0):
        self.noInputs=m
        self.noOutputs=r
        self.noHiddenLayers=p
        self.noNeuronsPerHiddenLayer = h
        self.layers=[Layer(self.noInputs,0)]
        self.layers+=[Layer(self.noNeuronsPerHiddenLayer, self.noInputs)]
        self.layers+=[Layer(self.noNeuronsPerHiddenLayer, 
                            self.noNeuronsPerHiddenLayer) for k in 
                            range(self.noHiddenLayers-1)]
        self.layers+=[Layer(self.noOutputs,self.noNeuronsPerHiddenLayer)]

    def activate(self, inputs):
        i = 0
        for n in self.layers[0]:
            n.output=inputs[i]
            i+=1
        for l in range(1, self.noHiddenLayers + 1):
            for n in layers[l]:
                info = []
                for i in range(n.noInputs):
                    info.append(self.layers[l-1].neurons[i].output)
                n.activate(info)
	

    def errorsBackpropagate(self, err):
        for l in range(self.noHiddenLayers+1, 1, -1):
            i=0
            for n1 in self.layers[l]:
                if (l == self.noHiddenLayers + 1):
                    n1.err(err[i])
                else:
                    sumErr = 0.0
                    for n2 in self.layers[l+1]:
                        sumErr += n2.weight[i] * n2.err
                    n1.err=sumErr
                for j in range(n1.noInputs):
                    netWeight = n1.weight[j]+LEAR_RATE*n1.err()*self.layers[l-1].neurons[j].output
                    n1.weight[j]= netWeight
                i+=1

    def errorComputationRegression(self,target, err):
        globalErr = 0.0
        for i in range(self.layers[self.noHiddenLayers + 1].noNeurons):
            err.append(target[i] - self.layers[self.noHiddenLayers + 1].neurons[i].output)
            globalErr += err[i] * err[i]
        return(globalErr)
    
    def errorComputationClassification(self,target, noLabels, err):
        # normalise the output of neurons from the output layer (softmax transformation; 
        # sum of transformed outputs is 1, each transformed output behaves like a probability)
        transfOutputs = []
        maxx = self.layers[self.noHiddenLayers + 1].neurons[0].output
        for i in range(1, noLabes):
            if (self.layers[self.noHiddenLayers + 1].neurons[i].output > maxx):
                maxx = layers[noHiddenLayers + 1].neurons[i].output
        sumExp=0.0
        for i in range(1, noLabes):
            sumExp += exp(self.layers[self.noHiddenLayers + 1].neurons[i].output-maxx)
        for i in range(1, noLabes):
            transfOutputs.append(exp(self.layers[self.noHiddenLayers+1].neurons[i].output-maxx)/sumExp)
        maxx = transfOutputs[0]
        computedlabel = 1
        for i in range(1, noLabes):
            if (transfOutputs[i] > maxx):
                maxx = transfOutputs[i]
                computedlabel = i + 1
        if (target == computedlabel):
            err[0] = 0
        else:
            err[0] = 1
        globalErr = err[0]
        return globalErr
    
    def checkGlobalErr(self,err):
        #regression
        error=sum(err)
        if (abs(error)<1/(10**8)):
            return True
        else:
            return False
        """    
        #clasification
        correct=sum(err)
        error=correct/len(err)
        if error>0.95:
            return True
        else:
            return False
        """
    def learning(self,inData,outData):
        stopCondition = False
        epoch = 0
        globalErr = []
        while (( not stopCondition) and (epoch < EPOCH_LIMIT)):
            globalErr = []
            #for each training example
            for d in range(len(inData)):
                self.activate(inData[d])	 #activate all the neurons; propagate forward the signal
                err = []		            #backpropagate the error of neurons from the output layer
                globalErr[d] = self.errorComputationRegression(outData[d], err)
                #globalErr[d] = self.errorComputationClassification(outData[d][0], 2, err)
                self.errorsBackPropagate(err)
            stopCondition = self.checkGlobalErr(globalErr)
            epoch+=1
    def testing(self, inData, outData):
        globalErr=[]
        for d in range(len(inData)): #for each testing example
            self.activate(inData[d]) #activate all the neurons; propagate forward the signal
            err = []			    #compute the error of neurons from the output layer
            globalErr[d] = self.errorComputationRegression(outData[d], err)
		 #globalErr[d] = self.errorComputationClassification(outData[d][0], 2, err)


def readData(noExamples,noFeatures,noOutputs,inData,outData,fileName):
    pass
        

def normaliseData(noExamples, noFeatures, trainData, noTestExamples, testData):
    #statistical normalisation
    for j in range(noFeatures):
        summ=0.0
        for i in range(noExamples):
            summ+=trainData[i][j]
        mean=summ/noEamples
        squareSum=0.0
        for i in range(noExamples):
            squareSum += (trainData[i][j] - mean)**2;
        deviation=sqrt(squareSum/noExamples)
        for i in range (noExamples):
            trainData[i][j]=(trainData[i][j]-mean)/deviation
        for i in range(noTestExamples):
            testData[i][j]=(testData[i][j]-mean)/deviation
    #min-max normalization
    """
    for j in range(noFeatures):
        minn=min([trainData[i][j] for i in range(noExamples)])
        maxx=max([trainData[i][j] for i in range(noExamples)])
        for i in range(noExamples):
            trainData[i][j]=LIM_MIN+trainData[i][j]*(LIM_MAX-LIM_MIN)/(maxx - minn)
         for i in range(noTestExamples):
            testData[i][j]=LIM_MIN+testData[i][j]*(LIM_MAX-LIM_MIN)/(maxx - minn)
    """

def main_ANN():
    #to do some variables initialisations
    readData(noTrainExamples, noFeatures, noOutputs, inTrainData, outTrainData, "dataRegression.train")
    readData(noTestExamples, noFeatures, noOutputs, inTestData, outTestData, "dataRegression.test")
    
    #readData(noTrainExamples, noFeatures, noOutputs, inTrainData, outTrainData, "dataClassification.train")
    #readData(noTestExamples, noFeatures, noOutputs, inTestData, outTestData, "dataClassification.test")

    net = Network(noFeatures, noOutputs, 1, 2)

    #normaliseData(noTrainExamples, noFeatures, inTrainData, noTestExamples, inTestData)
    #net = Network(noFeatures, noOutputs, 1, 2)

    net.learning(inTrainData, outTrainData)
    net.testing(inTestData, outTestData)
