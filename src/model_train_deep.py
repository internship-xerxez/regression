import numpy as np
from keras_preprocessing.image import ImageDataGenerator
from keras.layers import Dense, Input, Flatten
from keras.models import Model
from glob import glob
import os
import argparse
from get_data_deep import get_data_deep
import matplotlib.pyplot as plt
from keras.applications.vgg19 import VGG19
import tensorflow

def train_model_deep(config_file):
    config=get_data_deep(config_file)
    if train == True:
        img_size = config['model']['image_size']
        trn_set = config['model']['train_path']
        te_set= config['model']['test_path']
        num_cls = config['load_data_deep']['num_classes']
        rescale = config['img_augment']['rescale']
        shear_range = config['img_augment']['shear_range']
        zoom_range= config['img_augment']['zoom_range']
        verticalf = config['img_augment']['vertical_flip']
        horizontalf = config['img_augment']['horizontal_flip']
        batch = config['img_augment']['batch_size']
        class_mode = config['img_augment']['class_mode']
        loss = config['model']['loss']
        optimizer = config['model']['optimizer']
        metrics = config['model']['metrics']
        epochs = config['model']['epochs']

        print(type(batch))

        resnet = VGG19(input_shape=img_size +[3], weights='imagenet', include_top=False)

        for p in resnet.layers:
            p.trainable = False

        op = Flatten()(resnet.output)
        prediction = Dense(num_cls, activation='softmax')(op)
        
        mod = Model(input=resnet.input, outputs=prediction)
        print(mod.summary())
        img_size = tuple(img_size)

        mod.compile(loss=loss, optimizer=optimizer, metrics=metrics)

        tra











if __name__ == '__main__':
    
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('--config',default='deep_params.yaml')
    passed_args = args_parser.parse_args()
    train_model_deep(config_file=passed_args.config)