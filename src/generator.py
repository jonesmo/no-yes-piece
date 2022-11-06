import numpy as np
import librosa
import librosa.display
import pydub
from pydub import AudioSegment
from pydub.playback import play
from matplotlib import pyplot as plt
import math
from numpy import mean
from numpy.random import randint
from numpy.random import seed
import IPython
import IPython.display
from IPython.display import Audio, display
import soundfile as sf
import os
import re
import random

path_to_audio_samples = "../no_yes_samples/"
path_to_grains = "../grain_samples/"

no_files = [filename for filename in os.listdir(path_to_audio_samples) if re.search("no*", filename)]
yes_files = [filename for filename in os.listdir(path_to_audio_samples) if re.search("yes*", filename)]

yes_1, sr_yes_1 = librosa.load(os.path.join(path_to_audio_samples, random.choice(yes_files)))
yes_1_length = len(yes_1)
maximum_grain_length = sr_yes_1  # in number of samples
minimum_grain_length = sr_yes_1 / 10

random_grain_length = np.random.randint(minimum_grain_length, maximum_grain_length)

starting_sample = np.random.randint(0, yes_1_length - random_grain_length + 1)
ending_sample = starting_sample + random_grain_length
grain_0 = yes_1[starting_sample:ending_sample]
grain_0_file = os.path.join(path_to_grains, 'grain_0.wav')

if os.path.exists(grain_0_file):
    os.remove(grain_0_file)
sf.write(grain_0_file, grain_0, sr_yes_1, 'PCM_24')

# generate ten grains
# for index in range(0, 10):
#     grain = 