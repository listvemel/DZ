import wave
import struct

input_file = "in.wav"
output_file = "output.wav"
volume_multiplier = float(input()) #если число > 1, то аудио становится громче, а если < 1, то тише
inp_wave = wave.open(input_file, 'rb')
out_wave = wave.open(output_file, 'wb')

num_channels = inp_wave.getnchannels()
sample_width = inp_wave.getsampwidth()
frame_rate = inp_wave.getframerate()
num_frames = inp_wave.getnframes()

out_wave.setnchannels(num_channels)
out_wave.setsampwidth(sample_width)
out_wave.setframerate(frame_rate)
out_wave.setnframes(num_frames)

min_amplitude = -32768
max_amplitude = 32767

for _ in range(num_frames):
    frame = inp_wave.readframes(1)
    unpacked_frame = struct.unpack("<h", frame)
    new_amplitude = int(unpacked_frame[0] * volume_multiplier)
    new_amplitude = max(min_amplitude, min(max_amplitude, new_amplitude))
    new_frame = struct.pack("<h", new_amplitude)
    out_wave.writeframes(new_frame)

print(output_file)