def train_model(ModelClass, X, Y, **kwargs):
  model = ModelClass(**kwargs)
  model.fit(X, Y)
  accuracy_score = round(model.score(X, Y) * 100, 2)
  
  return model, accuracy_score