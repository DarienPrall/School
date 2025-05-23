#---------------------------------------------------------
# Instructions
# 1. Install TensorFlow
# 2. Import the necessary libraries
# 3. Load the Fashion MNIST dataset
# 4. Preprocess the data
# 5. Build 3 different CNN models
# 6. Compile the models
# 7. Train the models
# 8. Evaluate the models
# 9. Compare and Conclude
#---------------------------------------------------------

# 1. Install TensorFlow
# import tensorflow as tf
# print("TensorFlow version:", tf.__version__)


# 2. Import the necessary libraries
# - I need to use TensorFlow for bulding and training the CNN models.
# - I will use Keras for building and training deep learning models.
import tensorflow as tf

from tensorflow.keras import layers, models
from tensorflow.keras.datasets import fashion_mnist


# 3. Load the Fashion MNIST dataset
# - I will pre-slit into traning and testing datasets.

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

# 4. Preprocess the data
# - I need to reshape the images
# - I also need to add a channel dimension to the images
# - Then I will need to normalize the pixel values to be between 0 and 1 to improve the model performance
train_images = train_images.reshape((60000, 28, 28, 1)) / 255.0
test_images = test_images.reshape((10000, 28, 28, 1)) / 255.0
print(f"Train images shape: {train_images.shape}")
print(f"Test images shape: {test_images.shape}")

# 5. Build 3 different CNN models
# - Each of the models will explore different design choices
# Model 1 will be a basic CNN structure
# Model 2 will have increased number of filters
# Model 3 will have a different activation function

# Model 1: Basic CNN
model1 = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(10, activation='softmax')
])
print(f"Model 1 summary:\n{model1.summary()}")

# Model 2: Increased number of filters
model2 = models.Sequential([
    layers.Conv2D(64, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(10, activation='softmax')
])
print(f"Model 2 summary:\n{model2.summary()}")

# Model 3: Different activation function
model3 = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='sigmoid', input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='sigmoid'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(128, activation='sigmoid'),
    layers.Dense(10, activation='softmax')
])
print(f"Model 3 summary:\n{model3.summary()}")


# Step 6: Compile the models
# - I will use the Adam optimizer and sparse categorical crossentropy loss function
# - Loss function is used to measure how well the model is performing
# - I will also use accuracy as a metric to evaluate the model performance

for model in [model1, model2, model3]:
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    
# Step 7: Train the models
# - I will fit each model separately
# - I will use validation_split=0.2 to monitor overfitting
# - I will also train for 10 epochs as specified in the instructions
history1 = model1.fit(train_images, train_labels, epochs=10, validation_split=0.2)
history2 = model2.fit(train_images, train_labels, epochs=10, validation_split=0.2)
history3 = model3.fit(train_images, train_labels, epochs=10, validation_split=0.2)

# Step 8: Evaluate the models
test_loss1, test_acc1 = model1.evaluate(test_images, test_labels)
test_loss2, test_acc2 = model2.evaluate(test_images, test_labels)
test_loss3, test_acc3 = model3.evaluate(test_images, test_labels)

print(f" Model 1 Accuracy (Basic CNN): {test_acc1:.4f}")
print(f" Model 2 Accuracy (Increased Filters): {test_acc2:.4f}")
print(f" Model 3 Accuracy (Different Activation): {test_acc3:.4f}")

