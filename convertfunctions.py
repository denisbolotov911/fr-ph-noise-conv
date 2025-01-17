# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 14:57:12 2025

@author: Denis Bolotov
"""

import numpy as np

# Define delay time for 1 meter fiber delay line
delay_line_length = 1  # meter
tau = delay_line_length * 5e-9  # seconds

# ============================
# Frequency Noise ↔ Phase Noise
# ============================

def freq_noise_sqrt_to_phase_noise_sqrt(freq_noise_sqrt):
    """Convert Frequency Noise [Hz/√Hz] → Phase Noise [μrad/√Hz]"""
    S_nu = freq_noise_sqrt ** 2  # Hz²/Hz
    S_phi_differ = ((2 * np.pi * tau) ** 2) * S_nu  # rad²/Hz
    return np.sqrt(S_phi_differ) * 1e6  # μrad/√Hz

def phase_noise_sqrt_to_freq_noise_sqrt(phase_noise_micro_rad_sqrt):
    """Convert Phase Noise [μrad/√Hz] → Frequency Noise [Hz/√Hz]"""
    S_phi_differ = (phase_noise_micro_rad_sqrt * 1e-6) ** 2  # rad²/Hz
    S_nu = S_phi_differ / ((2 * np.pi * tau) ** 2)  # Hz²/Hz
    return np.sqrt(S_nu)  # Hz/√Hz

def freq_noise_to_phase_noise_sqrt(freq_noise_psd):
    """Convert Frequency Noise [Hz²/Hz] → Phase Noise [μrad/√Hz]"""
    S_phi_differ = ((2 * np.pi * tau) ** 2) * freq_noise_psd  # rad²/Hz
    return np.sqrt(S_phi_differ) * 1e6  # μrad/√Hz

def phase_noise_sqrt_to_freq_noise(phase_noise_micro_rad_sqrt):
    """Convert Phase Noise [μrad/√Hz] → Frequency Noise [Hz²/Hz]"""
    S_phi_differ = (phase_noise_micro_rad_sqrt * 1e-6) ** 2  # rad²/Hz
    return S_phi_differ / ((2 * np.pi * tau) ** 2)  # Hz²/Hz

# ================================
# Frequency Noise ↔ dB Phase Noise
# ================================

def freq_noise_sqrt_to_phase_noise_db(freq_noise_sqrt):
    """Convert Frequency Noise [Hz/√Hz] → Phase Noise [dB (rad/√Hz)]"""
    S_nu = freq_noise_sqrt ** 2  # Hz²/Hz
    S_phi_differ = ((2 * np.pi * tau) ** 2) * S_nu  # rad²/Hz
    return 10 * np.log10(S_phi_differ)  # dB(rad²/Hz)

def freq_noise_to_phase_noise_db(freq_noise_psd):
    """Convert Frequency Noise [Hz²/Hz] → Phase Noise [dB (rad/√Hz)]"""
    S_phi_differ = ((2 * np.pi * tau) ** 2) * freq_noise_psd  # rad²/Hz
    return 10 * np.log10(S_phi_differ)  # dB(rad²/Hz)

def phase_noise_db_to_freq_noise_sqrt(phase_noise_db):
    """Convert Phase Noise [dB (rad/√Hz)] → Frequency Noise [Hz/√Hz]"""
    S_phi_differ = 10 ** (phase_noise_db / 10)  # rad²/Hz
    S_nu = S_phi_differ / ((2 * np.pi * tau) ** 2)  # Hz²/Hz
    return np.sqrt(S_nu)  # Hz/√Hz

def phase_noise_db_to_freq_noise(phase_noise_db):
    """Convert Phase Noise [dB (rad/√Hz)] → Frequency Noise [Hz²/Hz]"""
    S_phi_differ = 10 ** (phase_noise_db / 10)  # rad²/Hz
    return S_phi_differ / ((2 * np.pi * tau) ** 2)  # Hz²/Hz

# ================================
# Phase Noise ↔ dB Phase Noise
# ================================

def phase_noise_sqrt_to_phase_noise_db(phase_noise_micro_rad_sqrt):
    """Convert Phase Noise [μrad/√Hz] → Phase Noise [dB (rad/√Hz)]"""
    S_phi_differ = (phase_noise_micro_rad_sqrt * 1e-6) ** 2  # rad²/Hz
    return 10 * np.log10(S_phi_differ)  # dB(rad²/Hz)

def phase_noise_db_to_phase_noise_sqrt(phase_noise_db):
    """Convert Phase Noise [dB (rad/√Hz)] → Phase Noise [μrad/√Hz]"""
    S_phi_differ = 10 ** (phase_noise_db / 10)  # rad²/Hz
    return np.sqrt(S_phi_differ) * 1e6  # μrad/√Hz

# ================================
# Frequency Noise ↔ Frequency Noise
# ================================

def freq_noise_sqrt_to_freq_noise(freq_noise_sqrt):
    """Convert Frequency Noise [Hz/√Hz] → Frequency Noise [Hz²/Hz]"""
    return freq_noise_sqrt ** 2  # Hz²/Hz

def freq_noise_to_freq_noise_sqrt(freq_noise_psd):
    """Convert Frequency Noise [Hz²/Hz] → Frequency Noise [Hz/√Hz]"""
    return np.sqrt(freq_noise_psd)  # Hz/√Hz


