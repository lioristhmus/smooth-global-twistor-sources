# Computational supplement to Global wave completion and recognition of smooth twistor sources

Manuscript version 1.0 · 22 November 2026

Three finite calculations test signs and normalizations used in the [paper](../paper/smooth-global-twistor-sources-en-v1.0.md). All equalities are evaluated over integers, a quadratic ring or rational numbers. The [inputs](inputs.json), [calculations](check.py) and [recorded output](results/verified.json) accompany this guide. The code was written for this paper. It imports neither the local manuscript's computations nor their recorded results.

## 1. Translated kernels on the flat torus (Example 4.7)

**Question.** Which identities of the remote bisolution survive Fourier truncation? Use $L=2\pi$, $a=\pi/3$, $s=t_p-x_p^1-t_q+x_q^1$. The circle delta has Fourier coefficient $1/L$. Thus $LK_N(s)=\sum_{|n|\le N}c_n e^{ins}$, where $c_n=z^n+z^{-n}$ and $z=e^{i\pi/3}$. The program evaluates this expression using $z^2=z-1$ and independently compares it with the six periodic integer weights.

**Tests.** The frequency vector for each mode is $(n,-n,-n,n)$ in the variables $(t_p,x_p^1,t_q,x_q^1)$. Both wave symbols must annihilate it. Transposition reverses $n$ and must preserve the coefficient. On the slice $t_p=t_q=0$, after removing the common factor $e^{in(y^1-x^1)}/L$, the coefficients of the field–field, normal–field, field–normal and normal–normal traces must be $(c_n,inc_n,-inc_n,n^2c_n)$. In each saved row the first entry is $n$; the two single-normal entries are the multipliers of $i$. Both normal derivatives use the future unit normal. The two first derivatives must be exchanged by transposition. The controls double the first spatial frequency at $n=1$ and reverse the sign of the second normal trace.

| Cutoff $N$ | Number of modes | $LK_N(0)$ | Erroneous first wave symbol at $n=1$, including $c_1$ |
| --- | ---: | ---: | ---: |
| 1 | 3 | 4 | 3 |
| 2 | 5 | 2 | 3 |
| 4 | 9 | −4 | 3 |

Each finite sum satisfies the two wave equations and is symmetric. Its nonzero diagonal value witnesses the loss of support localization under truncation. The distributional kernel in Example 4.7 vanishes near the diagonal because its two translated delta hypersurfaces miss that neighborhood. Off-diagonal singularities and the global wavefront obstruction are properties of the distributional example; finite trigonometric polynomials are smooth everywhere. These tests do not decide uniqueness in Theorem 4.4.

## 2. Mixed traces and evaluation (Theorems 5.3 and 5.5)

**Question.** Is the middle inverse in the mixed composition required, and do the same normalizers transport a point evaluation? Use three real two-dimensional spaces in orthonormal coordinates, with transpose for the physical adjoint. For each carrier let $D_a$ be the positive diagonal scale and $O_a$ the rational rotation given in the input. A triple $(x,y,d)$ represents the matrix with rows $(x,-y)/d$ and $(y,x)/d$. Put $H=\operatorname{diag}(2,3)$, $R=H^2$, $E_a=D_aO_aH$ and $C_{ab}=E_aR^{-1}E_b^T$. Then $C_a=C_{aa}=D_a^2$ and the positive inverse root is $W_a=D_a^{-1}$. The point slot is represented by the column $v=(2,-3)^T$, so $e_a=W_a E_a R^{-1}v$.

**Tests.** Form $T_{ab}=W_aC_{ab}W_b$ and compare it with the independent expression $O_aO_b^T$. For every ordered triple verify $C_{ab}C_b^{-1}C_{bc}=C_{ac}$ and $T_{ab}T_{bc}=T_{ac}$. For every ordered pair verify the adjoint inverse and $T_{ab}e_b=e_a$. In all, 27 triples and nine ordered pairs pass. In the stored zero-based indexing, $T_{02}$ has rows $(5,-12)/13$ and $(12,5)/13$, and $e_0=(1,-1)^T$. Dropping the middle inverse fails on the triple $(0,1,2)$. Applying $C_{01}$ directly to the normalized evaluation at carrier 1 also fails.

This is the finite matrix factorization in the proofs. The microlocal calculus, proper support, complex-linear internal adjoint, and the connection on all sections require the arguments in §5.

## 3. Change of frame in the analytic interface (Lemma 16.2)

**Question.** When the factor frame is replaced by $u\nu$, which coefficient keeps its calibrated image fixed, and what sign does its logarithmic derivative have? Work at $x=0$ with $u(x)=-2+3x$ and a constant old interface coefficient $f=5$. Independently solve $uF_{\rm new}=f$ to first order by multiplying first jets. This gives $F_{\rm new}(0)=-5/2$ and $F'_{\rm new}(0)=-15/4$. The product jet is $(5,0)$, and the logarithmic derivative is $3/2$, equal to $-u'(0)/u(0)$.

Keeping the old coefficient violates the calibrated value. Reversing the sign of the connection term gives a nonzero derivative of the product. This checks the scalar change of frame on a nonvanishing real analytic germ at one point. It assumes that the calibrated source and the original frame have been supplied. It does not construct a holomorphic interface, a global root, or a descent isomorphism.

## Reproduction and integrity

The recorded run used CPython 3.12.13 (standard library) on Linux aarch64, with the locally installed Docker image ID given in the result. All mathematical calculations, including the cutoff-one pilot, ran inside one foreground container. The pilot's peak RSS was 16,824 KiB; after the remaining cases it was 16,948 KiB. Elapsed time in the JSON measures the calculations inside the container. Resource measurements and the VM service snapshot vary between runs; the entries under **results** are deterministic.

The recorded image is `python@sha256:d50fb7611f86d04a3b0471b46d7557818d88983fc3136726336b2a4c657aa30b` for `linux/arm64` (Python 3.12 slim, Debian Bookworm). With this image installed in Docker and cgroup v2 available, run the commands below from this directory. Use one shared account and lock for all jobs on the host. Choose a fresh output path. The [launcher](run.py) refuses to overwrite an existing result or take an occupied lock. It records the VM limits and existing service usage, enforces a 60-second foreground execution deadline, checks the Docker configuration, and confirms termination before releasing the common lock. Inside the container the [job entry point](job.py) verifies the effective cgroup limits before running the pilot: 128 MiB memory, zero additional swap, half a CPU and 32 processes. The container has no network, a read-only root, a 1 MiB temporary filesystem for the input, bounded logs, OOM termination enabled and no restart.

~~~sh
python3 run.py results/replay.json
shasum -a 256 -c SHA256SUMS
~~~

Compare the two JSON files' **results** objects for replay agreement. The manifest covers the recorded guide, code, inputs and original result. The original result file was saved at 2026-11-22T06:20:09Z (filesystem modification time, UTC). The recorded duration measures elapsed computation time. The service snapshot retains resource readings with service names omitted. The paper's theorem statements and proofs give the corresponding general assertions.

