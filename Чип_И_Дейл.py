import wave
import struct

input_file = "in.wav"
output_file = "output.wav"
inp_wave = wave.open(input_file, 'rb')
out_wave = wave.open(output_file, 'wb')

num_channels = inp_wave.getnchannels()
sample_width = inp_wave.getsampwidth()
frame_rate = inp_wave.getframerate()
num_frames = inp_wave.getnframes()

out_wave.setnchannels(num_channels)
out_wave.setsampwidth(sample_width)
out_wave.setframerate(frame_rate * 2)
out_wave.setnframes(num_frames // 2)

for _ in range(num_frames // 2):
    frame = inp_wave.readframes(2)
    out_wave.writeframes(frame)

inp_wave.close()
out_wave.close()

print(output_file)