from keras.models import Sequential
from keras.layers import Dense
import numpy, os


def get_next_move(tile_grid, army_grid):

    model = Sequential()
    model.load_weights('training/save.model')

    next_move = model.predict(tile_grid, army_grid)

    return next_move

def train():
    for filename in os.listdir('training/replays_final'):
        seed = 7
        numpy.random.seed(seed)

        dataset = numpy.loadtxt('training/replays_final/' + filename, delimiter=" ")
        X = dataset[:,len(dataset)/2]
        Y = dataset[:,len(dataset)/2]

        model = Sequential()
        model.add(Dense(12, input_dim=8, init='uniform', activation='relu'))
        model.add(Dense(8, init='uniform', activation='relu'))
        model.add(Dense(1, init='uniform', activation='sigmoid'))

        model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

        model.fit(X, Y, nb_epoch=150, batch_size=10)

        model.save('training/save.model')

        pass

if __name__ == '__main__':
    train()
