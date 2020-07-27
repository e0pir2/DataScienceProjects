"""
paths, labels, etc
"""

import os

DATASET_PATH = r"C:\Users\rbwes\Documents\Programmierworkspaces\Python\data\BNP_Paribas_cardif_claims_management"
TRAINSET_PATH = os.path.join(DATASET_PATH, 'train.csv')
TESTSET_PATH = os.path.join(DATASET_PATH, 'test.csv')
SUBMISSION_PATH=os.path.join(DATASET_PATH,'sample_submission.csv')