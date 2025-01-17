# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 14:57:12 2025

@author: Denis Bolotov
"""

import numpy as np

# Define delay time for 1 meter fiber delay line
delay_line_length = 1  # meter
tau = delay_line_length * 5e-9  # seconds

def freq_noise_to_phase_noise(freq_noise_sqrt):
    S_nu = freq_noise_sqrt ** 2  # Convert to Hz^2/Hz
    S_phi_differ = ((2 * np.pi * tau) ** 2) * S_nu  # Convert to rad^2/Hz
    return np.sqrt(S_phi_differ) * 1e6  # μrad/√Hz

def phase_noise_to_freq_noise(phase_noise_micro_rad_differ):
    S_phi_differ = (phase_noise_micro_rad_differ * 1e-6) ** 2  # rad^2/Hz
    S_nu = S_phi_differ / ((2 * np.pi * tau) ** 2)  # Hz^2/Hz
    return np.sqrt(S_nu)  # Hz/√Hz

def phase_noise_to_freq_noise_psd(phase_noise_micro_rad_differ):
    S_phi_differ = (phase_noise_micro_rad_differ * 1e-6) ** 2  # rad^2/Hz
    S_nu = S_phi_differ / ((2 * np.pi * tau) ** 2)  # Hz^2/Hz
    return S_nu  # Hz^2/Hz

def freq_noise_to_freq_noise_sqrt(S_nu):
    return np.sqrt(S_nu)  # Hz/√Hz

def freq_noise_sqrt_to_freq_noise(S_nu):
    return (S_nu)** 2  # Hz^2/Hz

def freq_psd_to_phase_noise(S_nu):
    S_phi_differ = ((2 * np.pi * tau) ** 2) * S_nu  # rad^2/Hz
    return np.sqrt(S_phi_differ) * 1e6  # μrad/√Hz

def phase_noise_to_db(phase_noise_micro_rad_differ):
    S_phi_differ = (phase_noise_micro_rad_differ * 1e-6) ** 2  # rad^2/Hz
    S_phi_db = 10 * np.log10(S_phi_differ)  # dB(rad^2/Hz)
    return S_phi_db

def db_to_phase_noise(phase_noise_db):
    S_phi_differ = 10 ** (phase_noise_db / 10)  # rad^2/Hz
    return np.sqrt(S_phi_differ) * 1e6  # μrad/√Hz

def freq_noise_to_phase_noise_db(freq_noise_sqrt):
    S_nu = freq_noise_sqrt ** 2  # Hz^2/Hz
    S_phi_differ = ((2 * np.pi * tau) ** 2) * S_nu  # rad^2/Hz
    S_phi_db = 10 * np.log10(S_phi_differ)  # dB(rad^2/Hz)
    return S_phi_db

def freq_psd_to_phase_noise_db(S_nu):
    S_phi_differ = ((2 * np.pi * tau) ** 2) * S_nu  # rad^2/Hz
    S_phi_db = 10 * np.log10(S_phi_differ)  # dB(rad^2/Hz)
    return S_phi_db

def db_to_freq_noise(phase_noise_db):
    S_phi_differ = 10 ** (phase_noise_db / 10)  # rad^2/Hz
    S_nu = S_phi_differ / ((2 * np.pi * tau) ** 2)  # Hz^2/Hz
    return np.sqrt(S_nu)  # Hz/√Hz

def db_to_freq_noise_psd(phase_noise_db):
    S_phi_differ = 10 ** (phase_noise_db / 10)  # rad^2/Hz
    S_nu = S_phi_differ / ((2 * np.pi * tau) ** 2)  # Hz^2/Hz
    return S_nu  # Hz^2/Hz

