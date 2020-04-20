# Data Stewardship Course DMP

## Introduction

In this experiment the evaluation of the two classification algorithms: random forest and multilayer perceptron (MLP) will be shown, on the example of an analysis of [thyroid disease record dataset](https://www.openml.org/d/57). The goal is to show how the algorithm acts upon different train/test set splits, parameters and scaling, and to check which combination of the mentioned characteristics produce the best (most accurate) model. Dataset consist of 3772 instances, 30 attributes and 4 classes. The data is preprocessed, and the mentioned algorithms are executed, in Weka Toolkit (Explorer). For the purposes of the Data Stewardship course, the part of the experiment with MLP will be used.

## Software

For this experiment [Weka Toolkit (Explorer) GUI 3.8.4](https://waikato.github.io/weka-wiki/downloading_weka/) is used.

## Steps 

1.	Preprocessing – in this step missing values are removed, for TBG and TBG_measured features, since TBG_features denotes that TBG value is not measured for any of the instances. Then, missing values are replaced using ‘ReplaceMissingValues’ from Weka Explorer in the preprocessing tab. Moreover, the algorithm should work with numerical values, which is not the case for our dataset, because most of the values are of ‘boolean’/nominal type. The way for turning them into the numeric value is by using ‘NominalToBinary’ filter. It converts all nominal attributes into binary numeric attributes
2.	Subsampling – since the dataset is very small, with 3772 instances, subsampling was not needed.
3.	Parameterizing – each of the mentioned algorithms makes use of different parameters which can be changed in order to produce different (better or worse) models. MLP has following parameters: batchSize, decay, hiddenLayers, learningRate, momentum, seed and training time. Some of the parameters were taken into account and changed with some common values which were found on https://machinelearningmastery.com/. 
4.	Scaling – this step is performed by normalizing ‘age’ feature of the dataset, since it is the only attribute that could be normalized. It is performed using ‘Normalize’ filter function of the preprocessing tab in Weka.
5.	Training/test set split – changing the percentage of training and test sets used for creating a model.
6.	Evaluation – after each step is performed, the evaluation based on CCI – correctly classified instances, MAE – mean absolute error and time to create a model is done. 

## Reproduce the experiment

1. Preprocessing - in the Preprocessing tab in Weka GUI, open and apply preprocessing functions from /weka_experiment/preprocessing one by one.
2. Parameterizing - in the classification tab in Weka GUI, either upload model and run the data set on one of the existing models which can be found in /weka_experiment/classification_algorithm/multilayer_perceptron/200419/parameters/, or open the existing parameters from the corresponding experiment folder and start the classification by itself and then compare two models.
3. Training/test set split - in the classification tab in Weka GUI, change the percentage of the test set split and compare to the existing models in /weka_experiment/classification_algorithm/multilayer_perceptron/YYMMDD/training_test_split/.
4. Scaling - in the preprocessing tab in Weka GUI, open and apply scaling functions from /weka_experiment/classification_algorithm/multilayer_perceptron/200419/scaling/ and then run the classification algorithm with default values in the classification tab. As in two previous examples, compare two models.

It is possible that models slightly deviate from one another.

## Sources

This experiment is done originally as part of one of the assignments of the Business Intelligence course at Vienna University of Technology. The original experiment and the teport can be found under /original_experiment/


## Licence
<p xmlns:dct="http://purl.org/dc/terms/" xmlns:vcard="http://www.w3.org/2001/vcard-rdf/3.0#">
  <a rel="license"
     href="http://creativecommons.org/publicdomain/zero/1.0/">
    <img src="http://i.creativecommons.org/p/zero/1.0/88x31.png" style="border-style: none;" alt="CC0" />
  </a>
  <br />
  To the extent possible under law,
  <a rel="dct:publisher"
     href="https://orcid.org/0000-0001-7084-3423">
    <span property="dct:title">Mensur Besirovic</span></a>
  has waived all copyright and related or neighboring rights to
  <span property="dct:title">Data Stewardship Course DMP</span>.
This work is published from:
<span property="vcard:Country" datatype="dct:ISO3166"
      content="AT" about="https://github.com/mensBash/DataStewardship">
  Österreich</span>.
</p>
