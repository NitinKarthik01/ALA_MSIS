import numpy as np
from gensim.models import KeyedVectors
import string
from Vector_Implementation.vector import Vec



model = KeyedVectors.load(
    "/Users/nitinsrikarthikeya/Documents/ALA_MSIS/glove50/glove_50_fast.wordvectors"
)

stop_words = {
    "the", "a", "an", "and", "or", "of", "to",
    "in", "on", "for", "is", "are", "was", "were",
    "with", "at", "by", "from"
}

def preprocess(text):

    print("Preprocessing started.......")

    text = text.lower()

    text = text.translate(str.maketrans("", "", string.punctuation))

    token1 = text.split()

    token2 = []
    for t in token1:
        if t not in stop_words:  # remove stop words
            token2.append(t)

    tokens = []
    for t in token2:
        if len(t) > 2:           # remove words <= 2
            tokens.append(t)

    print("Preprocessing completed.......")

    return tokens



tags = [ "research", "innovation", "education", "university", "students",
    "faculty", "campus", "engineering", "medicine", "technology",
    "curriculum", "collaboration", "publication", "laboratory", "scholarship",
    "mentorship", "internship", "entrepreneurship", "accreditation", "alumni", ]


def build_tag_matrix(model, tags):

    tag_names, Tag = [], []

    for tag in tags:

        words = tag.split()

        for w in words:
            if w not in model.key_to_index:
                raise ValueError("Word is not in model")
        vectors = [model[w] for w in words]

        dimensions = len(vectors[0])
        # vectors[0] selects the first word vector from the list of vectors.
        # len(vectors[0]) gives the number of components in that vector.
        # Since we use GloVe 50, each word vector has 50 dimensions 
        # and the mean vector shoudl also have 50 dimesnions


        mean_vector = []

        for i in range(dimensions):
            total = 0

            for vector in vectors:
                total += vector[i]

            mean_vector.append(total / len(vectors))

        Tag.append(mean_vector)
        tag_names.append(tag)

    return tag_names, Tag

def build_text_matrix(model, tokens):
    vocab_tokens =[]
    oov = []

    for t in tokens:
        if t in model.key_to_index:
            vocab_tokens.append(t)

        else :
            oov.append(t)

    Text = [model[t] for t in vocab_tokens]
    return vocab_tokens, oov, Text



def cosine_similarity(Tag, Text):
    tag_vectors = []
    S = []
    for j in range(len(Tag)):
        tag_vectors.append(Vec([float(x) for x in Tag[j]]))

    for i in range(len(Text)):
        w_vec = Vec([float(x) for x in Text[i]])

        row =[]
        for t_vec in tag_vectors:
            row.append(w_vec.cos_sim(t_vec))

        S.append(row)

    return S


def rank_tags(tag_names, S, vocab_tokens):

    results = []
    for j in range(len(tag_names)):
        best_score = S[0][j]
        best_row = 0

        for i in range(len(S)):
            if S[i][j] > best_score:
                best_score = S[i][j]
                best_row = i

        results.append(
            (tag_names[j], best_score, vocab_tokens[best_row])
        )

    # Sort results in descending order
    for i in range(len(results)):

        max_index = i

        for j in range(i + 1, len(results)):

            if results[j][1] > results[max_index][1]:
                max_index = j

        results[i], results[max_index] = results[max_index], results[i]

    return results



if __name__ == "__main__":


    file_path = "/Users/nitinsrikarthikeya/Documents/ALA_MSIS/Assignment_2/text.txt"

    with open(file_path, "r", encoding="utf-8") as file:
        sentence = file.read()

    tokens = preprocess(sentence)

    tag_names, Tag = build_tag_matrix(model, tags)

    vocab_tokens, oov, Text = build_text_matrix(model, tokens)

    S = cosine_similarity(Tag, Text)

    results = rank_tags(tag_names, S, vocab_tokens)

    print("\nOut-of-vocabulary words:", oov)

    print("\nRanked Tags:")
    for tag, score, word in results:
        print(tag, ":", score, "| Matching word:", word)
    



