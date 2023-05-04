import pickle

class ModelSaver:
    def __init__(self):
        

    def save_model(self, model, filename):
        self.model = model
        with open(filename + '.model', 'wb') as f:
            pickle.dump(self.model, f)
        print(f"Model saved as {filename}.model")

    @staticmethod
    def load_model(filename):
        with open(filename + '.model', 'rb') as f:
            model = pickle.load(f)
        print(f"Model loaded from {filename}.model")
        return model
