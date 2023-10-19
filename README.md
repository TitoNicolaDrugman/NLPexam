# NLPexam

# ADSM - (Almost) Detecting Spam Messages
**Exam Date: July 2023**

📚 "Text Classification: Spam vs. Ham" - A Natural Language Processing (NLP) Project 📩

In our NLPexam project, we tackle the challenge of creating a machine learning classifier model that can binary predict whether a given SMS message is spam or ham (non-spam). We approach this text classification task with a focus on preprocessing, data analysis, and model selection.

## Table of Contents

- [Introduction](#introduction)
- [Data](#data)
- [Methodology](#methodology)
- [Models](#models)
- [Results](#results)
- [Issues Encountered](#issues-encountered)
- [Project Recap](#project-recap)
- [Final Conclusion](#final-conclusion)
- [Contributing](#contributing)

## Introduction

In this NLP exam project, the aim was to develop a binary classifier capable of distinguishing between spam and non-spam (ham) SMS messages. The work of me and my colleagues encompasses various aspects of NLP, including data preprocessing, cleaning, and the application of machine learning techniques.

## Data

The dataset provided is in .csv format and consists of 5572 sentences (SMS messages) along with their corresponding classifications (spam or ham). Notably, the dataset is highly unbalanced, with spam messages accounting for approximately 13% of the entire dataset. To mitigate this class imbalance, we employ the RandomOverSampler technique to duplicate some random elements from the minority class, making it less outnumbered.

## Methodology

We follow a structured methodology for our NLP project, including:

- Checking for duplicates and cleaning the dataset.
- Removing short messages with less than three characters.
- Removing English stop words and other common words used in messages.
- Applying stemming to reduce words to their base form.
- Splitting the dataset and using RandomOverSampler to balance the classes.
- Utilizing CountVectorizer to convert text documents into token counts.
- Employing TF-IDF to capture word importance.
- Using word embeddings with two strategies: BPE + PyTorch and GloVe.

## Models

Our project explores the performance of three distinct models:

1. **XGBoost**: A gradient-boosted decision tree classifier, suitable for handling high-dimensional, sparse data.
2. **LSTM**: A recurrent neural network (RNN) with Long Short-Term Memory cells designed to process sequential data.
3. **BERT**: Bidirectional Encoder Representations from Transformers, an advanced language model for text classification.

## Results

We present the results achieved using different strategies and models. These results include accuracy scores, F1 scores, and confusion matrices. Notably, XGBoost outperformed other models in terms of accuracy and F1 score.

## Issues Encountered

Throughout the project, we encountered some challenges, including handling dataset formats, resource limitations in Google Colab, and balancing the dataset.

## Project Recap

In summary, our project involved several key steps, including transforming the NUS SMS corpus for BPE training, preprocessing the dataset, implementing RandomOverSampler, creating document-term matrices, applying TF-IDF, and experimenting with different word embeddings. We evaluated three models to classify SMS messages and compared their performance.

## Final Conclusion

Our NLP exam project, though challenging, was a valuable learning experience. We have provided insights into the performance of different models and preprocessing techniques for text classification. We acknowledge that the results may not meet our initial high expectations, but the project has been an opportunity to apply NLP concepts in a real-world context.



## Contributing

If you have ideas for new features, improvements, or bug fixes, please open an issue or submit a pull request. Let's enhance our NLP project collaboratively.





