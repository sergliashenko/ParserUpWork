from src import textProcessing
from src import word2VecDistance
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler


def main():
    # get keywords
    keywords = textProcessing.get_top_keywords(5)
    threshold = 0.3  # need modify
    matrix = word2VecDistance.similarity_for_all_vacancies(keywords, threshold)

    X = StandardScaler().fit_transform(matrix)
    db = DBSCAN(eps=0.3, min_samples=2).fit(X)
    print(db.labels_)



if __name__ == "__main__":
    main()