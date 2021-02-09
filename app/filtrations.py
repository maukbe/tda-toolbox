from gtda.images import DensityFiltration, RadialFiltration, HeightFiltration, DilationFiltration, ErosionFiltration, SignedDistanceFiltration
from enum import Enum
import numpy as np
import streamlit as st
import math


class Filtration(Enum):    
    RADIAL = 'Radial'
    DENSITY = 'Density'
    HEIGHT = 'Height'
    DILATION = 'Dilation'
    EROSION = 'Erosion'
    SIGNED_DISTANCE = 'Signed Distance'

def plot_filtration(filtration, binarized_image):
    st.write(filtration.plot(filtration.fit_transform(binarized_image), colorscale="jet"))

def density_filtration(binarized_image):
    radius = st.number_input('Enter radius', value=3.0, step=0.1)
    return DensityFiltration(radius=radius)

def radial_filtration(binarized_image):
    st.text('Specify centre')
    max_x = binarized_image.shape[2]
    max_y = binarized_image.shape[1]
    x = st.number_input('x', min_value=0, max_value=max_x, value=math.floor(max_x/2))
    y = st.number_input('y', min_value=0, max_value=max_y, value=math.floor(max_y/2))
    return RadialFiltration(center=np.array([x, y]))

def height_filtration(binarized_image):
    st.text('Specify direction')
    x = st.number_input('x',value=1)
    y = st.number_input('y',value=1)
    return HeightFiltration(direction=np.array([x, y]))


def get_number_iterations(min_value=0, value=3, step=1 ):
    iterations = st.number_input('Number of iterations (0 reaches all deactivated pixels)',min_value=min_value, value=value, step=step)
    if iterations == 0:
        iterations = None
    return iterations

def dilation_filtration(binarized_image):
    iterations = get_number_iterations()
    return DilationFiltration(n_iterations=iterations)

def erosion_filtration(binarized_image):
    iterations = get_number_iterations()
    return ErosionFiltration(n_iterations=iterations)

def signed_distance_filtration(binarized_image):
    iterations = get_number_iterations()
    return SignedDistanceFiltration(n_iterations=iterations)


filtration_map = {
                Filtration.RADIAL.value: radial_filtration,
                Filtration.DENSITY.value: density_filtration,
                Filtration.HEIGHT.value: height_filtration,
                Filtration.DILATION.value: dilation_filtration,
                Filtration.EROSION.value: erosion_filtration,
                Filtration.SIGNED_DISTANCE.value: signed_distance_filtration
                }

def create_filtration(filtration, binarized_image):
    return filtration_map[filtration](binarized_image)


