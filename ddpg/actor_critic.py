from keras.layers.core import Dense
from keras.models import Sequential
from keras.optimizers import Adam
from keras.regularizers import l2

DIR = 'weights'


class AbstractBase:
    def __init__(self, *args):
        raise NotImplementedError('Abstract class')

    def summary(self):
        return self.model.summary()

    def train(self, X, y, batch_size):
        return self.model.fit(
            X, y,
            batch_size=batch_size,
            epochs=1,
            verbose=0
        )

    def predict(self, inputs):
        return self.model.predict(inputs)

    def set(self, weights):
        self.model.set_weights(weights)

    def get(self):
        return self.model.get_weights()

    def dump(self, name=None):
        self.model.save_weights('{}/{}.h5'.format(DIR, name or self.name), overwrite=True)

    def load(self, name=None):
        self.model.load_weights('{}/{}.h5'.format(DIR, name or self.name))


class Actor(AbstractBase):
    def __init__(
        self, name, input_shape, output_shape, hidden_layers,

        alpha=10**-4,

        hidden_activation='relu',
        output_activation='tanh',

        loss='mean_squared_error'
    ):
        model = Sequential()
        model.add(Dense(hidden_layers[0], input_shape=input_shape))
        for num_nodes in hidden_layers[1:]:
            model.add(Dense(num_nodes, activation=hidden_activation))
        model.add(Dense(output_shape[0], activation=output_activation))
        model.compile(optimizer=Adam(lr=alpha), loss=loss)

        self.model = model
        self.name  = name


class Critic(AbstractBase):
    def __init__(
        self, name, input_shape, output_shape, hidden_layers,

        alpha=10**-3,

        hidden_activation='relu',
        output_activation='linear',
        weight_decay=10**-2,

        loss='mean_squared_error'
    ):
        model = Sequential()
        model.add(Dense(hidden_layers[0], input_shape=input_shape, kernel_regularizer=l2(weight_decay)))
        for num_nodes in hidden_layers[1:]:
            model.add(Dense(num_nodes, activation=hidden_activation, kernel_regularizer=l2(weight_decay)))
        model.add(Dense(output_shape[0], activation=output_activation, kernel_regularizer=l2(weight_decay)))
        model.compile(optimizer=Adam(lr=alpha), loss=loss)

        self.model = model
        self.name  = name
