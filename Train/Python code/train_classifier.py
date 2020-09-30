
# Train logistic regression model
from sklearn.linear_model import LogisticRegression
def train(df):
    data_repo = data.txt #os.environ['DATA_REPO']
    df = pd.read_json(data_repo)


    # Select features
    x = df.loc[:, df.columns != 'labels']

    # Select label
    y = df['labels']

    #train model
    clf = LogisticRegression().fit(x, y)

    clf_api = os.environ['CLF_API']
    if clf_api:
        clf.save(os.path.join(clf_api), "classifier")

    if type(classifier) == LogisticRegression:
        return 'Logistic regression model is trained'