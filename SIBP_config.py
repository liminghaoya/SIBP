# config.py

CIFAR10_CONFIGS = {
    'badnet': {
        'dataset': 'cifar10',
        'poison_type': 'none',
        'poison_rate': 0,
        'u': 1.9,
        'epochs': 7
    },
    'blend': {
        'dataset': 'cifar10',
        'poison_type': 'none',
        'poison_rate': 0,
        'u': 1.9,
        'epochs': 5
    },
    'SIG': {
        'dataset': 'cifar10',
        'poison_type': 'none',
        'poison_rate': 0,
        'u': 1.3,
        'epochs': 8
    },
    'WaNet': {
        'dataset': 'cifar10',
        'poison_type': 'none',
        'poison_rate': 0,
        'u': 1.7,
        'epochs': 7
    },
    'trojan': {
        'dataset': 'cifar10',
        'poison_type': 'none',
        'poison_rate': 0,
        'u': [1.9,1.7],
        'epochs': [4,4]
    },
    'TaCT': {
        'dataset': 'cifar10',
        'poison_type': 'none',
        'poison_rate': 0,
        'u': [2.2,1.2,1.6,1.5],
        'epochs': [5,4,4,8]
    }
}

GTSRB_CONFIGS = {
    'badnet': {
        'dataset': 'gtsrb',
        'poison_type': 'none',
        'poison_rate': 0,
        'u': 1.8,
        'epochs': 4
    },
    'blend': {
        'dataset': 'gtsrb',
        'poison_type': 'none',
        'poison_rate': 0,
        'u': [0.5, 0.1, 2.5],
        'epochs': [20, 10, 15]
    },
    'SIG': {
        'dataset': 'gtsrb',
        'poison_type': 'none',
        'poison_rate': 0,
        'u': [1.2, 0.1, 0.02,2],
        'epochs': [10, 2, 8, 2]
    },
    'WaNet': {
        'dataset': 'gtsrb',
        'poison_type': 'none',
        'poison_rate': 0,
        'u': 0.1,
        'epochs': 20
    },
    'trojan': {
        'dataset': 'gtsrb',
        'poison_type': 'none',
        'poison_rate': 0,
        'u': 0.4,
        'epochs': 18
    },
    'TaCT': {
        'dataset': 'gtsrb',
        'poison_type': 'none',
        'poison_rate': 0,
        'u': 0.5,
        'epochs': 20
    }
}
