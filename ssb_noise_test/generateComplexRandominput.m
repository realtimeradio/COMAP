function out = generateComplexRandominput(nSamples, kind)
%generates nSamples of random values in the range -1,1.  complex.  kind
%determines the distribution of samples.

range=0.5;
if strcmp(kind,'RealImag')
    realPart=unifrnd(-range,range,nSamples,1);
    imagPart=unifrnd(-range,range,nSamples,1);
    out=realPart+1j*imagPart;
    
elseif strcmp(kind,'PhaseMag')
    powsLog=unifrnd(-5,log10(range),nSamples,1);
    phases=unifrnd(0,2*pi,nSamples,1);
    out=10.^powsLog.*exp(1j*phases);
else error('RYAN ANGRY');end