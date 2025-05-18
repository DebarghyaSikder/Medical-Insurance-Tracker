from Insurance.entity import artifact_entity,config_entity
from Insurance.exception import InsuranceException
from Insurance.logger import logging
from typing import Optional
import os,sys 
from sklearn.pipeline import Pipeline
import pandas as pd
from Insurance import utils
from Insurance.utils import load_object,save_object
import numpy as np
from sklearn.preprocessing import LabelEncoder
#from imblearn.combine import SMOTETomek
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import RobustScaler
from Insurance.config import TARGET_COLUMN
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from Insurance.predictor import ModelResolver
from Insurance.entity.artifact_entity import ModelPusherArtifact,DataTransformationArtifact,ModelTrainerArtifact
from Insurance.entity.config_entity import ModelPusherConfig
from Insurance.predictor import ModelResolver
from Insurance.entity.config_entity import MODEL_FILE_NAME

class ModelPusher:
    def __init__(self,
                 model_pusher_config:ModelPusherConfig,
                 data_transformation_artifact:DataTransformationArtifact,
                 model_trainer_artifact:ModelTrainerArtifact):
        try:
            self.model_pusher_config = model_pusher_config
            self.data_transformation_artifact = data_transformation_artifact
            self.model_trainer_artifact = model_trainer_artifact
            self.model_resolver = ModelResolver(model_registry=self.model_pusher_config.saved_model_dir)
        except Exception as e:
            raise InsuranceException(e, sys)
        
    def initiate_model_pusher(self)->ModelPusherArtifact:    
        try:
            # Model and Target encoder data
            logging.info(f"Loading transformer model and target encoder data")
            transformer=load_object(file_path=self.data_transformation_artifact.transform_object_path)
            model=load_object(file_path=self.model_trainer_artifact.model_path)
            target_encoder=load_object(file_path=self.data_transformation_artifact.target_encoder_path) # Target encoder
            
            # Model pusher directory
            logging.info(f"Saving model into model pusher dir")
            save_object(file_path=self.model_pusher_config.pusher_transformer_path, obj=transformer)
            save_object(file_path=self.model_pusher_config.pusher_model_path, obj=model) # Model.pusher_transformer_path, obj=transformer)
            save_object(file_path=self.model_pusher_config.pusher_target_encoder_path, obj=target_encoder)
            
            # Save model
            logging.info(f"Saving model iin saved model dir")
            transform_path=self.model_resolver.get_latest_save_transformer_path()
            model_path=self.model_resolver.get_latest_save_model_path() 
            target_encoder_path=self.model_resolver.get_latest_save_target_encoder_path()
            
            save_object(file_path=transform_path, obj=transformer)
            save_object(file_path=model_path, obj=model)    
            save_object(file_path=target_encoder_path, obj=target_encoder)
            
            model_pusher_artifact=ModelPusherArtifact(pusher_model_dir=self.model_pusher_config.pusher_model_dir,
                                                      saved_model_dir=self.model_pusher_config.saved_model_dir)
            return model_pusher_artifact
            
        except Exception as e:
            raise InsuranceException(e, sys)   
            