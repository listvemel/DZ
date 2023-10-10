import wave
import struct

input_file = "in.wav"
output_file = "output.wav"
slowdown_factor = int(input())
inp_wave = wave.open(input_file, 'rb')
out_wave = wave.open(output_file, 'wb')

num_channels = inp_wave.getnchannels()
sample_width = inp_wave.getsampwidth()
frame_rate = inp_wave.getframerate()
num_frames = inp_wave.getnframes()

out_wave.setnchannels(num_channels)
out_wave.setsampwidth(sample_width)
out_wave.setframerate(frame_rate // slowdown_factor) 
out_wave.setnframes(num_frames * slowdown_factor)  

for _ in range(num_frames):
    frame = inp_wave.readframes(1)  
    for _ in range(slowdown_factor):
        out_wave.writeframes(frame)  

print(output_file)