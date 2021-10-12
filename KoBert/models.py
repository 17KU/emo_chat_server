from django.db import models

#터미널에 입력해서 설치할 것들
'''
pip install mxnet
pip3 install torch
#!pip3 install torchvision
pip install transformers==3.0.2
pip install gluonnlp
pip install sentencepiece
pip install pandas
pip install git+https://git@github.com/SKTBrain/KoBERT.git@master
'''

import torch
from torch import nn
import torch.nn.functional as F
import torch.optim as aoptim
from torch.utils.data import Dataset, DataLoader
import gluonnlp as nlp
import numpy as np
from tqdm import tqdm, tqdm_notebook

from kobert.utils import get_tokenizer
from kobert.pytorch_kobert import get_pytorch_kobert_model

from transformers import AdamW
from transformers.optimization import get_cosine_schedule_with_warmup

import pandas as pd


