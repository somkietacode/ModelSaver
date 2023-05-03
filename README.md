# Model Saver

Model Saver is a Python package that provides a simple and convenient way to save and load machine learning models using `pickle`. It is designed specifically for models trained using the Scikit-learn library (`sklearn`) but can be used with other models as well.

## Installation

You can install Model Saver using pip:

```
pip install model_saver
```

## Usage

To use Model Saver, first import the `ModelSaver` class:

```python
from model_saver import ModelSaver
```

## Saving a Model
To save a trained machine learning model, create an instance of the ModelSaver class and call the save_model method:

```python
from sklearn.linear_model import LinearRegression

# Train a linear regression model
X_train = ...
y_train = ...
model = LinearRegression()
model.fit(X_train, y_train)

# Save the trained model
saver = ModelSaver()
saver.save_model(model, "linear_regression")
```

This will save the trained LinearRegression model as a binary file with the name "linear_regression.model" in the current working directory.

## Loading a Model

To load a saved machine learning model, create an instance of the ModelSaver class and call the load_model method:

```python
# Load the saved model
loaded_model = saver.load_model("linear_regression")

# Use the loaded model to make predictions
X_test = ...
y_pred = loaded_model.predict(X_test)
```

This will load the saved LinearRegression model from the binary file named "linear_regression.model" in the current working directory using the ModelSaver class, and use the loaded model to make predictions.

## Contributing
Contributions to Model Saver are welcome! To contribute, please fork the repository, make your changes, and submit a pull request.

## License
Model Saver is licensed under the MIT License. See the LICENSE file for more information.
