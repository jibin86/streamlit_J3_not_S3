from numpy import dot
from numpy.linalg import norm
import pandas as pd

def cos_sim(A, B):
    return dot(A, B)/(norm(A)*norm(B))

def recommend_combined(product):
    df_encode_new = pd.read_csv("df_encode_new.csv")
    df_encode_new = df_encode_new.drop(columns=df_encode_new.columns[0])

    df_encode_review = pd.read_csv("df_encode_review.csv")
    df_encode_review = df_encode_review.drop(columns=df_encode_review.columns[0])
    
    for i in range(len(df_encode_new)):
        df_encode_new.iloc[i, -1] = cos_sim(product, df_encode_new.iloc[i, 3:-1])

    df_encode_new = df_encode_new.sort_values(by='cos', ascending=False)
    recomm_1 = df_encode_new.iloc[0, :]

    for i in range(len(df_encode_review)):
        df_encode_review.iloc[i, -1] = cos_sim(recomm_1[3:-1], df_encode_review.iloc[i, 2:-1])

    df_encode_review = df_encode_review.sort_values(by='cos', ascending=False)

    return recomm_1, df_encode_review.iloc[0:5,]

def get_sim_data(product):
    
    sim1 , sim2_list = recommend_combined(product)

    return sim1[['title', 'image', 'body']], sim2_list[['title', 'image']]