from inspect import getmembers, isfunction
import loggerGenerator
import numpy as np
import pandas as pd
import torch
# import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split


def testing_torch_availability():
    print(torch.__version__)

    print(dir(torch))

    print(getmembers(torch, isfunction))

    print(torch.cuda.is_available())

    print(torch.cuda.current_device())

    print(torch.cuda.device_count())

    print(torch.cuda.get_device_name())

    print(torch.cuda.memory_stats())

    print(torch.cuda.memory_allocated())


def kaggle_data_set():
    myData = pd.read_csv("diabetes.csv")
    print(myData.head())
    # print(diabetes.isnull().sum())

    # myData['Outcome'] = np.where(myData['Outcome'] == 1, "Diabetic", "No Diabetic")
    # print(myData.head())
    # sns.pairplot(myData, hue="Outcome", )
    # plt.show()

    X = myData.drop('Outcome', axis=1).values  # independent features
    # print(X)
    y = myData['Outcome'].values  # dependent features
    # print(y)
    # X is numpy array here
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    print("X_train: \n", "type: ", type(X_train), "  shape: ", X_test.shape, "    Dtype: ", X_train.dtype, "\n", X_train)
    print("X_test: \n", "type: ", type(X_test), "  shape: ", X_test.shape, "    Dtype: ", X_test.dtype, "\n", X_test)
    print("y_train: \n", "type: ", type(y_train), "  shape: ", y_train.shape, "    Dtype: ", y_train.dtype, "\n", y_train)
    print("y_test: \n", "type: ", type(y_test), "  shape: ", y_test.shape, "    Dtype: ", y_test.dtype, "\n", y_test)


def main() -> None:
    # pyTorchLogger.debug("Inside main()")
    # testing_torch_availability()
    kaggle_data_set()


if __name__ == "__main__":
    # Getting loggers
    pyTorchLogger = loggerGenerator.my_loggers()

    main()
