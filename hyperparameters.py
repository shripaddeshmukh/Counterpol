pendulum_config = {
    'method': 'grid',
    'metric': {
        'name': 'performance_objective_orig',
        'goal': 'minimize'
    },
    'parameters': {
        'env': {
            'values': ['Pendulum-v1']
        },
        'pretrained_save_path': {
            'values': ['../training_rl_agents/models/Pendulum-v1/']
        },
        'model_id': {
            'values': [400000, 600000, 800000]
        },
        'learning_rate': {
            'values': [5e-3]
        },
        'kl_weight': {
            'values': [1e5]
        },
        'num_rollouts': {
            'values': [10]
        },
        'num_pol_iters': {
            'values': [100]
        },
        'max_cf_iters': {
            'values': [10]
        },
        'max_rollout_length': {
            'values': [1000]
        },
        'reward_range': {
            'values': [1000]
        },
        'target_return': {
            'values': [-1250, -1000, -750, -500, -250]
        },
        'delta_return': {
            'values': [37.5]
        },
        'grad_clip_value': {
            'values': [1.0]
        },
        'seed': {
            'values': [0, 1, 2]
        }
    }
}

acrobot_config = {
    'method': 'grid',
    'metric': {
        'name': 'performance_objective_orig',
        'goal': 'minimize'
    },
    'parameters': {
        'env': {
            'values': ['Acrobot-v1']
        },
        'pretrained_save_path': {
            'values': ['../training_rl_agents/models/Acrobot-v1/']
        },
        'model_id': {
            'values': [15000, 30000, 45000]
        },
        'learning_rate': {
            'values': [1e-3]
        },
        'kl_weight': {
            'values': [1e0]
        },
        'num_rollouts': {
            'values': [10]
        },
        'num_pol_iters': {
            'values': [100]
        },
        'max_cf_iters': {
            'values': [10]
        },
        'max_rollout_length': {
            'values': [500]
        },
        'reward_range': {
            'values': [500]
        },
        'target_return': {
            'values': [-120, -110, -100, -90, -80]
        },
        'delta_return': {
            'values': [2.5]
        },
        'grad_clip_value': {
            'values': [1.0]
        },
        'seed': {
            'values': [0, 1, 2]
        }
    }
}


cartpole_config = {
    'method': 'grid',
    'metric': {
        'name': 'performance_objective_orig',
        'goal': 'minimize'
    },
    'parameters': {
        'env': {
            'values': ['CartPole-v1']
        },
        'pretrained_save_path': {
            'values': ['../training_rl_agents/models/CartPole-v1/']
        },
        'model_id': {
            'values': [30000]
        },
        'learning_rate': {
            'values': [1e-3]
        },
        'kl_weight': {
            'values': [1e1]
        },
        'num_rollouts': {
            'values': [10]
        },
        'num_pol_iters': {
            'values': [100]
        },
        'max_cf_iters': {
            'values': [10]
        },
        'max_rollout_length': {
            'values': [500]
        },
        'reward_range': {
            'values': [500]
        },
        'target_return': {
            'values': [450, 350, 250, 150, 50]
        },
        'delta_return': {
            'values': [10]
        },
        'grad_clip_value': {
            'values': [1.0]
        },
        'seed': {
            'values': [0, 1, 2]
        }
    }
}

lunarlander_config =  {
        'env': 'LunarLander-v2',
        'learning_rate': 0.0005,
        'kl_weight': 10,
        'num_rollouts': 10,
        'model_id': 100000,
        'num_pol_iters': 10,
        'max_cf_iters': 250,
        'max_rollout_length': 500,
        'reward_range': 500,
        'target_return': [100, 150, 0, -50],
        'delta_return': 5,
        'grad_clip_value': 0.5,
        'pretrained_save_path': './orig_ckpts/',
        'seed': 0
    }

bipedalwalker_config = {
    'env': 'BipedalWalker-v3',
    'learning_rate': 5e-4,
    'kl_weight': 1,  
    'num_rollouts': 5,
    'model_id': 150000,
    'num_pol_iters': 200,
    'max_cf_iters': 5,
    'max_rollout_length': 1600,  
    'reward_range': 400,  
    'target_return': [50, 150],  
    'delta_return': 10,
    'grad_clip_value': 1.0,
    'pretrained_save_path': '../training_rl_agents/models/BipedalWalker-v3/',
    'seed': 0
}
