# Wave kernels on Kasner and torus backgrounds

These computations accompany Paper 4, Lior Isthmus, *Global wave completion and recognition of smooth twistor sources*, v1.0. They follow scalar waves across Cauchy surfaces, separate the two time-frequency branches, detect a singularity away from the diagonal and compare three presentations of the same spacetime. [Paper v1.0](https://doi.org/10.5281/zenodo.24443685)

### 4.1 · Surface transport on Kasner spacetime

§5, Definitions 5.1 and 5.4, and Theorems 5.3 and 5.5. The spatial torus has period 2π and Kasner exponents (−1/3, 2/3, 2/3). The signature is +−−−, the future normal is ∂t and the spatial volume is t dx. Along an axis of exponent p, put z = |k|t^(1−p)/(1−p). The field sqrt(π/[4(1−p)]) H₀⁽²⁾(z) has a past temporal covector and Klein–Gordon charge +1. Apply the normal derivative before multiplying by sqrt(t). Writing zₐ = sqrt(tₐ)f(tₐ), the mixed trace is zₐ conjugate(zᵦ) and its diagonal normalizer is 1/|zₐ|.

The 16 signed modes cover two axes and |k| = 1, 2, 4, 8. Opposite spatial signs share a temporal ODE. RK4 and the Hankel expression start from the same Cauchy data. The first test compares the evolved and analytic amplitudes, traces and normalizers at t = 1, 1.5, 2. Its rank-one composition identities follow algebraically from the mode products. All four physical trace combinations are recorded per mode. The aggregate refinement norm uses the other observables. Dropping the half-density changes the diagonal, and conjugating the time branch changes the phase and charge. [Evolution](code/kasner/evolve.py) · [Hankel solution](code/kasner/hankel.py) · [Observables and controls](code/kasner/kasner.py) · [Transport tables](reference/kasner/kasner/results.json)

A second test restarts the numerical evolution on each emitting surface. At its finest step the phase error against Hankel is 2.06e−6. At the off-surface point (t, x) = (1.25, 0.37), the **point-evaluation error against Hankel is 2.41e−8**. The covariance residual comparing the transported numerical evaluation with the receiving surface's numerical evaluation is 3.08e−9. The three-surface composition discrepancy is 2.48e−7. The last two measurements compare independently stepped intervals within this numerical transport. [Interval implementation](code/kasner/return_paths.py) · [Refinement results](reference/kasner/return_paths/results.json)

### 4.2 · Localizing the time-frequency branch

Theorems 4.4–4.5. On the circle the selected series has coefficient 1/(2n) at frequency −n, n ≥ 1. A smooth compact window χ localizes it near zero. Smoothness gives rapid decay on the opposite side and the selected side has leading term χ(0)/(2k). We sample k = 8, 16, 32, 64, 128, 256 and compare with the conjugate branch and an added smooth series with coefficients exp(−√n)/(2n). At k = 256 on the finest grid, the selected coefficient has magnitude 0.0019532, opposite-side leakage is 5.77e−9 and the smooth addition contributes 3.48e−9. The extra sum uses the **same discrete window and convolution** with a longer frequency cutoff. Its 9.59e−9 relative difference measures truncation sensitivity. On two Kasner axes a window in optical time compares the Hankel mode with its conjugate against the same oscillation. At k = 256 the opposite-to-matched ratios are 1.16e−5 and 1.15e−5. These are finite-band observations of the predicted orientation. [Window and convolution](code/wave/waves.py) · [Frequency tables](reference/wave/waves/results.json)

### 4.3 · Detecting singularities away from the diagonal

Example 4.7. Place the two shifts at ±1.2 on the flat circle. The action of the two translated deltas on a test function ψ is ψ(1.2) + ψ(−1.2). This gives independent distributional values of 0, 1.2 and 1 for the tests near the diagonal, positive shift and negative shift, respectively. At cutoff 256 the numerical pairing errors are 1.05e−7, 3.95e−6 and 3.46e−7. A finite sum can have values across the entire circle. Its pairings with smooth tests are the quantities that converge to the delta action. [Shift tests](code/wave/waves.py) · [Pairing table](reference/wave/waves/results.json) · [Partial sums at three cutoffs](reference/wave/waves/remote.svg)

On the two Kasner axes, modes propagated by RK4 from t = 1 are compared at t = 1.23 with a finite 768-mode Hankel sum using the same initial branch and test functions. At cutoff 256 the greatest pairing differences are 9.65e−7 and 1.07e−6. Reversing the propagated branch gives 0.88 and 0.97. The separate Brinkmann plane-wave example illustrates a characteristic identity. A profile depending only on u solves the wave equation in this metric, and the chosen ray with initial du/ds = 0 stays at constant u. Both zero residuals follow from that choice. [Kasner evolution and reference](code/wave/curved.py) · [Curved pairing table](reference/wave/curved/results.json)

### 4.4 · Comparing three coordinate presentations

§§5 and 7. Three overlapping slabs use the same Kasner torus, point identification, axial k = 4 scalar mode and Hankel branch. The initial times are 1, 1.5 and 2. Each run evolves the scale factors, expansion rates, wave and axial ray from its own initial surface. The affine clocks reparametrize the same ODE. Spatial shears and translations enter the coordinate formulas, and the free initial phase of each mode cancels from its kernel. The coordinate change around a triple overlap and the initial volume densities agree algebraically.

At 64 steps, the discrepancies between these separately initialized runs are 5.73e−10 in the pulled-back metric, 7.25e−11 in the two-point kernel, 1.49e−8 in the mixed-trace evaluation comparison and 1.08e−6 in normalized triple transport. The curvature readout uses the evolved expansion rates. At t = 1.27 its difference from the exact Kretschmann scalar 64/(27t⁴) for the middle initialization is 1.28e−12. Omitting the coordinate change gives a metric discrepancy of 1.38 for the chosen charts. This comparison concerns the scalar mode on these slabs. Spin lifts, general module comparisons and recognition of arbitrary atlases belong to the paper's broader setting. [Chart equations and comparisons](code/wave/atlas.py) · [Four refinement levels](reference/wave/atlas-traces/results.json)

## Reproduce from the archive

Use a POSIX host with Python 3.10 or later, Docker CLI and a local Linux Docker engine with cgroup v2, a shared bind-mount directory and at least 2 GiB of VM memory. The host runner uses only the Python standard library. Start Docker first. With network access, obtain the public runtime images by immutable digest:

```sh
docker pull --platform linux/amd64 sagemath/sagemath@sha256:e068670ae5863b54b2550e72437ec637b0283acb0dc712c8584c124dbf44e667
docker pull --platform linux/arm64 python@sha256:d50fb7611f86d04a3b0471b46d7557818d88983fc3136726336b2a4c657aa30b
```

The SageMath 10.9 image supplies Linux x86-64 Python 3.12.3, NumPy 2.4.4, SciPy 1.17.1 and Matplotlib 3.10.8. The two Kasner transport jobs use the Linux ARM64 Python 3.12.13 image and its system math library. The remaining jobs use SageMath. The tested host used Docker on macOS with Linux image emulation available. Enable emulation for any required non-native architecture. Different architectures, libraries and independently rebuilt images may produce different floating-point bytes; the exact-output test below applies to the pinned environments.

On a host with existing background services, identify them with `docker ps`. For each running container that you have checked is an unrelated background service, put its name in the space-separated `MATH_BACKGROUND_SERVICES` environment variable. For example, for two verified background services named svc1 and svc2, use `export MATH_BACKGROUND_SERVICES="svc1 svc2"`. The default is empty. An unlisted running workload stops the run. All cooperating mathematics jobs on the machine must use the same atomic directory lock, `~/.local/state/math-job.lock`, under one shared execution account. The runner records ownership, checks live VM and cgroup limits and releases the lock after confirming container termination. Each foreground computation runs offline with at most one CPU, no swap, 1,200 MiB memory or less, 48 PIDs and a ten-minute limit; temporary storage and logs are bounded.

Place the ZIP and its matching .zip.sha256 file together in a new, otherwise empty directory. From there, after obtaining the required images, run the following command chain. Extraction proceeds only if the external SHA-256 check succeeds.

```sh
shasum -a 256 -c paper4-global-wave-additional-computations-2026-11-24-r2.zip.sha256 &&
unzip paper4-global-wave-additional-computations-2026-11-24-r2.zip &&
python3 paper4-global-wave-additional-computations-2026-11-24-r2/reproduce.py results
```

The runner first verifies the unpacked manifest. It creates a fresh sibling output directory and executes the ordered dependency list in [jobs.json](jobs.json). To run again, use a new output directory name. Inputs to each job are generated in earlier stages or supplied by the experiment code; the saved reference results are used for comparison. The order is Kasner surface transport, the interval return test, localized branch and shift tests, curved propagation, then the three-chart comparison.

Expected terminal output is `PASS: 5 jobs, 54 scientific files`. The generated `results/verification.json` lists the matched file counts; each stage has a UTC execution receipt, live limits, logs and its scientific outputs. The [reference directory](reference) contains the measured numerical tables and figures. The [expected digests](expected-sha256.json) also cover regenerated intermediate data. Timestamps and resource counters are recorded separately from that comparison.

Copyright 2026 Lior Isthmus. See [licenses and attribution](LICENSES.md). This additional computation package accompanies the cited paper v1.0. Its date is 2026-11-24 UTC.
