"""#Importing Libraries """

import ipynb

# Save the file as an ipynb file.

import numpy as np
import typing
from typing import Any, Tuple
from sklearn.model_selection import train_test_split

import pathlib

import einops
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

import tensorflow as tf
import tensorflow_text as tf_text

"""#Defining the Shapechecker"""

#@title
class ShapeChecker():
  def __init__(self):
    # Keep a cache of every axis-name seen
    self.shapes = {}

  def __call__(self, tensor, names, broadcast=False):
    if not tf.executing_eagerly():
      return

    parsed = einops.parse_shape(tensor, names)

    for name, new_dim in parsed.items():
      old_dim = self.shapes.get(name, None)

      if (broadcast and new_dim == 1):
        continue

      if old_dim is None:
        # If the axis name is new, add its length to the cache.
        self.shapes[name] = new_dim
        continue

      if new_dim != old_dim:
        raise ValueError(f"Shape mismatch for dimension: '{name}'\n"
                         f"    found: {new_dim}\n"
                         f"    expected: {old_dim}\n")

"""# Loading the Dataset"""

import pandas as pd
ORM_data = pd.read_excel('13_OM_70.xlsx')

"""#Reading Data from Dataset"""

ORM_data.head()

OM_Regular = ORM_data['OM_Regular'].values
OM_Prediction = ORM_data['OM_Prediction'].values

X = OM_Regular
Y = OM_Prediction

"""#### Dividing data as Target and Context"""

# target_raw =  Y
# context_raw = X
# print(context_raw[-1])

# print(target_raw[-1])

"""### Create a tf.data dataset

From these arrays of strings you can create a `tf.data.Dataset` of strings that shuffles and batches them efficiently:
"""

BUFFER_SIZE = len(context_raw)
BATCH_SIZE = 1

is_train = np.random.uniform(size=(len(target_raw),)) < 0.8

train_raw = (
    tf.data.Dataset
    .from_tensor_slices((context_raw[is_train], target_raw[is_train]))
    .shuffle(BUFFER_SIZE)
    .batch(BATCH_SIZE))
val_raw = (
    tf.data.Dataset
    .from_tensor_slices((context_raw[~is_train], target_raw[~is_train]))
    .shuffle(BUFFER_SIZE)
    .batch(BATCH_SIZE))

# for example_context_strings, example_target_strings in train_raw.take(1):
#   print(example_context_strings[:5])
#   print()
#   print(example_target_strings[:5])
#   break

"""### Text preprocessing

One of the goals of this tutorial is to build a model that can be exported as a `tf.saved_model`. To make that exported model useful it should take `tf.string` inputs, and return `tf.string` outputs: All the text processing happens inside the model. Mainly using a `layers.TextVectorization` layer.

#### Standardization

The model is dealing with multilingual text with a limited vocabulary. So it will be important to standardize the input text.

The first step is Unicode normalization to split accented characters and replace compatibility characters with their ASCII equivalents.

The `tensorflow_text` package contains a unicode normalize operation, We may or may not decide to Use this for ORM data. I kept it in the experiment
"""

# example_text = ‘’)

# #example_text = tf.constant('class1,table2,obj1,atr1')
# print(example_text.numpy())
# print(tf_text.normalize_utf8(example_text, 'NFKD').numpy())

#import re

#def tf_lower_and_split_punct(text):

def tf_lower_and_split_punct(text):
  # Split accented characters.
  text = tf_text.normalize_utf8(text, 'NFKD')
  text = tf.strings.lower(text)
  # Keep space, a to z, and select punctuation.
  text = tf.strings.regex_replace(text, '', '')
  # Add spaces around punctuation.
  text = tf.strings.regex_replace(text, '', r'')
  # Strip whitespace.
  text = tf.strings.strip(text)

  text = tf.strings.join(['[START]', text, '[END]'])

  return text


def decoder(outputs):
  # Convert the outputs to a list of strings.
  outputs_list = [tf.strings.join([tf.strings.as_text(output), ' ']) for output in outputs]

  # Remove all the spaces from the outputs.
  outputs_list = [output.replace(' ', '') for output in outputs_list]

  # Return the outputs as a single string.
  return ''.join(outputs_list)


# Create a model.
model = tf.keras.models.Sequential([
  tf.keras.layers.TextVectorization(
      standardize=tf_lower_and_split_punct,
      max_tokens=10000),
  tf.keras.layers.LSTM(128),
  tf.keras.layers.Dense(10000, activation='softmax')
])

# Train the model.
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(train_raw, epochs=10)

# Evaluate the model.
model.evaluate(val_raw)

# Translate a sentence.
t = tf.constant('This is a test.')

# Translate the input text.
outputs = model.predict([t])

# Decode the outputs.
output = decoder(outputs)

# Print the output.
print(output)
