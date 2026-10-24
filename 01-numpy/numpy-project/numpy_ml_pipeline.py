import numpy as np 

## TASK 1: Token Processing:

int_token = np.arange(100,160).reshape(10,6)

train_tokens, test_tokens = np.vsplit(int_token, [8])

print("testing sentences")

for sentence in test_tokens:
    print(sentence)

# Validation
print("Training shape:", train_tokens.shape)
print("Testing shape:", test_tokens.shape)
print("Total tokens:", int_token.size)

#.......................................................................................................................


## TASK 2: Data Cleaning:

weights = np.array([1,2,0,-999.0,9,7,-999.0,50])
anomaly_indices = np.where(weights == -999.0)
valid_mask = weights > 0

clean_weight = weights[valid_mask]
sorted_weight = np.sort(clean_weight)
print(sorted_weight)
print(anomaly_indices)

#........................................................................................................................

## TASK 3: Feature Scaling:

raw_features = np.arange(10.0,51.0,8).reshape(2,3)
features_copy = np.copy(raw_features)
log_features = np.log(features_copy)
scaled_feature = log_features * 0.5
print(raw_features, log_features , scaled_feature )

#..................................................................................................................................

# TASK 4: Embedding Analysis:

embeddings = np.array([[0.2, 0.5, 0.8, 0.1],
                       [0.6, 0.3, 0.4, 0.9],
                       [0.1, 0.7, 0.5, 0.4]])

embeddings_mean = np.mean(embeddings, axis=1)

embeddings_transpose = np.transpose(embeddings)

similarity_scores = np.dot(embeddings, embeddings_transpose)

print(similarity_scores)
print(embeddings_mean)
print(embeddings)