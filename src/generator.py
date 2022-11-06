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
import os
import re

path_to_audio_samples = "../no_yes_samples/"

no_files = [filename for filename in os.listdir(path_to_audio_samples) if re.search("no*", filename)]
yes_files = [filename for filename in os.listdir(path_to_audio_samples) if re.search("yes*", filename)]

print(no_files)
print(yes_files)