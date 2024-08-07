import pickle

# Create a dummy model object
class DummyModel:
    def predict(self, filepath):
        return "Healthy"

# Save the dummy model to a file
model = DummyModel()
with open('app/model/disease_model.pkl', 'wb') as f:
    pickle.dump(model, f, protocol=pickle.HIGHEST_PROTOCOL)
