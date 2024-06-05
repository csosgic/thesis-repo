# saving the model to CNN_model.keras file
model.save('CNN_model.keras')

# loading the model from CNN_model.keras file
from keras.models import load_model 
model = keras.saving.load_model('CNN_model.keras')