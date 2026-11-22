"""Exact finite specializations of Examples 4.7, Theorems 5.3/5.5 and Lemma 16.2."""
import json
from fractions import Fraction as Q
from pathlib import Path


def require(value, name):
    if not value:
        raise RuntimeError(name)


def sixth_root(n):
    # Coordinates of z^n in Z[z]/(z^2-z+1), z=exp(i*pi/3).
    a, b = 1, 0
    for _ in range(n % 6):
        a, b = -b, a + b
    return a, b


def torus(cfg):
    require((cfg["period"], cfg["shift"]) == ("2*pi", "pi/3"), "period and shift")
    results = []
    for cutoff in cfg["cutoffs"]:
        weights = {}
        traces = []
        for n in range(-cutoff, cutoff + 1):
            pos, neg = sixth_root(n), sixth_root(-n)
            c, b = pos[0] + neg[0], pos[1] + neg[1]
            require(b == 0, "shift pair is real")
            require(c == (2, 1, -1, -2, -1, 1)[n % 6], "translated delta weights")
            weights[n] = c
            # Ordered variables (t_p, x_p, t_q, x_q); normal is +d/dt.
            pt, px, qt, qx = n, -n, -n, n
            require(c * (px**2 - pt**2) == c * (qx**2 - qt**2) == 0, "wave")
            trace = [c, c * pt, c * qt, -c * pt * qt]
            require(trace == [c, n*c, -n*c, n*n*c], "four trace coefficients")
            traces.append([n, *trace])
        require(all(c == weights[-n] for n, c in weights.items()), "transpose")
        require(all(traces[-1-j][2] == row[3] for j, row in enumerate(traces)), "transposed first traces")
        # Normalize by L; all phases on the diagonal are unity.
        diagonal = sum(weights.values())
        wrong_wave = weights[1] * (cfg["wrong_spatial_frequency"]**2 - 1)
        require(diagonal != 0 and wrong_wave != 0, "negative controls")
        require(traces[-1][2] != traces[-1][3], "wrong second normal sign")
        results.append(dict(cutoff=cutoff, normalized_diagonal=diagonal,
                            wrong_wave_at_n1=wrong_wave, rows=traces))
    return results


def mul(a, b):
    return [[sum(x*y for x, y in zip(row,col,strict=True)) for col in zip(*b)]
            for row in a]


def chain(a, *matrices):
    for b in matrices:
        a = mul(a,b)
    return a


def tr(a):
    return list(map(list,zip(*a)))


def diag(x, y):
    return [[Q(x),Q(0)],[Q(0),Q(y)]]


def carriers(cfg):
    scales = [diag(*s) for s in cfg["scales"]]
    W = [diag(1/s[0][0], 1/s[1][1]) for s in scales]
    O = [[[Q(x,d),Q(-y,d)],[Q(y,d),Q(x,d)]] for x,y,d in cfg["rotations"]]
    root = diag(*cfg["residue_root"])
    ri = diag(1/root[0][0]**2, 1/root[1][1]**2)
    E = [chain(s,o,root) for s,o in zip(scales,O,strict=True)]
    C = [[chain(a,ri,tr(b)) for b in E] for a in E]
    T = [[chain(W[i],C[i][j],W[j]) for j in range(3)] for i in range(3)]
    v = [[Q(x)] for x in cfg["evaluation"]]
    e = [chain(w,a,ri,v) for w,a in zip(W,E,strict=True)]
    for a in range(3):
        require(T[a][a] == diag(1,1), "identity")
        for b in range(3):
            require(T[a][b] == mul(O[a],tr(O[b])) == tr(T[b][a]), "independent normalized transport")
            require(mul(T[a][b],e[b]) == e[a], "evaluation")
            for c in range(3):
                require(mul(T[a][b],T[b][c]) == T[a][c], "composition")
                require(chain(C[a][b],W[b],W[b],C[b][c]) == C[a][c], "mixed factorization")
    require(mul(C[0][1],C[1][2]) != C[0][2], "omitted middle inverse")
    require(mul(C[0][1],e[1]) != e[0], "raw mixed trace on normalized evaluation")
    return dict(triples=27, pairs=9, T02=T[0][2], evaluation0=e[0],
                missing_inverse_detected=True, raw_evaluation_detected=True)


def frame(cfg):
    # First jets represented by their value and derivative at zero.
    u, du, f = map(Q,(cfg["u0"],cfg["u1"],cfg["f0"]))
    def product(a,b):
        return (a[0]*b[0], a[1]*b[0]+a[0]*b[1])
    # Solve (u F_new)(x) = f to first order before comparing the formula.
    value = f/u
    derivative = -du*value/u
    initialized = product((u,du),(value,derivative))
    require(initialized == (f,0) and value == f/u, "framed evaluation")
    coefficient = derivative/value
    require(coefficient == -du/u, "induced logarithmic derivative")
    require(product((u,du),(f,0)) != initialized, "unchanged frame map")
    require(product((u,du),(value,value*du/u))[1] != 0, "opposite connection sign")
    return dict(interface_value=value, interface_derivative=derivative,
                connection_change=coefficient, frame_product=initialized,
                fixed_map_detected=True, wrong_sign_detected=True)


if __name__ == "__main__":
    cfg = json.loads((Path(__file__).parent/"inputs.json").read_text())
    out = dict(torus=torus(cfg["torus"]), carriers=carriers(cfg["carriers"]),
               frame=frame(cfg["frame"]))
    print(json.dumps(out, default=str, sort_keys=True, indent=2))

