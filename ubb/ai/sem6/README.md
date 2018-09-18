Neural Networks

Normalize data
1. Statistical
  - Sample - mean and stddev
  - V' = (V - mean) / stddev

2. Min - Max
  - V' = VMIN + (V - MIN) / (MAX - MIN) * (VMAX - VMIN)
  VMIN = -1
  VMAX = 1

Network:
   - input layer
   - hidden layer
   - output layer
   - activation function:
      - liniar: f(x) = x
      - sigmoind: f(x) = 1 / 1 + exp(-x)

Source code:
  class Neuron:
    def __init__(self, noI):
      self.noInput = noI
      self.weights = [random() * 2 - 1  for k in range(self.noInputs)]
      self.err = 0
      self.output = 0

    def activate(self, info):
      net = sum([self.weights[i] * info[i] for i in range(self.noInputs)])
      self.output = net #liniar
      #self.output = 1 / (1 + exp(-net))

    def setErr(self, value):
      self.err = value    #liniar
      #for sigmoid:
      #self.w = self.outout * (1 - self.output) * value

  class Layer:
    def __init__(self, noN, noI):
      self.noN = noN
      self.neurons = [Neuron(noI) for i in range(self.noNn)]

  class Network:
    def __init__(self, m, r, p, h):
      self.noI = m
      self.noO = r
      self.noH = p
      self.noNPHL = h #neurons per hidden layer
      self.layers = [Layer(noInputs, 0)]
      self.layers += [Layer(self.noNPHL, self.noInputs)]
      self.layers += [Layer(self.noNPHL, self.self.noNPHL) \
                          for i in range (self.noH - 1)]

      self.layers += [Layer(self.noO, self.noNPHL
    def active(self, inputs):
      i = 0
      for n in self.layers:
        n.output = inputs[i]
        i += 1
      for l in range(1, self.noHL + 2):
        info = [self.layers[l-1].neurons[i].output \
                for i range(self.layers[l - 1].noN)]
        for n in self.layer[l].neurons:
          n.activate(info)

    def errorBackPropagate(self, err):
      for i in range(self.noHL + 1, 0, -1):
        i = 0
        for n in self.layers[l].neurons:
          if l == self.noHL + 1:
            n1.setErr(err[i])
          else:
            sumErr sum([n2.wight[i] * nr.err \
                    for n2 in self.layers[l + 1].neurons])
            n1.setErr(sumEr)
          for j in range(n1.noI):
            n1.weight[j] = n1.weight[j] * learn_rate * 
              n1.err * self.layers[l - 1].neurons[i].output
        i += 1
