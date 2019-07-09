
clear
clc
close all
addpath('/home/jkocz/casper/ssb_noise_tests')

%this code generates randomized inputs for testing SSB

%generate time

nTimeSteps=100000;
latency=11;

time=(0:(nTimeSteps-1)).';

din_prototype.time=time;
din_prototype.signals.values=zeros(nTimeSteps,1);

kindThisCoeffs='PhaseMag';
kindThisData='PhaseMag';

simin_c1=din_prototype;
simin_c2=din_prototype;
simin_c3=din_prototype;
simin_c4=din_prototype;
simin_fft_out0=din_prototype;
simin_fft_out8=din_prototype;

simin_c1.signals.values(:)=generateComplexRandominput(nTimeSteps,kindThisCoeffs);
simin_c2.signals.values(:)=generateComplexRandominput(nTimeSteps,kindThisCoeffs);
simin_c3.signals.values(:)=generateComplexRandominput(nTimeSteps,kindThisCoeffs);
simin_c4.signals.values(:)=generateComplexRandominput(nTimeSteps,kindThisCoeffs);
simin_fft_out0.signals.values(:)=generateComplexRandominput(nTimeSteps,kindThisData);
simin_fft_out8.signals.values(:)=generateComplexRandominput(nTimeSteps,kindThisData);


sim('dsp_test_v01',time);

out_expec12=simin_c1.signals.values.*simin_fft_out0.signals.values + simin_c2.signals.values.*simin_fft_out8.signals.values;
out_expec34=simin_c3.signals.values.*simin_fft_out0.signals.values + simin_c4.signals.values.*simin_fft_out8.signals.values;

out_act12=simout_12.signals.values;
out_act34=simout_34.signals.values;


out_expec_cat=[out_expec12 out_expec34];
out_act_cat=[out_act12 out_act34];

out_expec_shifted=out_expec_cat(1:(end-latency),:);
out_act_shifted=out_act_cat(latency+1:end,:);

out_err=out_act_shifted-out_expec_shifted;

err_rms=rms(out_err(:));
expec_rms=rms(out_expec_shifted(:));

err_relative=err_rms/expec_rms

%%
figure;
s=subplot(3,1,1);
plot(abs(out_expec_shifted));
title('expec')

s(2)=subplot(3,1,2);
plot(abs(out_act_shifted));
title('act')

s(3)=subplot(3,1,3);
plot(abs(out_err));
title('error')

linkaxes(s,'x')
