# 
# This file is released under terms of MIT License
# (C) 2017 - Ezhil Language Foundation
#
# This function will filter a given WAV file in frequency domain
# using the particular cutoff frequency.
# 
function wav_filter(wav_filename,f_cutoff)
if nargin < 1
    error('usage: wav_filter(wav_filename,{f_cutoff=10k})')
elseif nargin < 2
    f_cutoff = 10e3; %10k
end
    
[data,fs] = wavread(wav_filename);
%these windows de-emphasize the speech seriously must do some zero-padding before I guess
%hanning_w = hamming(length(data),"symmetric");
%plot(hanning_w)
window = ones(size(data));
source_energy = sum(abs(data.^2))/length(data);
q = fftshift(fft(data.*window));
qr = q(ceil(length(q)/2):end);
fr = linspace(0,fs/2,length(qr));
%plot(fr,abs(qr));
idx = find(fr > f_cutoff);
qr(idx(1):end) = 0; %freq domain filtering
qrec = real(ifft([qr; zeros(size(qr))]));
dest_energy = sum(abs(qrec.^2))/length(data);
gain = sqrt( source_energy/dest_energy );
qrec_amp = qrec*gain;
wavwrite(qrec_amp,fs,sprintf("filter_%d.wav",f_cutoff));
%wavwrite(qrec,fs,sprintf("filter_%d_nogain.wav",f_cutoff));
fprintf('done!\n');
end
