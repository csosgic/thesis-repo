# saving the model to LSTM_model.keras file
model.save('LSTM_model.keras')

# loading the model from LSTM_model.keras file
from keras.models import load_model 
model = keras.saving.load_model('LSTM_model.keras')