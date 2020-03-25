import numpy as np
from natsort import natsorted
from PIL import Image
import glob
import os

files = glob.glob("*.jpg") 
files = natsorted(files)
imgs = [ Image.open(i) for i in files ]

stitched = np.hstack( (np.asarray(i) for i in imgs ) )

stitched = Image.fromarray(stitched)
stitched.save( os.getcwd() + '.png' )    