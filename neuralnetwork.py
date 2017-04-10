from keras.models import Sequential
from keras.layers import Dense
import numpy


def get_next_move(tile_grid, army_grid):
    """

    Inputs:
    ---
    tile_grid
    A 2D array with values -4 to 2 in each cell
    -4=Fog Obstacle; -3=Fog; -2=Mountain; -1=Empty Land; 0=Enemy; 1=EnemyGeneral; 2=Town; 3=Own; 4=OwnTown/OwnGeneral;
    ---
    army_grid
    A 2D array with army values of each square (0+)
    
    Returns:
    A tuple ((x, y), (x2, y2))
    (moving army from one coord to another)

    """
    return ((0, 0), (0,0))

def train(game):
    for turn in game:
        # fix random seed for reproducibility
        seed = 7
        numpy.random.seed(seed)



        # load pima indians dataset
        dataset = numpy.loadtxt("pima-indians-diabetes.csv", delimiter=",")
        # split into input (X) and output (Y) variables
        X = dataset[:,0:8]
        Y = dataset[:,8]
        1
        2
        3
        4
        5
        # load pima indians dataset
        dataset = numpy.loadtxt("pima-indians-diabetes.csv", delimiter=",")
        # split into input (X) and output (Y) variables
        X = dataset[:,0:8]
        Y = dataset[:,8]

        # create model
        model = Sequential()
        model.add(Dense(12, input_dim=8, init='uniform', activation='relu'))
        model.add(Dense(8, init='uniform', activation='relu'))
        model.add(Dense(1, init='uniform', activation='sigmoid'))

        model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

        model.fit(X, Y, nb_epoch=150, batch_size=10)


        # evaluate the model
        scores = model.evaluate(X, Y)
        print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
        1
        2
        3
        # evaluate the model
        scores = model.evaluate(X, Y)
        print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
        pass

if __name__ == '__main__':
    train('game_data.csv')
