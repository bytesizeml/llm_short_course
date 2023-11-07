import streamlit as st
import numpy as np
import numpy.linalg as la
import pickle 


# Compute Cosine Similarity
def cosine_similarity(x,y):

    x_arr = np.array(x)
    y_arr = np.array(y)

    ############################
    ### WRITE YOUR CODE HERE ###
    ############################
    # return 


# Function to Load Glove Embeddings
def load_glove_embeddings(glove_path="Data/embeddings.pkl"):
    """
    First step: Download the 50d Glove embeddings from here - https://www.kaggle.com/datasets/adityajn105/glove6b50d
    Second step: Format the glove embeddings into a dictionary that goes from a word to the 50d embedding.
    Third step: Store the 50d Glove embeddings in a pickle file of a dictionary.
    Now load that pickle file back in this function
    """

    with open(glove_path,"rb") as f:
        embeddings_dict = pickle.load(f)
    
    return embeddings_dict

# Get Averaged Glove Embedding of a sentence
def averaged_glove_embeddings(sentence, embeddings_dict):
    """
    Simple sentence embedding: Embedding of a sentence is the average of the word embeddings
    """
    words = sentence.split(" ")
    glove_embedding = np.zeros(50)
    count_words = 0

    ############################
    ### WRITE YOUR CODE HERE ###
    ############################

    """
    for word in words:
        
    return 
    """



# Load glove embeddings
glove_embeddings = load_glove_embeddings()

# Gold standard words to search from
gold_words = ["flower","mountain","tree","car","building"]

# Text Search
st.title("Search Based Retrieval Demo")
st.subheader("Pass in an input word or even a sentence (e.g. jasmine or mount adams)")
text_search = st.text_input("", value="")


# Find closest word to an input word
if text_search:
    input_embedding = averaged_glove_embeddings(text_search, glove_embeddings)
    cosine_sim = {}
    for index in range(len(gold_words)):
        cosine_sim[index] = cosine_similarity(input_embedding, glove_embeddings[gold_words[index]])

    ############################
    ### WRITE YOUR CODE HERE ###
    ############################

    # Sort the cosine similarities
    # sorted_cosine_sim =

    st.write("(My search uses glove embeddings)")
    st.write("Closest word I have between flower, mountain, tree, car and building for your input is: ")
    st.subheader(gold_words[sorted_cosine_sim[0][0]] )
    st.write("")

