from Insurance.entity import artifact_entity,config_entity
from Insurance.exception import InsuranceException
from Insurance.logger import logging
from typing import Optional
import os,sys 
from sklearn.pipeline import Pipeline
import pandas as pd
from Insurance import utils
import numpy as np
from sklearn.preprocessing import LabelEncoder
#from imblearn.combine import SMOTETomek
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import RobustScaler
from Insurance.config import TARGET_COLUMN
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split



## Model define and Trainer
## Set a Threshold for our new model. If newer model accuracy is less than this threshold, we will not use it and continue with previous running model
## We check for Overfitting and Underfitting of data
class ModelTrainer:
    def __init__(self, model_trainer_config:config_entity.ModelTrainingConfig,
                 data_transformation_artifact:artifact_entity.DataTransformationArtifact):
        
        try:
            self.model_trainer_config = model_trainer_config
            self.data_transformation_artifact = data_transformation_artifact
        except Exception as e:
            raise InsuranceException(e, sys)
        
        
    def train_model(self,X,y):
        try:
            lr=LinearRegression()
            lr.fit(X,y)
            return lr
        except Exception as e:
            raise InsuranceException(e, sys)

    def initiate_model_trainer(self)->artifact_entity.ModelTrainerArtifact:
        try:
            # Load the transformed training and testing data
            train_arr = utils.load_numpy_array_data(file_path=self.data_transformation_artifact.transformed_train_path)
            test_arr = utils.load_numpy_array_data(file_path=self.data_transformation_artifact.transformed_test_path)

            # Separate features and target variable
            X_train,y_train=train_arr[:,:-1],train_arr[:,-1]
            X_test,y_test=test_arr[:,:-1],test_arr[:,-1]
            

            # Train the model
            model = self.train_model(X=X_train, y=y_train)

            
            yhat_train = model.predict(X_train)
            r2_train_score=r2_score(y_true=y_train,y_pred=yhat_train)
            
            yhat_test = model.predict(X_test)
            r2_test_score=r2_score(y_true=y_test,y_pred=yhat_test)
            
            if r2_test_score<self.model_trainer_config.expected_accuracy:
                raise Exception(f"Model is not good as not expected accuracy: {self.model_trainer_config.expected_accuracy}:model_actual_accuracy:{r2_test_score}")
            
            
            # Check if overfitting
            diff=abs(r2_train_score-r2_test_score)
            
            if diff>self.model_trainer_config.overfitting_threshold:
                raise Exception(f"Train model and test score diff is more than {self.model_trainer_config.overfitting_threshold}")
            
            
            utils.save_object(file_path=self.model_trainer_config.model_path,
                             obj=model)

            # Prepare artifact
            model_trainer_artifact = artifact_entity.ModelTrainerArtifact(
                model_path=self.model_trainer_config.model_path,
                r2_train_score=r2_train_score,
                r2_test_score=r2_test_score
            )

            return model_trainer_artifact

        except Exception as e:
            raise InsuranceException(e, sys)
        