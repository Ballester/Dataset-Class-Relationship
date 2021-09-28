# Dataset Class Relationship
### Finds the relationship between the classes of two datasets based on synsets and names

In this example ImageNet and TU-Berlin Sketch dataset classes are being matched by their class names.
The results can be used for reusing the embeddings of a pre-trained model during the fine-tuning of a target dataset in domain adaptation scenarios. Further explanation is given on https://github.com/ballester/lateral-representation-learning

Requirements:
  * NLTK with wordnet
