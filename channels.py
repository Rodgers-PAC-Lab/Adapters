"""Lists of channels in the order they are on the probes.

Seems like this file should be the one called probes.py
"""

import pandas
import numpy as np


## These are the channels numbers for each probe 
# Channel numbers are always sorted from superficial to deep

# This is the Neuronexus numbering for the Poly2 channels sorted by depth
# from superficial to deep.
poly2_NN_sort_by_depth = [
    23, 10, 24,  9, 25,  8, 26,  7, 27,  6, 28,  5, 29,  4, 30,  3, 31,
    2, 32,  1, 22, 11, 21, 12, 20, 13, 19, 14, 18, 15, 17, 16]

# This is the Neuronexus numbering for the Edge channels sorted by depth
# from superficial to deep.
edge_NN_sort_by_depth = [
    32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 
    16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# Cambridge NeuroTech H3
h3_sort_by_depth = [
    21, 23, 24, 30, 29, 16, 18, 20, 27, 19, 17, 25, 26, 32, 28, 22, 
    1, 3, 5, 7, 9, 11, 13, 15, 31, 14, 12, 10, 8, 6, 4, 2,
    64, 62, 60, 58, 56, 54, 52, 50, 34, 51, 53, 55, 57, 59, 61, 63, 
    44, 42, 41, 35, 36, 49, 47, 45, 38, 46, 48, 40, 39, 33, 37, 43,
]

# Janelia probe channels, sorted by depth
janelia_sort_by_depth = (
    list(range(1, 24)) + [28, 24, 32, 25, 29, 26, 30, 27, 31] + 
    [34, 38, 35, 39, 36, 40, 33, 41, 37] + list(range(42, 65)))

# Extract out the subset of janelia_sort_by_depth that is on each connector
janelia_top_channels = list(range(1, 17)) + list(range(49, 65))
janelia_bottom_channels = list(range(17, 49))
janelia_top_sort_by_depth = [ch for ch in janelia_sort_by_depth 
    if ch in janelia_top_channels]
janelia_bottom_sort_by_depth = [ch for ch in janelia_sort_by_depth 
    if ch in janelia_bottom_channels]


## Calculating the exact depth of each channel
# Calculate the actual depth of the janelia channels (will use this later)
janelia_depth_df = pandas.DataFrame.from_dict(
    {'J': janelia_sort_by_depth})
janelia_depth_df['Z'] = np.arange(0, 64 * 20, 20, dtype=int)

h3_depth_df = pandas.DataFrame.from_dict(
    {'Prb': h3_sort_by_depth})
    
h3_depth_df['Z'] = np.arange(0, 64 * 20, 20, dtype=int)

