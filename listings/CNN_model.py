model = Sequential()
model.add(Conv1D(filters=64, kernel_size=6, activation='relu', padding='same', input_shape=(72, 1)))
model.add(BatchNormalization())

model.add(MaxPooling1D(pool_size=(3), strides=2, padding='same'))

model.add(Conv1D(filters=64, kernel_size=6, activation='relu', padding='same', input_shape=(72, 1)))
model.add(BatchNormalization())
model.add(MaxPooling1D(pool_size=(3), strides=2, padding='same'))

model.add(Conv1D(filters=64, kernel_size=6, activation='relu', padding='same', input_shape=(72, 1)))
model.add(BatchNormalization())
model.add(MaxPooling1D(pool_size=(3), strides=2, padding='same'))

model.add(Flatten())
model.add(Dense(64, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(8, activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])