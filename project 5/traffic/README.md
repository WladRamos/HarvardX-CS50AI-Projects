My first attempt was to adapt the model used in lecture 5 in handwriting.py, so I changed the input shape to input_shape=(IMG_WIDTH, IMG_HEIGHT, 3) and the output layer to tf.keras.layers.Dense(NUM_CATEGORIES, activation="softmax"). Then I ran it with the larger dataset and noticed that the accuracy was very low, not exceeding 34%. So, I decided to continue making changes to the layers to achieve more satisfactory results.

The first change I decided to make was to add one more convolutional layer and one more pooling layer. This time the results for the gtsrb dataset were much more satisfactory, reaching 90% accuracy in the tenth epoch, and on the testing set, it reached 96% accuracy. I would like to get closer to 98 or 99%, so I decided to test different numbers and sizes for the convolutional layers and different pool sizes for the pooling layers.

I then changed the pooling size to (3, 3) and also altered the numbers of filters and filter sizes of the convolutional layers, setting them to 64, (5, 5) in the first convolutional layer and 128, (5, 5) in the second one. When running the training, the result seemed more satisfactory, increasing from 90% to 92%, but on the testing set, the accuracy dropped from 96 to 95%. So, I tried more tests to reach a satisfactory result.

After several attempts to change values, I decided to add a third convolutional layer followed by another pooling layer, with the layers configured as follows: first convolutional -> 64, (5, 5), first pooling -> (2,2), second convolutional ->128, (3, 3), second pooling -> (2, 2), third convolutional ->256, (3, 3), third pooling -> (3, 3). Additionally, I added another hidden layer, now having two, the first one with 256 units and the second one with 128 units, each of them with a dropout of 0.4. This configuration gave me the best result, reaching almost 97% accuracy in the tenth epoch.

After all these tests, I concluded that to surpass the 96% barrier, a significant increase in the complexity of the model is required for a very small improvement. As can be seen from this report, many layers were added and various parameters were changed just to raise the accuracy percentage by approximately 1%.






