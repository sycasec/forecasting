import argparse
import numpy as np
import torch

# import pandas as pd
# from lib.dataloader import get_dataloader_cde

# loading npz file
# data = np.load("PEMS04.npz")
# data = np.load("../data/PEMS07/PEMSd7.npz")
data = np.load("../data/PEMSD4/test.npz")

# print(f"keys: {data.files}")

for key in data.files:
    print(f"key={key}: shape={data[key].shape}")

# print(f"first 5 samples: \n {data['data'][:,:,0][:5]}")
print(f"first 5 x samples: \n {data['x'][:,:,0][:,:,0][:5]}")

# config = configparser.ConfigParsergg

# args = argparse.Namespace(
#     dataset="PEMSD4",
#     column_wise=False,
#     test_ratio=0.2,
#     val_ratio=0.2,
#     lag=12,
#     horizon=12,
#     missing_test=False,
#     missing_rate=0.1,
#     batch_size=64,
#     normalizer="std",
#     tod=False,
# )
#
# s = [train_loader, val_loader, test_loader, scaler, times] = get_dataloader_cde(
#     args,
#     normalizer=args.normalizer,
#     tod=args.tod,
#     dow=False,
#     weather=False,
#     single=False,
# )
# # print("=" * 15)
# # print(s)
#
# # Get the first batch from the DataLoader
# first_batch = next(iter(train_loader))
#
# # Inspect the structure of the first element
# print("Data tuple structure:", len(first_batch))

# for i, data in enumerate(train_loader):
#     if i >= 5:
#         break
#     inputs, targets = data
#
#     inputs = inputs.numpy()
#     targets = targets.numpy()
#     print(f"Batch {i+1}: Inputs shape: {inputs.shape}, Targets shape: {targets.shape}")

data.close()
