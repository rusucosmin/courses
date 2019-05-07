import wave
from math import ceil
import numpy as np

byte_depth_to_dtype = {1: np.uint8, 2: np.uint16, 4: np.uint32, 8: np.uint64}

sound = wave.open('cosmin.rusu@epfl.ch.wav', "r")

num_channels = sound.getnchannels()
sample_width = sound.getsampwidth()
num_frames = sound.getnframes()
sound_frames = sound.readframes(num_frames)

bytes_to_recover = 2500000

def roundup(x, base=1):
    return int(ceil(x / base)) * base

def lsb_deinterleave_bytes(carrier, num_bits, num_lsb, byte_depth=1):
    plen = roundup(num_bits / num_lsb)
    carrier_dtype = byte_depth_to_dtype[byte_depth]
    payload_bits = np.unpackbits(
        np.frombuffer(carrier, dtype=carrier_dtype, count=plen).view(np.uint8)
    ).reshape(plen, 8 * byte_depth)[:, 8 - num_lsb:8]
    return np.packbits(payload_bits).tobytes()[:num_bits // 8]

data = lsb_deinterleave_bytes(sound_frames, 8 * bytes_to_recover, 1,
                              byte_depth=sample_width)

data = bytes(data)
i = data.find(bytes("COM402", 'utf-8'))

print(data[i:i+52])

