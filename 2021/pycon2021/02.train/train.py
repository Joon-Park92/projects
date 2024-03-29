import numpy as np
from sklearn.linear_model import LogisticRegression

import mlflow
import mlflow.sklearn

if __name__ == "__main__":

    mlflow.set_tracking_uri("http://localhost:5000")

    X = np.array([-2, -1, 0, 1, 2, 1]).reshape(-1, 1)
    y = np.array([0, 0, 1, 1, 1, 0])
    lr = LogisticRegression()
    lr.fit(X, y)

    experiment = mlflow.get_experiment_by_name("Pycon2021")
    with mlflow.start_run(experiment_id=experiment.experiment_id):
        score = lr.score(X, y)

        # Log metric
        print("Score: %s" % score)
        mlflow.log_metric("score", score)

        # Log model
        mlflow.sklearn.log_model(lr, "model")
        print("Model saved in run %s" % mlflow.active_run().info.run_uuid)
