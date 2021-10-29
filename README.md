# COMAP

This repository contains source code for the COMAP ROACH2 system

## Downloading

To download, clone this repository and its submodules:

```
git clone https://github.com/realtimeradio/comap
cd comap
git submodule init
git submodule update
```

This will obtain an appropriate `mlib_devel` version, against which
the FPGA designs in this repository have been compiled.

## Building

### Environment Configuration

Create a `startsg.local` environment file. An appropriate template (used
for compiling on `maze.caltech.edu`) is `startsg.local.maze`. This contains:

```
export XILINX_PATH=/data/Xilinx/14.7/ISE_DS
export MATLAB_PATH=/data/matlab-r2013b
export GAVRT_PATH=/home/jackh/src/comap/legacy_casper

export XILINX_PLATFORM=lin64
export CASPER_SKIP_STARTUP_M=1
export CASPER_USE_XILINX_CAST=1
```

Modify the first 3 lines with appropriate paths. The `legacy_casper`
GAVRT library is distributed as part of this repository.

The COMAP FPGA designs have been compiled using the following tool versions:

  - MATLAB R2013b
  - Xilinx ISE 14.7
  - Ubuntu 16.04.6 LTS

Other OS / tool versions may work, but haven't been tested.

### Loading FPGA Designs

1. Start simulink by running, at the top-level of this repository:

```
./startsg startsg.local
```

MATLAB will start and after a few moments the terminal will become responsive.

2. Load Xilinx System Generator

Empirical evidence is that System Generator can fail to load when used with
Ubuntu 16.04 (which is not an officially supported OS). To work around this,
a manual start script has been created to be run after MATLAB starts.

In the MATLAB prompt, execute:

```
>> runme
```

After a minute, System Generator will complete loading, and the MATLAB prompt will
once again become responsive.

### Loading FPGA Models

The COMAP ROACH2 Simulink model is `fpga_src/comap_v31.slx`.

This model compiles using the `casper_xps` flow, and meets timing at an ADC
sample rate of 4.28 GSamples/second. This corresponds to a "simulink" clock
rate of 267.5 MHz.

A manual change to the configuration of the FFT blocks in this design is necessary
if the FFTs are redrawn (for example, because of a library update using
`update_casper_blocks`). Without this change, the design won't quite meet timing.

Change the FFT stage 2 butterfly logic to use soft-logic, rather than DSP slices,
for its adders. This can be set manually using the Simulink dialog prompt, or
from the MATLAB prompt with the commands:

```
>> set_param([bdroot '/fft_wideband_real1/fft_biplex_real_4x/biplex_core/fft_stage_2'], 'dsp48_adders', 'off')
>> set_param([bdroot '/fft_wideband_real/fft_biplex_real_4x/biplex_core/fft_stage_2'], 'dsp48_adders', 'off')
```

## Changelog

The following modifications have been made to the `comap_v30.slx` design (compiled at 250 MHz) in order to meet timing at 267.5 MHz:

 1. Create new control environment variable `CASPER_USE_XILINX_CAST` and regenerate all blocks with this set to `1`, to avoid using CASPER custom cast logic.
 2. Set convert latency to `2` (was `1`) in FFT blocks.
 3. Turn off DSP48 adders in stage 2 of FFT blocks
 4. Add fanout registers to address lines of coefficient `cX_Y` RAM blocks, and compensate for latency change at `ssbX` inputs.
 5. Add fanout-control of `valid` GoTo blocks, providing 4 copies to drive downstream logic
 6. Change various small counters to implement in behavioural HDL
 7. Add `UCF` yellow block, to link placement constraints into CASPER build process.

None of these changes should have any functional effect on the design, though the total FFT latency has been somewhat increased.
