import unittest
from sklearn.tree import DecisionTreeClassifier
from src.demo import train_model

class TestDemo(unittest.TestCase):
  def test_train_model_should_return_instance_of_model_and_accuracy_score(self):
    model, accuracy = train_model(DecisionTreeClassifier, [[1, 1, 1], [1, 1, 1]], [0, 1])

    self.assertIsInstance(model, DecisionTreeClassifier)
    self.assertIsInstance(accuracy, float)