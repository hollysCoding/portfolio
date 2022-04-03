import nltk
#porter 2 stemmer is better than original porter stemmer
from porter2stemmer import Porter2Stemmer

stemmer = Porter2Stemmer()

import numpy
import tflearn
import tensorflow
import random
import json
import pickle

with open("intents.json") as file:
    data = json.load(file)

try:
    with open("data.pickle", "rb") as f:
        words, labels, training, output = pickle.load(f)
except:
    words = []  #words in patterns in one list
    labels = [] #labels in list
    docs_x = [] #lists of all the diff patterns
    docs_y = [] #tags of words which is the pattern

    '''
    For every intent in the dictionaries we loop through the different patterns and perform tokenization and add the tokenized words to an empty list 
    We put th patterns in one list, and the corresponding tags to another list. 
    Added labels to the labels list
    '''
    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            wrds = nltk.word_tokenize(pattern)
            words.extend(wrds)
            docs_x.append(wrds)
            docs_y.append(intent["tag"])

            if intent["tag"] not in labels:
                labels.append(intent["tag"])

    #stemmed all the tokenized words in the patterns from the words list using a porter2stemmer. Removed punctiation
    words = [stemmer.stem(w.lower()) for w in words if w not in "?"]
    words = sorted(list(set(words)))
    labels = sorted(labels)

    #right now we have strings and neural networks only understand numbers.
    #we use bag of words for one hot encoding
    #we use the bag of words as our training data

    training = []
    output = []

    out_empty = [0 for _ in range(len(labels))]
    for x, doc in enumerate(docs_x):
        bag = []

        wrds = [stemmer. stem(w) for w in doc]

        for w in words:
            if w in wrds:
                bag.append(1)
            else:
                bag.append(0)

        output_row = out_empty[:]
        output_row[labels.index(docs_y[x])] = 1

        training.append(bag)
        output.append(output_row)

    #changing training and output into numpy arrays
    training = numpy.array(training)
    output = numpy.array(output)

    with open("data.pickle", "wb") as f:
        pickle.dump((words, labels, training, output), f)

#lets use tensorflow
'''
We have an input data which is the length of our training data. We have two hidden layers with 8 neurons fully connected,
Also connected to an output layer which has neurons representing each of our classes. 
Our model is predicting which tag we should take from to give a response to the user 
As input we get the bag of words, and as output we get the label of what we should respond with and what tag it comes from
As we add more intents and tags we would probably want to add more neurons to our hidden layers 
Each neuron represents a specific class
'''





#resetting all the underlying data graph
#tensorflow.reset_default_graph()
#define input shape we are expecting for our model
net = tflearn.input_data(shape = [None, len(training[0])])
#add fully connected layer to our neural network. 8 neurons for hidden layer
net = tflearn.fully_connected(net, 8) #hidden layer
net = tflearn.fully_connected(net, 8)#2nd hidden layer
net = tflearn.fully_connected(net, len(output[0]), activation = "softmax") #output layer. sfotmax will go through and give us a probability about each neuron in that layer and that will be our output for the network
net = tflearn.regression(net)

#deep neural network
model = tflearn.DNN(net)

#passing in our training data
#epoch is the number of times its going to see the same data
#hopefully the more it sees the data the more itll be better at classifying it
#I want to write something to try it different times and find thhe accuracy

try:
    model.load("model.tflearn")
except:
    model.fit(training, output, n_epoch=1000, batch_size=8, show_metric=True)
    model.save("model.tflearn") #saving the model as tflearn



#then we stem the user input and convert to lower
#we turn the user input into bag of words
def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1

    return numpy.array(bag)

def chat():
    print("This is your bot, Jasper. You can start talking. Type quit to stop.")
    while True:
        inp = input("You: ")
        if inp.lower() == "quit":
            break

        #passing in bag of words to the prediction
        results = model.predict([bag_of_words(inp, words)])[0]
        #the neural network returns the probablility that the user is talking about each label, so this will let us pick the top prediction
        results_index = numpy.argmax(results)
        #figuring out which response to display
        tag = labels[results_index]


        #if its not atleast 75% sure of the label then it prints idk
        if results[results_index] > 0.75:
            for tg in data["intents"]:
                 if tg['tag'] == tag:
                     responses = tg['responses']

            print(random.choice(responses))
        else:
            print("I dont know what you're saying, human.")


chat()