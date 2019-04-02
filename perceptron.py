import random
import pprint
class Perceptron(object):
    def __init__(self, input_size, lr=1, epochs=100):
        self.weights = [0] * (input_size + 1)
        # add one for bias
        self.epochs = epochs
        self.lr = lr

    def activation_fn(self, x):
        #print( " x=", x)
        #funcao binaria
        return 1 if x >= 0 else 0

        #funcao bipolar
        # return 1 if x >= 0 else -1



    def weighted_sum(self, x, w):
        if(len(x) != len(w)):
            raise Exception("List with differents sizes")
        r = 0
        for i in range(len(w)):
            r += x[i] * w[i]
        return r

    def predict(self, x):
        z = self.weighted_sum(self.weights, x)
        a = self.activation_fn(z)
        return a

    def fit(self, X, d):
        for _ in range(self.epochs):
            for i in range(len(d)):
                x = [1] + X[i]
                y = self.predict(x)
                e = d[i] - y
                for j  in range(len(self.weights)):
                    self.weights[j] = self.weights[j] + self.lr * e * x[j]


if __name__ == "__main__":
    first_class = "Iris-setosa"
    second_class = "Iris-versicolor"
    excluded_class = "Iris-virginica"
    number_of_class_values = 4

    data_set = []
    with open("iris.txt", "r") as data_set_file:
        lines = data_set_file.read().split()
        for i in range(len(lines)):
            lines[i] = lines[i].split(",")
        for line in lines:
            if(line[-1] != excluded_class):
                for j in range(len(line) - 1):
                    line[j] = float(line[j])
                data_set.append(line)
    
    if(data_set == []):
        print("Erro na leitura de arquivo ou arquivo vazio")

    data_set_size = len(data_set)
    training_set_size = int(data_set_size / 2)
    testing_set_size = data_set_size - training_set_size

    data_set_index_to_train = random.sample(range(0, data_set_size), training_set_size)
    data_set_index_to_test = list(set(range(0, data_set_size)) - set(data_set_index_to_train))


    training_set = []
    training_set_answer = []
    for index in data_set_index_to_test:
        training_set.append(data_set[index][:-1])

        if(data_set[index][-1] == first_class):
            training_set_answer.append(1)
        elif(data_set[index][-1] == second_class):
            training_set_answer.append(0)

    testing_set = []
    testing_set_answer = []
    mapping_test_index_to_data_index = []
    for index in data_set_index_to_test:
        testing_set.append(data_set[index][:-1])

        if(data_set[index][-1] == first_class):
            testing_set_answer.append(1)
        elif(data_set[index][-1] == second_class):
            testing_set_answer.append(0)
    
    perceptron = Perceptron(number_of_class_values, 0.1, 100)
    
    perceptron.fit(training_set, training_set_answer)
    
    for index, value in enumerate(perceptron.weights):
        print("W_" + str(index) + ": " + str(value))

    number_of_right_answers = 0
    number_of_wrong_answers = 0

    list_prediction_answer = []

    for index, test in enumerate(testing_set):
        test = [0] + test
        prediction = perceptron.predict(test)

        if(prediction == testing_set_answer[index]):
            number_of_right_answers += 1
        else:
            number_of_wrong_answers += 1

        prediction_answer = [index]
        if(prediction == 1):
            prediction_answer.append(first_class)
        else:
            prediction_answer.append(second_class)

        if(testing_set_answer[index] == 1):
            prediction_answer.append(first_class)
        else:
            prediction_answer.append(second_class)
        
        list_prediction_answer.append(prediction_answer)

    pprint.pprint(list_prediction_answer)

    print("Total de acertos: " + str(number_of_right_answers))
    print("Total de erros: " + str(number_of_wrong_answers))
