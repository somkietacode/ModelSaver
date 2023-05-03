import pickle

class ModelSaver:
    def __init__(self, model):
        self.model = model

    def save_model(self, filename):
        with open(filename + '.model', 'wb') as f:
            pickle.dump(self.model, f)
        print(f"Model saved as {filename}.model")

    @staticmethod
    def load_model(filename):
        with open(filename + '.model', 'rb') as f:
            model = pickle.load(f)
        print(f"Model loaded from {filename}.model")
        return model
