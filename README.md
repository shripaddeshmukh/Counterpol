This repository contains the code for the paper _"Counterfactual Explanation Policies in RL"_ by Shripad Vilasrao Deshmukh, Srivatsan R, Supriti Vijay, Jayakumar Subramanian and Chirag Agarwal. The paper is available on arXiv at [https://arxiv.org/abs/2307.13192](https://arxiv.org/abs/2307.13192). If you need any help or have any questions, please feel free to reach out to Shripad on this email ID: svdeshmukh@umass.edu

## Repository Organization
The repository is organized as follows:
```
Counterpol
├── README.md (This file)
├── hyperparameters.py (Hyperparameter configurations for all 5 environments)
├── code (Code for reproducing _Counterpol_ results)
│   ├── counterpol_lunarlander.ipynb
│   └── orig_ckpts (Stable-baselines A2C checkpoints trained on LunarLander)
│       ├── lunarlander-v2_100000_steps.zip
│       ├── lunarlander-v2_150000_steps.zip
│       └── lunarlander-v2_200000_steps.zip
└── additional_results (Additional results on LunarLander-v2 and BipedalWalker-v3)
	├── lunarlander
	│   └── Scenario X
	│       ├── gifs
	│       │   ├── A2C.gif
	│       │   └── Counterpol_Target_Return_<>.gif
	│       └── imgs
	│           ├── A2C.png
	│           └── Counterpol_Target_Return_<>.png
	└── bipedalwalker
		└── Scenario X
			├── gifs
			│   ├── PPO.gif
			│   └── Counterpol_Target_Return_<>.gif
			└── imgs
				├── PPO.png
				└── Counterpol_Target_Return_<>.png
```

## Running the code
To run the code, you would need to setup a conda environment as follows:

```sh
conda create -n counterpol python=3.8 -y
conda activate counterpol
conda install jupyter ipykernel -y
python -m ipykernel install --user --name counterpol
pip install "gym[box2d]"
pip install "stable-baselines3[extra]"
pip install torch torchvision torchaudio tqdm wandb
conda install ffmpeg -y
pip install pyglet==1.5.27
```

This will create a Jupyter kernel named _counterpol_, which can then be activated for running counterfactual estimation.

## Citation
Please consider citing this work if you find it useful using the following BibTeX entry:

```bibtex

@article{deshmukh2023counterfactual,
  title={Counterfactual Explanation Policies in RL},
  author={Deshmukh, Shripad V and Vijay, Supriti and Subramanian, Jayakumar and Agarwal, Chirag and others},
  journal={arXiv preprint arXiv:2307.13192},
  year={2023}
}
```