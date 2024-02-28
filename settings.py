from numba import njit
import numpy as np
import glm
import math

WIN_RES = glm.vec2(800, 600)

# colors
BG_COLOR = glm.vec3(0, 0.1, 0.2)