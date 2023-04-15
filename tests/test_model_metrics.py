from sklearn.metrics import accuracy_score

from src.train import prepare_data_and_train_model


class TestModelMetrics:
    def test_model_accuracy_score_should_be_above_threshold(self):
        model, X_test, Y_test = prepare_data_and_train_model()
        Y_pred = model.predict(X_test)

        accuracy = accuracy_score(Y_test, Y_pred)

        assert accuracy > 0.869
