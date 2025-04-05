import numpy as np
import simpleaudio as sa
from enum import Enum

class NoteFrequencies(Enum):
    C4 = 261.63
    D4 = 293.66
    E4 = 329.63
    G4 = 392.00
    A4 = 440.00

def generate_note_wave(frequency, duration=0.5, sample_rate=44100):
    """Generate a bluesy waveform for a given frequency"""
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    
    # Create a bluesy waveform with harmonics
    wave = 0.5 * np.sin(2 * np.pi * frequency * t)
    wave += 0.3 * np.sin(2 * np.pi * frequency * 1.5 * t)  # Blues third
    wave += 0.2 * np.sin(2 * np.pi * frequency * 2 * t)    # Octave
    
    # Apply envelope
    envelope = np.concatenate([
        np.linspace(0, 1, int(0.1 * sample_rate)),
        np.ones(int(0.6 * sample_rate)),
        np.linspace(1, 0, int(0.3 * sample_rate))
    ])
    wave = wave[:len(envelope)] * envelope
    
    # Normalize and convert to 16-bit
    wave *= 32767 / np.max(np.abs(wave))
    return wave.astype(np.int16)

def play_solid_note(solid_name):
    """Play the corresponding note for a Platonic solid"""
    note_map = {
        "Tetrahedron": NoteFrequencies.C4,
        "Cube": NoteFrequencies.D4,
        "Octahedron": NoteFrequencies.E4,
        "Dodecahedron": NoteFrequencies.G4,
        "Icosahedron": NoteFrequencies.A4
    }
    
    if solid_name in note_map:
        frequency = note_map[solid_name].value
        wave = generate_note_wave(frequency)
        play_obj = sa.play_buffer(wave, 1, 2, 44100)
        return play_obj
    return None