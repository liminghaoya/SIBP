from fine_training import fine_train
from SIBP_config import CIFAR10_CONFIGS, GTSRB_CONFIGS
import torch


def configure_and_train(config, pre_modelpath, model_path):
    """
    配置训练参数并执行fine_train函数。

    :param config: 从配置文件中读取的攻击方法配置
    :param pre_modelpath: 预训练模型路径
    :param model_path: 模型保存路径
    """
    poison_type = config['poison_type']
    poison_rate = config['poison_rate']
    print('poison_rate',poison_rate)
    u = config['u']
    epochs = config['epochs']
    dataset = config['dataset']


    if isinstance(u, list) and isinstance(epochs, list):
        for i in range(len(u)):
            fine_train(dataset, poison_type, poison_rate, pre_modelpath, model_path, u[i], epochs[i])
            pre_modelpath=model_path

    else:
        fine_train(dataset, poison_type, poison_rate, pre_modelpath, model_path, u, epochs)



def main():
    # 选择数据集配置：CIFAR-10 或 GTSRB
    dataset_config = CIFAR10_CONFIGS  # 或者 GTSRB_CONFIGS

    # 设置路径
    #需要净化的模型路径
    pre_modelpath = './poisoned_train_set/cifar10/badnet_0.100_poison_seed=0/full_base_aug_seed=2333_ori.pt'
    #净化后模型的存储路径
    model_path = './poisoned_train_set/cifar10/badnet_0.100_poison_seed=0/full_base_aug_seed=2333.pt'

    # 选择攻击方法
    selected_attack = 'badnet'  # 可替换为 'blend', 'SIG', 'WaNet', 'trojan', 'TaCT'

    config = dataset_config[selected_attack]
    configure_and_train(config, pre_modelpath, model_path)


if __name__ == "__main__":
    main()
