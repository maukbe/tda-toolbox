import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import os
import pandas as pd
from gtda.plotting import plot_heatmap
from PIL import Image
import matplotlib 
from gtda.images import Binarizer
from gtda.images import DensityFiltration

st.title('TDA Toolbox')

uploaded_file = st.file_uploader("Choose an image...", type="jpg")

if st.checkbox('Show heatmap'):
    image = Image.open(uploaded_file)
    img_array = np.array(image)
    heatmap = plot_heatmap(img_array)
    st.write(heatmap)

if st.checkbox('Binarise image'):
    threshold = st.slider('Threshold', 0.0, 1.0, 0.5, 0.05)
    binarizer = Binarizer(threshold=threshold)
    pre_bin_image = img_array[None, :, :]
    binarized_image = binarizer.fit_transform(pre_bin_image)
    st.write(binarizer.plot(binarized_image))

    RADIAL_FILTRATION = 'Radial'
    DENSITY_FILTRATION = 'Density'
    filtrations = (RADIAL_FILTRATION, DENSITY_FILTRATION)

    if st.checkbox('Apply filtration'):
        filtration = st.selectbox('Choose filtration', filtrations)
        if filtration == RADIAL_FILTRATION:
            pass
        elif filtration == DENSITY_FILTRATION:
            radius = st.number_input('Enter radius', value=3.0, step=0.1)
            # st.text('This operation may take a while to run. Click "Generate" to view the filtration')
            # if st.button('Generate'):
            density_filtration = DensityFiltration(radius=radius)
            density_filtered_image = density_filtration.fit_transform(binarized_image)
            filtered_image = density_filtration.plot(density_filtered_image, colorscale="jet")
            st.write(filtered_image)