import pandas as pd
import os
import logging
import logging.config
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from lightgbm import LGBMRegressor
import warnings

warnings.filterwarnings("ignore", category=FutureWarning)

# load logging config
logging.config.fileConfig("logger.conf")

# Folder and the CSV file
data_folder = '../data'
csv_filename = 'winequality-red.csv'

# Get the current working directory
current_directory = os.getcwd()

# The full path to the CSV file
csv_path = os.path.join(current_directory, data_folder, csv_filename)

if __name__ == '__main__':
    logging.info('Process started')

    # Read the CSV file into a DataFrame
    logging.info('Loading the data')
    df = pd.read_csv(csv_path)

    # Get a data snapshot
    logging.info('Data snapshot')
    print(df.head())

    # Get a data description
    logging.info('Feature statistics')
    print(df.describe())

    # Get a data relevant plots
    logging.info('Generating scatter plots')
    numerical_columns = df.columns[df.dtypes != 'object'].drop('quality')
    plt.figure(figsize=(12, 8))

    # Iterate through numerical columns and create scatter plots
    for column in numerical_columns:
        plt.scatter(df[column], df['quality'], alpha=0.5)
        plt.xlabel(column)
        plt.ylabel('quality')
        plt.title(f'Scatter plot between {column} and quality')
        plt.grid(True)
        plt.savefig(f'../figs/scatter_plot_{column}_vs_quality.png')
        plt.clf()

    # Close any remaining plot windows
    plt.close()

    # Build the model
    logging.info('Building the Model')

    # Splitting the DataFrame
    X = df.drop(columns=['quality'])
    y = df['quality']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=24
    )

    logging.info(f'Sahpe of train dataset:\n{X_train.shape}')
    logging.info(f'Shape of test dataset:\n{X_test.shape}')

    # Initialize the models
    logging.info('Fitting the Models')
    models = {
        'Linear Regression': LinearRegression(n_jobs=-1),
        'LightGBM': LGBMRegressor(n_jobs=-1),
        'RandomForest': RandomForestRegressor(n_jobs=-1)
    }

    best_model = None
    best_mse = float('inf')

    for model_name, model in models.items():
        logging.info(f'Training {model_name}')
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        mse = mean_squared_error(y_test, y_pred)
        logging.info(f'{model_name} MSE: {mse}')

        if mse < best_mse:
            best_mse = mse
            best_model = model_name

    logging.info(f'Best Model: {best_model} with MSE: {best_mse}')

    logging.info('Process ended successfully')
