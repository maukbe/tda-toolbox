import streamlit as st
import numpy as np
import os
from gtda.plotting import plot_heatmap
from PIL import Image
import matplotlib 
from gtda.images import Binarizer
from filtrations import create_filtration, Filtration, plot_filtration
from gtda.homology import CubicalPersistence
from gtda.diagrams import HeatKernel

st.title('TDA Toolbox')

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png"]) 

if uploaded_file:
    image = Image.open(uploaded_file)
    img_array = np.array(image)
    heatmap = plot_heatmap(img_array)
    st.write(heatmap)

    threshold = st.slider('Threshold', 0.0, 1.0, 0.5, 0.05)
    binarizer = Binarizer(threshold=threshold)
    pre_bin_image = img_array[None, :, :]
    binarized_image = binarizer.fit_transform(pre_bin_image)
    st.write(binarizer.plot(binarized_image))

    filtration_name = st.selectbox('Choose filtration', [filtration.value for filtration in list(Filtration)])
    filtration = create_filtration(filtration_name, binarized_image)
    plot_filtration(filtration, binarized_image)

    # Persistance
    cubical_persistence = CubicalPersistence()
    inage_cubical = cubical_persistence.fit_transform(filtration.fit_transform(binarized_image))

    st.write(cubical_persistence.plot(inage_cubical))

    # Heat Kernel
    sigma = st.slider('Sigma', 0.0,1.0,0.5,0.05)
    bins = st.slider('Bins', 0,1000, 50, 10)
    heat = HeatKernel(sigma=sigma, n_bins=bins, n_jobs=-1)
    heat_image = heat.fit_transform(inage_cubical)

    # Visualise the heat kernel for H1
    st.write(heat.plot(heat_image, homology_dimension_idx=1, colorscale='jet'))
