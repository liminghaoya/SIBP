import torch
import torch.nn as nn
import numpy as np



def SIBP(net, u):
    """
    计算并应用SIBP（内置绝对连续函数）方法

    :param net: 神经网络模型
    :param u: 调整系数
    :return: 应用SIBP方法后的神经网络模型
    """

    #针对VGG模型 我们计算出PGNs为以下的层数
    newname_all=[
        'features.12', 'features.13', 'features.14', 'features.15', 'features.16', 'features.17', 'features.18','features.19', 'features.20',
        'features.21', 'features.22', 'features.23', 'features.24', 'features.25', 'features.26', 'features.27',
        'features.28', 'features.29', 'features.30', 'features.31', 'features.32', 'features.33', 'features.34',
        'features.35', 'features.36', 'features.37', 'features.38'
           ]
    # newname_all=['features.0', 'features.1', 'features.3', 'features.4', 'features.7', 'features.8', 'features.10',
    #              'features.11', 'features.15', 'features.18', 'features.21', 'features.25', 'features.27', 'features.28',
    #              'features.31', 'features.34', 'features.35', 'features.38', 'features.40', 'features.41']

    params = net.state_dict()
    activations = {}
    name_app_cov, name_app_bat = [], []

    # 计算动态阈值
    for name, m in net.named_modules():
        if isinstance(m, nn.Conv2d):
            for idx in range(m.weight.shape[0]):
                weight = m.weight[idx].reshape(m.weight.shape[1], -1).cpu()
                std = weight.std(dim=1, unbiased=False)
                if name in newname_all:
                    name_app_cov.append((weight / std.view(-1, 1)).abs().max())
        elif isinstance(m, nn.BatchNorm2d):
            std = m.running_var.sqrt()
            weight = m.weight
            if name in newname_all:
                name_app_bat.append((weight / std).abs())

    # 计算均值
    overall_mean_cov = torch.mean(torch.tensor([torch.mean(tensor).item() for tensor in name_app_cov]))
    overall_mean_bat = torch.mean(torch.tensor([torch.mean(tensor).item() for tensor in name_app_bat]))
    Threshold_cov = overall_mean_cov if not np.isnan(overall_mean_cov) else 1
    Threshold_bat = overall_mean_bat if not np.isnan(overall_mean_bat) else 1

    # 应用SIBP方法
    i = 0
    for name, m in net.named_modules():
        i += 1
        if isinstance(m, nn.Conv2d):
            channel_abs_cont = []
            for idx in range(m.weight.shape[0]):
                weight = m.weight[idx].reshape(m.weight.shape[1], -1).cpu()
                std = weight.std(dim=1, unbiased=False)
                channel_abs_cont.append((weight / std.view(-1, 1)).abs().max())
                activations[name] = ((weight / std.view(-1, 1)).abs()).tolist()
            channel_abs_cont = torch.Tensor(channel_abs_cont)
            index = torch.where(channel_abs_cont > channel_abs_cont.mean() + 0.5 * Threshold_cov * channel_abs_cont.std())[0]
            print(index)
            params[name + '.weight'][index] = 0

        elif isinstance(m, nn.BatchNorm2d):
            std = m.running_var.sqrt()
            weight = m.weight
            channel_abs_cont = (weight / std).abs()
            activations[name] = channel_abs_cont.tolist()

            index = torch.where(channel_abs_cont > channel_abs_cont.mean() + u * Threshold_bat * channel_abs_cont.std())[0]
            print(index)
            params[name + '.weight'][index] *= 0
            params[name + '.bias'][index] *= 0

    net.load_state_dict(params)

    return net
