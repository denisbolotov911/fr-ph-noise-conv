# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 09:54:22 2025

@author: Denis Bolotov
"""

import streamlit as st
import numpy as np

# Define delay time for 1 meter fiber delay line
delay_line_length = 1  # meter
tau = delay_line_length * 5e-9  # seconds

# Conversion Functions
def freq_noise_to_phase_noise(freq_noise_sqrt):
    S_nu = freq_noise_sqrt ** 2  # Hz^2/Hz
    S_phi_differ = ((2 * np.pi * tau) ** 2) * S_nu  # rad^2/Hz
    return np.sqrt(S_phi_differ) * 1e6  # μrad/√Hz

def phase_noise_to_freq_noise(phase_noise_micro_rad_differ):
    S_phi_differ = (phase_noise_micro_rad_differ * 1e-6) ** 2  # rad^2/Hz
    S_nu = S_phi_differ / ((2 * np.pi * tau) ** 2)  # Hz^2/Hz
    return np.sqrt(S_nu)  # Hz/√Hz

def freq_noise_to_freq_noise_psd(freq_noise_sqrt):
    return freq_noise_sqrt ** 2  # Hz^2/Hz

def freq_noise_psd_to_freq_noise(freq_noise_psd):
    return np.sqrt(freq_noise_psd)  # Hz/√Hz

def freq_psd_to_phase_noise(freq_noise_psd):
    S_phi_differ = ((2 * np.pi * tau) ** 2) * freq_noise_psd  # rad^2/Hz
    return np.sqrt(S_phi_differ) * 1e6  # μrad/√Hz

def phase_noise_to_db(phase_noise_micro_rad_differ):
    S_phi_differ = (phase_noise_micro_rad_differ * 1e-6) ** 2  # rad^2/Hz
    return 10 * np.log10(S_phi_differ)  # dB(rad^2/Hz)

def db_to_phase_noise(phase_noise_db):
    S_phi_differ = 10 ** (phase_noise_db / 10)  # rad^2/Hz
    return np.sqrt(S_phi_differ) * 1e6  # μrad/√Hz

def freq_noise_to_phase_noise_db(freq_noise_sqrt):
    S_nu = freq_noise_sqrt ** 2  # Hz^2/Hz
    S_phi_differ = ((2 * np.pi * tau) ** 2) * S_nu  # rad^2/Hz
    return 10 * np.log10(S_phi_differ)  # dB(rad^2/Hz)

def freq_psd_to_phase_noise_db(freq_noise_psd):
    S_phi_differ = ((2 * np.pi * tau) ** 2) * freq_noise_psd  # rad^2/Hz
    return 10 * np.log10(S_phi_differ)  # dB(rad^2/Hz)

def db_to_freq_noise(phase_noise_db):
    S_phi_differ = 10 ** (phase_noise_db / 10)  # rad^2/Hz
    S_nu = S_phi_differ / ((2 * np.pi * tau) ** 2)  # Hz^2/Hz
    return np.sqrt(S_nu)  # Hz/√Hz

def db_to_freq_noise_psd(phase_noise_db):
    S_phi_differ = 10 ** (phase_noise_db / 10)  # rad^2/Hz
    return S_phi_differ / ((2 * np.pi * tau) ** 2)  # Hz^2/Hz

# Streamlit App
st.title("Frequency/Phase Noise Converter Tool")
st.markdown("### Convert between Frequency and Phase Noise Metrics")
st.info("Ensure input values are for a 1-meter delay line.")

# Unit Options
units = ["Frequency Noise [Hz/√Hz]", "Frequency Noise [Hz²/Hz]",
         "Phase Noise [μrad/√Hz]", "Phase Noise [dB (rad/√Hz)]"]

# Input Unit Dropdown
input_unit = st.selectbox("Select Input Unit:", units)

# Output Unit Dropdown (excluding the selected input unit)
output_options = [unit for unit in units if unit != input_unit]
output_unit = st.selectbox("Select Output Unit:", output_options)

# Dynamic Input Field: Allow negative input only for dB
if input_unit == "Phase Noise [dB (rad/√Hz)]":
    input_value = st.number_input("Enter the value to convert:", format="%.2f")
else:
    input_value = st.number_input("Enter the value to convert:", min_value=0.0, format="%.2f")

# Full Conversion Logic
if st.button("Convert"):
    if input_unit == "Frequency Noise [Hz/√Hz]" and output_unit == "Phase Noise [μrad/√Hz]":
        result = freq_noise_to_phase_noise(input_value)
    elif input_unit == "Frequency Noise [Hz/√Hz]" and output_unit == "Frequency Noise [Hz²/Hz]":
        result = freq_noise_to_freq_noise_psd(input_value)
    elif input_unit == "Frequency Noise [Hz²/Hz]" and output_unit == "Frequency Noise [Hz/√Hz]":
        result = freq_noise_psd_to_freq_noise(input_value)
    elif input_unit == "Frequency Noise [Hz²/Hz]" and output_unit == "Phase Noise [μrad/√Hz]":
        result = freq_psd_to_phase_noise(input_value)
    elif input_unit == "Frequency Noise [Hz/√Hz]" and output_unit == "Phase Noise [dB (rad/√Hz)]":
        result = freq_noise_to_phase_noise_db(input_value)
    elif input_unit == "Frequency Noise [Hz²/Hz]" and output_unit == "Phase Noise [dB (rad/√Hz)]":
        result = freq_psd_to_phase_noise_db(input_value)
    elif input_unit == "Phase Noise [μrad/√Hz]" and output_unit == "Frequency Noise [Hz/√Hz]":
        result = phase_noise_to_freq_noise(input_value)
    elif input_unit == "Phase Noise [μrad/√Hz]" and output_unit == "Phase Noise [dB (rad/√Hz)]":
        result = phase_noise_to_db(input_value)
    elif input_unit == "Phase Noise [dB (rad/√Hz)]" and output_unit == "Phase Noise [μrad/√Hz]":
        result = db_to_phase_noise(input_value)
    elif input_unit == "Phase Noise [dB (rad/√Hz)]" and output_unit == "Frequency Noise [Hz/√Hz]":
        result = db_to_freq_noise(input_value)
    elif input_unit == "Phase Noise [dB (rad/√Hz)]" and output_unit == "Frequency Noise [Hz²/Hz]":
        result = db_to_freq_noise_psd(input_value)
    else:
        result = "Conversion not available."

    st.success(f"Result: {result:.3e} {output_unit}")

