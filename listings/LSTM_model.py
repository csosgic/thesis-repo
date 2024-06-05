model = Sequential()
model.add(LSTM(units=64, return_sequences=True, input_shape=(72, 1)))
model.add(BatchNormalization())

model.add(LSTM(units=64, return_sequences=True))
model.add(BatchNormalization())

model.add(LSTM(units=64))
model.add(BatchNormalization())

model.add(Dense(64, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(8, activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])