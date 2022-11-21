# %%
import numpy as np
import time
from time import sleep
from .init import qdac
from qcodes.utils.dataset.doNd import do1d, do2d

# %% mapz
do2d(magnet.bpar, -0.1, 0.1, 201, 3, yoko.Vsd, -1.3e-3, 1.3e-3, 401, 1.1*Lockin1.time_constant(), Lockin1.CondX, Lockin1.P)
