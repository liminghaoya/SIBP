## SIBP: Self-Inspecting Backdoor Purification through Adaptive Identification of Suspicious Neurons

![image-20240819163642397](https://github.com/liminghaoya/SIBP/blob/main/data/pipline.jpg)

SIBP is a backdoor defence method based on the observation that some neurons in an infected DNN are maliciously activated during training, with different activation changes in different branches.SIBP considers de-poisoning from a more latent layer of neuron poisoning, and we don't need to know the type of attack, and it is effective for both visible trigger backdoor attacks and invisible trigger backdoor attacks, and it maintains the classification accuracy of the original model. SIBP is a backdoor defence method based on the observation that some neurons in an infected DNN are maliciously activated during training, with different activation changes in different branches.SIBP considers de-poisoning from a more latent layer of neuron poisoning, and we don't need to know the type of attack, and it is effective for both visible trigger backdoor attacks and invisible trigger backdoor attacks, and maintains the classification accuracy of the original model. accuracy of the original model.



We used the methods integrated in [backdoor-toolbox](https://github.com/vtu81/backdoor-toolbox) for poisoning model training and metrics evaluation.

The specific training and evaluation methods are described in the links above.

## Dependency

This code was developed using torch==1.13.1+cu116. To set up the required environment, install PyTorch with CUDA manually, then by installing the other packages `pip install -r requirement.txt`.

### Preliminary

Datasets:

The original CIFAR10 and GTSRB datasets will be downloaded automatically.

Before any experiments, first initialise the clean retention and validation data using the command `python create_clean_set.py -dataset=$DATASET -clean_budget $N`, where `$DATASET = cifar10, gtsrb`

### Quick start

For example training a backdoor model that is attacked by BadNets

```
# Create a poisoned training set
python create_poisoned_set.py -dataset=cifar10 -poison_type=badnet -poison_rate=0.1
# Train on the poisoned training set
python train_on_poisoned_set.py -dataset=cifar10 -poison_type=badnet -poison_rate=0.1
# Test the backdoor model
python test_model.py -dataset=cifar10 -poison_type=badnet -poison_rate=0.1
```

Get a clean fine-tuned dataset:

```
#Changing the number of clean samples to be obtained, 2% i.e. 1000 sheets were selected for this experiment.
./poison_tool_bo/none.py 

# Create a clean training set
python create_poisoned_set.py -dataset=cifar10 -poison_type=none -poison_rate=0
```

SIBP：

```
python main_defense.py
```

