from tensorflow.keras.layers import TextVectorization
text_vectorization = TextVectorization()

print("\n-------------------------------------------------")
print("\nDataset 1: A space between every pair of tokens")

dataset_1 = [
    "I am using a seq-2-seq model.",
    "The model is suitable for machine translation.",
    "I enjoy coding.",
]
print(dataset_1)

text_vectorization.adapt(dataset_1)

vocabulary = text_vectorization.get_vocabulary()
print("\nDataset 1 - Vocabulary: \n", vocabulary)

test_sentence = "I am using a seq-2-seq Transformer model." 
print("\nEncode this sentence: ", test_sentence) 

encoded_sentence = text_vectorization(test_sentence)
print("\nEncoded Sentence: \n", encoded_sentence)

inverse_vocab = dict(enumerate(vocabulary))
decoded_sentence = " ".join(inverse_vocab[int(i)] for i in encoded_sentence)
print("\nDecoded Sentence:\n", decoded_sentence)

print("\n-------------------------------------------------")
print("\nDataset 2: No space between every pair of tokens")
dataset_2 = [
    "Iamusingaseq-2-seqmodel.",
    "Themodelissuitableformachinetranslation.",
    "Ienjoycoding.",
]
print(dataset_2)
text_vectorization.adapt(dataset_2)


vocabulary = text_vectorization.get_vocabulary()
print("\nDataset 2 - Vocabulary: \n", vocabulary)

test_sentence = "I am using a seq-2-seq Transformer model." 
print("\nEncode this sentence: ", test_sentence) 

encoded_sentence = text_vectorization(test_sentence)
print("\nEncoded Sentence: \n", encoded_sentence)

inverse_vocab = dict(enumerate(vocabulary))
decoded_sentence = " ".join(inverse_vocab[int(i)] for i in encoded_sentence)
print("\nDecoded Sentence:\n", decoded_sentence)

print("\n-------------------------------------------------")
print("\nDataset 3: A comma between every pair of tokens")
dataset_3 = [
    "I,am,using,a,seq-2-seqmodel.",
    "The,model,is,suitable,for,machine,translation.",
    "I,enjoy,coding.",
]
print(dataset_3)
text_vectorization.adapt(dataset_3)


vocabulary = text_vectorization.get_vocabulary()
print("\nDataset 3 - Vocabulary: \n", vocabulary)

test_sentence = "I am using a seq-2-seq Transformer model."
print("\nEncode this sentence: ", test_sentence) 

encoded_sentence = text_vectorization(test_sentence)
print("\nEncoded Sentence: \n", encoded_sentence)

inverse_vocab = dict(enumerate(vocabulary))
decoded_sentence = " ".join(inverse_vocab[int(i)] for i in encoded_sentence)
print("\nDecoded Sentence:\n", decoded_sentence)


text_vectorization = TextVectorization(standardize=None)
print("\n-------------------------------------------------")
print("\nDataset 4: A comma between every pair of tokens. However, the the comma is not removed during pre-processing.")
dataset_4 = [
    "I,am,using,a,seq-2-seqmodel.",
    "The,model,is,suitable,for,machine,translation.",
    "I,enjoy,coding.",
]
print(dataset_4)
text_vectorization.adapt(dataset_4)

vocabulary = text_vectorization.get_vocabulary()
print("\nDataset 4 - Vocabulary: \n", vocabulary)

test_sentence = "I am using a seq-2-seq Transformer model."
print("\nEncode this sentence: ", test_sentence) 

encoded_sentence = text_vectorization(test_sentence)
print("\nEncoded Sentence: \n", encoded_sentence)

inverse_vocab = dict(enumerate(vocabulary))
decoded_sentence = " ".join(inverse_vocab[int(i)] for i in encoded_sentence)
print("\nDecoded Sentence:\n", decoded_sentence)
