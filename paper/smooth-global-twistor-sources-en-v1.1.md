# Global wave completion and recognition of smooth twistor sources

*Lior Isthmus*[^1] · 2026-11-22

[^1]: Email: [lioristhmus@proton.me](mailto:lioristhmus@proton.me) · ORCID: [0009-0004-7908-9876](https://orcid.org/0009-0004-7908-9876)

<div id="sec:abstract"></div>

## Abstract

We give a correspondence for smooth connected, oriented and time-oriented globally hyperbolic Ricci-flat four-manifolds with specified spin structures. The soldering and Lorentz form on the source point manifold determine a metric required to be globally hyperbolic. The Cartan and incidence equations recover its vacuum geometry and full rays with their realized intervals. Under the local smooth source hypotheses, full arrows correspond to causally convex isometric open embeddings with specified spin lifts. Physical scale and both Weyl chiralities are retained. A scalar wave kernel compares Cauchy carriers and their point evaluations. Four traces on the entire square of one possibly noncompact spacelike Cauchy hypersurface determine its bisolution class modulo globally smooth kernels. Each ordinary-pair atlas passing the quotient and causal tests has a unique completion up to marked full comparison. Universal presentation uses the local coverage theorem. The classical maximal development gives a terminal source for fixed marked vacuum data. Completion commutes with smooth base change for spacetime bundles over finite-dimensional bases with local common-Cauchy presentations; these exist locally for fibers with compact Cauchy hypersurfaces. For compact connected analytic vacuum data, persistence identifies the analytic and smooth marked geometric developments on their full point domains. With the analytic source and calibration inputs, completion compares whole-real source germs with the analytic metric locus and identifies the marked terminal sources.

<div id="sec:contents"></div>

## Contents

- [1. Introduction](#sec:scope-and-main-result)
- [2. Global Cauchy evolution and regularity](#sec:global-cauchy-regularity)
- [3. Global null incidence and realized affine domains](#sec:global-null-incidence)
- [4. Global wave completion from Cauchy data](#sec:p4-global-wave-completion)
- [5. Global carrier comparisons and evaluation](#sec:global-carrier-completion)
- [6. Independent geometric and scalar admission](#sec:global-independent-geometric-admission)
- [7. Independently normalized full sources and their comparisons](#sec:global-normalized-full-sources)
- [8. Relative carriers and causal restriction](#sec:relative-carrier-restriction)
- [9. Restrictions and full source embeddings](#sec:global-source-open-embeddings)
- [10. Maximal globally hyperbolic source developments](#sec:global-maximal-source-development)
- [11. Ordinary-pair atlases and geometric descent](#sec:global-ordinary-pair-atlases)
- [12. Global completion of ordinary-pair atlases](#sec:ordinary-atlas-global-completion)
- [13. Wave families on a common Cauchy manifold](#sec:common-cauchy-wave-families)
- [14. Families of full comparisons and ordinary-pair atlases](#sec:parameter-family-correspondence)
- [15. Analytic sources along an entire real spacetime](#sec:global-analytic-real-germs)
- [16. The structured analytic comparison and global wave completion](#sec:global-analytic-wave-bridge)
- [17. Dependencies and scope of the correspondence](#sec:dependencies-and-scope)
- [Appendix A. Analytic persistence for compact Cauchy data](#sec:compact-analytic-persistence)
- [AI and tool use disclosure](#sec:ai-and-tool-use-disclosure)
- [References](#sec:references)

<div id="sec:scope-and-main-result"></div>

## 1. Introduction

The local twistor correspondence retains both Weyl chiralities of a smooth vacuum metric. To extend it to a whole spacetime, one must identify every point on each null ray, its realized affine interval, and the singularities of a wave kernel between points that need not lie in one chart. Our spacetimes are connected, oriented and time-oriented, globally hyperbolic Ricci-flat four-manifolds at physical scale, with a specified principal spin structure.

Recognition starts on the point manifold of the source. Its soldering and Lorentz form determine the candidate metric, whose global hyperbolicity is an admission condition (Definition 6.1). The Cartan equations identify its vacuum connection and curvature (Proposition 6.2), and the maximal connected leaves identify its full ray incidence (Theorem 6.4). Under the local inputs of §1.1 the complete source comparisons are precisely the orientation- and time-orientation-preserving isometric open embeddings with causally convex image and specified spin lift (Theorems 7.7 and 9.4). Their lifts intertwine evaluation and point differentiation and satisfy the stored overlap equations.

The normalized mixed traces of a scalar wave kernel compare the carrier algebras and carry a point evaluation from one Cauchy surface to another. To make these comparisons globally we need its singularity class on the whole spacetime product. In [Example 4.7](#ex:torus-remote-bisolution), an exact bisolution vanishes near the entire diagonal but remains singular between distant points. Thus agreement on sufficiently small neighborhood squares does not determine a global distribution class. We construct the canonical class $[\Lambda_g^+]\in\mathcal D'(M\times M)/C^\infty(M\times M)$ and characterize it, among bisolutions modulo smooth kernels, by its four Cauchy traces on the entire square $\Sigma\times\Sigma$ of one whole spacelike Cauchy hypersurface (Theorems 4.4–4.5). Extending the local carrier comparisons also requires controlled compositions on noncompact Cauchy hypersurfaces and an incidence that retains each spacetime point and the actual domain of each null geodesic. Relative Cauchy carriers provide the full comparisons on these retained domains.

We call the analytic projective correspondence *Paper 1*, its analytic global extension *Paper 2*, and the local smooth correspondence *Paper 3* ([Isthmus 2026a](#ref-IsthmusProjective2026); [Isthmus 2026b](#ref-IsthmusGlobal2026); [Isthmus 2026c](#ref-IsthmusSmooth2026)). Section 1.1 collects the smooth local inputs. In particular, Paper 3, §6.6, gives complete Cauchy factorization and carrier comparisons on common retained wave neighborhoods.

An ordinary pair consists of two cohomology classes of weights $2$ and $-6$ in the admissible domain of Paper 3, represented in its coefficient complexes for the real CR geometry of the initial sphere bundle. Executing such a pair gives a local chart; the charts and their overlap comparisons form the global presentation. Theorem 1.4 completes each given globally admitted atlas and is fully faithful on its arrows. To present every independently admitted full source this way, we also invoke the local coverage theorem of Paper 3.

The twistor motivation is to retain both interacting gravitational chiralities in a single source description. Penrose's formulation of the googly problem asks for the opposite interacting helicity within the same twistor conventions, and his palatial proposal enlarges holomorphic functions by twistor differential operators ([Penrose 2015](#ref-Penrose2015)). The use of an operator algebra is therefore compatible with that proposal, although an algebra attached to an already given metric alone would not supply a source construction of general Einstein solutions.

The contact description of the light-ray space and its identification with a Cauchy cosphere bundle are established Lorentzian geometry; the Cauchy contact-form multiplier is the redshift formula of Chernov and Nemirovski ([Chernov and Nemirovski 2018](#ref-ChernovNemirovski2018), §1, Theorem 1.2). The global Cauchy and Fourier-integral ingredients used below likewise come from the standard hyperbolic and microlocal theory ([Bär, Ginoux and Pfäffle 2007](#ref-BarGinouxPfaeffle2007), §3; [Bär and Strohmaier 2019](#ref-BarStrohmaier2019), Appendix A; [Duistermaat 1972](#ref-Duistermaat1972), §1, Theorem 1.1). The global Hadamard existence theorem is an external input ([Gérard and Wrochna 2014](#ref-GerardWrochna2014), §8.2). We retain the relevant proofs and normalizations where they are needed to compare the actual point labels, physical scales and realized ray domains of the sources.

Functorial assignment of algebras to globally hyperbolic spacetimes and the time-slice property have an established formulation in locally covariant quantum field theory ([Brunetti, Fredenhagen and Verch 2003](#ref-BrunettiFredenhagenVerch2003), Definition 2.1 and Theorem 2.2). Here the carrier algebra belongs to a larger classical source that also retains the physical geometry, point incidence, spin lift, evaluation and connection. In particular, an invertible Cauchy carrier comparison need not be an isomorphism of the full point-labelled sources (Example 9.6). The source equivalence concerns those complete classical records; a quantum state and gravitational quantization require additional structures described in §17.2.

We call the admission tests independent because they can be applied before an ordinary-pair atlas is known. Definition 7.1 tests the supplied algebra, full evaluation and point connections against the native model of the metric read from the source, with compatible normalizations on overlaps.

For fixed smooth marked vacuum data, the classical Einstein maximal-development theorem transfers through the full source correspondence to a terminal marked source development ([Sbierski 2016](#ref-Sbierski2016), Theorem 2.8). With the separate local coverage input, it also gives a terminal atlas development. The construction and full comparisons extend to supplied smooth locally trivial spacetime bundles over finite-dimensional bases with local common-Cauchy presentations, joint smoothing, full descent and arbitrary smooth base change. Fibers with compact Cauchy hypersurfaces admit these local presentations automatically (Theorem 1.5).

Independently of the source correspondence, Appendix A proves that every smooth globally hyperbolic vacuum development of compact connected real analytic constraint data admits a unique compatible analytic structure on its entire point manifold, making the metric and prescribed initial embedding analytic. It retains the given principal spin bundle and makes the initial spin marking analytic. The proof combines a classical analytic Cauchy construction ([Fourès-Bruhat 1952](#ref-FouresBruhat1952), Chapter IV, §1) with Grauert approximation ([Grauert 1958](#ref-Grauert1958), Proposition 8), uniform local wave-coordinate control and Alinhac–Métivier propagation ([Alinhac and Métivier 1984](#ref-AlinhacMetivier1984), Theorem 1.2.2). This identifies the analytic and smooth marked geometric development categories and their maximal spacetime under the canonical marked comparison (Theorem 16.8). Under its separate analytic inputs, the calibrated source correspondence then identifies the marked terminal sources, preserving their complete records (Corollary 16.9).

We first construct the wave class and recognize the fields and their arrows. We then treat marked developments, presentations by ordinary pairs and variation in families. The comparison on the analytic locus comes last; §17.1 records which earlier results each step uses.

<div id="sec:local-inputs-and-conventions"></div>

### 1.1. Local inputs and conventions

All manifolds are smooth, Hausdorff and second countable, and have no boundary unless stated otherwise. A spacetime is connected, oriented and time-oriented, with Lorentzian signature $(+---)$. Its metric is retained at its physical scale. The gravitational application has dimension four, $\operatorname{Ric}(g)=0$, and an actual principal $\operatorname{Spin}^+(1,3)$ lift of the oriented and time-oriented orthonormal frame bundle. No self-duality condition is imposed on the Weyl curvature. The constructions of §§2–4 and the scalar family theorem in §13 require neither the Einstein equation nor a spin structure; §5 uses the complete calculus and module normalization of Paper 3 on a Ricci-flat background.

By a *whole Cauchy hypersurface* we mean a smooth spacelike hypersurface met exactly once by every inextendible causal curve in the spacetime under consideration. Its induced Riemannian metric need not be complete, and the hypersurface need not be compact. The existence of a smooth spacelike Cauchy hypersurface follows from Bernal–Sánchez, Theorem 1.1 ([Bernal and Sánchez 2005](#ref-BernalSanchez2005)). Global hyperbolicity does not imply affine completeness of the null geodesics; the domains retained below can have finite endpoints.

For kernels on $X\times Y$, the complete quotient identifies distributions whose difference is smooth on the whole product. It imposes no decay condition on that difference. A kernel representative is *properly supported* if both projections of its support to the factors are proper. Whole-carrier operators are composed using properly supported representatives; their smooth kernels form a two-sided ideal for these compositions. For the relative carriers of §8, products are first localized in interior conic charts and only then passed to the complete quotient. Example 8.5 shows why an arbitrary relative comparison need not have a representative proper over both entire carriers. The exact spacetime bidistribution, the proper representatives of its carrier classes, and the class modulo all globally smooth kernels are different objects.

The symbol $\dagger$ denotes the physical conjugate-linear Hermitian adjoint. Paper 3 also equips its integer-order complete algebra with a complex-linear internal adjoint $*$. The proof of preservation of $*$ will use Paper 3, Lemma 6.13; it does not follow from physical unitarity alone. Half-density and phase-transition lines are carried by the actual operators, and spin lifts remain separate geometric data.

The additional local inputs are taken from the pinned version of Paper 3 ([Isthmus 2026c](#ref-IsthmusSmooth2026)). A *retained parent* is a larger coordinate, wave or phase domain on which the fields and comparison maps are defined, with a positive buffer around the smaller domains used in the conclusion. Local carrier statements retain every null direction over their point core and the connecting segments required by the comparison. The imported results are used in the following forms.

| Local input and location in Paper 3 | Form used here |
| --- | --- |
| **Geometry and complete models.** Theorem 2.9; Propositions 6.2–6.3, 7.4–7.5. | The Cartan equations identify the metric, connection and Weyl tensor. Soldering and the spin connection determine the optical and finite-rank models. The half-density algebra and shifted whole-sky module have classical realizations. |
| **Wave and full comparison.** Theorems 6.10, 6.14, 7.11; Lemma 6.13. | The selected kernel determines carrier comparisons on common retained parents. After common restriction, a physical isometry with specified spin lift lifts uniquely, preserving evaluation, every point direction of the connections and the stored comparison equations. Lemma 6.13 controls the internal adjoint. |
| **Execution.** Theorem 4.18; Corollary 2.12; Proposition 5.6; Definition 8.1. | Executing an admissible weighted pair gives the initial source and recovers the input exactly. The derived data develop locally; the retained positive scale restores the physical metric and spin identification. |
| **Coverage and family selection.** Theorem 5.7; Propositions 5.8, 8.4. | Each marked smooth Lorentzian Ricci-flat germ has an ordinary-pair presentation. In a supplied smooth finite-dimensional family on common representatives, one can select presentations locally with one radius, one extension branch and common buffered parents. |

The family clauses use the finite calculus and comparison estimates of Paper 3, Lemma 6.4 and Proposition 7.12, together with the family estimates in the cited construction results. Each prescribed finite coefficient depth and derivative order uses finitely many input seminorms and the retained nondegeneracy margins. The parents are fixed before those output orders; constants and required input orders may depend on the requested output orders and on the fixed retained data. A smooth comparison family is supplied when a comparison between different geometric families is requested.

Coverage is an additional input for the essential surjectivity of ordinary-atlas presentations. Completion of a supplied admitted atlas uses its execution and local comparisons, followed by the global constructions proved here. The analytic inputs are stated separately in §15–§16; the detailed dependency table is in §17.1.

<div id="sec:overview-main-results"></div>

### 1.2. Main results

<div id="thm:global-wave-completion-overview"></div>

**Theorem 1.1 (Geometric and wave completion on a fixed background).**

Let $(M,g)$ be a smooth globally hyperbolic oriented and time-oriented Ricci-flat Lorentzian four-manifold, with an actual spin structure. With the local complete symbols, internal adjoint, and module conventions of Paper 3, the following data are canonically associated to it.

1. The global bisolution, selected-frequency and commutator tests select a unique scalar class $[\Lambda_g^+]$ ([Theorem 4.4](#thm:p4-global-canonical-wave-class)). Exact double evolution by transposition on compactly supported tests applies to arbitrary distributional Cauchy matrices. Applied to the properly supported classical Hermitian matrix of Lemma 4.2, it gives an exact Hermitian representative. Among bisolutions modulo smooth kernels, the four traces on the entire square of one Cauchy hypersurface determine the class (Theorem 4.5).
2. The ray space $\mathcal N(M)$ is a Hausdorff cooriented contact five-manifold. Its full point-labelled incidence is properly embedded in $\mathcal N(M)\times M$, and each Cauchy hypersurface gives global ray coordinates with the actual maximal affine interval on every ray.
3. For any two whole spacelike Cauchy carriers, the normalized mixed traces give invertible complete graph operators $T_{ab}$ satisfying $T_{ab}T_{bc}=T_{ac}$. They identify the filtered complete algebras and their internal adjoints, the whole sky modules, the degree-one evaluations, and the point connections of §5.

These constructions are natural under orientation- and time-orientation-preserving isometries. Their scalar classes and geometric incidence restrict naturally to causally convex globally hyperbolic open subspacetimes.

*Proof.* The scalar construction, uniqueness and Cauchy characterization are Theorems 4.4–4.5; its restriction law is Corollary 4.6. The ray and incidence statements are Theorem 3.2 and Proposition 3.3, with the restriction law of Proposition 3.6. Lemma 5.2 supplies the proper global graph factorizations, Theorem 5.3 proves the normalized carrier identities, and Theorem 5.5 proves evaluation and connection covariance. The scalar and ray constructions use the metric; the spin structure is carried with the geometry. ∎

Section 4 uses the global Hadamard existence theorem of Gérard and Wrochna to identify the singularity class constructed from the local source symbols. The whole Cauchy trace condition excludes remote singularities. The source retains the resulting class modulo smooth kernels.

Sections 6–7 pass from this construction over a recognized metric to independent global admission and comparison. The geometric fields obey finite Cartan and incidence equations. Stored operator and module presentations come with invertible model normalizations and their overlap cells, tested on the entire point-labelled incidence above each ray chart. These are the normalized sources of the next theorem. Arbitrary algebroids that are merely locally standard, without such evaluation- and connection-compatible records, form a different class of objects.

<div id="thm:global-normalized-correspondence-overview"></div>

**Theorem 1.2 (Independent global recognition and full comparison).**

For the global normalized full sources of [Definitions 7.1–7.2](#def:global-independent-normalized-wave-packet), recognition induces an equivalence

$$
R:\mathsf{FullSrc}^{\infty}_{\mathrm{GH},0}
\longrightarrow\mathsf{Vac}^{\infty}_{\mathrm{GH},0}.
$$ {#eq:global-correspondence-overview}

The target is the groupoid of smooth globally hyperbolic oriented and time-oriented Ricci-flat Lorentzian four-manifolds at physical scale, with actual spin structures and global physical isometries carrying specified spin lifts. Every such isometry has exactly one full source lift modulo the normalized presentation cells, and every full source arrow is obtained this way. The correspondence retains the actual point and affine domains, both Weyl chiralities, finite-rank diagrams, full evaluation, point connections, native roots, and stored source and target associators. No compactness assumption on the Cauchy hypersurface or self-duality condition is imposed.

*Proof.* Proposition 6.2 recognizes the geometric Cartan fields, Theorem 6.4 recognizes the entire null incidence, and Lemma 6.5 identifies the independently initialized finite-rank models. Theorem 6.8 recovers the scalar fields by the global kernel tests. Theorem 7.7 proves the full Hom bijection with explicit stored overlap maps, and Corollary 7.8 constructs the two inverse comparisons and proves their triangle identities. ∎

In Example 7.9 a flat line twist changes the wave equation of the specified point evaluation. This obstructs a full normalization over every admissible algebra vertex. Sections 8–10 extend the correspondence to causally convex open embeddings and to maximal developments. Sections 11–12 give ordinary-pair atlas presentations, their effective descent and global completion. Universal atlas coverage invokes the additional local coverage theorem of Paper 3. Sections 13–14 first prove the varying-metric extension in common-Cauchy presentations and then descend it to supplied spacetime bundles, using joint smoothing classes and estimates on retained compact sets. The common-Cauchy presentations exist locally without further assumptions when the fibers have compact Cauchy hypersurfaces. Sections 15–16 prove the comparison with the analytic sources of Papers 1–2 under their separately stated analytic inputs.

<div id="thm:global-causal-development-overview"></div>

**Theorem 1.3 (Causal embeddings and maximal developments).**

The following statements hold for the independently normalized full sources of Definition 7.1.

Restricting all fields to a causally convex globally hyperbolic open point domain, and transporting their supplied normalizations by the relative carriers of §8, gives an admitted source. These restrictions are coherent under composition. Recognition extends to an equivalence

$$
R:\mathsf{FullSrc}^{\infty,\mathrm{cc}}_{\mathrm{GH},0}
\longrightarrow
\mathsf{Vac}^{\infty,\mathrm{cc}}_{\mathrm{GH},0},
$$ {#eq:global-causal-correspondence-overview}

where the source arrows are the full open comparisons of Definition 9.3 and the target arrows are physical-spin isometric open embeddings with causally convex image. Every such embedding has exactly one full source lift with its specified actual spin map. Cauchy arrows give invertible comparisons of the entire ray carriers, while retaining their point-domain inclusions and actual affine intervals.

For each smooth marked vacuum initial datum $\mathfrak d=(\Sigma,h,K,P_\Sigma)$ satisfying the constraints and conventions of Definition 10.1, the category $\mathsf{Dev}_{\mathrm{src}}(\mathfrak d)$ has a terminal object. Its recognized spacetime is a classical maximal globally hyperbolic development. Every other marked source development has exactly one full embedding into it, preserving the entire initial point and spin markings.

The initial manifold may be noncompact, and its Riemannian metric need not be complete. Maximality is taken within the stated category of smooth globally hyperbolic developments; realized null intervals may have finite endpoints.

*Proof.* The relative factorization and packet comparison are Lemma 8.2 and Theorem 8.3; Corollary 8.4 supplies their cocycle. Proposition 9.2 verifies all admission and stored-cell conditions for the restricted source, and Theorem 9.4 proves the embedding equivalence. Proposition 8.6 and Corollary 9.5 identify its Cauchy case. For the second assertion, Lemma 10.2 extends the actual initial spin structure, and Theorem 10.4 combines the embedding correspondence with the classical smooth maximal-development theorem of Sbierski, Theorem 2.8 ([Sbierski 2016](#ref-Sbierski2016)). ∎

The global wave completion, full-source recognition and marked maximal-development statements do not require an ordinary-pair atlas as input. The next theorem presents these objects by atlases of the ordinary two-class inputs of Paper 3 and identifies where its local coverage theorem is used. The independent source definition retains the global scalar admission condition. As Example 4.7 shows, agreement on the squares of sufficiently small point neighborhoods does not determine the kernel class on the whole spacetime product.

<div id="thm:ordinary-atlas-completion-overview"></div>

**Theorem 1.4 (Ordinary-pair atlases and global completion).**

Let $\mathsf{PairAtl}^{\infty,\mathrm{cc}}_{\mathrm{GH},0}$ be the category of executed ordinary-pair atlases and full open comparisons in Definitions 11.2 and 11.4. The quotient must pass the effective chart and topology tests of Definition 11.2(3), the principal spin transitions obey a strict cocycle, and the descended cone field satisfies the global hyperbolicity test.

Every supplied atlas admits a global completion by an independently normalized full source. The completion is unique up to the unique full comparison preserving its geometric marking and local atlas comparisons. Completion gives a fully faithful functor

$$
\mathcal C:
\mathsf{PairAtl}^{\infty,\mathrm{cc}}_{\mathrm{GH},0}
\longrightarrow
\mathsf{FullSrc}^{\infty,\mathrm{cc}}_{\mathrm{GH},0},
$$ {#eq:ordinary-atlas-completion-overview}

preserving and reflecting Cauchy arrows and isomorphisms. Atlases with compatible full comparisons descend effectively over a prescribed effective point and spin gluing whenever the resulting quotient satisfies the global admission tests. These assertions use the execution and local comparison theorems of Paper 3, without its assertion that every smooth Ricci-flat germ has an ordinary-pair presentation.

Assuming additionally Paper 3, Theorem 5.7, $\mathcal C$ is essentially surjective, and hence

$$
\mathsf{PairAtl}^{\infty,\mathrm{cc}}_{\mathrm{GH},0}
\simeq
\mathsf{FullSrc}^{\infty,\mathrm{cc}}_{\mathrm{GH},0}
\simeq
\mathsf{Vac}^{\infty,\mathrm{cc}}_{\mathrm{GH},0}.
$$ {#eq:ordinary-atlas-three-categories-overview}

The inverse comparisons retain all actual point and spin maps, physical scales, realized affine domains, complete evaluations, point connections and stored associators. The equivalence restricts to marked developments and presents the terminal source development of Theorem 1.3 by an ordinary-pair atlas.

*Proof.* Proposition 11.3 establishes geometric descent with the quotient and causal tests, Theorem 11.5 gives the full atlas Hom bijection, and Proposition 11.6 proves effective descent of already supplied atlases. Theorem 12.2 constructs the global completion and its unique comparisons, and Proposition 12.3 proves full faithfulness on actual atlas arrows. The only additional input for universal atlas coverage is the local coverage theorem applied in Theorem 11.7. Theorem 12.4 then constructs the source recovery and inverse comparisons; Corollary 12.5 transfers marked maximal development. ∎

Each chart retains its own whole ordinary input and auxiliary exterior extension. Its overlap maps compare the executed local fields, as in Paper 3, Definition 8.1. The atlas theorem neither selects one global ordinary pair nor assumes one global maximal initial hypersurface. The protected extension in Paper 3, Appendix B, is a dependency of universal coverage; completion and comparison of a supplied admitted atlas use the separate local execution and comparison inputs. The global scalar class is constructed after geometric descent and compared with the atlas on compatible causal refinements, rather than inferred solely from kernels on the original chart squares.

<div id="thm:global-family-correspondence-overview"></div>

**Theorem 1.5 (Finite-dimensional source families and spacetime bundles).**

Let $B$ be a finite-dimensional smooth parameter manifold, and let $g_\lambda$ be a jointly smooth family of globally hyperbolic, oriented and time-oriented Lorentzian metrics on one smooth four-manifold $M$. Supply a single smooth hypersurface $\Sigma\subset M$ that is spacelike and Cauchy for every member, with the common future coorientation. Then the scalar completion is defined as one class in the joint smoothing quotient on $B\times M^2$. This class has an exact Hermitian bisolution family representative. Among the locally uniform classical phase families specified in Theorem 13.6, with nonzero null covectors at both endpoints and jointly smooth residuals in both wave equations, the four Cauchy traces on the entire $B\times\Sigma^2$ characterize its joint class.

Suppose now that the metrics are Ricci-flat and carry a specified smooth family of spin structures. The native full source construction and recognition give an equivalence

$$
\mathsf{FullSrc}^{\infty,\mathrm{cc}}_{\mathrm{GH},0}(B)
\simeq
\mathsf{Vac}^{\infty,\mathrm{cc}}_{\mathrm{GH},0}(B)
$$ {#eq:global-family-correspondence-overview}

in the family categories of Theorem 14.4. Each object has its own fixed manifold and common Cauchy hypersurface over $B$. Every supplied smooth physical-spin isometric open embedding family with causally convex images has a unique smooth full lift. Its complete carrier maps, evaluations, point connections, actual spin maps and stored cells satisfy finite coefficient and derivative estimates on compact subsets of the retained parameter, point and homogeneous direction domains. The geometric parents are selected before the output orders. Neither a compact Cauchy hypersurface nor an exterior region on which the metrics are fixed is required.

A supplied ordinary-pair atlas family of Definition 14.5 has a joint full completion, unique up to the unique full comparison preserving its atlas marking and local comparisons, and completion is fully faithful. Assuming the smooth local coverage and selection results of Paper 3, Propositions 5.8 and 8.4, the ordinary-pair atlas category is also equivalent to both categories in the display. Its charts may have different parameter neighborhoods and spatial radii; they form a countable locally finite cover of $B\times M$.

More generally, let $\pi:\mathfrak M\to B$ be a supplied smooth locally trivial physical-spin vacuum bundle whose connected fibers are globally hyperbolic and which admits local common-Cauchy trivializations as in Definition 14.10. The joint scalar class is defined on $\mathfrak M\times_B\mathfrak M$, and the local full sources descend to an intrinsic source family. Recognition and completion give the equivalences of Theorem 14.15, with the same separate ordinary-coverage input. They are independent of the adapted cover and local Cauchy carriers and commute with arbitrary smooth base change. If every fiber has a compact Cauchy hypersurface, local common-Cauchy trivializations exist automatically. In this compact-Cauchy sector every supplied smooth fiberwise physical-spin isometric open embedding is a Cauchy embedding with causally convex image and has a unique full family lift.

*Proof.* Lemma 13.2 proves compact causal control and common causal comparison parents from the supplied common Cauchy hypersurface. Lemmas 13.3–13.4 establish the parameterized exact evolution and its joint microlocal calculus; Proposition 13.5 constructs the canonical Cauchy matrix family. Theorem 13.6 constructs and characterizes the global scalar class, and Proposition 13.7 gives its finite estimates. Proposition 14.2 supplies the actual geometric and spin transports, Theorem 14.3 proves the relative carrier family identities, and Theorem 14.4 gives the full Hom bijection and equivalence. Theorem 14.6 proves the atlas assertions, separating completion of supplied atlases from the additional local coverage input. Theorems 14.13 and 14.15 prove intrinsic scalar and full descent, including arbitrary smooth base change. Proposition 14.12 and Corollary 14.16 establish automatic admission and the embedding assertion for compact Cauchy fibers. ∎

The bundle statement uses common-Cauchy representatives only locally in the parameter space and allows geometric and spin monodromy. Its smoothness is in the parameterized complete calculus, with jointly smooth remainders; unrelated fiberwise smoothing errors cannot be discarded, as Example 13.8 demonstrates. Smoothness on the open realized ray domain does not imply continuity of its maximal affine endpoint functions, even for flat metrics (Example 14.8). Likewise, the fixed-data terminal development of Theorem 1.3 does not by itself produce a smooth family of entire maximal developments. These distinctions determine the scope of the family correspondence. Proposition 16.6 compares the common-Cauchy family construction with supplied conditioned analytic families, requiring the common Cauchy hypotheses on their real restrictions.

<div id="thm:global-analytic-comparison-overview"></div>

**Theorem 1.6 (Comparison with global analytic source germs).**

Let $\mathsf{AnOp}^{\mathrm{germ},\mathrm{cc}}_{\mathrm{GH},0}$ be the unmarked analytic operator source category of Definition 15.1, with its whole-sky analytic admission, actual root and frame data, and compatible Lorentz reality. Representatives are complex neighborhoods of the entire real globally hyperbolic spacetime; restriction recomputes null-path monodromy. Let $\mathsf{FullSrc}^{\infty,\mathrm{cc}}_{\mathrm{GH},0;\omega}$ be the full subcategory of smooth normalized sources whose recognized physical metrics admit a compatible real analytic structure. Under the analytic recognition and existence inputs of Papers 1–2 and the calibration of Paper 3, §9, on each admitted local model and its physical comparison arrows as specified in §16, there is an equivalence

$$
\mathcal W_\omega:
\mathsf{AnOp}^{\mathrm{germ},\mathrm{cc}}_{\mathrm{GH},0}
\longrightarrow
\mathsf{FullSrc}^{\infty,\mathrm{cc}}_{\mathrm{GH},0;\omega}.
$$ {#eq:global-analytic-comparison-overview}

It has compatible calibrated local comparisons from the sectorwise real restriction and smooth complete enrichment of the analytic representatives to the global wave source. They preserve the original root squares and base factors, whole-family frames, physical scales, spin maps, chiral records and coupled Lorentz square. Comparison cells relate the stored associators. Pulling the smooth evaluation and point connections back through the vertices defines the full fields on the enriched real presentation. The corrected transitions and arrows intertwine these fields on all complete sections. The real phase and designated real-path groupoid identify with the real ray incidence of §3 and its fiberwise pair groupoid, including the actual affine intervals. These comparisons are natural under causal open embeddings, and the original-source and geometric analytic realizations give the same equivalence through Theorem 15.2.

For supplied conditioned holomorphic families whose real restrictions satisfy Definition 13.1 on a common smooth manifold with a supplied common spacelike Cauchy hypersurface, Proposition 16.6 gives the finite smooth jet comparison on retained finite diagrams. This assertion retains the analytic bounds of the supplied representatives; the new interfaces belong to the smooth complete calculus.

Independently of these source inputs, let $\mathfrak d$ be compact connected real analytic vacuum constraint data with the actual initial spin marking of Definition 10.1. The classical analytic-persistence argument of Appendix A and Theorem 16.8 give

$$
\mathsf{Dev}^{\omega}_{\mathrm{geom}}(\mathfrak d)
\simeq\mathsf{Dev}^{\infty}_{\mathrm{geom}}(\mathfrak d).
$$ {#eq:analytic-development-equivalence-overview}

Under the analytic source inputs stated above, Corollary 16.9 gives

$$
\mathcal W_\omega(\mathcal A^{\max}_\omega(\mathfrak d))
\cong S^{\max}_\infty(\mathfrak d).
$$ {#eq:analytic-terminal-isomorphism-overview}

This source comparison is the unique marked full isomorphism, is natural under analytic initial-data isomorphisms with their actual spin lifts, and identifies the entire maximal point domains and realized affine intervals.

*Proof.* Theorem 15.2 proves the required unmarked whole-real germ correspondence, and Lemma 15.3 identifies its geometric image as a full subcategory of the smooth category. Proposition 15.5 proves the intrinsic real-path and affine comparison. Lemma 16.2 places the calibrated local interface on a global Cauchy carrier. Proposition 16.3 proves its descent using the actual quadratic-root and framed-overlap equations, with both associators and the Lorentz square retained. Theorem 16.4 constructs the equivalence and its inverse comparisons. Corollary 16.5 and Proposition 16.6 establish the restriction and conditioned-family assertions. Theorem 16.8 uses the classical analytic persistence of Appendix A to establish the geometric marked development equivalence. Corollary 16.9 combines that equivalence with the calibrated analytic source correspondence to establish the maximal-source isomorphism. ∎

<div id="sec:global-cauchy-regularity"></div>

## 2. Global Cauchy evolution and regularity

Let $(M,g)$ be a smooth, connected, time-oriented globally hyperbolic Lorentzian manifold without boundary, and let $\Sigma\subset M$ be a smooth spacelike Cauchy hypersurface. Compactness of $\Sigma$ is not assumed. The scalar wave operator is $P=\Box_g$. Scalar distributions are paired using the physical volume density. Write

$$
\gamma_0u=u|_\Sigma,\qquad \gamma_1u=n(u)|_\Sigma,
$$

where $n$ is the future unit normal. Multiplying both traces by the positive spatial half-density gives the convention of Paper 3; all regularity and uniqueness statements below are unchanged by this invertible smooth multiplication.

We use the following precise external inputs. Bär–Ginoux–Pfäffle, Theorems 3.2.11–3.2.12, give the smooth compact-data Cauchy solution, its support property, and continuity. Their Theorem 3.1.1 gives uniqueness for distributional homogeneous solutions with past-compact or future-compact support. The Fourier integral description of the exact Cauchy operators, with nonzero covectors at both endpoints, is Bär–Strohmaier, Theorem A.1 ([Bär, Ginoux and Pfäffle 2007](#ref-BarGinouxPfaeffle2007); [Bär and Strohmaier 2019](#ref-BarStrohmaier2019)).

We pass from compactly supported smooth data to arbitrary distributions by transposing the Cauchy operators on test functions. Compact causal shadows control the support needed for this transposition.

<div id="sec:support-and-distributional-evolution"></div>

### 2.1. Compact support control and distributional evolution

<div id="lem:compact-cauchy-shadows"></div>

**Lemma 2.1 (Compact Cauchy shadows and propagation strips).**

For every compact $K\subset M$ and every spacelike Cauchy hypersurface $\Sigma$, the sets

$$
J^+(K)\cap\Sigma,\qquad J^-(K)\cap\Sigma,\qquad
J^+(K)\cap J^-(\Sigma),\qquad
J^-(K)\cap J^+(\Sigma)
$$

are compact. In particular, the causal segments between $K$ and $\Sigma$ are contained in a compact subset of $M$.

*Proof.* This is Corollary A.5.4 of Bär–Ginoux–Pfäffle ([Bär, Ginoux and Pfäffle 2007](#ref-BarGinouxPfaeffle2007)). Its hypotheses require global hyperbolicity, a Cauchy hypersurface and compact $K$, and do not require compactness of $\Sigma$. The union of the last two compact sets contains all the stated segments. ∎

<div id="lem:distributional-zero-cauchy"></div>

**Lemma 2.2 (Uniqueness for distributional Cauchy data).**

Suppose $u\in\mathcal D'(M)$ satisfies $Pu=0$. Its two spacelike Cauchy traces are defined. If $\gamma_0u=\gamma_1u=0$, then $u=0$ on $M$.

*Proof.* Microlocal elliptic regularity gives

$$
\operatorname{WF}(u)\subset
\{(x,\xi)\in T^*M\setminus0:g^{-1}_x(\xi,\xi)=0\}.
$$

Every nonzero conormal to $\Sigma$ is timelike. Thus the pullbacks defining the two Cauchy traces exist. The same observation allows multiplication of $u$ by the characteristic function of the future of $\Sigma$: the singular covectors of that characteristic function are timelike conormals to $\Sigma$, and cannot cancel a characteristic covector of $u$.

Choose a smooth defining function $t$ increasing towards the future near $\Sigma$, and write $H(t)$ for the future characteristic function. In Gaussian coordinates near any point of $\Sigma$,

$$
P=\partial_t^2+b(t,x)\partial_t+P_t,
$$

where $P_t$ differentiates only tangentially. Distributional differentiation gives

$$
P(Hu)
=H Pu+\delta'(t)\,\gamma_0u
+\delta(t)\bigl(\gamma_1u+b(0,x)\gamma_0u\bigr).
$$

The formula follows by differentiating the distribution-valued function in the normal variable; its normal traces of every order exist by the same wavefront criterion. Equivalently, one can first regularize in tangential coordinates and then pass to the trace topology. The two prescribed zero traces make every boundary term vanish. The local formulas agree, so the globally defined future extension $u_+=\mathbf1_{J^+(\Sigma)}u$ satisfies $Pu_+=0$.

The support of $u_+$ is past-compact: its intersection with $J^-(K)$ is contained in the compact set $J^+(\Sigma)\cap J^-(K)$ for each compact $K$. The hypotheses of Bär–Ginoux–Pfäffle, Theorem 3.1.1, hold on a globally hyperbolic spacetime. Hence $u_+=0$. Applying the same argument with time reversed gives $u_-=0$ for the past extension. Their sum is $u$, and therefore $u=0$. ∎

The coefficient of $\delta(t)$ depends on the chosen normal-coordinate form, but vanishes whenever both Cauchy traces vanish. The proof consequently applies unchanged to a normally hyperbolic operator with smooth lower-order terms, and to a smooth rescaling of the trace convention.

<div id="lem:distributional-cauchy-evolution"></div>

**Lemma 2.3 (Exact Cauchy evolution of distributions).**

The exact smooth Cauchy solution operator extends to a linear map

$$
\mathcal U:\mathcal D'(\Sigma)\oplus\mathcal D'(\Sigma)
\longrightarrow\mathcal D'(M).
$$

It satisfies

$$
P\mathcal U f=0,\qquad
(\gamma_0,\gamma_1)\mathcal U f=f.
$$

The extension is unique. For each compact $K\subset M$, its restriction to $K$ depends only on initial data in a compact neighborhood of $J(K)\cap\Sigma$.

*Proof.* Write $\mathcal U=(\mathcal U_0,\mathcal U_1)$ on smooth compactly supported initial data. Each $\mathcal U_i$ has a distribution kernel. The exact Cauchy Fourier integral theorem places its wavefront set on the null relation from $\Sigma$ to $M$, with both endpoint covectors nonzero. Consequently its transpose takes a smooth compactly supported spacetime test density to a smooth initial test density.

Finite propagation gives

$$
\operatorname{supp}(\mathcal U_i^t\phi)
\subset J(\operatorname{supp}\phi)\cap\Sigma.
$$

The right-hand side is compact. The transpose is therefore a continuous map $\mathcal D(M)\to\mathcal D(\Sigma)$: on a fixed compact spacetime support, its initial support lies in one compact set, and local Fourier integral continuity gives all required seminorm estimates. One may also identify this transpose by the Green formula as a signed Cauchy trace of the smooth causal solution $E\phi$; the signs depend on the convention for $E$ and are not needed here.

For arbitrary distributional data, define

$$
\langle\mathcal U f,\phi\rangle
=\sum_{i=0}^1\langle f_i,\mathcal U_i^t\phi\rangle.
$$

Continuity of the transpose makes this a distribution on $M$. The operator identities $P\mathcal U_i=0$ and $\gamma_j\mathcal U_i=\delta_{ij}I$ are identities of kernels: they hold on smooth test data, and the kernel theorem identifies the operators. Their compositions with arbitrary initial distributions are defined by the nonzero endpoint wavefront condition and the compact-support localization just described. Thus the stated equation and Cauchy data hold. Lemma 2.2 proves uniqueness.

If two initial data agree near $J(K)\cap\Sigma$, their pairings against all $\mathcal U_i^t\phi$ with $\operatorname{supp}\phi\subset K$ agree, which proves the last assertion. ∎

<div id="prop:proper-cauchy-evolution"></div>

**Proposition 2.4 (Proper support between arbitrary Cauchy hypersurfaces).**

Let $P$ be a smooth normally hyperbolic operator on a finite-rank bundle over $M$. Let $\mathcal S_{ba}$ be its exact homogeneous Cauchy evolution matrix from $\Sigma_a$ to $\Sigma_b$, using field and future-normal traces. Each entry has a distribution kernel whose support is proper over both Cauchy hypersurfaces. The same assertion holds after multiplication by the physical half-density factors.

For evolution from $\Sigma_a$ to all of $M$, the kernel support is proper over the spacetime factor. Properness over the initial factor is not asserted.

*Proof.* The smooth Cauchy theorem and continuous dependence give the evolution operator and its distribution kernel ([Bär, Ginoux and Pfäffle 2007](#ref-BarGinouxPfaeffle2007), Theorems 3.2.11–3.2.12). Finite propagation puts the support of every entry of $\mathcal S_{ba}$ in the closed relation

$$
\mathcal R_{ba}
=\{(y,x)\in\Sigma_b\times\Sigma_a:y\in J(x)\}.
$$

Normal differentiation and multiplication by a smooth density do not enlarge support. For compact $K_b\subset\Sigma_b$, the part of this support lying over $K_b$ is a closed subset of

$$
K_b\times\bigl(J(K_b)\cap\Sigma_a\bigr),
$$

which is compact by Lemma 2.1. Interchanging $a$ and $b$ proves properness of the other projection. This uses neither an ordering nor disjointness of the two hypersurfaces. For a compact spacetime set $K$, the same argument uses $J(K)\cap\Sigma_a$. A solution from compact initial data can persist for arbitrarily long times, so this argument gives no properness over the initial factor for evolution to all of $M$. ∎

<div id="sec:smooth-and-passive-regularity"></div>

### 2.2. Smooth forcing and passive variables

<div id="lem:smooth-noncompact-cauchy"></div>

**Lemma 2.5 (Smooth data and forcing without support assumptions).**

For arbitrary smooth Cauchy data and arbitrary smooth forcing $f$ on $M$, the Cauchy problem $Pu=f$ has a unique smooth solution. On every compact output set, every finite output seminorm is controlled by finitely many input seminorms on compact sets. The solution operation therefore preserves smooth dependence on passive finite-dimensional parameters when $P$ is fixed.

*Proof.* Fix a compact output set and place it in the interior of a larger compact set $K$. The construction below then controls a neighborhood of the original output set. The part of its causal past or future between $K$ and $\Sigma$ is

$$
\mathcal H_\Sigma(K)
=\bigl(J^-(K)\cap J^+(\Sigma)\bigr)
\cup\bigl(J^+(K)\cap J^-(\Sigma)\bigr).
$$

It is compact by Corollary A.5.4 of Bär–Ginoux–Pfäffle. Choose compactly supported smooth cutoffs equal to one near this set and near $J(K)\cap\Sigma$. Apply the smooth compact-data Cauchy theorem to the cut-off forcing and data. Domain of dependence makes the solution near $K$ independent of these choices. For two output compacts the constructions agree on their overlap by the same property. They therefore define a smooth solution on all of $M$.

The usual compact-data Cauchy continuity, applied with the fixed cutoffs, gives the stated finite seminorm dependence. Uniqueness follows by subtracting two solutions and applying Lemma 2.2. Differentiation in a passive parameter commutes with the fixed linear Cauchy operation; its compact seminorm continuity gives every mixed derivative. ∎

<div id="lem:passive-cauchy-regularity"></div>

**Lemma 2.6 (Cauchy regularity with distributional passive variables).**

Let $X$ be a smooth finite-dimensional manifold and let $v\in\mathcal D'(X\times M)$. Suppose

$$
P_Mv\in C^\infty(X\times M)
$$

and both Cauchy traces on $X\times\Sigma$ are smooth jointly in $(x,y)$. Then $v\in C^\infty(X\times M)$.

*Proof.* The two trace distributions exist automatically. Indeed, at a nonzero conormal to $X\times\Sigma$ the $X$ covector vanishes and the $M$ covector is timelike. The principal symbol of $P_M$ is nonzero there, whereas the equation makes $v$ microlocally smooth at every such covector.

Use Lemma 2.5 with the smooth forcing and the two smooth initial traces to construct $w\in C^\infty(X\times M)$ with the same equation and data. Here $P$ is independent of $x$, so the passive-parameter assertion of that lemma applies on each compact parameter chart.

The distribution $z=v-w$ solves the homogeneous wave equation with zero Cauchy data. For any $\psi\in\mathcal D(X)$, integrate the $X$ variable against $\psi$ to obtain $z_\psi\in\mathcal D'(M)$. This pushforward is proper after multiplication by $\psi$, and commutes with $P$ and the spacelike traces. Therefore $Pz_\psi=0$ and its Cauchy data vanish. Lemma 2.2 gives $z_\psi=0$.

Pairing further with arbitrary $\phi\in\mathcal D(M)$ shows that $z$ vanishes on every tensor-product test function. Finite sums of such test functions are dense in $\mathcal D(X\times M)$ on each product of compact coordinate supports. Hence $z=0$. ∎

<div id="sec:double-cauchy-evolution"></div>

### 2.3. Double Cauchy evolution and smoothing

<div id="lem:global-double-cauchy-smoothing"></div>

**Lemma 2.7 (Global double-Cauchy smoothing).**

Let $D\in\mathcal D'(M\times M)$ satisfy

$$
P_pD,\ P_qD\in C^\infty(M\times M).
$$

Its four double Cauchy traces exist. If

$$
(\gamma_i\otimes\gamma_j)D
\in C^\infty(\Sigma\times\Sigma),
\qquad i,j\in\{0,1\},
$$

then $D\in C^\infty(M\times M)$.

*Proof.* The principal symbols of the partial operators are $g_p^{-1}(\xi,\xi)$ and $g_q^{-1}(\eta,\eta)$. A nonzero conormal to $\Sigma\times M$ has $\eta=0$ and timelike $\xi$, so $P_p$ is elliptic there. The analogous statement holds for $M\times\Sigma$. At a nonzero conormal to $\Sigma\times\Sigma$, at least one endpoint covector is a nonzero timelike conormal, and the corresponding partial operator is elliptic. Thus all the required restrictions, including normal derivatives, are defined.

Set

$$
d_i=(\gamma_i\otimes I)D
\in\mathcal D'(\Sigma\times M),\qquad i=0,1.
$$

The commutation of differential operators in distinct variables with these restrictions gives

$$
P_qd_i=(\gamma_i\otimes I)(P_qD)\in C^\infty(\Sigma\times M).
$$

Ellipticity of $P_q$ and smoothness of $P_qd_i$ exclude nonzero timelike second covectors from $\operatorname{WF}(d_i)$ even when the first covector vanishes, so the second restriction is transverse and composition of pullbacks identifies its two Cauchy data with the prescribed smooth product traces. Apply Lemma 2.6 with $X=\Sigma$ and the second copy of $M$ as the active spacetime. It follows that both $d_0$ and $d_1$ are jointly smooth.

Now regard the second copy of $M$ as the passive manifold and the first copy as the active spacetime. The residual $P_pD$ is smooth and the two first-variable Cauchy data of $D$ are $d_0,d_1$. A second application of Lemma 2.6 gives $D\in C^\infty(M\times M)$. ∎

This proof permits a zero covector at one endpoint before regularity is established. A proof that propagates two nonzero characteristic covectors from the outset would omit these possible singularities.

<div id="cor:double-evolution-quotient"></div>

**Corollary 2.8 (Double evolution modulo smooth kernels).**

For a $2\times2$ matrix $A$ of distribution kernels on $\Sigma\times\Sigma$, double exact Cauchy evolution defines

$$
\mathcal E_\Sigma(A)
=\sum_{i,j=0}^1
(\mathcal U_i\otimes\mathcal U_j)A_{ij}
\in\mathcal D'(M\times M).
$$

This is an exact bisolution with double Cauchy matrix $A$. If $A-\widetilde A$ is globally smooth, then $\mathcal E_\Sigma(A)-\mathcal E_\Sigma(\widetilde A)$ is globally smooth. Every exact bisolution is the double evolution of its four Cauchy traces. More generally, a bisolution modulo smooth kernels differs smoothly from the double exact evolution of its four traces.

*Proof.* On a test function on $M\times M$, apply the two transpose Cauchy operators. Their compact support and smoothness properties give a smooth compactly supported test matrix on $\Sigma\times\Sigma$, against which $A$ can be paired. For product compact output supports, the resulting initial support is contained in the product of two compact causal shadows. The tensor-product operation extends continuously to all test functions by the kernel theorem.

The exact equations and trace identities follow from Lemma 2.3 in each variable. If the initial matrix is smooth, successive application of Lemma 2.5 makes its double evolution jointly smooth. For an arbitrary bisolution modulo smooth kernels, subtract the constructed exact bisolution. The difference has smooth wave residuals and zero double traces, so Lemma 2.7 applies. In the exact homogeneous case, successive use of Lemma 2.2 makes the difference zero. ∎

For a Hermitian covariance matrix the same construction is written $\mathcal U A\mathcal U^\dagger$, with the chosen density convention. The tensor formula above states explicitly which two variables are evolved. No support assumption on an arbitrary distributional initial matrix is required for this operation. Proper representatives are needed later for the unrestricted composition of carrier operators.

<div id="sec:global-null-incidence"></div>

## 3. Global null incidence and realized affine domains

Let $(M,g)$ be a smooth oriented and time-oriented globally hyperbolic Lorentzian four-manifold. The local incidence models are those of Paper 3, Lemma 7.2 and Theorem 7.3, and the affine normalization agrees with Paper 2, Proposition 3.2 ([Isthmus 2026c](#ref-IsthmusSmooth2026); [Isthmus 2026b](#ref-IsthmusGlobal2026)). Here the metric and its causal geometry determine the incidence on the full smooth spacetime, including rays with finite affine endpoints.

The contact identification of the light-ray space with a Cauchy cosphere bundle and the Legendrian sky spheres belong to the established geometry of globally hyperbolic spacetimes; see Chernov and Rudyak, §1, equation (1.5) and Definition 1.11 ([Chernov and Rudyak 2008](#ref-ChernovRudyak2008)). The contact-form change between Cauchy hypersurfaces is the redshift identity of Chernov and Nemirovski, Theorem 1.2 ([Chernov and Nemirovski 2018](#ref-ChernovNemirovski2018)). The proofs below fix the signs, physical affine normalizations and maximal domains needed by the global source comparisons.

<div id="sec:null-rays-and-affine-domains"></div>

### 3.1. Rays, contact structure, and affine normalization

<div id="def:global-null-ray-data"></div>

**Definition 3.1 (Null phase and rays).**

Let $F$ be the bundle of future null tangent lines, equivalently the positive projectivization of the past null covectors through $[k]_+\mapsto[-g(k,\cdot)]_+$. Its projection is denoted by $p:F\to M$. A ray is a maximal future-oriented null geodesic, modulo positive affine reparametrization. Let $\mathcal N(M)$ be the set of rays and let $q:F\to\mathcal N(M)$ send a phase point to its ray. Initially give $\mathcal N(M)$ the quotient topology of $q$.

Fix a spacelike Cauchy hypersurface $\Sigma$, its future unit normal $n$, and $h=-g|_{T\Sigma}$. A normalized initial tangent has the form $n+v$ with $h(v,v)=1$. We identify this tangent with the unit spatial covector $h(v,\cdot)\in S_h^*\Sigma$.

<div id="thm:global-real-ray-flow"></div>

**Theorem 3.2 (Global ray coordinates and actual affine domain).**

The map assigning the normalized Cauchy hit identifies $\mathcal N(M)$ with the smooth manifold $S_h^*\Sigma$. Let $\gamma_z:I_z\to M$ be the maximal affine geodesic with normalized initial data $z\in S_h^*\Sigma$, with $0\in I_z$. Then

$$
D_{M,\Sigma}=\{(z,s)\in S_h^*\Sigma\times\mathbb R:s\in I_z\}
$$ {#eq:global-real-affine-domain}

is open, each $I_z$ is an open interval, and

$$
\Phi_\Sigma:D_{M,\Sigma}\longrightarrow F,
\qquad
\Phi_\Sigma(z,s)=\bigl(\gamma_z(s),[\dot\gamma_z(s)]_+\bigr)
$$ {#eq:global-real-affine-flow}

is a diffeomorphism. Under this identification $q$ is the projection to $z$. In particular $q$ is an open surjective submersion with connected interval fibers, and its smooth quotient is Hausdorff and second countable.

The quotient carries a cooriented contact structure. The identification with $S_h^*\Sigma$ carries it to the kernel of the tautological contact form $\lambda_\Sigma$.

*Proof.* We first justify that a maximal affine null geodesic is inextendible as an unparametrized causal curve. Suppose it had a causal endpoint in $M$. On a relatively compact coordinate neighborhood of that endpoint choose a coordinate $t$ with timelike differential. The future null directions normalized by $\mathrm dt(k)=1$ form a compact sphere bundle over the closure of a smaller neighborhood. In these normalized variables the projective geodesic equation is a smooth ordinary differential equation with bounded coefficients. Parametrization by $t$ therefore gives a limiting direction at a finite limiting value of $t$. For the affine tangent $k$, the equation for $\log k^t$ has the form

$$
\frac{\mathrm d}{\mathrm dt}\log k^t
=-\Gamma^t_{\alpha\beta}w^\alpha w^\beta,
\qquad w=\frac{k}{k^t},\qquad w^t=1.
$$

The right-hand side is bounded on that compact normalized bundle. Thus $k^t$ has a finite positive limit, the affine parameter has a finite limiting value, and the full tangent has a finite nonzero limit. The ordinary geodesic equation extends the solution through the endpoint, contradicting maximality. The past endpoint is treated in the same way.

Every maximal null geodesic consequently meets $\Sigma$ exactly once. Its future tangent can be uniquely normalized by $g(k,n)=1$, giving the stated element of $S_h^*\Sigma$. Smooth ordinary differential equation theory gives the open maximal domain $D_{M,\Sigma}$ and interval fibers.

Existence and uniqueness for the geodesic equation and the unique Cauchy hit make $\Phi_\Sigma$ surjective and injective. In checking injectivity, a repeated phase point on one geodesic would give a closed causal segment, which global hyperbolicity excludes. The inverse is smooth near each phase point: follow the finite geodesic segment to $\Sigma$ through finitely many flow boxes and use the implicit function theorem at the transverse hit. Transversality follows from $g(k,n)>0$. Normalization at the hit and the elapsed affine parameter are smooth. These local inverses agree by uniqueness. Hence $\Phi_\Sigma$ is a diffeomorphism. Projection from its open domain onto $S_h^*\Sigma$ is open and surjective, which also verifies the asserted quotient topology.

Transport the normalized affine tangent $k$ from $\Sigma$ along every ray and define the one-form $\eta=-g(k,\mathrm dp\,\cdot)$ on $F$. For a variation through the normalized affine geodesics, its variation field $J$ satisfies

$$
\frac{\mathrm d}{\mathrm ds}g(k,J)
=g(k,\nabla_Jk)
=\frac12Jg(k,k)=0.
$$

The $s$-direction also pairs to zero because $g(k,k)=0$. At the initial hit, $J$ is tangent to $\Sigma$ and $-g(k,J)=h(v,J)=\lambda_\Sigma(J)$. It follows that

$$
\Phi_\Sigma^*\eta
=\operatorname{pr}_{S_h^*\Sigma}^*\lambda_\Sigma.
$$ {#eq:global-contact-form-flow}

The tautological form on a unit cosphere bundle is a contact form. Thus its contact kernel descends from the null phase. Replacing the normalization multiplies $\eta$ by a positive function constant along each ray, so the contact distribution and its coorientation are intrinsic. ∎

<div id="prop:global-incidence-embedding"></div>

**Proposition 3.3 (Embedded skies and point-labelled incidence).**

For each $x\in M$, the sky $Q_x=q(p^{-1}(x))$ is an embedded Legendrian two-sphere in $\mathcal N(M)$. The map

$$
(q,p):F\longrightarrow\mathcal N(M)\times M
$$ {#eq:global-point-labelled-incidence}

is a proper closed embedding. Its image records the full point-labelled incidence, even when two distinct skies intersect or coincide as subsets of the ray space.

*Proof.* A ray cannot pass through the same spacetime point twice, because the intervening segment would be a closed causal curve. Hence $q|_{p^{-1}(x)}$ is injective. The kernel of $\mathrm dq$ is the geodesic line and projects to a nonzero vector under $\mathrm dp$; it therefore has zero intersection with $\ker\mathrm dp$. The sky map is an immersion. Its domain is the compact sphere $p^{-1}(x)$ and its target is Hausdorff, so it is an embedding. The contact-normal identity in Theorem 3.2 vanishes on the vertical tangent of $p$. The sky is thus an integral two-dimensional submanifold of a contact distribution in dimension five, hence Legendrian.

The map $(q,p)$ is injective by the same ray uniqueness. Its differential is injective because $\ker\mathrm dp\cap\ker\mathrm dq=0$. The sphere bundle $p$ is proper. For a compact subset $K\subset\mathcal N(M)\times M$, the preimage $(q,p)^{-1}(K)$ is a closed subset of the compact set $p^{-1}(\operatorname{pr}_M K)$. Thus $(q,p)$ is proper. A proper injective immersion between Hausdorff manifolds is a closed embedding.

The point label is retained in the second factor. The proof makes no injectivity assumption on the map $x\mapsto Q_x$ into the set of unlabelled subsets of $\mathcal N(M)$. ∎

<div id="prop:global-cauchy-affine-change"></div>

**Proposition 3.4 (Changes of Cauchy normalization).**

Let $\Sigma_a$ and $\Sigma_b$ be two smooth spacelike Cauchy hypersurfaces, with future unit normals $n_a,n_b$. Identify their ray spaces by the underlying rays. Let $k_a$ be the affine tangent normalized at $\Sigma_a$, and define

$$
\tau_{ab}(\gamma)=s_a(\gamma\cap\Sigma_b),
\qquad
r_{ab}(\gamma)=g(k_a,n_b)|_{\gamma\cap\Sigma_b}>0.
$$

Then $\tau_{ab}$ and $r_{ab}$ are smooth. The normalized affine parameters and tangents obey

$$
k_b=r_{ab}^{-1}k_a,
\qquad
s_b=r_{ab}(s_a-\tau_{ab}).
$$ {#eq:global-cauchy-affine-change}

The corresponding contact diffeomorphism $\chi_{ab}:S_{h_a}^*\Sigma_a\to S_{h_b}^*\Sigma_b$ satisfies

$$
\chi_{ab}^*\lambda_b=r_{ab}^{-1}\lambda_a.
$$ {#eq:global-cauchy-contact-multiplier}

Its homogeneous lift to the positive symplectizations is

$$
(z,\rho_a)\longmapsto
\bigl(\chi_{ab}(z),r_{ab}(z)\rho_a\bigr),
$$ {#eq:global-cauchy-homogeneous-lift}

and preserves the tautological one-form $\rho\lambda$. The changes carry the actual affine domains onto each other and satisfy the identity, inverse and triple laws. With all coefficients regarded as functions of the common ray,

$$
r_{ac}=r_{ab}r_{bc},
\qquad
\tau_{ac}=\tau_{ab}+r_{ab}^{-1}\tau_{bc}.
$$ {#eq:global-cauchy-affine-cocycle}

*Proof.* Every ray has a unique transverse hit on $\Sigma_b$. Around any fixed ray, finitely many flow boxes cover the segment from $\Sigma_a$ to that hit. The implicit function theorem for the final transverse intersection gives smooth dependence of the hit time and tangent. The stated functions are therefore smooth at every ray, including rays whose two hits coincide. No bound uniform over the whole ray space is used.

Multiplying $k_a$ by the constant $r_{ab}^{-1}$ gives the normalized initial tangent at $\Sigma_b$. The affine parameter with that tangent and zero at the new hit is exactly $r_{ab}(s_a-\tau_{ab})$. This identifies the maximal intervals, since either extension would extend the same geodesic in $M$.

The contact-normal one-form of Theorem 3.2 changes from $-g(k_a,\mathrm dp)$ to $r_{ab}^{-1}(-g(k_a,\mathrm dp))$. Restriction to the two Cauchy sections gives the contact multiplier. The displayed homogeneous lift then satisfies

$$
(r_{ab}\rho_a)\chi_{ab}^*\lambda_b
=\rho_a\lambda_a.
$$

At the hit on $\Sigma_c$, normalization gives $r_{bc}=r_{ac}/r_{ab}$. Evaluating the parameter change at that hit gives $\tau_{bc}=r_{ab}(\tau_{ac}-\tau_{ab})$. These are the two triple laws. The identity and inverse laws follow by taking repeated indices, or directly from the normalized parameter identities. ∎

The contact multiplier in [the contact-normalization formula](#eq:global-cauchy-contact-multiplier) is the redshift relation of Chernov and Nemirovski ([Chernov and Nemirovski 2018](#ref-ChernovNemirovski2018), Theorem 1.2). With the normalization $g(k_a,n_a)=1$ at the initial hit, the ratio of the frequency at $\Sigma_a$ to that at $\Sigma_b$ is $r_{ab}^{-1}$. The accompanying affine-origin and interval formulas fix its use in the retained source domains.

<div id="sec:causal-restriction-and-geometric-comparison"></div>

### 3.2. Causal restriction and geometric comparison

<div id="lem:common-cauchy-causal-convexity"></div>

**Lemma 3.5 (A common Cauchy hypersurface gives causal convexity).**

Let $U\subset M$ be open, and suppose a hypersurface $S\subset U$ is Cauchy both for $U$ and for $M$. Then $U$ is causally convex in $M$.

*Proof.* Let $\gamma:I\to M$ be an inextendible causal curve. For each connected component $J$ of $\gamma^{-1}(U)$, the curve $\gamma|_J$ is inextendible in $U$. At a finite endpoint of $J$ in $I$, continuity puts the ambient point outside $U$ by maximality of the component. At an endpoint of $I$, a causal extension in $U$ would also extend $\gamma$ in $M$. Thus neither type of endpoint permits an extension in $U$.

Every nonempty component $J$ consequently contains a hit on $S$. The ambient Cauchy property gives exactly one such hit for $\gamma$, so $\gamma^{-1}(U)$ has at most one component. Any causal segment in $M$ extends in both directions to an inextendible causal curve. If both its endpoints belong to $U$, its parameter interval lies in that single component. The entire segment belongs to $U$. ∎

<div id="prop:global-ray-restriction"></div>

**Proposition 3.6 (Restriction and Cauchy embeddings).**

Let $U\subset M$ be a causally convex globally hyperbolic open subspacetime. Extension of geodesics induces a contact diffeomorphism

$$
\mathcal N(U)\longrightarrow
\mathcal N_U(M):=\{\gamma\in\mathcal N(M):\gamma\cap U\ne\varnothing\},
$$ {#eq:global-ray-restriction}

where $\mathcal N_U(M)$ is open in $\mathcal N(M)$. The incidence over $U$ is the restriction of the point-labelled incidence of $M$. In ambient affine coordinates, each realized interval is $\{s\in I_\gamma:\gamma(s)\in U\}$, a nonempty open interval.

If $U$ contains a common Cauchy hypersurface of $U$ and $M$, then $\mathcal N_U(M)=\mathcal N(M)$. An orientation- and time-orientation-preserving isometric embedding identifying marked Cauchy hypersurfaces therefore induces a contact diffeomorphism of their ray spaces and an inclusion of their actual affine domains. A specified spin lift is retained as additional morphism data, with its central sign unchanged.

*Proof.* Causal convexity makes the intersection of any ambient ray with $U$ connected. It is open in the affine parameter and is maximal as a null geodesic in $U$. Conversely every maximal null geodesic of $U$ has a unique maximal geodesic extension in $M$. These operations are inverse on rays. Since $p^{-1}(U)$ is open in $F$ and $q$ is an open submersion, its image $\mathcal N_U(M)$ is open. The quotient of $p^{-1}(U)$ by its connected null leaves is both $\mathcal N(U)$ and this open submanifold, proving the smooth and contact assertions. The incidence and interval statements follow from the same identification.

Every ambient ray meets a common Cauchy hypersurface, so it meets $U$. For a marked development embedding, identify its image with an open subspacetime; an isometric embedding of equal-dimensional manifolds is a local diffeomorphism and has open image. Lemma 3.5 gives causal convexity. Geodesic uniqueness preserves the marked normalized tangents and affine parameters, hence gives interval inclusion. Isometries preserve the contact-normal identity. The spin map is transported as the given principal-bundle map, so no quotient of its sign is introduced. All constructions commute with composition by uniqueness of geodesics. ∎

<div id="prop:global-geometric-recognition"></div>

**Proposition 3.7 (Global geometric comparison from labelled skies).**

For $j=0,1$, let $(M_j,g_j)$ have its full null incidence as above and physical volume density $\mu_j$. Suppose $f:M_0\to M_1$ is an orientation-preserving diffeomorphism and $\Psi:\mathcal N(M_0)\to\mathcal N(M_1)$ is a coorientation-preserving contact diffeomorphism satisfying

$$
\Psi(Q_x)=Q_{f(x)},\qquad f^*\mu_1=\mu_0.
$$

Then $f$ is a time-orientation-preserving isometry, and $\Psi$ is its induced ray map. Conversely every such isometry induces this unique geometric comparison. Any specified compatible principal spin lift is preserved, including its central sign.

*Proof.* By Proposition 3.3, the product map $(\Psi,f)$ restricts to a diffeomorphism $\Phi:F_0\to F_1$ of the embedded incidence manifolds. Let $\alpha_j$ be positive contact forms on corresponding ray charts, with $\Psi^*\alpha_1=a\alpha_0$ and $a>0$. The contact-normal identity yields

$$
\ell_{1,\Phi(u)}\circ\mathrm df_x
=a(q_0(u))\ell_{0,u},
$$

where each $\ell_{j,u}$ is a nonzero past null covector. As $u$ runs over the whole point fiber, these covectors contain every past null direction. Thus $\mathrm df_x$ identifies the complete null cones.

A real quadratic form vanishing on every $(1,v)$ with $|v|=1$ is proportional to the Lorentz form: comparison at $v$ and $-v$ removes its mixed terms, and constancy of its spatial quadratic part on the sphere makes that part a scalar multiple of the Euclidean form. Consequently $f^*g_1=cg_0$ for a smooth nonzero scalar $c$. The common signature $(+---)$ excludes $c<0$. In four dimensions the volume density scales by $c^2$, so density preservation gives $c=1$. The positivity in the contact-normal identity preserves the past component and hence time orientation.

The incidence lift is now the covector lift of $f$. Its action on each ray is determined by geodesic uniqueness, so surjectivity of $q_0$ fixes $\Psi$. The converse follows by applying the actual covector lift of the isometry and descending through the connected null leaves. ∎

<div id="rem:global-geometry-proof-scope"></div>

**Remark 3.8 (Scope of the geometric results).**

The preceding results establish the global real geometric carriers and their actual affine domains. The complete carrier and evaluation comparisons are constructed in §5. In particular, the contact sky $Q_x$ is a smooth embedded Legendrian even when its projection to the base of a chosen carrier develops caustics. Such caustics concern the choice of phase presentation; they do not invalidate the incidence embedding. No assertion that distinct points have distinct unlabelled skies is used.

<div id="sec:p4-global-wave-completion"></div>

## 4. Global wave completion from Cauchy data

Let $(M,g)$ be a smooth, oriented and time-oriented, globally hyperbolic Lorentzian four-manifold without boundary. The signature is $(+---)$, and $P=\Box_g$ acts on scalar functions. Kernels in the spacetime variables use the physical volume density. Write $E=E^{\mathrm{ret}}-E^{\mathrm{adv}}$ for the causal propagator. The scalar results in this section require no Einstein equation or spin structure. Their application to the gravitational source uses the metric recognized from its Cartan fields.

The primed wavefront set is

$$
\operatorname{WF}'(K)=
\{(p,\xi;q,\eta):(p,\xi;q,-\eta)\in\operatorname{WF}(K)\}.
$$

Let $\mathcal C_g^+$ consist of pairs of nonzero null covectors on the same null bicharacteristic, with the frequency component used in Paper 3: in a future Gaussian coordinate, the temporal component of the first covector is $-|\xi|_h$. Both covectors in a pair are nonzero. Reversing both covectors gives the disjoint relation $\mathcal C_g^-$. We use the quotient by $C^\infty(M\times M)$, with no support or decay condition on a smooth representative of the zero class.

Fix a smooth spacelike Cauchy hypersurface $\Sigma$ with future unit normal $n$. If $\rho_\Sigma=|\mathrm dV_h|^{1/2}$ denotes its positive half-density, multiplication of the two scalar traces of §2 by $\rho_\Sigma$ gives the half-density traces

$$
\gamma_0u=\rho_\Sigma u|_\Sigma,
\qquad
\gamma_1u=\rho_\Sigma n(u)|_\Sigma.
$$

Thus each entry of the double trace matrix

$$
\Gamma_\Sigma K=
\bigl((\gamma_i\otimes\gamma_j)K\bigr)_{i,j=0,1}
$$ {#eq:p4-double-trace-matrix}

is a kernel on spatial half-densities. A matrix kernel is called smooth if all four entries are smooth on the whole of $\Sigma\times\Sigma$.

The global distributional Cauchy theorem and the double-Cauchy regularity lemma used below are proved in §2. We use their following consequences. Exact Cauchy evolution $\mathcal U_\Sigma$ extends to arbitrary distributional data; its transpose sends compactly supported test functions on $M$ continuously to compactly supported pairs on $\Sigma$. Double evolution of a smooth initial matrix is jointly smooth. If a bidistribution has smooth residuals for both wave equations and all four double traces are smooth, then the bidistribution is smooth on $M\times M$. These assertions use compact causal shadows and impose no growth condition at spatial infinity.

<div id="sec:p4-local-wave-input"></div>

### 4.1. Local scalar input and its Cauchy class

The local input from Paper 3 is its scalar construction in §6.3–§6.5: the positive normal symbol, the real charge, and Theorem 6.10 ([Isthmus 2026c](#ref-IsthmusSmooth2026)). On a sufficiently small causally convex globally hyperbolic neighborhood $V$, it supplies a classical kernel $L_V$ such that

$$
P_pL_V,\ P_qL_V\in C^\infty(V^2),
\qquad
L_V-L_V^T+iE_V\in C^\infty(V^2),
\qquad
\operatorname{WF}'(L_V)\subset\mathcal C_{g|V}^+.
$$ {#eq:p4-local-wave-input}

The proof of uniqueness in Paper 3 uses only these three tests. In particular, it applies when one of the compared distributions is supplied by another construction, without first assuming an oscillatory representation for that distribution. For a small open disk $O\subset\Sigma\cap V$, its four Cauchy traces have a classical pseudodifferential matrix representative with orders

$$
\begin{pmatrix}-1&0\\0&1\end{pmatrix}.
$$

In the notation of Paper 3, their complete class is

$$
A_O^{\mathrm{can}}=J_OR_O^{-1}J_O^\dagger,
\qquad
J_O=\begin{pmatrix}I\\-Q_O\end{pmatrix}.
$$ {#eq:p4-canonical-local-cauchy-matrix}

The formula includes the physical normal trace and the spatial half-density factors. The symbol of $(A_O^{\mathrm{can}})_{00}$ has leading term $(2|\xi|_h)^{-1}$. All equalities between these classical representatives are modulo smooth kernels. The local normal-symbol and charge calculations are expressions in the smooth metric and its derivatives; no vacuum identity enters these scalar calculations.

These local classes agree on overlaps. Indeed, around each point of an overlap choose a smaller causally convex globally hyperbolic neighborhood contained in both local parents. Causal compatibility identifies both restricted causal propagators with the propagator of that neighborhood. The difference of the two local kernels is symmetric modulo a smooth kernel, while its wavefront set lies in $\mathcal C_g^+$. Transposition puts that same wavefront set in $\mathcal C_g^-$. Their intersection is empty, so the difference is smooth. Taking its four noncharacteristic traces proves agreement of the complete Cauchy classes. The neighborhood may depend on the overlap point; a uniform collar width over a noncompact $\Sigma$ is not used.

<div id="def:p4-canonical-cauchy-class"></div>

**Definition 4.1 (Canonical global Cauchy class).**

A distributional matrix $A$ on $\Sigma\times\Sigma$ has the canonical Cauchy class if it is smooth off the diagonal and, near every diagonal point, it agrees modulo a smooth matrix with the complete class of [the local Cauchy matrix](#eq:p4-canonical-local-cauchy-matrix). Equivalently, it is locally a classical pseudodifferential matrix with the prescribed complete symbols and is smooth off the diagonal.

The definition is a condition on all of $\Sigma\times\Sigma$. Prescribing the complete symbol near the diagonal does not allow additional singularities away from it.

<div id="lem:p4-proper-cauchy-representative"></div>

**Lemma 4.2 (Proper realization of the Cauchy class).**

There is a properly supported classical matrix $A_\Sigma$ in the canonical Cauchy class. Any two distributional matrices in this class differ by a globally smooth matrix. The representative can be chosen Hermitian.

*Proof.* Choose a countable locally finite cover $\{O_i\}$ of $\Sigma$ by relatively compact coordinate disks on which the local Cauchy class is defined. Choose a smooth partition of unity $\{\phi_i\}$ with $\operatorname{supp}\phi_i\Subset O_i$ and functions $\chi_i\in C_c^\infty(O_i)$ equal to one on a neighborhood of $\operatorname{supp}\phi_i$. Let $A_i$ be a classical representative of the local matrix on $O_i^2$. Extend each cut-off kernel by zero and put

$$
A_\Sigma(x,y)=\sum_i\phi_i(x)A_i(x,y)\chi_i(y).
$$ {#eq:p4-proper-cauchy-gluing}

The sum is locally finite. Its support is contained in the union of the compact products $\operatorname{supp}\phi_i\times\operatorname{supp}\chi_i$. A compact set in either factor meets only finitely many $O_i$, so both support projections are proper.

Fix $x_0\in\Sigma$ and a local representative $A_0$ near $(x_0,x_0)$. Only finitely many summands occur near that point. In a neighborhood of the diagonal, the factors $\chi_i$ equal one wherever $\phi_i$ is nonzero. The local compatibility established above therefore gives

$$
A_\Sigma-A_0
=\sum_i\phi_i(A_i-A_0)
\quad\bmod C^\infty
$$

near $(x_0,x_0)$, and the right side is smooth. This also verifies the full symbol, rather than only its principal term. Each summand is smooth away from the diagonal; local finiteness gives the same property for their sum.

If $A$ and $B$ satisfy Definition 4.1, their difference is smooth near every point of the diagonal and is smooth at every off-diagonal point. Hence $A-B$ is smooth on the entire product. Finally, Paper 3's local canonical matrix is Hermitian modulo smooth kernels. The matrix $(A_\Sigma+A_\Sigma^\dagger)/2$ is properly supported, has the same canonical class, and is Hermitian. ∎

<div id="sec:p4-global-hadamard-witness"></div>

### 4.2. A global comparison distribution

We use the established existence of a Hadamard two-point distribution for a scalar normally hyperbolic operator with a smooth real potential on an arbitrary smooth globally hyperbolic spacetime. The potential is zero here. The deformation argument for Hadamard existence goes back to [Fulling, Narcowich and Wald 1981](#ref-FullingNarcowichWald1981). For the operator and sign conventions used below we follow [Gérard and Wrochna 2014](#ref-GerardWrochna2014), §8.2. To match conventions, use the operator $P_{\mathrm{GW}}=-\nabla^a\nabla_a$ of their §8.2 with metric $g_{\mathrm{GW}}=-g$ and zero potential. It equals $\Box_g$; the positive volume density and the advanced and retarded operators are unchanged. Their positive temporal covectors have the opposite sign from the component denoted $\mathcal C_g^+$ here. Their charged covariances satisfy $H_+-H_-=iE$, with the negative temporal component carried by $H_-$. Set

$$
H=\frac12\bigl(H_-+(H_+)^T\bigr).
$$ {#eq:p4-witness-sign-conversion}

Since $E^T=-E$, this gives a global distribution satisfying

$$
P_pH=P_qH=0,
\qquad
H-H^T=-iE,
\qquad
\operatorname{WF}'(H)\subset\mathcal C_g^+.
$$ {#eq:p4-global-hadamard-witness}

This existence result is used to verify the global singularities of a kernel constructed below. Neither $H$ nor its state-dependent smooth part is an input to that construction.

<div id="lem:p4-witness-cauchy-traces"></div>

**Lemma 4.3 (Cauchy traces of a global comparison distribution).**

The four traces $\Gamma_\Sigma H$ exist and have the canonical Cauchy class of Definition 4.1.

*Proof.* The conormal covectors to a spacelike hypersurface are timelike. They cannot equal either nonzero null endpoint covector of $\operatorname{WF}(H)$. The distributional pullback criterion therefore gives every field and normal trace. The same criterion estimates the wavefront set of the trace by restricting the endpoint covectors to $T\Sigma$.

Two distinct points of a spacelike Cauchy hypersurface cannot be joined by a causal curve. Consequently, the restricted null relation has no points over $(x,y)\in\Sigma^2$ with $x\ne y$. All four trace kernels are smooth off the diagonal.

Near a point of the diagonal, choose a local parent $V$ as in §4.1. Causal compatibility gives $E|_{V^2}=E_V$. Thus $H|_{V^2}$ and $L_V$ have the same commutator modulo smooth kernels and the same selected frequency relation. The transposition argument in §4.1 gives $H-L_V\in C^\infty(V^2)$. Taking all four traces identifies the complete matrix class with [the local Cauchy matrix](#eq:p4-canonical-local-cauchy-matrix). ∎

The pullback criterion used here is the standard wavefront-set restriction theorem. Only restriction to a noncharacteristic spacelike hypersurface is needed; the proof does not compose long-ray Fourier integral operators.

<div id="sec:p4-canonical-global-kernel"></div>

### 4.3. Construction and independent characterization

<div id="thm:p4-global-canonical-wave-class"></div>

**Theorem 4.4 (Canonical global wave class).**

There is exactly one class

$$
[\Lambda_g^+]\in\mathcal D'(M\times M)/C^\infty(M\times M)
$$

satisfying

$$
P_p\Lambda_g^+,\ P_q\Lambda_g^+\in C^\infty(M^2),
\qquad
\Lambda_g^+-(\Lambda_g^+)^T+iE\in C^\infty(M^2),
\qquad
\operatorname{WF}'(\Lambda_g^+)\subset\mathcal C_g^+.
$$ {#eq:p4-global-wave-admission}

For any spacelike Cauchy hypersurface $\Sigma$, choose the properly supported Hermitian matrix $A_\Sigma$ of Lemma 4.2. Exact double Cauchy evolution constructs a representative

$$
\Lambda_\Sigma
=\mathcal U_\Sigma A_\Sigma\mathcal U_\Sigma^\dagger.
$$ {#eq:p4-double-cauchy-construction}

This representative is an exact bisolution and can be chosen Hermitian. Its class is independent of the local parents, cover, partition, cutoffs, classical realizations, and Cauchy hypersurface.

*Proof.* Write $\mathcal U_\Sigma=(U_0,U_1)$ for the row of exact solution operators initialized by the two Cauchy data. [The double Cauchy construction](#eq:p4-double-cauchy-construction) means the bidistribution whose two-variable evolution is

$$
\Lambda_\Sigma
=\sum_{i,j=0}^1(U_i\otimes U_j)(A_\Sigma)_{ij}.
$$

The real Cauchy operators are complex-linearly extended. On test functions this is the kernel of the displayed operator expression with the physical volume pairing and the spatial half-density pairing. Its definition is legitimate for arbitrary initial distributional matrix entries because $\mathcal U_\Sigma^t$ maps compactly supported spacetime tests continuously to compactly supported initial tests. The Schwartz kernel theorem, or the tensor product of these continuous test-function maps, then defines a distribution on $M^2$. A compact endpoint set uses only its compact causal shadow on $\Sigma$; no global integral of an unbounded smoothing tail is taken.

Exact Cauchy evolution gives $P_p\Lambda_\Sigma=P_q\Lambda_\Sigma=0$ and $\Gamma_\Sigma\Lambda_\Sigma=A_\Sigma$. It commutes with complex conjugation, so the Hermitian choice in Lemma 4.2 makes $\Lambda_\Sigma$ Hermitian.

Choose the global comparison distribution $H$ from §4.2. Lemmas 4.2 and 4.3 give

$$
A_\Sigma-\Gamma_\Sigma H\in C^\infty(\Sigma^2;M_2(\mathbb C)).
$$

Both $H$ and $\Lambda_\Sigma$ are exact bisolutions. Their difference has the displayed smooth double Cauchy data. The double-Cauchy regularity lemma therefore yields

$$
\Lambda_\Sigma-H\in C^\infty(M^2).
$$ {#eq:p4-construction-witness-smoothing}

[The comparison identities](#eq:p4-global-hadamard-witness) now prove both the global frequency condition and the commutator condition in [the admission equations](#eq:p4-global-wave-admission). This comparison checks long null propagation on the whole product, including pairs outside every single local construction chart.

For uniqueness, let $D$ be the difference of two admitted kernels. Their commutator equations give $D-D^T\in C^\infty(M^2)$. Hence $D$ and $D^T$ have the same wavefront set. The former is contained in the selected frequency relation, while transposition of that relation puts the latter in the opposite component. Both endpoint covectors are nonzero, so these components are disjoint. Thus $\operatorname{WF}(D)$ is empty and $D$ is smooth globally.

All choices in the construction, including the choice of $\Sigma$, produce kernels satisfying the same three global tests. Their classes are equal by uniqueness. ∎

<div id="thm:p4-global-cauchy-characterization"></div>

**Theorem 4.5 (Cauchy characterization).**

Let $\Lambda\in\mathcal D'(M^2)$ satisfy

$$
P_p\Lambda,\ P_q\Lambda\in C^\infty(M^2).
$$

Then the following conditions are equivalent.

1. The class of $\Lambda$ satisfies the global frequency and commutator conditions in [the admission equations](#eq:p4-global-wave-admission).
2. For one entire spacelike Cauchy hypersurface $\Sigma$, the four traces $\Gamma_\Sigma\Lambda$ have the canonical Cauchy class of Definition 4.1.
3. For every entire spacelike Cauchy hypersurface $\Sigma$, the four traces have that class.

No Riemannian metric completeness is required. In conditions 2 and 3, the trace matrix has a properly supported classical representative modulo a globally smooth matrix.

*Proof.* Apply the noncharacteristic trace argument of Lemma 2.7 to the smooth residuals in both wave variables. For example, a conormal covector to $\Sigma\times M$ has a nonzero timelike first component and zero second component, so $P_p$ is elliptic at that covector. Smoothness of $P_p\Lambda$ excludes it from $\operatorname{WF}(\Lambda)$. Put $d_i=(\gamma_i\otimes I)\Lambda$. Then $P_qd_i=(\gamma_i\otimes I)P_q\Lambda$ is jointly smooth, so the same ellipticity argument gives both second-variable Cauchy traces of $d_i$. Taking a normal derivative does not enlarge the wavefront set. This argument also permits wavefront covectors whose other endpoint component is zero before the traces are taken.

Assume condition 1. Theorem 4.4 identifies $\Lambda$ modulo a globally smooth kernel with the representative constructed on any chosen $\Sigma$. Taking the four traces proves condition 3. Condition 3 implies condition 2.

Assume condition 2, and construct $\Lambda_\Sigma$ by Theorem 4.4 on the stated hypersurface. By Lemma 4.2,

$$
\Gamma_\Sigma(\Lambda-\Lambda_\Sigma)
\in C^\infty(\Sigma^2;M_2(\mathbb C)).
$$

The two wave residuals of $\Lambda-\Lambda_\Sigma$ are smooth. The double-Cauchy regularity lemma gives $\Lambda-\Lambda_\Sigma\in C^\infty(M^2)$. Therefore $\Lambda$ has the same global wavefront and commutator class, proving condition 1. The proper-representative statement follows from Lemma 4.2. ∎

The bisolution condition is a premise of Theorem 4.5. A condition on initial traces alone does not control a bidistribution added away from the initial hypersurface. The off-diagonal smoothness in Definition 4.1 is likewise part of the condition; a symbol near the diagonal does not determine it.

<div id="cor:p4-causal-wave-naturality"></div>

**Corollary 4.6 (Causal naturality and local comparison).**

Let $f:(N,h)\to(M,g)$ be an orientation- and time-orientation-preserving isometric open embedding between smooth globally hyperbolic spacetimes, with causally convex image. Then

$$
(f\times f)^*[\Lambda_g^+]=[\Lambda_h^+].
$$

In particular, on every retained causally convex local wave parent of Paper 3, the restriction of the global class is its canonical local scalar class. These comparisons preserve identities, compositions, and further causally convex restrictions.

*Proof.* The scalar operator and physical volume are invariant under $f$. The support characterization and uniqueness of advanced and retarded Green operators identify the restricted causal propagator with $E_h$ ([Bär, Ginoux and Pfäffle 2007](#ref-BarGinouxPfaeffle2007), Proposition 3.5.1). A null segment in $M$ with both endpoints in $f(N)$ remains in $f(N)$ by causal convexity. The restricted global frequency relation is therefore the frequency relation of $N$. Pullback of the global class satisfies all three tests of Theorem 4.4 on $N$ and hence is the unique such class. Local comparison is the same uniqueness argument using the local kernel of §4.1. The composition assertions follow from functoriality of pullback and equality of the resulting classes. ∎

<div id="sec:whole-cauchy-condition"></div>

### 4.4. The role of the whole Cauchy condition

<div id="ex:torus-remote-bisolution"></div>

**Example 4.7 (A symmetric remote bisolution).**

Take

$$
M=\mathbb R_t\times T^3,\qquad
g=\mathrm dt^2-(\mathrm dx^1)^2-(\mathrm dx^2)^2-(\mathrm dx^3)^2.
$$

Let $x^1$ have period $L$, put $u=t-x^1\pmod L$, and choose $0<a<L/2$. Define

$$
K(p,q)=
\delta_{S^1}\bigl(u(p)-u(q)-a\bigr)
+\delta_{S^1}\bigl(u(p)-u(q)+a\bigr).
$$

Then $K$ is a real symmetric exact bisolution, vanishes on an open neighborhood of the whole spacetime diagonal, and is globally singular. It violates the global positive null relation. Its field–field trace on $\{t=0\}^2$ is singular away from the diagonal even though this Cauchy surface is compact.

*Proof.* The maps $u(p)-u(q)\mp a$ to the circle are submersions, so the pullback delta distributions are defined. Locally $u$ is affine and $\mathrm du=\mathrm dt-\mathrm dx^1$ is null. Differentiating a distributional function of this affine null coordinate therefore gives

$$
P_pK=P_qK=0.
$$

Transposition interchanges the two summands; the evenness of the circle delta gives $K^T=K$. The set

$$
\{(p,q):d_{S^1}(u(p),u(q))<a/2\}
$$

is an open neighborhood of the full diagonal on which both summands vanish.

The two support hypersurfaces are disjoint because $0<a<L/2$. On either one, the wavefront covectors are

$$
(p,q;\lambda\,\mathrm du_p,-\lambda\,\mathrm du_q),
\qquad\lambda\ne0.
$$

After priming the second endpoint they become $(p,\lambda\,\mathrm du_p;q,\lambda\,\mathrm du_q)$. The vector dual to $\mathrm du$ is $\partial_t+\partial_{x^1}$; its null trajectories keep $u$ constant modulo $L$. The support condition $u(p)-u(q)=\pm a$ therefore prevents these endpoint covectors from lying on one null bicharacteristic. Both signs of $\lambda$ occur as well.

On $\Sigma=\{t=0\}$ the field–field trace is

$$
K_{00}(x,y)
=\delta_{S^1}(y^1-x^1-a)
+\delta_{S^1}(y^1-x^1+a).
$$

Its support is disjoint from the diagonal and its hypersurface singularities are nonzero. A classical pseudodifferential kernel is smooth off the diagonal, so $K_{00}$ is not such a kernel modulo a globally smooth remainder. Proper support is automatic on $\Sigma\times\Sigma$ because $\Sigma$ is compact; it does not remove this example. ∎

For any admitted global kernel $H$, the kernel $H+K$ has the same local restrictions as $H$ on sufficiently small point neighborhoods, the same wave equations, and the same commutator. It fails the global wavefront and Cauchy tests.

The local-to-global singularity theorem of Radzikowski assumes positive type for both the reference and compared two-point distributions, a wavefront-set condition on the reference, and agreement of the antisymmetric parts modulo smooth kernels and of the local singularity structure ([Radzikowski 1996](#ref-RadzikowskiVerch1996)). The admission used here imposes no positive-type condition. Example 4.7 identifies why the whole-Cauchy test is needed in this larger class.

<div id="rem:p4-wave-proof-scope"></div>

**Remark 4.8 (Scope of the fixed-background result).**

Theorem 4.4 constructs one actual global bidistribution before passing to complete classes. The metric and causal propagator are exact, while the kernel class discards globally smooth terms. The theorem is proved for a fixed smooth metric. A result for varying metrics requires joint smoothness in the parameter and both spacetime variables, with common compact causal domains for the local estimates; pointwise application of the theorem does not establish that additional assertion. Section 13 proves it under the supplied common Cauchy hypotheses, including the compact causal control needed on noncompact spacetimes.

The scalar result supplies the common kernel needed to compare distant carriers. Section 5 proves preservation of Paper 3's internal complex-linear adjoint, full moving modules and point connections on this fixed background. Sections 6–7 give the independent admission and source comparison results, retaining the stored associator cells.

<div id="sec:global-carrier-completion"></div>

## 5. Global carrier comparisons and evaluation

The scalar construction of §4 applies to a general globally hyperbolic metric. Here we assume that $g$ is Ricci-flat in order to use the local normalizations and complete modules of Paper 3. We retain the physical scale. All equalities of operator classes are modulo smooth kernels, and all products use properly supported representatives or the compact-local Cauchy construction of §2.

For the Fourier integral description of exact Cauchy evolution we use Bär–Strohmaier, Appendix A, Theorem A.1 ([Bär and Strohmaier 2019](#ref-BarStrohmaier2019)). Transverse composition uses Duistermaat, §1, Theorem 1.1, with its properness hypotheses on both the canonical-relation projection and the projection of the intersected kernel supports ([Duistermaat 1972](#ref-Duistermaat1972)). The whole-carrier graph maps supply the transverse relation composition, while Proposition 2.4 and the proper representatives used below supply the required kernel support. Lemma 5.2 applies these inputs to the selected local normal branch.

For a spacelike Cauchy hypersurface $\Sigma_a$, let $\mathcal H_a=|\Lambda^3T^*\Sigma_a|^{1/2}$ be its half-density line. Write $\gamma_0^a u=u|_{\Sigma_a}\mu_a^{1/2}$ and $\gamma_1^a u=n_a(u)|_{\Sigma_a}\mu_a^{1/2}$, where $\mu_a$ is the volume density of $h_a=-g|_{T\Sigma_a}$. A subscript $ab$ on an operator means that it acts from the $b$ carrier to the $a$ carrier; its ray map runs in the direction inverse to $\chi_{ab}$ of Proposition 3.4. Denote the fixed-background canonical class of Theorem 4.4 by $[\Lambda_g^+]$.

<div id="def:global-mixed-carrier-traces"></div>

**Definition 5.1 (Mixed traces and positive roots).**

For two whole Cauchy hypersurfaces, define

$$
C_{ab}=(\gamma_0^a\otimes\gamma_0^b)\Lambda_g^+,
\qquad C_a=C_{aa},\qquad W_a=C_a^{-1/2}.
$$ {#eq:global-mixed-carrier-traces}

The inverse square root is taken in the classical complete-symbol calculus, with positive physical principal symbol. The normalized comparison is

$$
T_{ab}=W_aC_{ab}W_b.
$$ {#eq:global-normalized-carrier}

These classes are well defined. The wavefront restriction is permitted because a nonzero null covector cannot be conormal to a spacelike hypersurface. The Cauchy characterization identifies $C_a$ with the canonical scalar operator of order $-1$ on $\Sigma_a$, with

$$
\sigma_{-1}(C_a)(x,\xi)=\frac{1}{2|\xi|_{h_a}}.
$$

It is Hermitian in the quotient. Symbol recursion therefore gives a unique Hermitian complete class $W_a$ with positive principal symbol, $W_a^2=C_a^{-1}$, and $W_aC_aW_a=I$. Existence of properly supported representatives uses locally finite quantization; no uniform ellipticity constant at spatial infinity is asserted.

<div id="lem:global-positive-graph-factorization"></div>

**Lemma 5.2 (Positive-branch factorization).**

Fix a reference Cauchy hypersurface $\Sigma$. There are globally defined complete classes $Q\in\Psi^1(\Sigma;\mathcal H)$ and $R\in\Psi^1(\Sigma;\mathcal H)$, with $R$ Hermitian and positive elliptic principal symbol, such that the canonical four-trace class is

$$
A_\Sigma=JR^{-1}J^\dagger,\qquad
J=\begin{pmatrix}I\\-Q\end{pmatrix}.
$$ {#eq:global-positive-initial-factorization}

Let $\mathcal U_\Sigma$ be exact Cauchy evolution with the two half-density traces as initial data. Put

$$
E_a=\gamma_0^a\mathcal U_\Sigma J.
$$

Then $E_a$ has a properly supported representative and is an elliptic classical Fourier integral operator of order zero on the full homogeneous null-flow graph from $T^*\Sigma\setminus0$ to $T^*\Sigma_a\setminus0$. It has a properly supported inverse in the complete graph calculus. Moreover,

$$
C_{ab}=E_aR^{-1}E_b^\dagger.
$$ {#eq:global-positive-graph-factorization}

*Proof.* Write $A_{ij}$ for the four entries of the canonical initial matrix. Since $A_{00}$ is elliptic, define its complete inverse $R=A_{00}^{-1}$ and set $Q=-A_{10}R$. In a Gaussian patch these are exactly the normal root and charge classes of Paper 3, Theorem 6.6 and Proposition 6.7. The local factorization there is $A=JR^{-1}J^\dagger$ ([Isthmus 2026c](#ref-IsthmusSmooth2026), Theorem 6.10 and §6.6). It holds to every degree at every nonzero cotangent point. Each of its entries is pseudodifferential and smooth off the diagonal, so it is a global complete-class identity. The local Hermiticity and positive principal symbol of $R$ give the stated global properties. Choose proper representatives by cutting off near the diagonal.

The exact Cauchy transfer from $\Sigma$ to $\Sigma_a$ is properly supported in both variables by Proposition 2.4. Composing its field row with proper representatives of $I$ and $Q$ therefore gives a proper representative of $E_a$.

We identify the spacetime Cauchy kernel before taking the target trace. Bär–Strohmaier, Theorem A.1, places the two exact Cauchy operators in the classical Fourier integral calculus on the union of the two spacetime null-flow relations ([Bär and Strohmaier 2019](#ref-BarStrohmaier2019)). Composition with the proper pseudodifferential column $J$ preserves that wavefront containment. Denote the selected and opposite components by $\mathcal R_\Sigma^{\mathrm{sel}}$ and $\mathcal R_\Sigma^{\mathrm{opp}}$. Thus

$$
\operatorname{WF}'(\mathcal U_\Sigma J)
\subset \mathcal R_\Sigma^{\mathrm{sel}}
\cup\mathcal R_\Sigma^{\mathrm{opp}}.
$$ {#eq:global-cauchy-two-branch-relation}

Both endpoint covectors are nonzero. This global assertion excludes additional singularities away from these relations, including any arising from distant point pairs.

On a sufficiently small Cauchy domain of dependence of a larger initial disk, the exact evolution of $J$ agrees with the positive-branch parametrix of Paper 3, Theorem 6.6, modulo a smooth kernel. Use a full short Cauchy parametrix on that domain, with the initial coordinate retained as a passive variable. The field and normal traces agree modulo smoothing and the wave residual is smooth, so Lemma 2.6 applies. Carrier and coordinate cutoffs are chosen to equal one on this entire smaller domain of dependence. Consequently the complete amplitude on $\mathcal R_\Sigma^{\mathrm{opp}}$ vanishes in the initial collar, and the initialized leading amplitude on $\mathcal R_\Sigma^{\mathrm{sel}}$ is nonzero.

The exact spacetime kernel satisfies $P(\mathcal U_\Sigma J)=0$. Along either component, its leading Fourier integral symbol therefore obeys the homogeneous transport equation of the Cauchy FIO calculus. On the opposite component it has zero initial value and hence vanishes along each null segment. After lowering the order, the next symbol has the same homogeneous transport equation, because the earlier coefficients and the wave residual vanish. Induction proves vanishing at every homogeneous order. Each segment from the initial hit to a specified spacetime covector is compact, so finitely many flow and phase charts carry out this induction through any caustics. On the selected component, the nonzero initialized leading symbol solves an invertible scalar transport equation and remains nonzero. We have therefore obtained a classical elliptic kernel on $\mathcal R_\Sigma^{\mathrm{sel}}$, modulo a kernel smooth on the whole spacetime–initial product.

For the composition with restriction, the restriction kernel is supported on the graph of the embedding $\iota_a:\Sigma_a\hookrightarrow M$. On the intersection of the two kernel supports in $\Sigma_a\times M\times\Sigma$, the intermediate point is $m=\iota_a(x)$. Projection to the outer variables $(x,y)$ is a homeomorphism onto the closed preimage of $\operatorname{supp}(\mathcal U_\Sigma J)$ under $(x,y)\mapsto(\iota_a(x),y)$ and is therefore proper. The selected null branch meets the spacelike section transversely, giving the homogeneous return graph of Proposition 3.4 and an order-zero field propagator by Duistermaat's composition theorem ([Duistermaat 1972](#ref-Duistermaat1972), §1, Theorem 1.1). All local phase expressions are expressions for this same exact kernel, so their half-density and phase-transition factors agree on overlaps. Several rays may connect the same pair of base points; their distinct cotangent data are retained. A one-ray phase expression represents the kernel only on its retained conic neighborhood, whereas the global wavefront containment and the branch elimination above control the rest of the product. The argument also applies when the two Cauchy hypersurfaces intersect.

For the inverse, form $H_a=E_a^\dagger E_a$. Proper graph composition puts $H_a$ in $\Psi^0(\Sigma;\mathcal H)$, and its principal symbol is the positive squared norm of the elliptic Fourier integral symbol. Let $G_a$ be a properly supported complete parametrix of $H_a$ and put $F_a=G_aE_a^\dagger$. Then $F_aE_a=I$ in the complete quotient. The class $\Pi_a=E_aF_a$ is an order-zero pseudodifferential idempotent on the target, with principal symbol one. Hence $Z_a=I-\Pi_a$ is an idempotent of order at most $-1$. The identity $Z_a=Z_a^2$ first lowers its order to at most $-2$ and, by repetition, to every negative order. Thus $Z_a$ has a smooth kernel, and $E_aF_a=I$ in the quotient. This proves both-sided invertibility with proper representatives. The construction uses the actual operator and its adjoint, so it requires no choice of a global scalar phase or independent trivialization of a Maslov line.

Finally, the global initial factorization and exact double evolution give

$$
\Lambda_g^+=\mathcal U_\Sigma JR^{-1}J^\dagger\mathcal U_\Sigma^\dagger
\quad\bmod C^\infty(M^2).
$$

Taking the two field traces proves the asserted mixed factorization. The change from the original glued initial representative to this factorized representative is globally smooth, so Lemma 2.7 justifies this replacement before taking traces. ∎

<div id="thm:global-carrier-cocycle"></div>

**Theorem 5.3 (Normalized comparisons between whole Cauchy surfaces).**

The classes $T_{ab}$ are properly supported elliptic Fourier integral classes of order zero on the full homogeneous null-flow graphs. Composing properly supported representatives and taking their complete classes gives

$$
\begin{aligned}
C_{ab}C_b^{-1}C_{bc}&=C_{ac},\\
T_{aa}&=I,\qquad T_{ab}T_{bc}=T_{ac},\\
T_{ab}^{-1}&=T_{ba}=T_{ab}^\dagger .
\end{aligned}
$$ {#eq:global-carrier-cocycle}

Conjugation by $T_{ab}$ identifies the complete pseudodifferential algebra sheaves on the two ray carriers. It preserves filtration and the complex-linear internal adjoint of Paper 3. It acts on the whole sky modules and obeys the same inverse and cocycle laws there. The comparisons are natural under time-oriented isometries and restrict to their local carrier counterparts. The two Cauchy hypersurfaces may intersect.

*Proof.* By Lemma 5.2, the complete inverse of $C_b=E_bR^{-1}E_b^\dagger$ is

$$
C_b^{-1}=(E_b^\dagger)^{-1}R E_b^{-1}.
$$

Inserting this expression between $C_{ab}$ and $C_{bc}$ cancels the inverse factors and proves the first identity. The identities for $T$ follow from $W_b^2=C_b^{-1}$ and $W_aC_aW_a=I$. Hermiticity gives $C_{ab}^\dagger=C_{ba}$ and $W_a^\dagger=W_a$, hence the adjoint formula. All compositions are defined with proper representatives. The proper smooth kernels form a two-sided ideal in these compositions, so the computations hold in the stated quotient.

The graph composition theorem gives a filtered algebra isomorphism under conjugation. The physical Hermitian-adjoint identity alone would not prove preservation of the complex-linear internal adjoint. For that assertion, fix a ray segment between the two carrier hits. Cover it by finitely many causally convex globally hyperbolic neighborhoods contained in Gaussian coordinate charts. Subdivide the segment and choose its successive carrier disks inside these neighborhoods. In each neighborhood use moving spacelike disks through the successive hits, and in the overlaps join the incoming and outgoing disks by the spacelike isotopies of Paper 3, Lemma 6.13. If the endpoint hits coincide, only a local interpolation is needed. Transverse intersection and compactness of this finite segment give smaller ray neighborhoods and positive boundary margins for all the required disks.

The global kernel restricted to each of these causally convex neighborhoods has the local canonical class, by Corollary 4.6. Thus the normalized comparison on each short step is the comparison of Paper 3, Theorem 6.14. Its conjugation preserves the internal adjoint by the formally real, internally skew normalized generator of Lemma 6.13. The mixed-factorization cancellation also holds for these localized disk carriers, because their return maps are invertible on the retained ray neighborhood. Consequently the finite product equals the restriction of the global $T_{ab}$. It preserves the internal adjoint on that neighborhood. Such neighborhoods cover the whole ray space, proving the assertion globally.

Graph Fourier integral operators take the complete Lagrangian module of a sky to the module of that sky on the other carrier. Their action contains the full classical amplitude. Actual operator composition proves semilinearity and all inverse and cocycle identities on these modules. The local phase transitions, including their native half-density factors, are those of the actual Fourier integral distributions.

An isometry carries the scalar canonical class to its counterpart by Corollary 4.6 and carries the physical half-density traces to the corresponding traces. It therefore carries $C_{ab}$. The uniqueness of the positive-principal complete root carries $W_a$, and their defining product carries $T_{ab}$. Restriction to a retained ray domain restricts these same formulas. ∎

<div id="def:global-point-evaluation"></div>

**Definition 5.4 (Point evaluation and moving module).**

For a fixed whole Cauchy carrier $\Sigma_a$, retain the point slot as a scalar and put

$$
C_{ap}=\gamma_0^a\Lambda_g^+(\,\cdot\,,p),
\qquad e_a(p)=W_aC_{ap}.
$$ {#eq:global-point-evaluation}

Let $L_{a,p}\subset T^*\Sigma_a\setminus0$ be the conic Lagrangian obtained by returning all chosen-branch null covectors at $p$ to $\Sigma_a$. Let $\mathscr M_a$ be the sheaf, in the point variable, of smooth classical Lagrangian distribution families on these $L_{a,p}$, valued in $\mathcal H_a$, with locally uniform symbol estimates after every finite point derivative. The permitted orders form the integer lattice of Paper 3: in point-conormal charts the homogeneous amplitude degrees are $j-\tfrac32$, $j\in\mathbb Z$, or equivalently $\tau^{j-1/2}$ in its normalized angular charts. The upper integer order is locally bounded. The actual half-density and Maslov transition factors are retained. Take the quotient by kernels smooth jointly in the point and carrier variables. Use the shifted module filtration of Paper 3, Proposition 6.3 and Definition 6.18.

The point label is retained in this definition. Its microlocal support is the labelled incidence in Proposition 3.3, or its homogeneous lift. It is not a single module obtained by identifying all points on a ray.

<div id="thm:global-evaluation-and-point-connection"></div>

**Theorem 5.5 (Full evaluation and point differentiation).**

The family $e_a$ is a well-defined global class of distribution-valued smooth families. It is elliptic and locally cyclic along every sky, with shifted filtration degree one. For every $p\in M$,

$$
T_{ab}e_b(p)=e_a(p).
$$ {#eq:global-evaluation-covariance}

Actual differentiation in the point variable defines a connection on $\bigcup_\ell F_\ell\mathscr M_a$. With $\nabla_X^{\mathrm{alg}}P=XP$ for point-dependent operator families, it satisfies

$$
\begin{aligned}
\nabla_X^{\mathrm{amb}}(fm)&=(Xf)m+f\nabla_X^{\mathrm{amb}}m,\\
\nabla_X^{\mathrm{amb}}(Pm)&=(XP)m+P\nabla_X^{\mathrm{amb}}m,\\
\nabla_X^{\mathrm{amb}}F_\ell\mathscr M_a&\subset F_{\ell+1}\mathscr M_a,\\
[\nabla_X^{\mathrm{amb}},\nabla_Y^{\mathrm{amb}}]
&=\nabla_{[X,Y]}^{\mathrm{amb}}.
\end{aligned}
$$ {#eq:global-point-connection}

The carrier maps intertwine these connections on every module section and every operator section.

*Proof.* The positive null relation has a nonzero carrier covector after restriction to $\Sigma_a$. Therefore fixing the point variable has no wavefront obstruction. The same absence of covectors purely conormal to a point slice gives a smooth distribution-valued family. For a compact set of points, the full phase fiber above it is compact because $p:F\to M$ is a sphere bundle and is proper. Its image under the Cauchy-hit map is therefore compact as well. A finite collection of the flow and phase neighborhoods used in Lemma 5.2 covers these directions and their retained compact segments. It supplies smooth nondegenerate phase charts with locally uniform symbol estimates for the whole family over that point set.

The mixed factorization remains valid when the second spacetime variable is retained as a point variable. The inverse cancellation in Theorem 5.3 gives

$$
C_{ab}C_b^{-1}C_{bp}=C_{ap}.
$$

Multiplication by $W_a$ proves the full evaluation identity. The operator $T_{ab}$ depends on the two fixed carriers and the background, not on the evaluated point.

If $p=b\in\Sigma_a$, the point column is $C_a(\rho_a(b)^{-1}\delta_b)$ in local half-density coordinates, where $\rho_a=(\det h_a)^{1/4}$. Thus

$$
e_a(b)=W_a^{-1}\bigl(\rho_a(b)^{-1}\delta_b\bigr).
$$

Its physical amplitude is nonzero with principal factor $(2|\xi|_{h_a})^{-1/2}\rho_a(b)^{-1}$, and with the Fourier normalization of Paper 3 the additional constant is $(2\pi)^{-3/2}$. This has shifted degree one. For a point away from $\Sigma_a$, use a small spacelike disk through it and the localized carrier comparison of Theorem 5.3. The preceding calculation and invertibility of that comparison establish ellipticity and local cyclicity in every sky direction. This is the all-order module calculation of Paper 3, Proposition 6.16, transported by the actual comparison.

For the connection, differentiate an actual local representative

$$
m(p,x)=\int e^{i\phi(p,x,\vartheta)}
a(p,x,\vartheta)\,\mathrm d\vartheta\,|\mathrm dx|^{1/2}.
$$

The differentiated amplitude is $Xa+i(X\phi)a$. The phase is homogeneous of degree one, so this raises the order by at most one. Differentiating a jointly smooth remainder keeps it jointly smooth. The operation is therefore independent of representatives and of phase coordinates. The scalar and algebra Leibniz rules, and the commutator identity, hold for actual distributions before passage to the quotient. They give the asserted connection laws.

Finally $T_{ab}$ is point-independent. Differentiation commutes with its action on every family, using properly supported representatives on each retained carrier chart. Thus the carrier operator intertwines both connections. The point derivative raises filtration order; covariance across carriers comes from the mixed kernel. ∎

<div id="rem:scalar-completion-scope"></div>

**Remark 5.6 (Scope of the wave completion).**

The wave enrichment compares whole Cauchy carriers and point-labelled modules over a recognized metric. Its scalar operators cannot distinguish the two central spin lifts. Sections 6–7 therefore retain the principal spin map as independent geometric data in a full comparison.

<div id="sec:global-independent-geometric-admission"></div>

## 6. Independent geometric and scalar admission

We first describe the geometric base without choosing a global Gaussian clock or a maximal hypersurface. We use the full finite Cartan equations obtained in Paper 3, Theorem 2.9 ([Isthmus 2026c](#ref-IsthmusSmooth2026)), and formulate them directly on the point manifold. This removes the initialized collar from the global definition while retaining its actual soldering, connection, curvature and principal spin data. The ordinary-pair construction and its local coverage theorem are not inputs to the recognition argument below.

<div id="sec:global-cartan-base"></div>

### 6.1. The unmarked Cartan base

<div id="def:global-cartan-base"></div>

**Definition 6.1 (Global vacuum Cartan data).**

Let $M$ be a connected oriented smooth four-manifold. The data consist of an oriented and time-oriented real rank-four bundle $(\mathbb E,\eta)$ of Lorentzian signature $(+---)$, an actual principal $\operatorname{Spin}^+(1,3)$ lift $\mathcal P$ of its oriented and time-oriented orthonormal frame bundle, and the following smooth fields:

1. An orientation-preserving bundle isomorphism $\theta:TM\to\mathbb E$.
2. A real $\eta$-metric connection $D$ on $\mathbb E$, with its induced connection on the specified spin lift.
3. A real algebraic Weyl tensor $C$ on $\mathbb E$.
4. A positive point density $\mu$.

As in Paper 3, put

$$
\eta\bigl(\mathcal C(u,v)z,w\bigr)=C(u,v,z,w).
$$

The finite differential and normalization tests are

$$
\begin{aligned}
D_X\theta(Y)-D_Y\theta(X)-\theta([X,Y])&=0,\\
\Omega_D(X,Y)&=\mathcal C(\theta X,\theta Y),\\
\mu&=\mu_\theta,
\end{aligned}
$$ {#eq:global-cartan-admission}

where $\mu_\theta$ is the pullback by $\theta$ of the positive Lorentzian volume density of $\eta$. Causality is defined directly by the inverse image under $\theta$ of the future cone of $\eta$. Require this cone field to be strongly causal and to have compact causal diamonds. These are the global hyperbolicity tests for the supplied causal cone.

Every field in this definition is supplied on all of $M$. The algebraic Weyl condition includes the curvature symmetries, the first algebraic Bianchi identity and vanishing Ricci contraction. It imposes no vanishing condition on either Weyl chirality. The definition contains no ordinary pair, extension operator, prior spacetime development, or existential assertion that these fields arise from a constructor.

<div id="prop:global-cartan-recognition"></div>

**Proposition 6.2 (Global Cartan recognition).**

On the given point manifold, the soldering and Lorentz form determine the physical metric; the bundle connection induces a tangent connection by the same identification. Explicitly,

$$
g(X,Y)=\eta(\theta X,\theta Y),
\qquad
\nabla_XY=\theta^{-1}D_X(\theta Y).
$$ {#eq:global-cartan-readout}

This is a smooth, oriented and time-oriented globally hyperbolic Ricci-flat metric at its specified scale. The connection $\nabla$ is its Levi–Civita connection, the supplied $C$ is its actual Weyl curvature, and $\mathcal P$ becomes an actual spin structure for $g$ by the frame map induced by $\theta^{-1}$. Its two chiral curvature blocks are the two blocks of the actual Weyl tensor.

Conversely, every spacetime in the stated gravitational scope gives such data by taking $\mathbb E=TM$, $\theta=I$, $D=\nabla^g$, $C=\operatorname{Weyl}(g)$, and its actual spin bundle and volume density. These constructions are inverse up to the explicit soldering identification. A specified orientation- and time-orientation-preserving spin isometry determines its unique Cartan comparison, and these comparisons preserve identities, inverses and composition.

*Proof.* The invertible soldering makes the displayed $g$ a smooth nondegenerate metric of the required signature. Its time orientation is exactly the supplied cone. Metric compatibility of $D$ gives $\nabla g=0$. Its torsion is

$$
T^\nabla(X,Y)
=\theta^{-1}\bigl(D_X\theta(Y)-D_Y\theta(X)-\theta([X,Y])\bigr)=0.
$$

Thus $\nabla$ is the Levi–Civita connection. Conjugating its curvature by $\theta$ gives

$$
\theta\bigl(R^\nabla(X,Y)Z\bigr)
=\Omega_D(X,Y)\theta Z
=\mathcal C(\theta X,\theta Y)\theta Z.
$$

The algebraic Weyl trace condition therefore gives $\operatorname{Ric}(g)=0$, and $C$ is precisely the Weyl curvature under the soldering. The differential Bianchi identity follows from the Levi–Civita connection and need not be supplied as additional freely prescribed curvature data. The density equality gives the actual physical volume. The causal curves and diamonds defined by $\theta$ are those of $g$, so the global causal tests give global hyperbolicity.

An oriented $\eta$-orthonormal frame of $\mathbb E$ becomes an oriented $g$-orthonormal frame of $TM$ by composition with $\theta^{-1}$. Composing the supplied principal spin projection with this frame isomorphism gives the recognized actual spin structure. This operation is an isomorphism of the given bundles and retains their central action. On the complexified two-form bundle, the Hodge operator has eigenvalues $\pm i$; the Weyl endomorphism preserves the two eigensubbundles. The two restrictions of the supplied real $C$ are consequently the actual, Lorentz-related chiral Weyl fields.

For the converse, the torsion and curvature equations are the standard identities of $\nabla^g$, and the remaining tests are its given metric, spin and causality conditions. Starting instead with supplied Cartan data, the canonical data of the recognized metric are identified with them by $\theta$, with the corresponding actual principal spin map. The connection identity follows from the definition of $\nabla$, and the curvature identity was just proved.

For an isometry $f:(M_0,g_0)\to(M_1,g_1)$, the only possible soldering-compatible Lorentz map is

$$
L=\theta_1\circ\mathrm df\circ\theta_0^{-1}.
$$ {#eq:global-cartan-comparison-map}

It preserves $\eta$. The isometry preserves the Levi–Civita connection and curvature, so $L$ intertwines the supplied $D$ and $C$. The specified actual spin lift is transported through the same two frame identifications. Conversely a Lorentz bundle comparison with this soldering identity preserves $g$. All formulas are functorial under composition. ∎

The use of the full Cartan identities in Definition 6.1 is equivalent to the geometric part of the initialized collar after its subsidiary argument. It does not require that one initialized collar cover $M$. In local Gaussian coordinates for the recognized metric, parallel transport of a spatial frame recovers the temporal equations of Paper 3, Definition 2.7. The extra choice of a maximal initial disk belongs to an ordinary-pair presentation, not to the global Cartan base.

<div id="sec:global-independent-incidence"></div>

### 6.2. Independent full incidence

<div id="def:global-independent-incidence"></div>

**Definition 6.3 (Global incidence admission).**

Over the data of Definition 6.1, supply a cooriented contact five-manifold $(Z,\mathcal H)$ and smooth maps

$$
M\xleftarrow{\ p\ }F\xrightarrow{\ q\ }Z.
$$ {#eq:global-admitted-double-fibration}

Require $p$ to be a proper surjective submersion with connected fibers diffeomorphic to $S^2$, and $q$ to be a surjective submersion with connected one-dimensional fibers. For every $x\in M$, the map $q|_{p^{-1}(x)}$ is an embedded Legendrian sphere.

For a positive local contact form $\alpha$ on $Z$, the covector $\ell_u\in T^*_{p(u)}M$ is determined by

$$
q^*\alpha=\ell\circ\mathrm dp.
$$ {#eq:global-admitted-contact-normal}

Require $\ell$ to be nonzero and to be a past null covector of the cone and quadratic form supplied by $\theta$. Equivalently, $\ell\circ\theta^{-1}$ is past null for $\eta$. A change of positive contact form multiplies $\ell$ by a positive function pulled back from $Z$.

The maps and tests are imposed on the entire supplied manifolds. In particular, $F$ contains every supplied point fiber, and a fiber of $q$ is a connected fiber of the global map, not a selected subinterval with a deleted endpoint in $F$. No prior identification with the ray space of the recognized metric is included in the definition.

<div id="thm:global-incidence-recognition"></div>

**Theorem 6.4 (Recognition of the complete ray incidence).**

The data of Definition 6.3 admit a canonical diffeomorphism over $M$

$$
\iota:F\longrightarrow\mathbb P_+\mathcal N^*_{\mathrm{past}}M,
\qquad
u\longmapsto(p(u),[\ell_u]_+).
$$ {#eq:global-incidence-recognition-map}

Under this map, $\ker\mathrm dq$ is the null-geodesic line distribution. Each entire fiber of $q$ is one maximal connected null leaf. Consequently $Z$ is canonically contact diffeomorphic to the full ray space $\mathcal N(M)$ of §3, and all point-labelled skies agree with their geometric counterparts.

Every whole Cauchy hypersurface of the recognized metric therefore gives the realized affine domain $D_{M,\Sigma}$ and the exact transition laws of Proposition 3.4 for the supplied incidence. No further ray cover, identification of distinct rays, or choice of incomplete leaf interval survives the admission tests. Conversely, the complete incidence constructed in §3 satisfies Definition 6.3.

*Proof.* Let $\lambda=q^*\alpha$. Because $q$ is a submersion and $\alpha$ is nowhere zero, $\lambda$ is nonzero. The Legendrian hypothesis makes $\lambda$ vanish on $\ker\mathrm dp$, so the displayed semibasic covector exists uniquely and depends smoothly on $u$. Rescaling $\alpha$ changes only its positive scale; hence $\iota$ is globally defined.

The contact condition implies

$$
\operatorname{rad}\bigl(\mathrm d\lambda|_{\ker\lambda}\bigr)
=\ker\mathrm dq.
$$

Indeed, $\mathrm dq$ maps $\ker\lambda$ onto $\mathcal H$ and $\mathrm d\alpha$ is symplectic on that contact plane. Consider a vector $v\in\ker\mathrm dp$ whose derivative under the projective covector map is zero. In a local scale this means $v(\ell)=c\ell$ for a scalar $c$. For $w\in\ker\lambda$,

$$
\mathrm d\lambda(v,w)=v(\ell)(\mathrm dp(w))=c\lambda(w)=0.
$$

It follows that $v\in\ker\mathrm dq$. The vertical sky map is an immersion, so $v=0$. Thus $\iota$ is an immersion on each point fiber. Its image lies in the past projective null sphere of $g$, which is a two-sphere. The fiber map is a local diffeomorphism between two-dimensional manifolds. Compactness of the fiber makes its image closed, while the local diffeomorphism makes it open. The target is connected, so the image is the entire sphere. The resulting covering has one sheet because its source is connected and its target is simply connected. Each point-fiber map is therefore a diffeomorphism. Since the map covers the identity and has an invertible vertical derivative, it is a local diffeomorphism on $F$; fiberwise bijectivity then makes it a global diffeomorphism.

To identify the line distribution, let $\vartheta=\xi_a\,\mathrm dx^a$ be the Liouville form on $T^*M\setminus0$, and let

$$
G(x,\xi)=\frac12g_x^{-1}(\xi,\xi),
\qquad
\iota_{X_G}\mathrm d\vartheta=-\mathrm dG.
$$

On the nonzero null cone, the symplectic orthogonal of the common kernel of $\mathrm dG$ and $\vartheta$ is spanned by $X_G$ and the radial Euler field. Both belong to that common kernel there: homogeneity gives $\vartheta(X_G)=2G$ and $\mathrm dG(E)=2G$. Projectivization removes the Euler direction. The remaining characteristic line is the projectivized null Hamiltonian line. The covector map preserves the tautological hyperplane, so the radical identity above identifies it with $\ker\mathrm dq$.

Let $L$ be the maximal connected null leaf through $u$. Its tangent lies in $\ker\mathrm dq$, so $q$ is locally constant along it and therefore constant on the whole connected leaf. Thus $L\subset q^{-1}(q(u))$. In the other direction, the connected fiber $q^{-1}(q(u))$ is a one-dimensional integral submanifold of the same line distribution. Every point of that fiber lies on the maximal leaf through $u$. Hence the fiber equals $L$. This argument uses the global map $q$; a hypothetical boundary separating two fibers on one maximal leaf would contradict constancy of $q$ on that leaf.

Theorem 3.2 identifies the smooth quotient by these full leaves with $\mathcal N(M)$. Both quotient maps are surjective submersions and open maps. Their common fibers give a bijection between the two quotients; local sections of the submersions make that bijection and its inverse smooth. The contact hyperplanes agree because their pullbacks agree with the tautological hyperplane on $F$. This proves the contact assertion and the equality of point-labelled skies. Transporting the geodesic flow coordinates of Theorem 3.2 now gives the actual maximal affine intervals and their transition laws, without any completeness assertion.

For the converse, §3 gives the sphere bundle $p$, the open submersion $q$ with connected interval fibers, and embedded Legendrian skies. Its contact-normal formula supplies the required past null covectors and the coorientation. All admission conditions are therefore satisfied. ∎

The global fiber hypotheses have separate roles. Compactness and connectedness of the point sphere give every null direction exactly once. Connectedness of the ray fibers prevents a quotient from identifying disconnected null leaves. Surjectivity excludes unused additional rays. These conditions do not follow merely from checking the contact-normal equation in isolated flow boxes.

<div id="sec:global-finite-rank-normalization"></div>

### 6.3. Finite-rank normalization on the whole incidence

The Cartan fields and actual spin bundle define the canonical tractor, local-twistor, infinity, optical-plane and screen models by the explicit formulas of Paper 3, Propositions 7.4–7.5. Those formulas are tensorial under actual spin changes and hence define global bundles and connections. The following lemma gives an independent global test for supplied copies. Initial comparison data are retained on a whole Cauchy ray section, which can be noncompact. A smooth spacelike Cauchy hypersurface exists for the recognized globally hyperbolic metric by Bernal–Sánchez, Theorem 1.1 ([Bernal and Sánchez 2005](#ref-BernalSanchez2005)); choosing one here does not impose a global Gaussian or maximal slicing.

The future affine generator $K$ below uses the normalization of §3. For its Cauchy-normalized contact form, the contact-normal covector is $\ell=-g(\mathrm dp(K),\cdot)$. The optical generator in Paper 3, Proposition 7.4, has base projection $g^{-1}\ell$ and is therefore $-K$ in this contact frame. For a contact form multiplied by a positive ray function $c$, that generator is $-cK$. The value-and-slope states and companion affine parameters are converted by this equality. In particular the physical selected value remains one, while its companion parameter has derivative $-c^{-1}$ with respect to the future affine parameter. These generator conventions are not identified without that conversion.

<div id="lem:global-initialized-finite-rank-normalization"></div>

**Lemma 6.5 (Global initialized connection test).**

Let $\Sigma$ be a whole Cauchy hypersurface and let $F_\Sigma=p^{-1}(\Sigma)$. Let $K$ be the future affine null generator normalized at $\Sigma$ as in Theorem 3.2. Supply finite-rank bundles $V^{\mathrm{can}},V^{\mathrm{s}}$ over $F$ with smooth connections $D^{\mathrm{can}},D^{\mathrm{s}}$, and an actual bundle isomorphism $J_0$ over all of $F_\Sigma$. There is a unique smooth invertible field $J$ on all of $F$ satisfying

$$
\nabla^{\operatorname{Hom}}_KJ
=D^{\mathrm{s}}_KJ-JD^{\mathrm{can}}_K=0,
\qquad J|_{F_\Sigma}=J_0.
$$ {#eq:global-initialized-finite-rank-transport}

It intertwines the full connections if and only if both of the following tests hold:

1. The pullback connections on $F_\Sigma$ agree under $J_0$ in every tangent direction of $F_\Sigma$, including its vertical sphere directions.
2. The computed $J$ satisfies, at every point of $F$ and for every tangent vector $W$ there (the component along $K$ drops out by antisymmetry),

   $$
   R^{\mathrm{s}}(K,W)J=JR^{\mathrm{can}}(K,W).
   $$ {#eq:global-finite-rank-curvature-test}

If both bundles and connections are pullbacks by $p$ of point bundles and point connections, the resulting full intertwiner descends to a unique bundle isomorphism over $M$. Parallel tensor identities and selected initialized optical, tractor and Jacobi states are preserved when their complete initial identities and corresponding actual differential equations are included. The construction preserves inverses and compositions with compatible initial data.

*Proof.* In the global flow coordinates of Theorem 3.2, $K=\partial_s$ and each fiber interval contains $s=0$. Along every finite segment from $0$ to $s$, solve the two ordinary parallel-transport equations. If their transport maps are denoted by $P^{\mathrm{s}}_{s,0}$ and $P^{\mathrm{can}}_{s,0}$, then

$$
J(z,s)=P^{\mathrm{s}}_{s,0}J_0(z)
\bigl(P^{\mathrm{can}}_{s,0}\bigr)^{-1}.
$$ {#eq:global-finite-rank-transport-formula}

Each segment is compact and lies inside its actual open flow domain. Smooth linear ordinary differential equations have an invertible solution along it. Local smooth dependence on $(z,s)$ makes the displayed field smooth everywhere on $D_{M,\Sigma}$, hence on $F$. No estimate uniform over all rays or at an omitted affine endpoint is required. Uniqueness along each ray gives global uniqueness.

Choose a local frame of transverse vector fields transported from $F_\Sigma$, so that $[K,W]=0$. For the transverse connection defect

$$
E(W)=\nabla_W^{\operatorname{Hom}}J
=D_W^{\mathrm{s}}J-JD_W^{\mathrm{can}},
$$

the curvature commutator gives

$$
\nabla_K^{\operatorname{Hom}}E(W)
=R^{\mathrm{s}}(K,W)J-JR^{\mathrm{can}}(K,W).
$$ {#eq:global-finite-rank-defect}

The initial tangential test makes $E(W)$ zero at $s=0$, and the mixed-curvature test makes its derivative zero. Uniqueness of the homogeneous finite ODE makes it zero along every ray segment. The transported transverse fields and $K$ span $TF$, so $J$ intertwines the full connections. For a nontransported frame the commutator contains its bracket term; expressing it in the transported frame gives the same assertion. Conversely, full intertwining restricts to the initial test and commutes with curvature, proving necessity.

Suppose now that the connections are pulled back from $M$. In a point-bundle trivialization, their covariant derivatives along a vector vertical for $p$ are ordinary vertical derivatives. The full intertwining identity therefore makes the matrix of $J$ constant along each connected fiber $p^{-1}(x)$. It determines a single point-bundle map $j_x$. Local sections of $p$ show that $j$ is smooth, and the full intertwining identity descends to the point connections. A second descended map would have the same pullback and hence would be equal. Invertibility follows from that of $J$.

An identity between parallel tensors propagates along $K$ from its given initial identity. The selected nonparallel states are tested by their actual initialized systems. For example, the tractor positions obey $D_KX=V$, $D_KV=0$ and $D_KI=0$, and the screen Jacobi pair obeys $D_KY=Q$, $D_KQ=-\mathcal RY$. Equality of the compared tidal endomorphisms makes the corresponding differences a homogeneous linear system with zero initial value. Thus these states agree as well. Tensor products, contractions and the stipulated real structures commute with the parallel comparisons.

The inverse of $J$ solves the reverse comparison equation with initial value $J_0^{-1}$. The product of two compatible comparisons solves the composite equation with the composite initial value. Their equality to the respective initialized solutions follows from the same uniqueness. Principal spin comparisons can be treated by actual principal parallel transport with a specified initial principal spin map. Their central sign is fixed by that initial map and is never quotiented. ∎

<div id="def:global-normalized-finite-rank-data"></div>

**Definition 6.6 (Normalized global finite-rank data).**

A supplied realization of one of the canonical finite-rank diagrams consists of its actual bundles, connections, selected tensors and states, together with its normalization on the whole $F_\Sigma$ and the tests of Lemma 6.5. The prescribed canonical model is built from $\theta,D,C$ and the actual spin bundle. For point-bundle copies the initial normalization is a point-bundle normalization over $\Sigma$, pulled back to $F_\Sigma$. The initial connection test is nevertheless imposed on every tangent direction of $F_\Sigma$.

The selected positions, infinity forms, optical roots and screen states obey their complete canonical tensor identities and the initialized equations of Paper 3, Propositions 7.4–7.5. In particular, equality of the screen tidal endomorphisms is part of the state comparison test. A normalization described on several initial charts includes its actual transition compatibility on all overlaps. Only the named canonical models and their tested copies are retained; an additional unnormalized local system is not a source datum of this definition.

By Lemma 6.5, these tests determine a global normalization. Choosing another Cauchy section and restricting that normalization to it gives the same global map on re-evolution, by uniqueness. Conversely the canonical models satisfy the tests with identity normalization. This condition controls global holonomy through the entire initial section. Requiring a connection equation locally and fixing a comparison at only one point would not provide the same conclusion.

<div id="sec:global-independent-scalar-admission"></div>

### 6.4. Independent scalar wave data and recovery

<div id="def:global-independent-scalar-wave"></div>

**Definition 6.7 (Independent global scalar wave class).**

Over Definitions 6.1 and 6.3, supply a scalar class

$$
[\Lambda]\in\mathcal D'(M\times M)/C^\infty(M\times M)
$$

satisfying the global tests

$$
\Box_{g,p}\Lambda,\ \Box_{g,q}\Lambda\in C^\infty(M^2),
\qquad
\Lambda-\Lambda^T+iE_g\in C^\infty(M^2),
\qquad
\operatorname{WF}'(\Lambda)\subset\mathcal C_g^+.
$$ {#eq:global-independent-scalar-tests}

Here $g=\eta(\theta,\theta)$ is the algebraic readout of the supplied fields, $E_g$ is the retarded-minus-advanced operator of its scalar wave operator with its supplied physical density, and the null relation is computed on the full incidence recognized in Theorem 6.4. The selected covectors are past directed, as in §4.

Equivalently, one may impose the two smooth wave residuals and the canonical four-trace class of Definition 4.1 on one whole Cauchy hypersurface. Theorem 4.5 proves equivalence of these two admission descriptions. The second description includes global off-diagonal smoothness on the entire Cauchy product; checking only diagonal germs is not the same test.

In a whole Cauchy half-density presentation, the supplied inverse, positive-principal root, mixed comparison, evaluation and point-connection fields are tested by the complete formulas of Definitions 5.1 and 5.4 and Theorem 5.5. In particular, the root obeys its complete square-root equation and positive principal normalization, $T_{ab}=W_aC_{ab}W_b$, $e_a(p)=W_aC_{ap}$, and the point connection acts by actual point differentiation on every complete coefficient family. Alternative stored algebra and module presentations require the invertible normalizations and overlap equations of the full source definition below.

These are sheaves of complete classes. On a noncompact ray carrier, the upper integer order is required to be locally bounded on the retained charts; no single upper order over the whole ray space is imposed. The integer module lattice and actual density and phase-transition factors are those of Definition 5.4.

<div id="thm:global-geometric-scalar-recovery"></div>

**Theorem 6.8 (Geometric and scalar construction and recovery).**

Every smooth globally hyperbolic oriented and time-oriented Ricci-flat four-manifold with actual spin has the independently admitted geometric, finite-rank and scalar data of Definitions 6.1, 6.3, 6.6 and 6.7. Conversely, such supplied data recover that enrichment of their recognized spacetime, in their supplied normalizations.

The geometric and scalar identifications preserve the actual point domain, full ray incidence, physical density, both Weyl chiralities, realized affine domains, specified spin structure, normalized finite-rank data, complete scalar classes, carrier maps, evaluations and all point directions of the connections. The constructions and identifications commute with physical spin isometries. On a causally convex globally hyperbolic open subspacetime, restrict the point and spin fields, the realized ray intervals, the normalized finite-rank identifications and the scalar kernel class. Sections 8–9 construct the corresponding relative carrier and whole-module comparisons.

*Proof.* Starting with a spacetime, Proposition 6.2 supplies its Cartan data. Section 3 supplies the incidence admitted by Theorem 6.4 and retains the actual affine intervals. The finite-rank formulas of Paper 3, Propositions 7.4–7.5, are global tensorial constructions from these fields and the actual spin structure. Their canonical copies with identity initial normalization satisfy Lemma 6.5. Theorem 4.4 constructs an actual representative of the independently tested scalar class. The complete inverse and positive-root recursions, followed by Theorems 5.3 and 5.5, give all the tested carrier and point fields.

Now start with the supplied data. Proposition 6.2 identifies their Cartan fields with the actual metric, connection and Weyl tensor of their readout, retaining the actual spin lift. Theorem 6.4 identifies their entire incidence with the full geometric incidence, rather than merely with local plaques. Lemma 6.5 identifies each normalized finite-rank copy with its canonical model on all of $F$, and descends the point models to $M$. Its initialized tensor and state equations identify the selected finite-rank records.

Theorem 4.4 identifies the supplied scalar class with $[\Lambda_g^+]$. Its mixed and point traces therefore agree with the canonical ones. The complete inverse and positive-principal square root are unique in their specified calculus, so their tested identities identify the supplied $C_a^{-1}$ and $W_a$. The defining products then identify every $T_{ab}$ and $e_a$. Equality of the point derivative on every coefficient family identifies both point connections. These identifications hold in the quotient by smooth kernels.

The construction followed by recognition is the identity on a spacetime and its actual spin structure. Recognition followed by construction has the explicit soldering, incidence, initialized finite-rank and complete scalar identifications just proved. Their naturality follows from the actual tensor and covector maps, uniqueness of initialized ordinary differential equations, and Corollary 4.6. The carrier and point comparisons are those of Theorems 5.3 and 5.5. On a causally convex subspacetime the geometric ray interval is restricted, the Green operators and scalar class restrict as in Corollary 4.6, and the already constructed finite-rank normalizations restrict as actual bundle maps. Reinitializing those restricted maps on a Cauchy section of the subspacetime returns them by Lemma 6.5. ∎

<div id="sec:global-normalized-full-sources"></div>

## 7. Independently normalized full sources and their comparisons

Starting with the spacetime, principal spin structure and full null incidence recovered in §6, we now impose tests on the wave packet and its stored presentations. The normalization records in this definition are part of the supplied data, as in Paper 3, Definitions 6.23 and 7.7 ([Isthmus 2026c](#ref-IsthmusSmooth2026)).

Fix one whole spacelike Cauchy hypersurface $\Sigma$ of the reconstructed metric and identify its nonzero cotangent bundle with the homogeneous ray carrier. It serves as a presentation carrier. Sections 4–5 identify the resulting constructions for every other whole Cauchy carrier. Write $\mathcal A_\Sigma$ for the sheaf of integer-order complete half-density operators and $\mathcal M_\Sigma$ for the sheaf of smooth point families of §5. The latter is microlocal on the full point-labelled incidence. Upper orders of general sheaf sections are locally bounded; no one upper order is required on a noncompact ray space. Every equality below is an equality of complete classes, with the point-family quotient taken by kernels jointly smooth in the carrier and point variables.

<div id="sec:global-wave-admission-records"></div>

### 7.1. Global wave admission and stored records

The smooth packet uses the first two root structures below. The third is retained only in the separately admitted analytic comparison of §16.

| Root datum | Type and defining comparison |
| --- | --- |
| Physical Cauchy normalizer | The complete operator $W_\Sigma\in\Psi^{1/2}(\Sigma;\mathcal H_\Sigma)$ satisfies $W_\Sigma^2=C_\Sigma^{-1}$ with positive physical principal symbol, as in Definition 5.1. It is reconstructed on each carrier. |
| Native density root | The carrier and conormal half-density lines retain their actual density-line squares. Their comparison uses the actual coordinate pushforward and the initialized leading symbol of the graph operator, including its phase-transition factors. |
| Calibrated analytic root | The analytic line $R_X$ retains its supplied square, relative quadratic base factor and factor frame. Its comparison with the native wave data is the additional calibrated interface of §16.1. |

For the carrier line, the native square is $\mathcal H_\Sigma^{\otimes2}\simeq\lvert\Lambda^3T^*\Sigma\rvert$. Under a coordinate change $y=b(x)$, half-density pushforward uses the positive Jacobian factor $\lvert\det D b^{-1}(y)\rvert^{1/2}$. The conormal square and radial normalization are those of Paper 3, Proposition 6.3. On a graph, the corresponding leading half-density symbol is initialized by the identity short-carrier transport; its continuation and composition are those of the actual mixed-kernel operators. Preservation of the native root means compatibility with these square maps, branches and phase-transition factors in the supplied model normalizations. Paper 3, Definition 7.7 and the proof of Theorem 7.11, specify this convention. The physical normalizer on the new carrier is computed from its own Cauchy kernel; conjugation of $W_\Sigma$ by the comparison need not give that normalizer.

Central specialization has a separate meaning. In a normalized local parameter chart, it restricts the complete symbol or amplitude coefficients, and their phase family, to a chosen parameter value. The kernel of this restriction is the ideal of smooth parameter functions vanishing there times the family algebra or module; the module assertion is Paper 3, Proposition 6.3, and the algebra assertion follows coefficientwise from the same argument. The required comparison test is that restriction before or after the supplied comparison gives the same fixed-parameter map under the supplied parameter identification, which is the identity for maps over a fixed base. These are maps in the joint smoothing quotient. They introduce no connection in external parameter directions; the point connections are still tested on every section of the full point family.

<div id="def:global-independent-normalized-wave-packet"></div>

**Definition 7.1 (Independent global normalized wave packet).**

*Native fields.* The packet includes the geometric, normalized finite-rank and scalar data of Definitions 6.1, 6.3, 6.6 and 6.7. In particular the scalar kernel is tested on all of $M^2$, and its complete inverse, positive root, mixed carrier maps, evaluation and point connections obey the global formulas. Retain the native half-density roots, full homogeneous ray maps and central-specialization maps of Paper 3, Propositions 6.2–6.3 and Definition 7.7, with the scalar enrichment tests of Definition 6.23. These fields form the native packet in the fixed Cauchy presentation; the following records allow independently supplied stored presentations of that packet.

*Local presentations and descent.* Choose an open conic cover $\{\Omega_i\}$ of $T^*\Sigma\setminus0$. On it supply algebras $\mathcal A_i$, complete modules $\mathcal M_i$, algebra transitions $\varphi_{ij}$, normalized associators $C_{ijk}\in1+F_{-1}\mathcal A_i$ with $C_{ijk}^*C_{ijk}=1$, and semilinear transitions $\tau_{ij}$. All transitions are invertible. Their domains include the full point-labelled incidence above $\Omega_i$, rather than a separately chosen small point core. Require the stored descent equations

$$
\begin{aligned}
\varphi_{ij}\varphi_{jk}
 &=\operatorname{Ad}(C_{ijk})\varphi_{ik},\\
C_{ijk}C_{ikl}
 &=\varphi_{ij}(C_{jkl})C_{ijl},\\
\tau_{ij}\tau_{jk}&=C_{ijk}\tau_{ik}.
\end{aligned}
$$ {#eq:global-stored-source-descent}

*Normalization tests.* Supply invertible maps

$$
n_i:\mathcal A_i\longrightarrow\mathcal A_\Sigma|_{\Omega_i},
\qquad
v_i:\mathcal M_i\longrightarrow\mathcal M_\Sigma|_{\Omega_i}.
$$ {#eq:global-stored-normalization-vertices}

Here $F_m$ denotes the filtration by order at most $m$. The algebra maps are unital and complex-linear, and $v_i$ is semilinear over $n_i$. Test the maps and their inverses on the complete products, filtrations, internal adjoints, module actions, full homogeneous characteristic maps, native roots and central specializations. In these normalizations the supplied evaluation is the entire family $e_\Sigma$ and the supplied connections act as actual point differentiation on every algebra and module section. In a point-dependent change of coordinates $m\mapsto Fm$, write the old and new connection operators as $X+A_X$ and $X+A'_X$, respectively. Intertwining them gives

$$
A'_X=F A_XF^{-1}-(XF)F^{-1}.
$$

The normalization records include overlap units $u_{ij}\in1+F_{-1}\mathcal A_\Sigma$, with $u_{ij}^*u_{ij}=1$, satisfying

$$
n_i\varphi_{ij}=\operatorname{Ad}(u_{ij})n_j,
\qquad
v_i\tau_{ij}=u_{ij}v_j.
$$ {#eq:global-stored-normalization-edges}

The units $u_{ij}$ are sections of the fixed-carrier algebra and are therefore basic in the point variable. Require the normalized algebra edge comparisons to commute with the algebra point connection on every smooth family of coefficients. These algebra families are defined on the point manifold times the carrier chart; they are not tested only after restriction to one sky. The displayed change-of-coordinates law applies on overlaps.

*Compatibility on overlaps.* Put $h_{ij}=n_i^{-1}(u_{ij})$. The corrected transitions are

$$
\begin{aligned}
\bar\varphi_{ij}
 &=\operatorname{Ad}(h_{ij}^{-1})\varphi_{ij}
 =n_i^{-1}n_j,\\
\bar\tau_{ij}
 &=h_{ij}^{-1}\tau_{ij}
 =v_i^{-1}v_j.
\end{aligned}
$$ {#eq:global-corrected-stored-transitions}

The stored evaluation is $e_i=v_i^{-1}e_\Sigma$, and hence $\bar\tau_{ij}e_j=e_i$. The corrected transitions also intertwine the full stored point connections. The corrected transitions compose strictly. The raw transitions carry the specified units and associators.

All these maps are sheaf maps, with their specified inverses, and the point-family maps act smoothly on each fixed finite filtration quotient. Algebra point families are sections of the pullback of the carrier algebra to $M\times\Omega_i$; the module families have their stated microsupport on the labelled incidence there. The algebra point-connection equation applies to every smooth point family of carrier coefficients, including basic coefficients independent of the point. Smooth functions of the point act by ordinary multiplication and are preserved by the normalization maps. The normalization of the complete overlap cells is tested as in Paper 3, Definition 7.7. Its triple equation follows from algebra descent and uniqueness of normalized implementing units in Lemma 7.5 below; the module descent equation verifies that the same cell acts on the whole module family.

*Resulting identification.* A *global normalized full source* consists of an admitted geometric source of §6, this packet, its finite-rank normalization records and its specified spin structure. A representative uses a whole Cauchy carrier and stored charts. Definition 7.2 identifies presentations by transporting their fields and normalization records together.

<div id="def:global-full-source-arrows"></div>

**Definition 7.2 (Full arrows and presentation equivalence).**

A global geometric comparison consists of an orientation-preserving point diffeomorphism $f:M_0\to M_1$, a coorientation-preserving contact diffeomorphism $\Psi:Z_0\to Z_1$, and the tests

$$
\Psi(Q_x)=Q_{f(x)},\qquad f^*\mu_1=\mu_0.
$$ {#eq:global-geometric-arrow-tests}

Theorem 6.4 and Proposition 3.7 identify this $f$ as a time-orientation-preserving physical isometry and determine its ray map. Supply an actual principal spin lift of the corresponding soldered orthonormal-frame map. The finite-rank comparison maps must preserve the normalized initial identifications; Lemma 6.5 then determines their full extensions. The initial values on another Cauchy section are the restrictions of those constructed normalizations.

The scalar vertices are invertible filtered algebra comparisons $k_i$ and invertible semilinear whole-module comparisons $\Xi_i$ over the full homogeneous ray comparison. They preserve the internal adjoint, native roots and central specializations. On every graded piece the algebra map is the homogeneous cotangent lift specified by the geometric comparison; its radial normalization is not free. The algebra vertices are unital and complex-linear. The module vertices act on smooth point functions by pullback under $f$; after target pullback they are linear over the source point functions.

After pulling the target sheaves back by $f$, require preservation of the evaluation and intertwining of the module and algebra point connections on every complete section

$$
\Xi e_0=e_1\circ f,
\qquad
\nabla^{\mathrm{amb},1}_{f_*X}\Xi
 =\Xi\nabla^{\mathrm{amb},0}_X,
\qquad
\nabla^{\mathrm{alg},1}_{f_*X}k
 =k\nabla^{\mathrm{alg},0}_X.
$$ {#eq:global-full-arrow-point-tests}

On a common refinement of the source and target ray covers, the vertices have normalized overlap units $a_{ij}$ satisfying

$$
\begin{aligned}
k_i\varphi^0_{ij}
 &=\operatorname{Ad}(a_{ij})\varphi^1_{ij}k_j,\\
a_{ij}\varphi^1_{ij}(a_{jk})C^1_{ijk}
 &=k_i(C^0_{ijk})a_{ik},\\
\Xi_i\tau^0_{ij}
 &=a_{ij}\tau^1_{ij}\Xi_j.
\end{aligned}
$$ {#eq:global-full-arrow-overlap-tests}

Both stored associators occur in this definition. Representatives are identified by common refinement and the normalized changes of presentation of Paper 3, Definition 7.7. In target coordinates, fix the raw target transitions $\varphi^1_{ij},\tau^1_{ij}$ and the associator $C^1_{ijk}$. Changing the comparison representative by $U_i\in1+F_{-1}$, $U_i^*U_i=1$, then gives

$$
k'_i=\operatorname{Ad}(U_i)k_i,
\qquad
\Xi'_i=U_i\Xi_i,
\qquad
a'_{ij}=U_i a_{ij}\varphi^1_{ij}(U_j^{-1}),
$$ {#eq:global-full-arrow-normalized-change}

Changing the reference Cauchy carrier from $\Sigma$ to $\Sigma'$ is another permitted presentation change. Reindex the conic domains by its full homogeneous return map and put $T=T_{\Sigma',\Sigma}$. The normalization records change by

$$
n'_i=\operatorname{Ad}(T)n_i,
\qquad v'_i=T v_i,
\qquad u'_{ij}=T u_{ij}T^{-1}.
$$ {#eq:global-carrier-presentation-change}

The inverse and triple laws for these changes are Theorem 5.3. The finite-rank initial normalizations on the new Cauchy section are obtained by restricting the unique global normalizations of Lemma 6.5.

A change of target coordinates transports the target evaluation, connections and normalization records along with the arrow vertices. For example, the new evaluation is $U_i e_1$ in those coordinates. To compare representatives, first use their supplied normalizations and the canonical carrier changes to express them in common native coordinates. Common refinement and compatible normalized cells identify those expressions. The actual point and principal spin maps must agree for representatives to be identified. In particular the two central spin lifts remain different arrows. The resulting quotient groupoid is $\mathsf{FullSrc}^{\infty}_{\mathrm{GH},0}$; the theorem below is stated for this quotient groupoid.

<div id="sec:global-normalized-rigidity"></div>

### 7.2. Global normalized rigidity

The following arguments use the local complete calculus of Paper 3, Lemmas 7.8–7.10, on the full conic incidence domains fixed above.

<div id="lem:global-normalized-inner-rigidity"></div>

**Lemma 7.3 (Inner rigidity on a conic ray domain).**

Let $\Omega\subset T^*\Sigma\setminus0$ be open and conic. An automorphism $\Phi$ of $\mathcal A_\Sigma|_\Omega$ covering the identity, preserving $*$ and acting identically on every graded piece has a unique expression

$$
\Phi=\operatorname{Ad}(U),
\qquad U\in1+F_{-1},\qquad U^*U=1.
$$

The construction commutes with restriction and applies to smooth finite-dimensional coefficient families. If $\Phi$ commutes with the algebra point connection, $U$ is basic in the point variable.

*Proof.* Work first on a conic coordinate neighborhood. If the first nonzero discrepancy lowers order by $k$, multiplicativity makes its leading term a derivation of homogeneous functions, and commutator preservation makes it a Poisson derivation. The leading internal adjoint on degree $m$ is multiplication by $(-1)^m$. Its preservation excludes odd $k$, so the first possible discrepancy has even $k\ge2$.

As in Paper 3, Lemma 7.8, this derivation is a smooth homogeneous symplectic vector field $V$. Let $E$ be the Euler field, $\lambda=\xi\,\mathrm dx$ and $\omega=\mathrm d\lambda$. Then $[E,V]=-kV$ and the one-form $\iota_V\omega$ is closed with Euler weight $1-k$. Its primitive is fixed by

$$
b=\frac{\lambda(V)}{1-k},
\qquad
\mathrm db=-\iota_V\omega.
$$ {#eq:global-negative-weight-primitive}

The denominator is nonzero. Consequently this step has no period obstruction on a multiply connected ray domain. Skew-symmetrize a complete operator with principal symbol $b$ to obtain $B^*=-B$ and remove the discrepancy by conjugation with $\exp(-B)$. Repeating produces a product convergent in each finite filtration quotient, with normalized unit $U$ and $U^*U=1$.

Two implementing units differ by a central unit in $1+F_{-1}$. Commutation with coordinate multiplication and differentiation makes every local central coefficient independent of the active cotangent coordinates. Such coefficients have degree zero, so a central unit in $1+F_{-1}$ is one. Local constructions therefore agree on every overlap and glue as a sheaf section on $\Omega$. Neither simple connectivity nor a global bound on unrelated operator orders is needed.

At each finite depth the recursion uses finitely many coefficient derivatives and divisions by nonzero integers, so it preserves smooth coefficient families. If $\Phi$ commutes with the point connection, its value on every basic carrier coefficient is independent of the point. The same is then true of each recursive coefficient of its unique normalized implementing unit. ∎

<div id="lem:global-full-incidence-faithfulness"></div>

**Lemma 7.4 (Faithfulness of full incidence and evaluations).**

Let $\Omega\subset T^*\Sigma\setminus0$ be open and conic, and let $P$ be a basic complete carrier operator on $\Omega$. If

$$
P e_\Sigma(p)=0
$$

on the full labelled incidence above $\Omega$, as a joint complete-family identity, then $P=0$ on $\Omega$.

Suppose also that $\Phi=\operatorname{Ad}(U)$ is as in Lemma 7.3 and $\Phi$ preserves the algebra point connection. Let $F$ be a semilinear module comparison over $\Phi$ that preserves the evaluation and the module point connection in every direction. Then $U=I$ and $F=I$ on that full incidence whenever the underlying geometric comparison is the identity.

*Proof.* Fix any carrier covector in $\Omega$ and a relatively compact conic neighborhood on which $P$ has an upper order $m$. The leading module symbol of the first identity is

$$
\sigma_m(P)|_{L_p}\,\sigma_1(e_\Sigma(p))=0.
$$

The evaluation symbol is nonzero. Every covector in $\Omega$ is tested by at least one of these skies: its base point on the whole Cauchy hypersurface is itself an allowed evaluation point. Thus $\sigma_m(P)$ vanishes on the neighborhood. Drop the order and repeat. Every homogeneous coefficient vanishes, so the complete class is zero there. Such neighborhoods cover $\Omega$.

For the second statement, the algebra point-connection equation and Lemma 7.3 make $U$ basic. The map $U^{-1}F$ is a module automorphism over the identity algebra. On each connected flattened angular cap, the calculation in Paper 3, Lemma 7.9, shows that it is multiplication by a smooth scalar $c$ depending only on point parameters.

The smooth-coefficient step in this calculation can be seen directly in the normalized angular model of Paper 3, Proposition 6.3. Flatten the local sky, write $q=(q^1,q^2)$ for its angular coordinates and $\tau$ for the positive radial variable, and let $u$ be its degree-zero generator. On a formal section $b(q,\tau)u$, the exact actions on the coefficient $b$ are

$$
D_z=\tau,
\qquad D_{q^a}=\partial_{q^a},
\qquad z=-\partial_\tau+\frac{1}{2\tau}.
$$ {#eq:global-flattened-module-rigidity-actions}

Put $G=U^{-1}F$ and write $G(u)=a(q,\tau)u$. Semilinearity over the identity algebra makes $G$ commute with every smooth angular multiplier $f(q)$ and every integer power of the invertible $D_z$. Hence, for every integer $j$,

$$
G\bigl(f(q)\tau^j u\bigr)
=f(q)\tau^j a(q,\tau)u.
$$ {#eq:global-module-smooth-coefficient-commutant}

Finite sums establish this identity on each finite filtration quotient. Preservation of the filtration and coefficientwise completeness extend it to an arbitrary complete section. Thus $G$ is multiplication by $a$. This uses all smooth coefficient multipliers and requires no polynomial approximation argument. Commutation with $D_{q^a}$ and with the operator $zD_z+\tfrac12$, both of which annihilate $u$, gives

$$
\partial_{q^a}a=0,
\qquad \tau\partial_\tau a=0.
$$ {#eq:global-module-residual-scalar-equations}

The homogeneous expansion of $a$ therefore contains only a degree-zero term, constant on the connected cap. That term is the scalar $c$; the stipulated smooth family structure allows it to depend smoothly on the passive point parameters. Invertibility makes it nonzero.

The scalar may initially depend on the cap or the component of the sky-chart intersection. Preservation of the full evaluation gives $cUe_\Sigma(p)=e_\Sigma(p)$ on each such cap. Since the principal symbol of $U$ is one and the evaluation is elliptic of degree one, its leading term gives $c=1$ on that cap. Thus $(U-I)e_\Sigma(p)=0$ on every incidence chart. The first part makes $U=I$ throughout $\Omega$, and then $F=I$ on every module chart. This proof does not assume that a sky intersects $\Omega$ in a connected set. ∎

<div id="lem:global-normalization-coherence"></div>

**Lemma 7.5 (Coherence and absence of an additional normalized twist).**

The normalization records of Definition 7.1 obey

$$
u_{ij}u_{jk}=n_i(C_{ijk})u_{ik}.
$$ {#eq:global-normalization-triple-identity}

They therefore give a comparison, in the quotient of Definition 7.2, between the stored packet and its native presentation on a whole Cauchy hypersurface. The comparison retains the actual stored associators. A normalized automorphism of fixed comparison vertices is trivial.

*Proof.* Conjugate the algebra descent equation by the two normalization vertices. The edge equations give

$$
\operatorname{Ad}(u_{ij}u_{jk})
=\operatorname{Ad}\bigl(n_i(C_{ijk})u_{ik}\bigr).
$$

Both implementing elements are normalized units: their principal term is one and their remaining terms have negative order. Their ratio is therefore a central normalized unit. The center calculation in Lemma 7.3 makes that ratio the identity, proving the triple equation. This also proves that $n_i(C_{ijk})$ is basic, since it equals $u_{ij}u_{jk}u_{ik}^{-1}$.

The module equation verifies that precisely the same cell acts on the whole module family. Indeed, semilinearity gives

$$
u_{ij}u_{jk}v_k
 =v_i\tau_{ij}\tau_{jk}
 =v_i C_{ijk}\tau_{ik}
 =n_i(C_{ijk})u_{ik}v_k.
$$

Together with the two edge equations, the derived triple equation is exactly the full comparison equation from the stored packet to its native presentation. It holds in every complete degree and on the entire specified incidence. The corrected transitions of Definition 7.1 are its strict presentation in the normalized coordinates.

For a normalized automorphism of fixed vertices, the algebra equation gives $\operatorname{Ad}(U)=I$ with $U\in1+F_{-1}$. The center argument in Lemma 7.3 gives $U=I$. ∎

The full-incidence domain in these lemmas is essential. A unit that is tested only on rays through one small point core is determined only on the corresponding tested open ray set. Here every ray of every normalization overlap is tested at its hit on the whole Cauchy hypersurface. The global kernel condition is equally essential: normalization on all small point squares alone would not exclude Example 4.7.

<div id="sec:global-full-hom-proof"></div>

### 7.3. The global full Hom theorem

<div id="prop:global-native-isometry-lift"></div>

**Proposition 7.6 (Native lift of a global isometry).**

Let $f:(M_0,g_0)\to(M_1,g_1)$ be an orientation- and time-orientation-preserving global isometry. Choose whole Cauchy carriers $\Sigma_0\subset M_0$ and $\Sigma_1\subset M_1$, and let $C_f$ denote physical half-density pushforward from $\Sigma_0$ to $f(\Sigma_0)$. Then

$$
F_f=T^1_{\Sigma_1,f(\Sigma_0)}C_f,
\qquad
J_f(P)=F_f P F_f^{-1}
$$ {#eq:global-native-isometry-lift}

give a full comparison of the native scalar packets. They preserve the complete evaluation, all point connections, filtration, internal adjoint, full homogeneous characteristic map and native half-density roots. They have identity, inverse and composition laws in the complete quotient.

*Proof.* The image $f(\Sigma_0)$ is a whole spacelike Cauchy hypersurface of $M_1$, so the comparison operator in the formula is supplied by Theorem 5.3. Its graph is the full null return graph. Actual half-density pushforward has the homogeneous cotangent graph of $f|_{\Sigma_0}$ and the positive Jacobian square root. Its composition with the normalized carrier operator is therefore defined with proper representatives and has the required graph and root.

Corollary 4.6 identifies the two global scalar kernel classes under $f$. It follows, by taking the physical half-density traces and the unique positive-principal complete roots, that

$$
C_f e_{\Sigma_0}^0(p)
 =e^1_{f(\Sigma_0)}(f(p)).
$$

Theorem 5.5 then gives $F_f e^0_{\Sigma_0}(p)=e^1_{\Sigma_1}(f(p))$. Both factors in $F_f$ are independent of the evaluated point. The point chain rule consequently proves the connection identities on every module section and, by conjugation, on every algebra section. Internal-adjoint preservation follows from Theorem 5.3 and physical half-density coordinate covariance in Paper 3's complete calculus.

For a second global isometry $h:M_1\to M_2$, naturality of the mixed traces and roots gives

$$
C_h T^1_{\Sigma_1,f(\Sigma_0)}
 =T^2_{h(\Sigma_1),hf(\Sigma_0)}C_{h|_{f(\Sigma_0)}}.
$$

Therefore the carrier cocycle and ordinary half-density composition give

$$
\begin{aligned}
F_hF_f
 &=T^2_{\Sigma_2,h(\Sigma_1)}C_h
   T^1_{\Sigma_1,f(\Sigma_0)}C_f\\
 &=T^2_{\Sigma_2,hf(\Sigma_0)}C_{hf}
 =F_{hf}.
\end{aligned}
$$ {#eq:global-native-isometry-composition}

The identity comparison is $I$ and the comparison for $f^{-1}$ is the inverse. Changing a chosen whole carrier conjugates this formula by the canonical $T$ operators, so the packet comparison is independent of that presentation choice. ∎

<div id="thm:global-full-source-hom"></div>

**Theorem 7.7 (Global full Hom).**

Let $S_0,S_1$ be global normalized full sources of Definitions 7.1–7.2, with recognized spacetimes and actual spin structures. Recognition induces a bijection

$$
\operatorname{Hom}_{\mathsf{FullSrc}^{\infty}_{\mathrm{GH},0}}(S_0,S_1)
\longrightarrow
\operatorname{Isom}^{+,\uparrow,\mathrm{spin}}(R S_0,R S_1).
$$ {#eq:global-full-source-hom-bijection}

The right side consists of global physical isometries with specified principal spin lifts. The full lift carries the optical and finite-rank fields, scalar kernel class and native root diagrams. Its vertices intertwine the algebra and module actions to every order, the full evaluation and both point connections. On overlaps the normalized units relate the two stored associators by the triple equation of Definition 7.2. Identity, inverse and composition are exact in the stated quotient groupoid.

*Proof.* A geometric source comparison has a point diffeomorphism preserving the full labelled contact incidence, its coorientation and physical density. Proposition 3.7, together with the geometric recognition in §6, identifies that map as a physical isometry. The actual principal spin lift is retained in the arrow data. Thus recognition is defined on arrows.

Conversely, let $(f,\widetilde f)$ be a physical isometry with its specified spin lift. Section 6 identifies the source incidences with the full metric null incidence; geodesic uniqueness gives their ray comparison and its affine-domain map. The canonical finite-rank constructions and their supplied initialized intertwining maps give the comparison of those fields. All these maps are actual bundle maps, including the central sign of $\widetilde f$.

For the scalar part, kernel uniqueness in Theorem 4.4 first identifies each independently supplied kernel class with the canonical one of its recognized metric. The inverse and square-root tests and the point-section and connection tests then identify every other native field with §4–§5. Use Proposition 7.6 to obtain $F_f$ and $J_f$ between these native packets.

We give the stored comparison explicitly. Pull the target cover back under the full homogeneous ray map and choose a common refinement. Suppress these pullbacks in the notation. Write $(n_i^r,v_i^r,u_{ij}^r)$ for the normalization records of source $r=0,1$. Set

$$
\begin{aligned}
k_i&=(n_i^1)^{-1}J_f n_i^0,\\
\Xi_i&=(v_i^1)^{-1}F_f v_i^0,\\
a_{ij}&=(n_i^1)^{-1}
 \left(J_f(u_{ij}^0)(u_{ij}^1)^{-1}\right).
\end{aligned}
$$ {#eq:global-stored-full-lift}

The first and third arrow equations follow directly by inserting the two normalization edge equations. All products are in the same complete carrier model on the refined ray overlap. For the triple equation put $V_{ij}=n_i^1(a_{ij})$. Lemma 7.5 gives

$$
u_{ij}^r u_{jk}^r=n_i^r(C_{ijk}^r)u_{ik}^r.
$$

Consequently

$$
\begin{aligned}
n_i^1\!\left(a_{ij}\varphi_{ij}^1(a_{jk})C_{ijk}^1\right)
 &=V_{ij}u_{ij}^1V_{jk}(u_{ij}^1)^{-1}n_i^1(C_{ijk}^1)\\
 &=J_f(u_{ij}^0u_{jk}^0)(u_{ik}^1)^{-1}\\
 &=J_f(n_i^0(C_{ijk}^0))V_{ik}\\
 &=n_i^1\!\left(k_i(C_{ijk}^0)a_{ik}\right).
\end{aligned}
$$ {#eq:global-stored-full-lift-triple-check}

Invertibility of $n_i^1$ proves the middle arrow equation with both associators. The scalar, root and connection identities at the vertices follow by transporting them through the supplied normalizations; point-dependent coordinate changes contribute exactly the derivative term in Definition 7.1.

For uniqueness, compose a second lift with the inverse of the constructed lift. Its geometric and actual spin labels are identities. Lemma 7.5 transports it to the native presentation, allowing a conic refinement for its vertices. On each such chart, the point-connection equation makes the vertex's action on basic algebra coefficients basic. Its graded action is the identity, so Lemma 7.3 supplies a unique basic implementing unit $U_i$ on that chart. On every connected angular cap the remaining module comparison is $cU_i$. The full evaluation makes $c=1$ at leading order; Lemma 7.4 then gives $U_i=I$ on the whole ray chart. Thus all native algebra and whole-module vertices are identities.

Its remaining finite-rank maps are identities by their initialized uniqueness in §6. Any residual normalized change of stored vertices or overlap cells is trivial by Lemma 7.5, after the allowed common refinement. Hence the original two arrows are equal in the quotient of Definition 7.2. In particular there is no additional flat scalar or normalized inner automorphism over a fixed point map and a fixed spin lift.

The native identity and composition laws are Proposition 7.6. In stored coordinates, if $f:S_0\to S_1$ and $h:S_1\to S_2$ are composable, choose the same intermediate normalization on one refinement. Their composite has vertices $k_i^h k_i^f$, $\Xi_i^h\Xi_i^f$ and overlap units

$$
a_{ij}^{hf}=k_i^h(a_{ij}^f)a_{ij}^h.
$$ {#eq:global-stored-arrow-composition}

Substituting the two triple equations gives

$$
a_{ij}^{hf}\varphi_{ij}^2(a_{jk}^{hf})C_{ijk}^2
 =(k_i^h k_i^f)(C_{ijk}^0)a_{ik}^{hf}.
$$

The middle associator is eliminated by its actual transition equation, not omitted. A change of intermediate presentation inserts a normalization and its inverse; their vertices cancel and the formula in Definition 7.2 gives the same quotient arrow. The unique lift is therefore functorial. ∎

<div id="cor:global-full-source-equivalence"></div>

**Corollary 7.8 (The native correspondence and its two inverse comparisons).**

Let $\mathsf{Vac}^{\infty}_{\mathrm{GH},0}$ be the groupoid of smooth oriented and time-oriented globally hyperbolic Ricci-flat Lorentzian four-manifolds at physical scale, with actual spin structures and global physical-spin isometries. Recognition gives an equivalence

$$
R:\mathsf{FullSrc}^{\infty}_{\mathrm{GH},0}
\longrightarrow\mathsf{Vac}^{\infty}_{\mathrm{GH},0}.
$$ {#eq:global-native-source-equivalence}

Its inverse is the geometric and wave construction of §3–§6, including the independently tested normalization records. The units and counits preserve all source fields and satisfy both triangle identities. The statement concerns these normalized full sources; their presentation by atlases of ordinary input pairs is established separately in §11–§12 under the named local coverage input.

*Proof.* For a spacetime $M$, take its actual metric Cartan fields, full null incidence and canonical finite-rank diagrams. Sections 4–5 construct its native wave packet and its comparisons between whole Cauchy carriers. Identity normalizations in intrinsic carrier coordinates, or their actual chart expressions with the induced cells, satisfy Definition 7.1. Thus the geometric and wave construction gives a source $N M$ and an actual physical-spin identification $\varepsilon_M:R N M\to M$.

For a physical-spin isometry $f:M\to M'$, define $Nf$ to be the unique lift of $\varepsilon_{M'}^{-1}f\varepsilon_M$ provided by Theorem 7.7. Its identity and composition laws make $N$ a functor, and $\varepsilon:RN\Rightarrow1$ is natural. Define $\eta_S:S\to NRS$ as the unique full arrow over $\varepsilon_{RS}^{-1}$. The Hom bijection makes $\eta$ natural. Applying $R$ to the first triangle gives

$$
\varepsilon_{RS}\,R\eta_S=I_{RS}.
$$

For the second triangle, the arrow $N(\varepsilon_M)\eta_{NM}$ has identity physical-spin image by the defining arrow formula for $N$. Faithfulness of $R$ makes it the identity of $NM$. Thus both triangles hold with every actual spin map and every stored complete comparison retained.

Changing a reference Cauchy hypersurface or stored presentation gives another such construction and another identification $\varepsilon'_M$. The unique full lift of $(\varepsilon'_M)^{-1}\varepsilon_M$ compares the two constructions naturally, and composition follows from the same Hom bijection. ∎

<div id="ex:global-flat-line-normalization"></div>

**Example 7.9 (A flat line twist obstructs normalization of a fixed evaluation).**

Let $M=\mathbb R\times T^3$ with the flat product metric $\mathrm dt^2-\sum_{j=1}^3(\mathrm dx^j)^2$, and let $x^1$ have period $L$. On the trivial complex line bundle choose

$$
\nabla^L=\mathrm d+i\frac{\vartheta}{L}\,\mathrm dx^1,
\qquad \vartheta\notin2\pi\mathbb Z.
$$

It is flat, but its parallel transport around the first spatial circle is multiplication by $e^{-i\vartheta}$. Tensor the native point-module family with this line and equip it with

$$
\nabla^{\mathrm{tw}}_X
=\nabla^{\mathrm{native}}_X\otimes1
 +1\otimes\nabla^L_X.
$$

Keep the native algebra and scalar kernel, and fix the evaluation $e^{\mathrm{tw}}=e\otimes1$ in the global line frame $1$, where $e=e_\Sigma$ is the point evaluation for the carrier $\Sigma=\{t=0\}$. This evaluation is elliptic of degree one.

No semilinear normalization over any algebra vertex allowed by Definition 7.1 can carry this specified evaluation to the native evaluation and intertwine the point connections on all sections.

*Verification.* Write $a=\vartheta/L$. Take the exact bisolution representative of Theorem 4.4. In Definition 5.4 the field trace and $W_\Sigma$ act on its first variable, so $\Box_p e=0$ in the joint complete class. Suppose the normalization records exist. Use Theorem 5.5 to express them on $\Sigma$, and take a vertex $v$ in a chart containing a carrier direction with $\xi_1\ne0$. Each point derivative raises the filtration order by at most one, so the all-section connection identity applies again to the differentiated section. Contracting the two derivatives with the flat inverse metric gives $v(\Box_{\mathrm{tw}}e^{\mathrm{tw}})=\Box_p e=0$. Invertibility would make the twisted residual zero in every chart.

In the global frame the first spatial derivative is $\partial_{p^1}+ia$. With signature $(+---)$ the residual is therefore

$$
\Box_{\mathrm{tw}}e^{\mathrm{tw}}
=\bigl(-2ia\,\partial_{p^1}e+a^2e\bigr)\otimes1.
$$

Restrict the point to $b\in\Sigma$. The derivative is tangential there, and Theorem 5.5 gives $W_\Sigma e(b)=\delta_b$ modulo joint smoothing in flat half-density coordinates. Acting on the carrier variable of the restricted residual thus gives $-2ia\,\partial_{b^1}\delta_b+a^2\delta_b$ in the line frame. Its first-order conormal symbol is nonzero wherever $\xi_1\ne0$, since $a\ne0$. This incidence is among those tested on the chart; conic and point cutoffs can be chosen equal to one near it. A zero complete class would give a smooth kernel there after carrier action. This contradiction uses only the evaluation, the point connections and invertibility of $v$. ∎

<div id="sec:relative-carrier-restriction"></div>

## 8. Relative carriers and causal restriction

Let $U\subset M$ be a causally convex globally hyperbolic open subspacetime. The metric is smooth and Ricci-flat, and the orientations and physical scale on $U$ are the restrictions of those on $M$. The background metrics and inclusions are fixed throughout this section; central specializations concern the passive coefficient families of their specified models. Write $\Lambda_M$ and $\Lambda_U$ for representatives of the canonical classes of Theorem 4.4. Proposition 3.6 identifies $\mathcal N(U)$ with the open set $\mathcal N_U(M)$ of ambient rays meeting $U$, and Corollary 4.6 gives

$$
[\Lambda_U]=[\Lambda_M|_{U\times U}].
$$ {#eq:relative-native-kernel-restriction}

The latter equality is a global equality modulo $C^\infty(U\times U)$. Causal convexity is used both for the restriction of the advanced and retarded Green operators and for identifying the restricted null relation with the intrinsic null relation of $U$.

Choose whole smooth spacelike Cauchy hypersurfaces $\Sigma_M\subset M$ and $\Sigma_U\subset U$. The second hypersurface need not be Cauchy in $M$. Let $\Omega_U^M\subset T^*\Sigma_M\setminus0$ be the positive homogeneous lift of $\mathcal N_U(M)$. Following a covector along its selected null bicharacteristic to $\Sigma_U$ defines a homogeneous symplectic diffeomorphism

$$
\kappa_{U,M}:\Omega_U^M\longrightarrow T^*\Sigma_U\setminus0.
$$ {#eq:relative-homogeneous-ray-map}

Indeed, an ambient ray meeting $U$ has exactly one maximal connected portion in $U$, and that portion has exactly one transverse Cauchy hit. The argument of Proposition 3.4 gives smoothness, the positive normal multiplier, and preservation of the tautological one-form. In particular, the radial variable in this map is fixed by the physical covector transport. It is not an additional choice of a homogeneous lift.

The relative affine change is defined on precisely these rays. Let $k_M$ and $s_M$ be their future affine tangent and parameter normalized at $\Sigma_M$, and put

$$
\tau_{U,M}(\gamma)=s_M(\gamma\cap\Sigma_U),
\qquad
r_{U,M}(\gamma)=g(k_M,n_U)|_{\gamma\cap\Sigma_U}>0.
$$

Then

$$
\begin{aligned}
k_U&=r_{U,M}^{-1}k_M,
&s_U&=r_{U,M}(s_M-\tau_{U,M}),\\
I_{\gamma,U}^{\Sigma_U}
&=r_{U,M}\bigl(I_{\gamma,U}^{\Sigma_M}-\tau_{U,M}\bigr),
&I_{\gamma,U}^{\Sigma_M}
&=\{s\in I_{\gamma,M}^{\Sigma_M}:\gamma_M(s)\in U\}.
\end{aligned}
$$ {#eq:relative-affine-normalization}

The hitting time and multiplier are smooth by the finite-flow-box and transverse-intersection argument of Proposition 3.4. Rescaling an affine tangent by the ray-constant factor $r_{U,M}^{-1}$ and shifting its origin proves the displayed formulas. This gives the relative version of that proposition without assuming that $\Sigma_U$ is Cauchy in $M$. The actual contact forms and finite-rank fields can be retained by restriction; replacing their Cauchy normalization uses these same coordinate and scale changes.

<div id="def:relative-graph-comparison"></div>

**Definition 8.1 (A relative graph comparison).**

A relative graph comparison over $\kappa_{U,M}$ is a section of the sheaf of complete classical Fourier integral classes on its graph. Its action and products are defined locally as follows. About a graph point choose source and target conic neighborhoods with compact cosphere closures, contained in larger neighborhoods on which the graph is a diffeomorphism. Choose properly supported order-zero microlocal cutoffs with compact base supports and full symbol one near the smaller conic sets. Form the cut-off kernels and their products first; then take the complete class on the smaller sets. Two kernels represent the same section when their difference is smoothing there.

The resulting class is independent of the cutoffs. The inserted differences vanish microlocally near the retained graph, and all the cut-off compositions are properly supported, so the usual smoothing-ideal argument applies. This is the graph version of restricting the complete operator sheaves of §7 to an open conic domain. An arbitrary global integral involving an unrestricted smooth remainder is not part of this definition.

For a conic set with noncompact cosphere closure, the definition is made on a cover of the indicated kind. Symbol orders and seminorm estimates are local on that cover. A representative defined on the full carrier product can determine a section of this sheaf even when its support is not proper over both carrier factors.

Use the physical half-density traces of §5, and set

$$
\begin{aligned}
C_{U,M}&=(\gamma_0^U\otimes\gamma_0^M)\Lambda_M,&
C_M&=(\gamma_0^M\otimes\gamma_0^M)\Lambda_M,\\
C_U&=(\gamma_0^U\otimes\gamma_0^U)\Lambda_U,&
W_M&=C_M^{-1/2},\qquad W_U=C_U^{-1/2}.
\end{aligned}
$$ {#eq:relative-mixed-traces}

All traces exist by the noncharacteristic restriction criterion. The positive-principal complete roots $W_M,W_U$ are constructed separately on their respective whole Cauchy hypersurfaces by Definition 5.1. Proper representatives of these pseudodifferential roots act in the two variables of $C_{U,M}$ and define the normalized mixed kernel

$$
T_{U,M}=W_U C_{U,M}W_M.
$$ {#eq:relative-normalized-carrier}

It will be used as a relative graph comparison. We write $T_{M,U}=T_{U,M}^{\dagger}$ for its reverse graph class; the dagger is the physical Hermitian adjoint, distinct from the complex-linear internal adjoint on the complete algebra.

<div id="lem:relative-positive-factorization"></div>

**Lemma 8.2 (Relative positive-branch factorization).**

The mixed kernel $C_{U,M}$ is, modulo a globally smooth kernel on $\Sigma_U\times\Sigma_M$, a classical elliptic Fourier integral kernel on the graph of $\kappa_{U,M}$. In the notation of Lemma 5.2 the field block is $C_M=R_M^{-1}$. With $A_M=J_MC_MJ_M^{\dagger}$, put

$$
E_U=\gamma_0^U\mathcal U_{\Sigma_M}J_M.
$$ {#eq:relative-positive-field-transfer}

There is a representative of $E_U$ proper over $\Sigma_U$. It has order zero on the selected graph, and the following identities hold as global kernel classes whenever expressed by this Cauchy construction, and as localized complete classes:

$$
C_{U,M}=E_U C_M,
\qquad
C_U=E_U C_M E_U^{\dagger}.
$$ {#eq:relative-positive-factorization}

The operator $E_U$ has an inverse in the relative graph sheaf. Consequently $T_{U,M}$ has order zero and satisfies

$$
T_{M,U}T_{U,M}=I_{\Omega_U^M},
\qquad
T_{U,M}T_{M,U}=I_{T^*\Sigma_U\setminus0}.
$$ {#eq:relative-carrier-inverse}

The two inverse identities mean localized products as in Definition 8.1.

*Proof.* Exact ambient Cauchy evolution can be restricted to the spacelike hypersurface $\Sigma_U$. For a compact output set $K\subset\Sigma_U$, Lemma 2.1 places the relevant ambient initial support in a compact subset of $\Sigma_M$. Composing with proper representatives of the two entries of $J_M$ retains this property. Hence $E_U$ has a representative proper over $\Sigma_U$.

Apply the spacetime Cauchy-kernel argument of Lemma 5.2 with initial surface $\Sigma_M$, before taking the output trace. The exact kernel $\mathcal U_{\Sigma_M}J_M$ is a classical elliptic kernel on its selected spacetime null relation and is smooth off that relation. This includes elimination of the opposite branch to every order. Its restriction to the spacelike $\Sigma_U$ is noncharacteristic. Every resulting canonical-relation point comes from a ray meeting $\Sigma_U$, hence from an initial covector in $\Omega_U^M$. Conversely, every ray in this open domain meets $\Sigma_U$ exactly once, by causal convexity and the Cauchy property in $U$. The restricted relation is therefore exactly the graph of $\kappa_{U,M}$. Transverse restriction gives order zero and preserves the nonzero leading amplitude. These statements describe the whole wavefront set of $E_U$ on $\Sigma_U\times\Sigma_M$, not only its germs at selected graph points. The local phase expressions and their transition factors come from the same restricted exact distribution. Several base-point paths are allowed and are distinguished by their cotangent data.

Use the factorized representative of the ambient wave class from Lemma 5.2,

$$
\Lambda_M
=\mathcal U_{\Sigma_M}J_M C_MJ_M^{\dagger}
  \mathcal U_{\Sigma_M}^{\dagger}
\quad\bmod C^\infty(M^2).
$$

Taking one field trace on $\Sigma_M$ gives the identity field row, and taking the other on $\Sigma_U$ gives $E_U$. Taking both on $\Sigma_U$ gives the second formula, using the native kernel restriction above. These products are legitimate in the displayed factorized representative: compact output sets on each copy of $\Sigma_U$ have compact ambient initial shadows, and the intervening complete operators have proper representatives. The initial replacement error is globally smooth before either trace is taken, so its two restrictions remain globally smooth. In particular, no integration of a freely chosen nonproper smoothing tail is used to establish the factorization.

For graph inversion fix retained conic sets as in Definition 8.1 and insert their cutoffs. The elliptic graph calculus supplies a local parametrix $E_U^{-1}$ in the reverse graph. Equivalently, the construction in Lemma 5.2 using an elliptic parametrix of $E_U^{\dagger}E_U$ applies on these conic sets; the idempotent order-lowering argument makes the inverse two-sided. In the resulting local calculus,

$$
C_U^{-1}
=(E_U^{\dagger})^{-1}C_M^{-1}E_U^{-1}.
$$

Insert this identity between $C_{M,U}=C_{U,M}^{\dagger}$ and $C_{U,M}$. It gives

$$
C_{M,U}C_U^{-1}C_{U,M}=C_M
\quad\text{on }\Omega_U^M.
$$

The other cancellation uses $C_{U,M}=E_UC_M$ and gives $C_{U,M}C_M^{-1}C_{M,U}=C_U$. Multiplying by the endpoint roots proves both inverse identities. The roots have order $1/2$ and $C_{U,M}$ has order $-1$, so the normalized class has order zero. This proof is local on the graph after the cutoffs have been inserted, and hence establishes the identities on the whole relative domain by sheaf compatibility. ∎

<div id="thm:relative-wave-packet-comparison"></div>

**Theorem 8.3 (Restriction of the complete native wave packet).**

The class $T_{U,M}$ identifies the ambient complete algebra restricted to $\Omega_U^M$ with the complete algebra on $T^*\Sigma_U\setminus0$:

$$
\operatorname{Ad}(T_{U,M}):
\mathcal A_{\Sigma_M}|_{\Omega_U^M}
\longrightarrow \mathcal A_{\Sigma_U}.
$$ {#eq:relative-algebra-comparison}

The identification is understood over $\kappa_{U,M}$. It preserves the filtration, complex-linear internal adjoint and native carrier-change structure. It gives an invertible semilinear map of the whole point-labelled module families over $p\in U$, including their native half-density, phase-transition, root and central-specialization structures. The graph action carries the native density-line squares and phase factors. The physical inverse square roots in the mixed kernel are computed separately on its two carriers (Definition 8.1). In particular,

$$
T_{U,M}e_M(p)=e_U(p),\qquad p\in U.
$$ {#eq:relative-full-evaluation}

It intertwines the algebra point connection and the module point connection on every section. The construction is independent of the representatives, local cutoff systems and local phase choices. Its inverse is $T_{M,U}$, with the inverse identities interpreted as in Lemma 8.2.

*Proof.* The localized graph Egorov theorem and Lemma 8.2 give the filtered algebra isomorphism and its inverse. Graph Fourier integral action gives the corresponding semilinear maps on classical Lagrangian modules. Every operation is formed on cut-off representatives on the retained conic sets; smooth remainders are then a two-sided ideal. Thus these operations give well-defined maps of the complete sheaves.

For the internal adjoint and the native extra structure, fix the finite ray segment from $\Sigma_M$ to $\Sigma_U$. Choose the short carrier disks, overlapping Gaussian neighborhoods, and interpolating spacelike isotopies used in Theorem 5.3. Each small neighborhood can be chosen causally convex in $M$, so Corollary 4.6 identifies its scalar class with the local canonical class. Near the endpoint in $U$, this is also the scalar class of $U$. The localized cancellation of Lemma 8.2 identifies $T_{U,M}$ with the finite product of the normalized short-carrier comparisons of Paper 3, Theorem 6.14. Each such factor preserves the complex-linear internal adjoint by the internally skew normalized generator of Paper 3, Lemma 6.13. Their product therefore preserves that adjoint. The actual half-density and phase-transition factors are retained by the graph action of Paper 3, Proposition 6.3; the actual mixed distribution fixes their product. Central point functions commute with these point-independent operators, and restricting a smooth parameter coefficient commutes with each localized action. This proves the central-specialization identities of Definition 6.23 of that paper ([Isthmus 2026c](#ref-IsthmusSmooth2026)).

The native density squares are carried by the graph action. The physical normalizers $W_M$ and $W_U$ in the mixed formula are computed separately from their endpoint Cauchy kernels.

For evaluation, the factorization in Lemma 8.2 is valid with the second spacetime variable retained as a point in $U$. On each retained incidence chart it gives

$$
C_{U,M}C_M^{-1}C_{Mp}=C_{Up},
\qquad p\in U.
$$ {#eq:relative-point-factorization}

One can obtain this identity by taking the appropriate traces of the factorized ambient wave class. For a compact point set, its ambient initial shadow is compact; equivalently one can insert the same local graph cutoffs before the three factors are composed. The right-hand side agrees with the point column of $\Lambda_U$ by the global restriction identity. Multiplication by $W_U$ proves the full evaluation formula.

To check the entire point family, let $K\subset U$ be compact. The phase sphere bundle above $K$ is compact. Its ambient ray image is a compact subset of the open domain $\Omega_U^M/\mathbb R_+$, and its $U$-Cauchy image is compact as well. Finitely many retained conic charts with positive margins therefore cover all its sky directions. On each chart choose the carrier cutoffs independently of the point on a neighborhood of the relevant portion of $K$. The graph operators preserve every classical amplitude and have the required locally uniform symbol estimates after every finite point derivative. Consequently their action is defined on all module sections, with locally bounded upper order, and respects the quotient by remainders smooth jointly in the point and carrier variables.

The action is also defined on every conic chart with compact cosphere closure in $\Omega_U^M$, whether or not it meets those skies. On a smaller such chart, use matched nested cutoffs on both carriers as in Definition 8.1. The resulting forward and reverse graph operators preserve jointly smooth remainders and are inverse on all module families by Lemma 8.2. Their cutoffs are fixed in the point variable. On smaller charts whose compact cosphere closures are disjoint from the skies over $K$, both module families have zero complete class, jointly over a neighborhood of $K$, by the uniform phase estimates; the homogeneous ray map carries this disjointness to the other carrier. Applying the local inverse to the forward evaluation formula therefore gives

$$
T_{M,U}e_U(p)=e_M(p),\qquad p\in U,
$$ {#eq:relative-inverse-full-evaluation}

as an identity of the complete module sheaves on the entire retained conic domain. All products and smoothing statements here are localized on the smaller charts. The identities agree on refinements by Definition 8.1.

Finally, the two carriers and the background are fixed: $T_{U,M}$ has no point dependence. Actual point differentiation commutes with every localized operator and with its action on every family. It follows that

$$
\begin{aligned}
\nabla_X^{\mathrm{amb},U}(T_{U,M}m)
 &=T_{U,M}\nabla_X^{\mathrm{amb},M}m,\\
\nabla_X^{\mathrm{alg},U}
  \bigl(T_{U,M}PT_{M,U}\bigr)
 &=T_{U,M}(\nabla_X^{\mathrm{alg},M}P)T_{M,U}
\end{aligned}
$$ {#eq:relative-all-section-connections}

for every smooth point vector field and every admitted algebra or module section on $U$. This is an identity on all sections, not only on the distinguished evaluation family. Cutoff and phase independence follows from the common mixed kernel and the local smoothing-ideal argument in Definition 8.1. ∎

<div id="cor:relative-carrier-coherence"></div>

**Corollary 8.4 (Nested restriction and change of presentation).**

Let $V\subset U\subset M$ be causally convex globally hyperbolic open inclusions, and choose whole Cauchy hypersurfaces in the three spacetimes. On the ray domain of $V$ in the ambient carrier,

$$
T_{V,U}T_{U,M}=T_{V,M},
\qquad
\kappa_{V,U}\kappa_{U,M}=\kappa_{V,M}.
$$ {#eq:relative-carrier-cocycle}

The comparison for an identity inclusion and an unchanged carrier is the identity. Replacing either Cauchy hypersurface changes the relative comparison by the whole-Cauchy comparisons of Theorem 5.3. All these identities hold for the complete algebra, the whole point-labelled modules over $V$, the full evaluation, and both point connections. They are natural under orientation- and time-orientation-preserving physical isometries.

*Proof.* Geodesic uniqueness gives the homogeneous identity. Causal convexity is transitive, and Corollary 4.6 identifies the two successive restricted kernel classes with $[\Lambda_M|_{V^2}]$. On a retained conic ray neighborhood use the ambient initial carrier $\Sigma_M$ in the factorization of Lemma 8.2. The mixed factors then have the forms

$$
C_{V,U}=E_VC_ME_U^{\dagger},
\quad C_{U,M}=E_UC_M,
\quad C_{V,M}=E_VC_M.
$$

The local graph inverse of $E_U$ gives

$$
C_{V,U}C_U^{-1}C_{U,M}=C_{V,M}.
$$

Choose the cutoffs for all three factors on nested conic sets before performing this cancellation. All intermediate graph points then lie in the retained interiors, so contributions from the cutoff complements are smoothing there. Multiplication by the three endpoint roots gives the normalized cocycle. This local identity covers the whole domain of $V$.

The same computation with two choices of a carrier proves the presentation-change law, and repeated indices give the identity. Theorem 8.3 transports these actual graph-class products to every algebra and module section; its full evaluation and point-connection identities consequently obey the same cocycle. An isometry carries the canonical scalar class, the physical half-density traces and the positive-principal roots to their counterparts. It therefore carries the displayed mixed kernel and every retained local product to the corresponding mixed kernel and product. This proves naturality. ∎

<div id="ex:relative-carrier-nonproperness"></div>

**Example 8.5 (A relative comparison need not be proper over the ambient carrier).**

Take Minkowski space $M=\mathbb R^{1+3}$ and the open double cone

$$
U=\{(t,x):|t|+|x|<1\}.
$$

It is causally convex and globally hyperbolic. The hypersurfaces $\Sigma_M=\{t=0\}$ and $\Sigma_U=\{t=0,\ |x|<1\}$ identify with $\mathbb R^3$ and $B_1$. The relative conic domain is $T^*B_1\setminus0$ inside $T^*\mathbb R^3\setminus0$, and the normalized carrier comparison is the restriction class. Its kernel is

$$
\delta(x-y),\qquad (x,y)\in B_1\times\mathbb R^3,
$$

modulo a smooth kernel on that product. Its support is proper over $B_1$ but is not proper over $\mathbb R^3$. In fact, over the compact ambient closed unit ball the singular graph contains a sequence $(x_k,x_k)$ with $x_k\to\partial B_1$, which has no convergent subsequence in $B_1\times\mathbb R^3$. Adding a smooth kernel cannot remove these singular graph points. Thus no representative of this complete graph class can have support proper over the ambient carrier.

*Verification.* The double cone is $I^+((-1,0))\cap I^-((1,0))$, and each of its inextendible causal curves meets the displayed ball at $t=0$. An ambient null line meets $U$ precisely when its $t=0$ hit is in $B_1$: if it meets $(t,x)\in U$, its hit $x_0$ satisfies $|x_0|\le |x|+|t|<1$, and the converse follows at the hit itself. The two carrier hypersurfaces and their physical half-density data agree on $B_1$. The local native Cauchy kernel and its root consequently give the identity complete symbol on that ball. Both carrier hypersurfaces are ambient acausal, so the mixed kernel has no off-diagonal singularity. It is therefore the stated restriction class. The compactness argument proves the support assertion. ∎

<div id="prop:cauchy-open-whole-carriers"></div>

**Proposition 8.6 (Whole carriers for a Cauchy inclusion).**

Suppose in addition that $U$ contains a Cauchy hypersurface of $M$. Then every whole Cauchy hypersurface $\Sigma_U$ of $U$ is a whole Cauchy hypersurface of $M$. The relative ray domain is all of $T^*\Sigma_M\setminus0$, and $T_{U,M}$ is the whole-Cauchy comparison of Theorem 5.3. In particular it has a representative proper over both carriers, with its two-sided inverse and all the identities of that theorem.

Although this comparison acts on the entire ray space, the point domain of the restricted source is still $U$. Each ray retains precisely the affine interval specified by Proposition 3.6.

*Proof.* Extend a maximal causal curve in $U$ to a maximal causal curve in $M$. Its ambient extension meets the Cauchy hypersurface contained in $U$. Causal convexity makes the ambient curve's intersection with $U$ connected, so the given maximal portion in $U$ is precisely that intersection and meets the ambient Cauchy hypersurface. Thus this hypersurface is also Cauchy for $U$.

Conversely, every maximal causal curve of $M$ has a nonempty connected portion in $U$, since it meets that common Cauchy hypersurface. This portion is maximal in $U$: an endpoint of the portion at an ambient interior parameter lies outside $U$, and an extension beyond an ambient maximal endpoint would extend the ambient curve. It consequently meets $\Sigma_U$ exactly once. Hence $\Sigma_U$ is Cauchy for $M$. Every ambient ray meets $U$, so the ray domain is full by Proposition 3.6. Corollary 4.6 identifies the intrinsic Cauchy kernel and root on $\Sigma_U$ with the ambient ones. The mixed formula is therefore exactly that of Definition 5.1 for two whole Cauchy hypersurfaces of $M$, and Theorem 5.3 applies. The point and affine-domain assertions are those of Proposition 3.6. ∎

<div id="sec:global-source-open-embeddings"></div>

## 9. Restrictions and full source embeddings

The global Hom theorem concerns isomorphisms of whole sources. For an embedding, we compare the source with the fields of the target over the image of the point map and the open set of rays meeting that image. Theorem 8.3 constructs the native scalar restriction and compares its carriers. We now restrict the supplied geometric fields and stored complete records, prove their admission and coherence, and use this full restriction to define source embeddings and prove their Hom theorem. All objects retain their actual point domains, and a map of ray carriers alone is not an arrow.

<div id="sec:global-source-restriction-coherence"></div>

### 9.1. Coherent restriction of complete records

<div id="def:global-admissible-source-open"></div>

**Definition 9.1 (Admissible open restriction).**

Let $S$ be a global normalized full source with recognized point manifold $M$. An *admissible open* is a nonempty connected open subset $U\subset M$ that is causally convex in $M$ and globally hyperbolic with its restricted metric. Define the fieldwise restriction $S|_U$ by the following data; Proposition 9.2 verifies its full source admission. Its point incidence is $p^{-1}(U)$, its ray space is the open subset $Z(U)$ consisting of rays meeting $U$, and its scalar kernel is $[\Lambda|_{U\times U}]$. Its geometric and finite-rank bundles, connections and invariant tensors are their actual restrictions. The original contact forms and normalized finite-rank fields may be retained by restriction. When a selected state is expressed using the new Cauchy contact scale or affine origin, it is re-expressed by the [relative affine law](#eq:relative-affine-normalization) and the conventions of §6.3. In each ray the incidence fiber is the connected maximal interval lying in $U$; it is not replaced by the longer ambient interval.

For clarity we give the restriction of the stored complete records. Let $\Sigma_M$ be a whole Cauchy presentation for $S$, let $\Sigma_U$ be a whole Cauchy hypersurface of $U$, and let $\Omega_U\subset T^*\Sigma_M\setminus0$ be the homogeneous open set of ambient rays meeting $U$. Write

$$
T_{U,M}:\mathcal M_{\Sigma_M}|_{U,\Omega_U}
\longrightarrow\mathcal M_{\Sigma_U}
$$

for the relative carrier comparison of [Theorem 8.3](#thm:relative-wave-packet-comparison). Its inverse is defined as a complete graph-operator sheaf class on the corresponding open domains. Restrict the original conic charts and all point families to $\Omega_U$ and $U$, respectively, and reindex their ray domains by the homogeneous ray map. The normalization records of the restricted source are

$$
\begin{aligned}
n_i^U&=\operatorname{Ad}(T_{U,M})n_i^M,\\
v_i^U&=T_{U,M}v_i^M,\\
u_{ij}^U&=T_{U,M}u_{ij}^M T_{U,M}^{-1}.
\end{aligned}
$$ {#eq:global-open-restriction-records}

The stored transitions, associators, sections and connections are their restrictions in the original stored coordinates, with ray indices relabelled by the homogeneous ray map. The three displayed formulas change the native carrier in which the normalization vertices and overlap units take values. Finite-rank initial normalizations on $F_{\Sigma_U}$ are the restrictions of the actual global normalizations supplied by Lemma 6.5. Their selected position, companion and Jacobi states take their actual values at the new hit; no independent reset of those values is made. For example, if the ambient contact form is retained, its optical generator is $D_M=-r_{U,M}K_U$, so the companion derivative with respect to $s_U$ is $-r_{U,M}^{-1}$ with its inherited initial value, exactly as in §6.3. Thus restriction keeps the supplied records and their initialized states.

The products in this definition are sheaf compositions on interior conic charts of the retained open graph. They use the local proper representatives of Definition 8.1 and Lemma 8.2. No extension by zero across $\partial\Omega_U$, no globally proper mixed carrier operator, and no behavior at an omitted affine endpoint enters the definition.

<div id="prop:global-open-restriction-coherence"></div>

**Proposition 9.2 (Restriction of complete records and transitivity).**

Definition 9.1 gives an admitted global normalized full source with recognized spacetime $U$. If $V\subset U\subset M$ are successive admissible opens, then $V$ is admissible in $M$ and there is a canonical full comparison

$$
\rho_{V,U,M}:(S|_U)|_V\longrightarrow S|_V
$$ {#eq:global-open-restriction-transitivity}

over the identity point and spin maps. These comparisons are independent of Cauchy presentations and satisfy the unit and associativity coherence identities. Restriction of a full isomorphism to corresponding admissible opens is a full isomorphism of their restricted sources.

*Proof.* The geometric restriction is Proposition 3.6, and the native scalar admission and carrier tests restrict by Corollary 4.6 and Theorem 8.3. The actual finite-rank comparisons are restricted and reinitialized using Lemma 6.5, with the relative affine and contact changes of §8. The new carrier is a whole Cauchy carrier for $U$, so the coverage of the incidence required by Definition 7.1 holds there. The stored descent equations restrict to the reindexed domains. Applying the carrier comparison to the native sides of the normalization edge and triple equations gives their counterparts on the new carrier. In particular,

$$
u_{ij}^Uu_{jk}^U
=n_i^U(C_{ijk}|_U)u_{ik}^U.
$$

The internal adjoint, native roots and central specializations are preserved by the relative comparison. Its full evaluation and all-section connection identities give the corresponding admission tests in the new carrier. The corrected stored transitions are the ratios of the restricted vertices in Definition 7.1; the common carrier factors cancel. Actual finite-rank restriction followed by reinitialization returns the same maps by Lemma 6.5. All fields of an admitted source are therefore present and satisfy their required equations.

For a causal curve in $M$ with endpoints in $V$, causal convexity of $U$ first puts the curve in $U$, and causal convexity of $V$ in $U$ then puts it in $V$. Thus $V$ is causally convex in $M$; its assumed global hyperbolicity is unchanged. On the ray domain meeting $V$, the nested relative carrier identity of [Corollary 8.4](#cor:relative-carrier-coherence) is

$$
T_{V,U}T_{U,M}=T_{V,M}.
$$ {#eq:global-open-carrier-nested-identity}

Substitution into the three formulas of Definition 9.1 makes successive and direct restrictions identical in common carrier coordinates. Geometric fields, scalar restrictions on $V^2$, actual finite-rank maps, point connections and stored cells have the same transitivity. Their equality gives the displayed full comparison.

With different chosen Cauchy presentations, compare to one common presentation using Corollary 8.4. The resulting comparison has identity geometric and actual spin labels. Theorem 7.7 on $V$ makes it unique. For a chain of three inclusions, both composites of the $\rho$ maps have these same labels, so they coincide. The same argument gives the unit identity and independence of auxiliary presentations. This use of Theorem 7.7 is on the entire restricted source over $V$; its whole Cauchy carrier is $\Sigma_V$, whose evaluation points lie in $V$.

Finally, restrict a full isomorphism and all its comparison equations to the corresponding opens, then express the two sides in their relative Cauchy carriers. Theorem 8.3 preserves the full module, evaluation and connection identities, and restriction preserves the normalized overlap equations. The resulting maps are inverses on the retained domains and give the claimed full isomorphism. ∎

<div id="sec:global-source-embedding-hom"></div>

### 9.2. The embedding category and its full Hom theorem

<div id="def:global-full-source-open-embedding"></div>

**Definition 9.3 (Full open comparison).**

The objects of $\mathsf{FullSrc}^{\infty,\mathrm{cc}}_{\mathrm{GH},0}$ are those of Definition 7.1. A *full open comparison* $A:S_0\to S_1$ consists of an orientation-preserving smooth open embedding $f:M_0\to M_1$ with admissible image $U=f(M_0)$, together with a full comparison

$$
\widehat A:S_0\longrightarrow S_1|_U
$$ {#eq:global-source-open-comparison}

of Definition 7.2 whose point diffeomorphism is $f:M_0\to U$. In particular its ray map is a contact diffeomorphism $Z_0\to Z_1(U)$, its incidence map covers $f$ and retains each realized interval, and it includes an actual principal spin lift. Its complete algebra and whole-module vertices are invertible on these restricted target domains, preserve the full homogeneous map and native roots, and obey all evaluation, point-connection and stored overlap equations of Definition 7.2. They are not required to be invertible over rays or points outside the image.

Representatives are identified by the common refinements and normalized presentation changes of Definition 7.2 on the retained domains. The point map and actual spin map must agree. Changing a relative carrier presentation uses the canonical comparisons of Corollary 8.4 and Proposition 9.2. These changes transport the sections and connections along with their records.

If $A:S_0\to S_1$ lies over $f$ and $B:S_1\to S_2$ lies over $h$, restrict $B$ to $f(M_0)$, compose the resulting full comparisons, and use Proposition 9.2 to identify the iterated restriction with $S_2|_{hf(M_0)}$. This defines $B A$. The identity is the full identity comparison with image the entire point manifold.

Let $\mathsf{Vac}^{\infty,\mathrm{cc}}_{\mathrm{GH},0}$ have the recognized physical-spin spacetimes as objects and orientation-, time-orientation- and scale-preserving isometric open embeddings with causally convex image and specified principal spin lifts as arrows. A *Cauchy arrow* in either category is an arrow whose image contains a whole Cauchy hypersurface of its target.

<div id="thm:global-full-source-embedding-hom"></div>

**Theorem 9.4 (Full Hom for open embeddings).**

Definition 9.3 defines a category, and recognition extends to an equivalence

$$
R:\mathsf{FullSrc}^{\infty,\mathrm{cc}}_{\mathrm{GH},0}
\longrightarrow
\mathsf{Vac}^{\infty,\mathrm{cc}}_{\mathrm{GH},0}.
$$ {#eq:global-source-embedding-equivalence}

More precisely, for every pair of objects it gives a bijection

$$
\operatorname{Hom}(S_0,S_1)
\cong
\operatorname{Emb}^{+,\uparrow,\mathrm{spin}}_{\mathrm{cc}}
(RS_0,RS_1).
$$ {#eq:global-source-embedding-hom}

The bijection preserves composition, restrictions, Cauchy arrows and actual principal spin maps. The native construction is a quasi-inverse; recognizing a native source returns the given spacetime and spin structure. The unit and counit of Corollary 7.8 are natural also for these open comparisons, and their triangle identities continue to hold. A full open comparison is an isomorphism precisely when its point map is surjective.

*Proof.* A full open comparison is a full comparison onto the admitted restriction $S_1|_U$. The target metric $RS_1$ determines admissibility of the image $U$ and the restriction there. The sky and density tests of Definition 7.2 and Proposition 3.7 then identify the point map as a physical isometry from $RS_0$ onto $U$. The arrow supplies the principal spin lift of its frame map. Causal convexity is part of the image condition. Recognition is thus defined on arrows without assuming an isometry in the source-side definition.

Conversely, let $(f,\widetilde f)$ be a physical-spin isometric embedding with causally convex image $U$. Since $RS_0$ is globally hyperbolic, its isometric image $U$ is globally hyperbolic. Proposition 9.2 makes $S_1|_U$ an admitted source, and Theorem 7.7 supplies exactly one full comparison $S_0\to S_1|_U$ over $(f,\widetilde f)$. This gives the required open comparison and proves bijectivity. It also proves that the unique comparison uses the actual restricted records rather than only an object with the same recognized metric.

We record its native and stored formulas. Choose whole Cauchy carriers $\Sigma_0\subset M_0$ and $\Sigma_1\subset M_1$. The hypersurface $f(\Sigma_0)$ is a whole Cauchy hypersurface of $U$, and physical half-density pushforward along $f|_{\Sigma_0}$ is denoted by $C_f$. On the open target ray domain meeting $U$, set

$$
F_f=T^{1}_{\Sigma_1,f(\Sigma_0)}C_f,
\qquad
J_f=\operatorname{Ad}(F_f).
$$ {#eq:global-native-open-embedding-lift}

Here the first factor is the inverse relative-carrier comparison of Theorem 8.3, not an asserted globally proper operator between the two entire carriers. Its inverse exists on the retained conic domains. Its graph is the homogeneous ray embedding, and for every $p\in M_0$,

$$
F_f e^0_{\Sigma_0}(p)=e^1_{\Sigma_1}(f(p)).
$$

The full connection identities follow because the graph comparison is basic in the evaluated point and the chain rule applies on each finite coefficient quotient. The inverse on the image, adjoint, root and full homogeneous normalization identities follow from Lemma 8.2, Theorem 8.3 and physical half-density pushforward.

Refine the source ray cover against the pullback of the target cover to that open ray image, and restrict all target point families to $U$. With the normalization records written in these native coordinates, the stored vertices and overlap units are

$$
\begin{aligned}
k_i&=(n_i^1)^{-1}J_f n_i^0,\\
\Xi_i&=(v_i^1)^{-1}F_f v_i^0,\\
a_{ij}&=(n_i^1)^{-1}
\left(J_f(u_{ij}^0)(u_{ij}^1)^{-1}\right).
\end{aligned}
$$ {#eq:global-open-stored-comparison}

All factors are defined on the same retained overlap after this reindexing. As in Theorem 7.7, the normalization edge and triple identities give

$$
\begin{aligned}
k_i\varphi^0_{ij}
 &=\operatorname{Ad}(a_{ij})\varphi^1_{ij}k_j,\\
a_{ij}\varphi^1_{ij}(a_{jk})C^1_{ijk}
 &=k_i(C^0_{ijk})a_{ik},\\
\Xi_i\tau^0_{ij}
 &=a_{ij}\tau^1_{ij}\Xi_j.
\end{aligned}
$$ {#eq:global-open-stored-comparison-equations}

Both raw associators are retained. The same calculation is valid sheafwise because all its products have been localized inside the retained conic graph before composition.

The uniqueness argument can also be checked directly in these coordinates. Express two comparisons in the carrier $f(\Sigma_0)$ of the restricted target. Every retained ray then has a tested point on that Cauchy hypersurface lying inside $U$. Lemmas 7.3–7.4 remove the difference of the two native algebra and module vertices, and Lemma 7.5 removes the normalized overlap ambiguity. Ambient $\Sigma_1$ hits outside $U$ are not used as evaluation points. The actual finite-rank maps agree by their restricted initialized uniqueness, and the principal spin label is already fixed.

If $f:M_0\to M_1$ and $h:M_1\to M_2$ have causally convex images, then $hf(M_0)$ is causally convex in $M_2$: any causal curve between its points first lies in $h(M_1)$, and its pullback then lies in $f(M_0)$. The image is globally hyperbolic because it is isometric to $M_0$. Thus the composite is admissible. The relative carrier composition law of Corollary 8.4, followed by actual half-density composition, gives $F_hF_f=F_{hf}$ on the ray domain of the composite. In stored coordinates the composite has

$$
k_i^{hf}=k_i^h k_i^f,
\qquad
\Xi_i^{hf}=\Xi_i^h\Xi_i^f,
\qquad
a_{ij}^{hf}=k_i^h(a_{ij}^f)a_{ij}^h,
$$ {#eq:global-open-stored-composition}

where the entries for $h$ are restricted to the image of $f$. Substituting the two triple equations yields

$$
a_{ij}^{hf}\varphi^2_{ij}(a_{jk}^{hf})C^2_{ijk}
 =(k_i^h k_i^f)(C^0_{ijk})a_{ik}^{hf}.
$$

The intermediate associator cancels through its transition equation. Proposition 9.2 proves independence from iterated restrictions and carrier choices. Associativity and the identity laws also follow from the Hom bijection, since both sides lift the same composite point and actual spin maps. These arguments make Definition 9.3 a category and recognition a fully faithful functor.

Corollary 7.8 already supplies essential surjectivity and inverse object comparisons. Define the native functor on open arrows by the unique lifts just constructed. Functoriality follows from uniqueness. The naturality squares for the old unit and counit now commute for open arrows because their two paths have the same recognized point and spin maps. The old triangle identities concern isomorphisms and remain valid. Recognition detects Cauchy arrows by their point images. Finally, an inverse arrow would provide an inverse point map, so an isomorphism must be surjective. If the point map is surjective, Theorem 7.7 supplies its inverse full comparison. ∎

<div id="sec:global-source-cauchy-embeddings"></div>

### 9.3. Cauchy carriers and retained spacetime domains

<div id="cor:global-cauchy-source-carriers"></div>

**Corollary 9.5 (Cauchy comparisons and domain information).**

A Cauchy arrow induces a contact diffeomorphism of the entire ray spaces and an invertible comparison of the entire native Cauchy carrier algebras. For such an arrow the native operator $F_f$ in the proof of Theorem 9.4 can be represented by the whole-carrier operators of Theorem 5.3. The full source arrow is an isomorphism exactly when its point embedding is surjective.

*Proof.* Every maximal ray of the target meets its whole Cauchy hypersurface contained in the image, so every target ray lies in the retained ray domain. Causal convexity makes each intersection with the image connected, and Proposition 3.6 therefore gives a diffeomorphism onto the entire target ray space. Proposition 8.6 makes the image of any source Cauchy carrier a whole target Cauchy carrier. Theorem 5.3 thus applies to the two whole carriers in the formula. Cauchy arrows are closed under composition: the second arrow sends the whole Cauchy hypersurface contained in the first image to a whole Cauchy hypersurface of the final target, again by Proposition 8.6. The full-source isomorphism criterion is Theorem 9.4 and retains the actual point domain. ∎

<div id="ex:global-cauchy-slab-domain"></div>

**Example 9.6 (A Cauchy comparison with a smaller affine domain).**

Let $M=\mathbb R^{1,3}$ with $g=\mathrm dt^2-|\mathrm dx|^2$, its standard orientations and a fixed spin structure, and let $U=(-1,1)\times\mathbb R^3$. The inclusion is a causally convex Cauchy embedding. Choose $\Sigma=\{t=0\}$ for both sources. Their homogeneous ray carriers and native complete carrier algebras agree, and their carrier comparison is the identity. Their entire point-labelled sources differ: for the future affine normalization with $\mathrm dt(K)=1$, the realized interval of each ray is $(-1,1)$ in $U$ and $\mathbb R$ in $M$. The inclusion is consequently not a full-source isomorphism.

*Verification.* Monotonicity of $t$ on future causal curves makes the slab causally convex. The displayed hypersurface is Cauchy in both spacetimes. The two scalar classes agree on $U^2$ by restriction, so their traces and complete roots on this common carrier agree. The null lines have $t=s$ after the stated normalization, giving the two intervals. The point inclusion is not surjective, and Theorem 9.4 gives the last conclusion. ∎

The full embedding correspondence now gives the comparison maps needed for marked global developments. Ordinary-pair atlas presentations are treated separately in §11–§12.

<div id="sec:global-maximal-source-development"></div>

## 10. Maximal globally hyperbolic source developments

The embedding theorem transfers the global Cauchy property of the vacuum Einstein equation to normalized full sources. The classical existence theorem is an external input: for smooth vacuum constraint data on a connected three-manifold, the theorem of [Choquet-Bruhat and Geroch 1969](#ref-ChoquetBruhatGeroch1969) gives a globally hyperbolic development receiving an initial-data-preserving isometric embedding from every other such development. We use the smooth formulation in [Sbierski 2016](#ref-Sbierski2016), Theorem 2.8. No compactness or completeness hypothesis on the initial Riemannian metric is imposed there. We supply the actual spin extension and the source comparison argument below.

<div id="def:global-marked-vacuum-data"></div>

**Definition 10.1 (Marked vacuum data and source developments).**

A marked vacuum initial data set is

$$
\mathfrak d=(\Sigma,h,K,P_\Sigma),
$$

where $\Sigma$ is a connected oriented smooth three-manifold, $h$ is a smooth Riemannian metric, $K$ is a smooth symmetric two-tensor, and $P_\Sigma$ is an actual principal $\operatorname{Spin}(3)$ lift of the oriented $h$-orthonormal frame bundle. The data obey

$$
R_h+(\operatorname{tr}_hK)^2-|K|_h^2=0,
\qquad
\operatorname{div}_hK-\mathrm d(\operatorname{tr}_hK)=0.
$$ {#eq:global-marked-vacuum-constraints}

Our sign convention is $h=-\iota^*g$ and

$$
K(X,Y)=-g(\nabla_{\iota_*X}n,\iota_*Y),
$$ {#eq:global-initial-second-form-sign}

where $n$ is the future unit normal. Thus $K=\tfrac12\partial_t h_t$ when $g=\mathrm dt^2-h_t$ in Gaussian coordinates, as in Paper 3, Theorem 2.6 ([Isthmus 2026c](#ref-IsthmusSmooth2026)). The initial orientation and the future normal determine the spacetime orientation.

A *marked source development* of $\mathfrak d$ is a global normalized full source $S$ together with an embedding $\iota:\Sigma\to RS$ onto a whole smooth spacelike Cauchy hypersurface and an actual principal $\operatorname{Spin}(3)$ identification

$$
\beta:P_\Sigma\longrightarrow\iota^*P_{RS,n}.
$$ {#eq:global-initial-spin-marking}

Here $P_{RS,n}$ is the reduction of the actual Lorentz spin bundle to frames whose future time vector is $n$, and $\beta$ covers the spatial orthonormal-frame map induced by $\iota$. The induced metric and second fundamental form must be exactly $h,K$. A morphism is a full open comparison $(A,f,\widetilde f)$ satisfying

$$
f\iota_0=\iota_1,
\qquad
\widetilde f\,\beta_0=\beta_1.
$$ {#eq:global-marked-development-arrow}

The latter equation is an equality of actual principal maps on the marked initial reduction. Denote the resulting category by $\mathsf{Dev}_{\mathrm{src}}(\mathfrak d)$. Its geometric counterpart $\mathsf{Dev}_{\mathrm{geom}}(\mathfrak d)$ has the same initial markings and physical-spin isometric embeddings as arrows. Lemma 3.5 shows that all these development arrows have causally convex image and are Cauchy arrows.

<div id="lem:global-initial-spin-extension"></div>

**Lemma 10.2 (Actual spin extension from a Cauchy marking).**

Let $(M,g,\iota)$ be an oriented and time-oriented globally hyperbolic development of $(\Sigma,h,K)$. The prescribed $P_\Sigma$ extends to an actual Lorentz spin structure on $M$ with an initial identification $\beta$. Any two such extensions have a unique frame-compatible principal spin isomorphism that agrees with their initial identifications.

If $f:M_0\to M_1$ is a time-orientation-preserving isometric embedding of two such marked developments with $f\iota_0=\iota_1$, it has a unique actual spin lift satisfying $\widetilde f\beta_0=\beta_1$.

*Proof.* Choose a smooth future timelike vector field on $M$ and multiply it by a positive smooth function so that its norm in a complete auxiliary Riemannian metric is bounded. The resulting vector field $X$ is complete: bounded auxiliary speed gives a limit at any finite flow-parameter endpoint, and the smooth local flow then extends the orbit. Its orbits are also inextendible as unparametrized timelike curves. If an orbit approached an endpoint in $M$ as its flow parameter tended to $+\infty$ or $-\infty$, it would eventually remain in a flow box with $X=\partial_r$. There $r(s)=s+c$, which cannot converge to an interior point of that box. Finite-parameter endpoints have already been excluded by completeness. Every orbit therefore meets $\iota(\Sigma)$ once. Transversality and smooth dependence of the flow show that

$$
\Phi:\mathbb R\times\Sigma\longrightarrow M,
\qquad
\Phi(s,x)=\operatorname{Fl}^X_s(\iota(x))
$$ {#eq:global-marked-cauchy-flow}

is a diffeomorphism. It is a product identification relative to the specifically marked hypersurface. Its other slices need not be spacelike, and no such property is used.

On $\iota(\Sigma)$, adjoining the future unit normal to a spatial orthonormal frame identifies the Lorentz frame bundle with the extension of the spatial frame bundle by $\operatorname{SO}^+(1,3)$. Correspondingly extend the prescribed principal bundle by its structure group:

$$
P^{\mathrm{Lor}}_\Sigma
=P_\Sigma\times_{\operatorname{Spin}(3)}
\operatorname{Spin}^+(1,3).
$$

It has its actual double covering of the Lorentz frame bundle over $\iota(\Sigma)$. Levi-Civita parallel transport along the finite orbit segment from $\Phi(0,x)$ to $\Phi(s,x)$ identifies that frame fiber with the frame fiber over $\Phi(s,x)$. It preserves the metric, orientation and time orientation and depends smoothly on $(s,x)$. Pulling $P^{\mathrm{Lor}}_\Sigma$ to $\mathbb R\times\Sigma$ and using this frame identification defines the required principal spin bundle over $M$ and its actual initial marking.

For uniqueness, start with two extensions and their fixed identification over the initial reduction. Equivariance extends that identification to all Lorentz spin frames over $\iota(\Sigma)$. Lift the same frame-transport paths to the two spin double coverings. Unique path lifting extends the initial comparison to a smooth frame-compatible principal map over every orbit. Local covering charts show smoothness, and uniqueness of path lifting makes it equivariant for the structure group. Any two such comparisons differ by a continuous function with values in $\{+1,-1\}$. The function is one along the initial hypersurface and hence on connected $M$, so the comparison is unique. In particular choices of the auxiliary timelike flow lead to uniquely isomorphic marked extensions.

For the last assertion, pull the target spin structure back under the frame map of $f$. Its prescribed initial identification agrees with the source marking after applying $\beta_1\beta_0^{-1}$. The uniqueness statement just proved supplies a unique comparison between this pullback spin structure and the source structure. This is precisely the required spin lift of $f$. Its central sign is fixed by the initial marking. ∎

<div id="lem:global-marked-development-uniqueness"></div>

**Lemma 10.3 (Uniqueness of a marked development embedding).**

There is at most one morphism between two objects of $\mathsf{Dev}_{\mathrm{geom}}(\mathfrak d)$, and at most one morphism between two objects of $\mathsf{Dev}_{\mathrm{src}}(\mathfrak d)$.

*Proof.* Suppose $f_1,f_2:M_0\to M_1$ are two time-orientation-preserving isometric embeddings agreeing with the marked initial maps. Their values and differentials agree on the tangent space to the initial hypersurface. Each differential also sends the future unit normal to the same future unit normal. Hence their full one-jets agree at an initial point.

Isometric immersions with the same one-jet at a point agree on a connected domain, by Sbierski, Lemma 3.1 ([Sbierski 2016](#ref-Sbierski2016)). The mechanism is geodesic uniqueness: in a normal neighborhood of an agreement point, both maps send each radial geodesic to the same target geodesic with the same initial vector. The set where the maps and their differentials agree is consequently open; it is closed by smoothness and is nonempty. Connectedness gives $f_1=f_2$ on $M_0$.

Lemma 10.2 makes their actual spin lifts equal. The full Hom bijection of Theorem 9.4 then makes two full source comparisons with these labels equal. ∎

<div id="thm:global-maximal-source-development"></div>

**Theorem 10.4 (Maximal globally hyperbolic source development).**

For every marked vacuum initial data set $\mathfrak d$ of Definition 10.1, the category $\mathsf{Dev}_{\mathrm{src}}(\mathfrak d)$ has a terminal object $S_{\max}(\mathfrak d)$. Its recognized spacetime is a classical maximal globally hyperbolic development of $(\Sigma,h,K)$, equipped with the actual spin extension and the initial marking of Lemma 10.2.

For every marked source development $S$ there is a unique full source embedding

$$
S\longrightarrow S_{\max}(\mathfrak d)
$$ {#eq:global-maximal-source-universal-arrow}

preserving the initial point and spin markings. This embedding preserves all complete fields, source and target associators, evaluations and point connections on its image. It sends each source incidence fiber to its actual interval inside the corresponding maximal-development ray. Any two choices of $S_{\max}(\mathfrak d)$ have a unique full marked isomorphism.

*Proof.* Apply the classical smooth maximal-development theorem stated at the start of this section to obtain $(M_{\max},g_{\max},\iota_{\max})$. Its usual signature can be changed to $(+---)$ by multiplying the metric by $-1$; the Levi-Civita connection and Ricci tensor do not change, and the initial second-form convention is the one in Definition 10.1. The initial orientation and future normal provide the required spacetime orientation. Lemma 10.2 supplies a spin structure and actual initial marking. The native construction of Corollary 7.8 gives a normalized full source with this recognized geometry; transport the initial maps through its recognition identification. Call the result $S_{\max}(\mathfrak d)$.

Let $S$ be any other marked source development. Its recognized geometry is a smooth globally hyperbolic development of the same data by Definition 10.1. The classical maximal property gives an initial-data- and time-orientation-preserving isometric embedding $f:RS\to M_{\max}$. It preserves the spacetime orientation because it preserves the marked spatial orientation and future normal. The image contains $\iota_{\max}(\Sigma)$, which is Cauchy in both the image and $M_{\max}$. Lemma 3.5 proves causal convexity of that image, so $f$ belongs to the embedding category of Theorem 9.4. Lemma 10.2 supplies its unique actual spin lift matching the two initial markings. Theorem 9.4 now lifts this pair to a full source embedding $S\to S_{\max}(\mathfrak d)$.

Lemma 10.3 proves uniqueness of this full marked embedding. Thus $S_{\max}(\mathfrak d)$ is terminal. The complete-field assertion is part of the full Hom theorem, and the assertion about ray intervals follows from the fieldwise restriction used in its definition. Terminal objects have unique mutually inverse marked arrows, proving independence of all choices. ∎

<div id="cor:global-marked-development-correspondence"></div>

**Corollary 10.5 (Correspondence of marked developments).**

Recognition and the native construction restrict to an equivalence

$$
\mathsf{Dev}_{\mathrm{src}}(\mathfrak d)
\simeq
\mathsf{Dev}_{\mathrm{geom}}(\mathfrak d).
$$ {#eq:global-marked-development-equivalence}

It preserves and reflects maximal globally hyperbolic developments. Changing the entire initial marking by an orientation-preserving initial-data isometry with an actual $\operatorname{Spin}(3)$ lift gives the corresponding unique marked comparison of maximal sources; the identity and composition laws follow from uniqueness.

*Proof.* Theorem 9.4 is fully faithful on the underlying open comparisons. Restricting its Hom bijection to maps obeying the two marking equations of Definition 10.1 gives full faithfulness on the marked development categories. Every geometric marked development has a native source, and its initial maps transport through the counit of Corollary 7.8, giving essential surjectivity. Terminal objects are preserved and reflected by this equivalence. For a change of initial marking, regard the target marked development as a development of the source data by precomposing its initial maps with that change. Theorem 10.4 gives the unique comparison; applying the inverse change gives its inverse. Composition follows because two such composites preserve the same actual initial marking. ∎

<div id="rem:global-maximal-source-scope"></div>

**Remark 10.6 (Meaning of maximality).**

Theorem 10.4 transfers the classical Einstein maximal-development theorem through the full source embedding correspondence. The terminal property is relative to smooth globally hyperbolic developments of the fixed marked data. It allows finite affine intervals and gives no extension beyond a Cauchy horizon. Corollary 12.5 presents this object by an atlas under the local coverage hypothesis.

<div id="sec:global-ordinary-pair-atlases"></div>

## 11. Ordinary-pair atlases and geometric descent

The independent full sources of §6–§10 need no ordinary-pair presentation. To present a global source by ordinary data, we execute a pair of classes in each chart. Each chart retains its whole input and physical scale, while its comparisons are defined on the actual overlaps of retained spacetime cores. The resulting global object is an atlas of such executions; the different whole inputs are not identified outside those cores.

Two local results from Paper 3 have different roles in this construction. Its Theorem 7.11 gives the full comparison over a supplied physical isometry and actual spin lift, after restricting to suitable local representatives. This suffices for descent and for the comparison of already supplied atlases. Its Theorem 5.7 supplies an ordinary-pair presentation of an arbitrary smooth Ricci-flat germ and is used separately for coverage. The latter theorem includes the protected relative extension of Paper 3, Appendix B. Throughout this section those results are inputs in the precise pinned revision listed in the bibliography ([Isthmus 2026c](#ref-IsthmusSmooth2026)).

<div id="sec:ordinary-atlas-local-comparisons"></div>

### 11.1. Executed charts and locally represented comparisons

An executed ordinary-pair chart consists of a display $P=(c,r,V,\mathfrak m)$ of Paper 3, Definition 8.1, together with its retained actual domains. Here

$$
c=(c_+,c_-)
\in H^1(\mathscr E_2^\bullet)
\oplus H^1(\mathscr E_{-6}^\bullet)
$$

is a pair of degree-one classes in the actual coefficient complexes of Paper 3, Proposition 3.7, on the flat initial sphere bundle $P_+T^*\mathbb R^3\simeq\mathbb R^3\times S^2$. The weighted admissibility conditions are those of its §5.1. Here $r>0$ is the physical scale, $V$ is its marked initial patch, and $\mathfrak m$ includes the actual spin marking and the retained spacetime point. The whole pair is executed by Paper 3, Theorem 4.18, its derived initial data are developed, and the numerical scale is restored by that paper's Proposition 5.6. These operations supply the local metric, actual spin structure, Cartan fields and finite-rank diagrams. Their local wave enrichment and stored presentations are those of Paper 3, Definition 7.7.

Write $W_P$ for a retained buffered wave parent and $O_P\subset W_P$ for the actual point core used as a chart. The parent and its carrier markings satisfy Paper 3, Definition 6.12, with all null directions over the core retained. The core may be further restricted, with buffered parents retained for the necessary transverse transports. Such a restriction may select a new spacetime marking inside its smaller core; it retains the same whole input and executed fields. It is a nonempty connected open four-manifold, and we may initially take it relatively compact and globally hyperbolic in its executed geometry. Neither $O_P$ nor $W_P$ denotes the whole $\mathbb R^3$ domain of the generating pair. Denote the executed complete local source, restricted to these markings, by $E P$.

<div id="lem:ordinary-atlas-local-comparison-sheaf"></div>

**Lemma 11.1 (Comparisons on prescribed overlap domains).**

Let $P,P'$ be executed charts. Suppose $f:D\to D'$ is an actual physical isometry between open subsets of their point cores, with a specified actual principal spin lift. On $D$ there is a unique locally represented full comparison over these labels, in the following sense: every point has a retained neighborhood on which the comparison is an actual representative satisfying all full source equations of Paper 3, Definition 7.7, and the representatives agree after restriction and normalized presentation changes on common refinements. These locally represented comparisons form a sheaf on the prescribed point domain. They have identity, inverse, composition and restriction laws.

The representatives cover the prescribed domain of the physical and spin maps; the retained neighborhoods may vary across it.

*Proof.* At any $p\in D$, re-mark the restricted source and target displays at $p$ and $f(p)$ as in Paper 3, Definition 7.7. These spacetime marks are auxiliary presentation labels; the whole pairs, their initial readouts and the retained parent fields are unchanged. Restrict $f$ and its spin lift to sufficiently small common isometric neighborhoods and then to the retained parents required by Paper 3, Theorem 7.11. That theorem constructs a full lift, including the whole moving sky, all complete coefficients, evaluation, both point connections and stored cells, on a smaller neighborhood of that point. These neighborhoods cover $D$.

For two representatives over the same actual point and spin maps, the uniqueness part of that theorem identifies their germs at every point of their common domain. Equality is therefore realized on a further cover by smaller retained neighborhoods and compatible normalized presentation changes. This is precisely the declared equivalence of local representatives. A compatible collection over an open cover glues by taking the union of its representatives; the overlap equivalence makes the resulting collection well defined. The same local uniqueness proves separatedness and uniqueness of this glued section. Thus the locally represented comparisons form a sheaf. No one uniform shrinking of a noncompact or disconnected overlap is required.

The local identity, inverse, composition and restriction laws are Paper 3, Theorem 7.11. They pass to these collections after common refinement. Their principal spin maps compose as supplied. Every asserted identity holds on the full point families of its local representative, not only on evaluations at individual points. ∎

<div id="sec:ordinary-atlas-records"></div>

### 11.2. The atlas records and the quotient tests

<div id="def:global-ordinary-pair-atlas"></div>

**Definition 11.2 (Globally admitted ordinary-pair atlas).**

An ordinary-pair atlas $\mathcal P$ consists of executed charts and overlap comparisons satisfying the following local and global conditions.

1. It has a countable collection of executed charts $P_i$ with actual cores $O_i$, buffered parents $W_i$, local metrics $g_i$ at physical scale, and actual principal spin bundles $P_i^{\mathrm{spin}}$. The metrics and bundles are read from those executions; they are not additional generating inputs.
2. For each ordered pair supply an open set $O_{ij}\subset O_j$ and a diffeomorphism $\theta_{ij}:O_{ij}\to O_{ji}\subset O_i$, with the identity, inverse and cocycle laws on their full defined domains. Empty overlaps are allowed. Supply actual principal spin maps $\widetilde\theta_{ij}$ covering the corresponding frame maps and obeying the same laws as literal principal maps. On each $O_{ij}$ supply a locally represented full comparison $A_{ij}:E P_j\to E P_i$ of Lemma 11.1 over $(\theta_{ij},\widetilde\theta_{ij})$. Require $A_{ij}A_{jk}=A_{ik}$ in that sheaf of comparisons wherever the compositions are defined. No component of an overlap is omitted.
3. Form the quotient $X=(\bigsqcup_i O_i)/\!\sim$ generated by these point identifications. Test that the quotient maps $\iota_i:O_i\to X$ are injective open maps and that the declared transition domains are exactly their overlaps:

   $$
   \iota_j^{-1}\bigl(\iota_i(O_i)\bigr)=O_{ij},
   \qquad
   \iota_i\theta_{ij}=\iota_j\quad\text{on }O_{ij}.
   $$ {#eq:ordinary-atlas-effective-chart-tests}

   Require $X$ to be connected and Hausdorff, and the family $U_i=\iota_i(O_i)$ to be locally finite. The countable chart bases then make $X$ second countable. These are global quotient tests, including exclusion of additional identifications caused by chains of overlaps.

4. The local full comparison tests identify the metric cone and physical density on overlaps. On the quotient charts of item 3 these agreeing cones define a cone field on $X$. Require that field to be strongly causal and all its causal diamonds $J^+(x)\cap J^-(y)$ to be compact. This is the global hyperbolicity test on $X$.

For the complete records in item 2, retain the source and target stored associators. In a common local ray refinement, let $a,b,c$ index the stored charts within one executed source, and write its transitions as $\varphi^i_{ab},\tau^i_{ab},C^i_{abc}$. An overlap comparison from chart $j$ to chart $i$ has algebra vertices $k_{ij,a}$, module vertices $\Xi_{ij,a}$ and normalized edge units $t_{ij,ab}$. Besides its evaluation and all-section connection tests, it obeys

$$
\begin{aligned}
k_{ij,a}\varphi^j_{ab}
 &=\operatorname{Ad}(t_{ij,ab})\varphi^i_{ab}k_{ij,b},\\
t_{ij,ab}\varphi^i_{ab}(t_{ij,bc})C^i_{abc}
 &=k_{ij,a}(C^j_{abc})t_{ij,ac},\\
\Xi_{ij,a}\tau^j_{ab}
 &=t_{ij,ab}\tau^i_{ab}\Xi_{ij,b}.
\end{aligned}
$$ {#eq:ordinary-atlas-full-overlap-equations}

Thus the atlas cocycle is an equality of full comparisons modulo their stated presentation changes. After one further common refinement, equality of two representatives is expressed by their actual normalized change-of-presentation units, transporting their evaluations and connections at the same time. If $U_{ijk}$ compares $A_{ij}A_{jk}$ with $A_{ik}$, then in compatible vertex coordinates

$$
k_{ij}k_{jk}=\operatorname{Ad}(U_{ijk})k_{ik},
\qquad
\Xi_{ij}\Xi_{jk}=U_{ijk}\Xi_{ik},
$$

and the edge units have the transformation law of Definition 7.2. On quadruple overlaps the normalized changes obey

$$
U_{ijk}U_{ikl}=k_{ij}(U_{jkl})U_{ijl}.
$$ {#eq:ordinary-atlas-presentation-coherence}

These equations are required on their local representatives and are preserved under refinement. Their uniqueness follows from the normalized center calculation in Paper 3, Lemma 7.8, or Lemma 7.3 here. The strict actual spin cocycle is separate: a sign in a principal spin transition cannot be removed by a scalar presentation cell.

<div id="prop:ordinary-atlas-geometric-descent"></div>

**Proposition 11.3 (Geometric descent of a supplied atlas).**

Every atlas of Definition 11.2 determines a smooth oriented and time-oriented globally hyperbolic Ricci-flat spacetime $Q\mathcal P$ at physical scale, with an actual principal spin structure. Its underlying manifold is the tested quotient $X$. Each $\iota_i$ is an actual physical-spin identification from the chart onto its image, and the descended structure is unique with these identifications. The charts and overlap maps supply the local inputs for descent.

*Proof.* The injective open quotient maps and exact overlap tests give an atlas on $X$ whose coordinate changes are the supplied smooth diffeomorphisms. The Hausdorff test and the countable union of the images of countable chart bases make this a Hausdorff second-countable smooth four-manifold. There is no additional local quotient by an undisplayed transition. Connectedness is one of the global tests.

Every local representative of $A_{ij}$ is a full source comparison. Paper 3, Theorem 7.11, therefore recognizes its point map as a physical isometry, including orientation, time orientation and numerical scale. These are identities of smooth fields, so their validity on a cover of $O_{ij}$ proves them on the entire declared overlap. Thus the $g_i$ and orientations descend to unique smooth fields on $X$. Lorentz signature and Ricci flatness are local and are inherited from each executed chart. Item 4 gives global hyperbolicity for the descended cone. No assertion of global hyperbolicity follows from the quotient topology alone.

Glue the principal bundles $P_i^{\mathrm{spin}}$ by the actual maps $\widetilde\theta_{ij}$. The strict cocycle makes this equivalence relation compatible with the principal action. On $U_i$ the quotient is identified with $P_i^{\mathrm{spin}}$, so these local trivializations make it a smooth principal $\operatorname{Spin}^+(1,3)$ bundle over $X$. The frame-covering maps agree under the derivative transitions, giving its actual double cover of the descended oriented and time-oriented orthonormal frame bundle. The central signs used in the gluing are retained. Standard local bundle trivializations over the Hausdorff second-countable base give a Hausdorff second-countable total space.

These local identifications also prove uniqueness: any descended metric or principal bundle with the specified chart identifications agrees on every member of the cover, and its transition maps are exactly the supplied ones. Tensorial geometric and finite-rank diagrams glue through the same physical-spin identifications. Carrier-dependent scales and affine origins are compared by their specified changes. ∎

<div id="sec:ordinary-atlas-arrows-descent"></div>

### 11.3. Arrows and effective descent

<div id="def:ordinary-atlas-embedding-category"></div>

**Definition 11.4 (Atlas comparisons).**

Let $\mathsf{PairAtl}^{\infty,\mathrm{cc}}_{\mathrm{GH},0}$ have the atlases of Definition 11.2 as objects. An arrow $\mathcal P\to\mathcal P'$ consists of a smooth open embedding $f:X\to X'$ with causally convex image, together with compatible locally represented full comparisons between their executed charts over $f$. Concretely, refine the source point cover against the pullbacks of target chart images. On a cover of each refined point domain supply a full comparison over the map $\iota_j'^{-1}f\iota_i$, with its actual spin lift. Require the comparison diagrams with all source and target transitions to commute in the sheaf of Lemma 11.1, with strict equality of their actual point and spin maps. All stored equations are those in Definition 11.2, on their actual local domains.

Representatives are identified by common point and ray refinements and normalized presentation changes. Identified representatives have the same point map and the same induced actual principal spin map. An atlas refinement restricts its point cores and retains the whole input of the parent chart, with its actual inclusion comparisons; refinements give canonical isomorphisms in this category.

Composition uses the local full comparison composition after a common refinement. The image condition is tested with the descended metric. It is global: local isometry of individual pieces alone does not assert injectivity or causal convexity of their assembled map. Restricting atlas records to an arbitrary open set means restricting their point charts and comparison sheaves; if its recognized geometry is globally hyperbolic, each connected component gives an admitted atlas after an appropriate locally finite refinement.

<div id="thm:ordinary-atlas-full-hom"></div>

**Theorem 11.5 (Full Hom for supplied atlases).**

The construction $Q$ of Proposition 11.3 extends to a fully faithful functor

$$
Q:\mathsf{PairAtl}^{\infty,\mathrm{cc}}_{\mathrm{GH},0}
\longrightarrow\mathsf{Vac}^{\infty,\mathrm{cc}}_{\mathrm{GH},0}.
$$ {#eq:ordinary-atlas-geometric-functor}

For two supplied atlases its Hom map is a bijection onto the physical isometric open embeddings with causally convex image and specified actual spin lifts. It preserves restrictions and Cauchy arrows.

*Proof.* A supplied local full comparison recognizes the local point map as a physical isometry. These equations hold on a cover of $X$, so the specified global embedding $f$ is a physical isometry onto its image. Compatibility with the atlas spin transitions makes its local principal maps glue to one actual principal spin lift. The image is causally convex by the arrow test and globally hyperbolic because it is isometric to $X$. Thus $Q$ maps arrows to the stated geometric arrows.

Conversely, let $(f,\widetilde f)$ be such a physical-spin embedding. At each point select a source chart and a target chart containing its image, and restrict to a point neighborhood on which both chart maps are defined. Their actual geometric and spin identifications give the prescribed local map between the executed sources. Lemma 11.1 supplies its unique locally represented full lift. On overlaps the two constructions differ only by the atlas transitions: after composing with those transitions, they lie over the same actual physical and spin map. Uniqueness in Lemma 11.1 makes the comparison diagram commute. The normalized representative cells satisfy the stored two-associator equations, with their usual composition formula, and their coherence is the equation in Definition 11.2. The unique lifts on this cover therefore glue to an atlas arrow over the given global map.

If two arrows have the same geometric and spin image, apply Lemma 11.1 on a common refinement. Their local representatives agree there in the required quotient, hence define the same atlas arrow. This proves the Hom bijection. Composition of geometric embeddings has causally convex image by the argument in Theorem 9.4. The locally constructed lift of the composite agrees with the composite of local lifts by their uniqueness, proving functoriality and the category laws. Actual principal maps compose before any scalar presentation quotient. Refinement, restriction and changes of local carrier give the same comparisons because they have the same actual labels. Cauchy arrows are detected by the image of their point maps. ∎

<div id="prop:ordinary-atlas-effective-descent"></div>

**Proposition 11.6 (Effective descent with the global admission tests).**

Let $X$ be a connected Hausdorff second-countable smooth four-manifold covered by open sets $V_a$. On each $V_a$ supply an ordinary-pair atlas, with its quotient identified with $V_a$, and compatible locally represented full isomorphisms over the identity on overlaps. Require the actual principal spin transitions to obey the strict cocycle and the full comparisons to obey their normalized cell cocycle. If the descended metric satisfies the global hyperbolicity test, these data descend to an admitted ordinary-pair atlas on $X$. Its restriction to each $V_a$ is isomorphic to the supplied atlas by comparisons compatible with the original descent data. Compatible arrows over a fixed admissible global point map descend uniquely.

*Proof.* First apply Proposition 11.3 locally. The overlap comparisons identify the metrics, orientations and physical densities on the $V_a$, so these smooth fields glue on the specified base $X$. Their actual spin maps glue the local principal bundles by the strict cocycle. The resulting metric is Ricci-flat by locality and globally hyperbolic by the stated test.

Collect the executed charts from the supplied atlases and restrict them to smaller cores within the $V_a$. The collected family covers $X$. On intersections of charts coming from different $V_a$, compose their local chart comparisons with the supplied descent comparison. Lemma 11.1 gives compatibility on refinements, and the given descent cocycle gives the triple identity. Both the raw source associators and the normalized comparison cells are transported by this composition.

We explain the countable locally finite choice of cores. A Hausdorff second-countable manifold has countable locally finite relatively compact refinements of open covers and shrinkings whose closures remain in the corresponding refinement sets. Choose such a refinement of the collected chart domains. Cover each compact closure in a shrinking by finitely many smaller retained neighborhoods belonging to its selected executed chart. The neighborhoods can be chosen inside the corresponding locally finite refinement set, so their union is still locally finite and countable and covers $X$. All whole input pairs are retained unchanged. The parent markings are restricted only where the common local comparison construction requires it. If desired, strong causality and a second local shrinking make these cores causally convex and globally hyperbolic simultaneously in the descended metric and in their executed parent; the two metrics agree on the local identification domain.

The resulting quotient is the given $X$: its chart maps are the actual inclusions through the supplied identifications, so they are injective and have precisely the declared overlaps. All quotient and causal tests of Definition 11.2 hold. The local inclusion comparisons give the isomorphisms to the original atlases, and their compatibility follows from the same descent maps used to define the cross-chart transitions.

For arrows, the compatible local point maps already cover the stipulated admissible global map. Their actual spin maps glue by their transition equations. Theorem 11.5 gives the unique full atlas lift of that map and spin lift; its restriction agrees with every supplied local arrow by Lemma 11.1. ∎

<div id="sec:ordinary-atlas-coverage"></div>

### 11.4. Coverage and the geometric equivalence

<span class="paper-leadin">**Common causal neighborhoods.**</span> Let a physical isometry identify open point neighborhoods in two globally hyperbolic spacetimes. Around a chosen point, take a causally convex target neighborhood inside the image, then a causally convex source neighborhood inside its preimage, and finally a smaller globally hyperbolic target diamond inside the latter image. A source causal curve joining points of the final preimage stays in the intermediate source neighborhood. Its image therefore stays in the final target diamond. The last diamond and its isometric preimage are globally hyperbolic and causally convex in their respective ambient spacetimes. The construction takes place inside the given isometry domains.

<div id="thm:ordinary-atlas-geometric-equivalence"></div>

**Theorem 11.7 (Coverage by ordinary-pair atlases).**

Assume Paper 3, Theorem 5.7, in addition to the execution and local full comparison inputs above. Every object of $\mathsf{Vac}^{\infty,\mathrm{cc}}_{\mathrm{GH},0}$ is the recognized geometry of a globally admitted ordinary-pair atlas. Consequently $Q$ is an equivalence. Its inverse returns an atlas up to full comparison, preserves actual principal spin maps and physical scale, and has natural unit and counit comparisons satisfying both triangle identities.

*Proof.* Let $(M,g,P_M)$ be a smooth globally hyperbolic physical-spin spacetime. At each point choose a spacelike tangent plane and a local actual spin marking. Paper 3, Theorem 5.7, produces a whole ordinary pair, physical scale and an isometry germ from its execution to the given metric germ, with the actual spin comparison. Choose an actual representative of that germ on some open core and shrink within its domain. This gives an executed chart and an actual physical-spin identification with an open neighborhood in $M$. Different points may require different pairs, scales and widths.

Apply the common-neighborhood construction above to each of these chart identifications. Further shrinking gives the retained buffers and whole-sky carrier coverage of Paper 3, Definitions 6.12 and 8.1.

Choose a countable locally finite covering refinement as in the proof of Proposition 11.6. Denote the actual chart identifications by $\iota_i:O_i\to U_i\subset M$, with their actual spin maps. On every actual overlap set put

$$
\theta_{ij}=\iota_i^{-1}\iota_j,
\qquad
\widetilde\theta_{ij}
=\widetilde\iota_i^{-1}\widetilde\iota_j.
$$ {#eq:ordinary-atlas-coverage-transitions}

They satisfy the strict point and principal spin cocycles on the entire defined overlaps, including disconnected ones. Lemma 11.1 supplies the corresponding locally represented full comparisons. Their triple law follows from uniqueness over these exact maps, with the representative cells of Definition 11.2. The quotient is $M$, so its Hausdorff, second-countability and global hyperbolicity tests hold. This constructs the required atlas with all its actual labels.

Theorem 11.5 supplies full faithfulness, so $Q$ is an equivalence. To state its inverse comparisons, choose one such atlas $K M$ and a physical-spin identification $b_M:QK M\to M$ for each object. For a geometric embedding $f:M\to N$, define $Kf$ by the unique atlas lift of

$$
b_N^{-1} f b_M.
$$ {#eq:ordinary-atlas-inverse-arrow}

The Hom bijection gives identities and composition. Its counit is $b$, and the unit at an atlas $\mathcal P$ is the unique arrow over $b_{Q\mathcal P}^{-1}$. Applying $Q$ to the naturality diagrams and to both triangle identities gives the corresponding identities of actual point and spin maps. Faithfulness proves them in the atlas category, with all complete source fields and cells retained. Changing the selections gives the unique natural comparison over the corresponding $b$ maps. ∎

<div id="rem:ordinary-atlas-dependency-scope"></div>

**Remark 11.8 (The extension input for ordinary-pair coverage).**

The extension input used for coverage preserves the data on a smaller initial disk and allows a decaying exterior tail; it does not prescribe the exterior fields or asymptotic charges. Its family version uses one selected extension whose finite weighted spatial and parameter estimates hold on the initially fixed base neighborhood. These are the conclusions of Paper 3, Theorem B.1, used in its Theorem 5.7 and Proposition 5.8. Existence obtained separately at each higher Sobolev order would not supply that same-branch family assertion.

<div id="sec:ordinary-atlas-global-completion"></div>

## 12. Global completion of ordinary-pair atlases

Let $\mathfrak A$ be an admitted ordinary-pair atlas of §11. Denote its recognized spacetime by $M=Q\mathfrak A$, including the descended numerical metric, orientations and actual spin bundle. Write $P_i$ for its ordinary-pair displays, $O_i$ for their retained execution cores and $\iota_i:O_i\to M$ for the quotient charts. As in §11, the overlap comparison $A_{ij}$ goes from the $j$-display to the $i$-display over $\theta_{ij}$, with $\iota_i\theta_{ij}=\iota_j$. The atlas comparisons are actual local full comparisons, represented on retained parents and taken modulo their normalized presentation changes and refinements.

The chart squares need not cover $M^2$, and a chart image need not be causally convex in $M$. We first descend the metric, then construct its whole-product wave class by Theorem 4.4 and compare the local kernels on common causally convex refinements.

<div id="def:ordinary-atlas-admitted-completion"></div>

**Definition 12.1 (An admitted global completion).**

An admitted global completion of $\mathfrak A$ consists of a global normalized full source $S$ of Definition 7.1, an actual physical-spin isometry

$$
b:RS\longrightarrow Q\mathfrak A,
$$ {#eq:ordinary-atlas-completion-marking}

and compatible local full comparisons $\eta_i$ from the executed displays $E P_i$ to the local fields of $S$, over $b^{-1}\iota_i$ and its specified principal spin map. These comparisons are invertible maps on their tested local domains, supplied on a common refinement of the point cores. Their representatives obey the full algebra, module, evaluation, point-connection, finite-rank and normalized two-associator comparison equations of Paper 3, Definition 7.7 ([Isthmus 2026c](#ref-IsthmusSmooth2026)). The target fields are the actual restrictions of $S$, expressed on retained conic domains by the relative carrier comparisons of §8. On overlaps require

$$
\eta_i A_{ij}=\eta_j
$$ {#eq:ordinary-atlas-completion-overlaps}

in that full comparison quotient. Principal spin maps in this identity agree as actual maps.

A morphism between two completions $(S_0,b_0,\eta^0)$ and $(S_1,b_1,\eta^1)$ is a full source isomorphism $A:S_0\to S_1$ such that

$$
b_1RA=b_0,
\qquad
A\eta_i^0=\eta_i^1
$$ {#eq:ordinary-atlas-completion-arrow}

on their common local refinements, including the actual spin maps. These objects and arrows form the completion groupoid over the fixed admitted atlas.

<div id="thm:ordinary-atlas-admitted-completion"></div>

**Theorem 12.2 (Existence and uniqueness of admitted global completion).**

Every supplied admitted ordinary-pair atlas has an admitted global completion. Its completion groupoid is nonempty and has exactly one arrow between every two objects. The global completion retains the descended physical metric and actual spin bundle, both Weyl chiralities, the whole point-labelled null incidence and realized affine domains, the normalized finite-rank models, and the entire canonical wave packet with its complete comparison records.

Its scalar class is the class of Theorem 4.4 on $Q\mathfrak A$. Uniqueness is within the independently admitted global sources: the global wavefront or equivalent whole-Cauchy test of Definition 6.7 is part of this assertion.

*Proof.* The geometric descent result of §11 supplies a smooth globally hyperbolic Ricci-flat spacetime $M$ with actual spin. This step uses the supplied geometric and principal-spin overlap equations and the global causal tests of the atlas.

Apply the native construction of §3–§7 to $M$. The full null phase is formed from its metric, and its quotient by the actual maximal null geodesics is identified with a whole Cauchy cosphere bundle by Theorem 3.2. This constructs its Hausdorff global ray space and connected realized intervals; it does not assume that a direct quotient of local ray charts has those properties. The finite-rank diagrams are the tensorial canonical models of §6.3, with identity initial comparisons on the entire Cauchy phase section. Theorem 4.4 constructs a global scalar representative and its unique admitted class on $M^2$. Theorems 5.3 and 5.5 construct its complete carrier algebra, point-labelled modules, full evaluation and all-section point connections.

Choose a whole Cauchy carrier $\Sigma_M$ for a presentation. On an open conic cover of $T^*\Sigma_M\setminus0$, use the restrictions of the intrinsic native algebra and module sheaves, with identity normalizations and identity native overlap cells. Each module chart is defined on the entire point-labelled incidence above that ray chart, for all $p\in M$. Thus these are global normalization records satisfying Definition 7.1. This supplies a global full source $N M$ and its physical-spin recognition map $b:RN M\to M$. The construction of these global records is separate from the comparison with the stored records of the input displays.

For the local comparisons in Definition 12.1, fix a point of $O_i$ and a buffered wave parent $W_i$ of its executed display. Apply the common-neighborhood construction at the beginning of §11.4 to the chart identification. The resulting $V\subset\iota_i(O_i)$ is globally hyperbolic and causally convex in $M$, with causally convex preimage in $W_i$.

On this common parent, Corollary 4.6 and Paper 3, Definition 6.9 and Theorem 6.10, identify the restriction of $[\Lambda_M]$ with the display's canonical class. The independent enrichment tests of Definition 6.23 of that paper impose the same kernel tests on the retained wave parent, including the case of a displaced scalar carrier ([Isthmus 2026c](#ref-IsthmusSmooth2026)). Choose a level of a smooth Cauchy time function on $V$ through the compared central point, giving a whole spacelike Cauchy surface $\Sigma_V$. Choose a retained disk $D$ around the preimage of the compared central point in the inverse image of $\Sigma_V$ under $\iota_i$. Choose a smaller point core $B$ about this point so that every selected null direction at a point of $B$ meets $D$ in its interior with a positive buffer. This follows from transversality at the central hit and compactness of the full projective sky, as in Paper 3, Definition 6.12. Write $\Sigma_i$ for the original scalar carrier of the display. It may be displaced from $B$ and need not lie in the domain of $\iota_i$.

In native carrier coordinates the scalar comparison is

$$
F_{i,B}
=T^M_{\Sigma_M,\Sigma_V}\,
  C_{\iota_i}^{D}\,
  T^i_{D,\Sigma_i}.
$$ {#eq:ordinary-atlas-local-completion-lift}

Here the first factor is the inverse relative carrier comparison for $V\subset M$, restricted to the conic directions over $\iota_i(D)$; the middle factor is actual half-density pushforward on that disk; and the last factor is the display's own local carrier comparison. All products are first formed with retained conic cutoffs. No value of $\iota_i$ on the displaced original carrier is required. The relative comparison theorem and Paper 3, Theorem 6.14, give an invertible graph-class map on the tested ray domain. Their evaluation identities give

$$
F_{i,B}e_i(p)=e_M(\iota_i(p)),\qquad p\in B.
$$ {#eq:ordinary-atlas-local-evaluation}

The factors are independent of the evaluated point, so the chain rule gives both point-connection identities on every algebra and module section. They preserve the full homogeneous covector map, internal adjoint, native half-density roots, phase transitions and central-specialization diagrams. On the finite-rank part, the soldering comparison and actual spin map identify the two canonical models. Their selected states are compared using the actual contact and affine normalizations of §3 and §8; no new initial value is inserted. These are the tensorial and initialized comparisons of Paper 3, Propositions 7.4–7.5, and §6.3 above. The auxiliary disk $D$ serves only as a scalar carrier. The executed display retains its original maximal Cartan data.

The comparison also retains the display's raw stored cells. In a local stored ray chart $\alpha$ of the $i$-display, write its normalization records as $n^i_\alpha,v^i_\alpha,u^i_{\alpha\beta}$. The maps into the native global presentation have vertices and edge units

$$
\begin{aligned}
k^i_\alpha&=\operatorname{Ad}(F_{i,B})n^i_\alpha,\\
\Xi^i_\alpha&=F_{i,B}v^i_\alpha,\\
a^i_{\alpha\beta}&=F_{i,B}u^i_{\alpha\beta}F_{i,B}^{-1}.
\end{aligned}
$$ {#eq:ordinary-atlas-local-stored-completion}

Substitution in the normalization edge equations gives the algebra and module comparison equations. The normalization triple identity gives

$$
a^i_{\alpha\beta}a^i_{\beta\gamma}
=k^i_\alpha(C^i_{\alpha\beta\gamma})
  a^i_{\alpha\gamma}.
$$ {#eq:ordinary-atlas-local-stored-triple}

The target here is native, with identity associator. The displayed equation retains the input associator on its tested local domain. For two stored completions the target associator also enters, as in Theorem 7.7.

Different intermediate disks and different common causal parents yield the same local full comparison. The carrier cocycles give this directly in native coordinates. For each use of pointed local uniqueness, re-mark the same executed displays at the currently compared spacetime point and its image. This changes neither their whole ordinary pairs, physical scales, initialized Cartan readouts nor actual spin bundles. One can compose either comparison with the inverse of the other: the resulting map is an automorphism of that admitted local display $E P_i$ over identity point and actual spin maps. Paper 3, Theorem 7.11, makes it the identity on a smaller common core.

On a refined overlap, $\eta_j^{-1}\eta_i A_{ij}$ is likewise an automorphism of $E P_j$ over the identity point and principal spin maps. The same theorem makes it the identity, proving $\eta_i A_{ij}=\eta_j$ including the normalized stored cells. Uniqueness on smaller cores glues these local maps as the sheaf of comparisons used in §11. Thus $(N M,b,\eta)$ is an admitted completion.

For two admitted completions, the actual physical-spin isometry $b_1^{-1}b_0:RS_0\to RS_1$ has one and only one full source lift $A$ by Theorem 7.7. On a common local refinement, $(\eta_i^1)^{-1}A\eta_i^0$ is an automorphism of $E P_i$ over identity point and actual spin maps. The local full Hom uniqueness just used makes it the identity. Hence $A\eta_i^0=\eta_i^1$ on every such refinement, and $A$ is the unique completion arrow. This proves the assertion about the completion groupoid.

Finally, the geometric identification sends both supplied scalar classes to globally admitted classes for the same metric on $M$. Theorem 4.4 identifies them modulo $C^\infty(M^2)$. Compare Example 4.7. ∎

<div id="prop:ordinary-atlas-completion-full-hom"></div>

**Proposition 12.3 (Completion of the supplied full atlas comparisons).**

Choose one admitted completion $\mathcal C\mathfrak A$ for each admitted atlas, with its marking $b_{\mathfrak A}$. Every full atlas arrow $a:\mathfrak A\to\mathfrak B$ has a unique full source embedding

$$
\mathcal C a:\mathcal C\mathfrak A\longrightarrow\mathcal C\mathfrak B
$$

whose local restrictions coincide with the supplied atlas arrow through the completion comparisons. These assignments form a fully faithful functor

$$
\mathcal C:
\mathsf{PairAtl}^{\infty,\mathrm{cc}}_{\mathrm{GH},0}
\longrightarrow
\mathsf{FullSrc}^{\infty,\mathrm{cc}}_{\mathrm{GH},0}.
$$ {#eq:ordinary-atlas-completion-functor}

It preserves and reflects Cauchy arrows and isomorphisms. A different choice of completions gives a unique compatible natural isomorphism.

*Proof.* The atlas arrow consists of compatible actual local full comparisons. Their point and principal spin maps descend by §11 to the causal physical-spin open embedding $Q a$. Theorem 9.4 gives the unique full source lift with

$$
R(\mathcal C a)
=b_{\mathfrak B}^{-1}(Q a)b_{\mathfrak A}.
$$ {#eq:ordinary-atlas-completed-arrow-readout}

It remains to verify that this constructed arrow realizes the supplied local data. On a common point refinement, compose an input chart's completion map with $\mathcal C a$, and compare this composite with the supplied atlas arrow followed by the output chart's completion map. The two actual point and spin maps agree by the displayed formula. Compose with the inverse output comparison, so that both resulting maps have the already executed input and output displays as endpoints. Paper 3, Theorem 7.11, makes these full local maps equal. This proves compatibility with the supplied local arrows, including their stored comparison cells.

Conversely, let $A:\mathcal C\mathfrak A\to\mathcal C\mathfrak B$ be a full source embedding. Its actual point and spin maps transport through the two $b$ maps to a causal embedding between the atlas bases. Refine the source chart cores so that each image is contained in a target chart. On a further common causal refinement, compose the source completion comparison, the restriction of $A$, and the inverse target completion comparison. These are actual full local source maps between the two executed displays. The completion overlap equations and the coherence of restriction in Proposition 9.2 make them agree on overlaps with the atlas transition maps. Hence they define an atlas arrow $a$. Its completed arrow equals $A$ by Theorem 9.4. If two atlas arrows have the same completion, their local maps agree after these same invertible comparisons, so the arrows are equal in the atlas refinement category. This proves full faithfulness directly on the supplied comparison maps.

Identity and composition follow either by this local construction or by applying the faithful recognition functor to the displayed arrow formula. The image property defining a Cauchy arrow, and surjectivity of the point embedding defining an isomorphism, are preserved by the marking isometries. Theorem 12.2 supplies the unique comparison between two chosen completions over each atlas. The two paths in its naturality square agree locally with the same supplied atlas arrow and therefore agree globally by Theorem 9.4. ∎

<div id="thm:ordinary-atlas-full-source-equivalence"></div>

**Theorem 12.4 (Ordinary-pair atlases and global full sources).**

Assume the ordinary-pair coverage theorem of Paper 3, Theorem 5.7, with its stated execution, physical-scale and actual-spin conclusions. Then the functor in Proposition 12.3 is an equivalence. In particular there are equivalences

$$
\mathsf{PairAtl}^{\infty,\mathrm{cc}}_{\mathrm{GH},0}
\simeq
\mathsf{FullSrc}^{\infty,\mathrm{cc}}_{\mathrm{GH},0}
\simeq
\mathsf{Vac}^{\infty,\mathrm{cc}}_{\mathrm{GH},0}.
$$ {#eq:ordinary-atlas-global-correspondence}

The atlas inverse uses local ordinary pairs with their own whole exterior inputs and physical scales. The inverse comparisons preserve the actual point and affine domains, spin maps, both Weyl chiralities, finite-rank fields, full evaluation, point connections, native roots and stored associators.

*Proof.* Proposition 12.3 gives full faithfulness. Let $S$ be a global normalized full source. Apply the coverage construction of Theorem 11.7 to its recognized spacetime $RS$. It gives an admitted ordinary-pair atlas $\mathcal L S$ and an actual physical-spin isometry

$$
d_S:Q\mathcal L S\longrightarrow RS.
$$ {#eq:ordinary-atlas-inverse-geometry}

This is the step that uses Paper 3, Theorem 5.7, and the protected extension result used in its proof. The local full comparisons are constructed by Paper 3, Theorem 7.11, and satisfy the atlas overlap equations by its uniqueness. Theorem 7.7 now lifts $d_S b_{\mathcal L S}$ to a unique full isomorphism

$$
\varepsilon_S:\mathcal C\mathcal L S\longrightarrow S.
$$ {#eq:ordinary-atlas-inverse-counit}

Composing the atlas comparisons into $\mathcal C\mathcal L S$ with $\varepsilon_S$ supplies compatible full local comparisons into $S$ over the maps $d_S\iota_i$. Thus $S$, marked over $Q\mathcal L S$ by $d_S^{-1}$, is an admitted completion of this atlas. Theorem 12.2 identifies $\varepsilon_S$ with its unique completion comparison. Consequently atlas completion recovers the independently supplied global source in its complete comparison category, including its original stored records. This proves essential surjectivity.

For completeness, the inverse can be made functorial with actual local arrows. For a source embedding $A:S\to S'$, use the local completion comparisons and $A$ on common causal refinements to construct the atlas maps from $\mathcal L S$ to $\mathcal L S'$ as in the converse direction of Proposition 12.3. Their recognized map is

$$
Q(\mathcal L A)=d_{S'}^{-1}(RA)d_S.
$$

Their identity and composition laws follow from the corresponding actual maps and full local uniqueness. The counit $\varepsilon$ is natural by Theorem 9.4. Define the unit $\zeta_{\mathfrak A}:\mathfrak A\to\mathcal L\mathcal C\mathfrak A$ by the local full lift of

$$
Q\zeta_{\mathfrak A}
=d_{\mathcal C\mathfrak A}^{-1}b_{\mathfrak A}^{-1}.
$$ {#eq:ordinary-atlas-inverse-unit}

Existence and uniqueness of this atlas arrow is the full atlas Hom theorem, Theorem 11.5. Its maps are the local comparisons already constructed between the two presentations of the same physical-spin source. The actual point and spin maps in

$$
\varepsilon_{\mathcal C\mathfrak A}\,
  \mathcal C(\zeta_{\mathfrak A})=I_{\mathcal C\mathfrak A},
\qquad
\mathcal L(\varepsilon_S)\,\zeta_{\mathcal L S}=I_{\mathcal L S}
$$ {#eq:ordinary-atlas-inverse-triangles}

cancel using the displayed formulas for $b,d$ and the arrow readouts. Faithfulness of $R$ and of $Q$, respectively, proves both triangle identities. All maps used in the cancellation are the full maps, so their actual principal spin labels and stored normalization cells are retained. The second equivalence in the statement is Theorem 9.4. ∎

<div id="cor:ordinary-atlas-maximal-development"></div>

**Corollary 12.5 (Maximal developments in ordinary-pair atlases).**

Under the coverage hypothesis of Theorem 12.4, let $\mathsf{Dev}_{\mathrm{atl}}(\mathfrak d)$ be the category of admitted ordinary-pair atlases whose recognized spacetime is supplied with the initial point and actual spin markings of Definition 10.1. Its arrows are the full atlas embeddings preserving those markings. Then completion induces an equivalence

$$
\mathsf{Dev}_{\mathrm{atl}}(\mathfrak d)
\simeq
\mathsf{Dev}_{\mathrm{src}}(\mathfrak d).
$$ {#eq:ordinary-atlas-marked-development-equivalence}

In particular this atlas category has a terminal object presenting the maximal globally hyperbolic source development of Theorem 10.4. Every other marked atlas development has one and only one full atlas embedding into it, and its completed embedding is the universal source embedding of that theorem.

*Proof.* Transport the initial point and principal spin maps through the marking $b_{\mathfrak A}$ of each completion. The full Hom bijection of Proposition 12.3 restricts to arrows satisfying both marking equations of Definition 10.1. The atlas construction of Theorem 12.4 supplies a representing atlas for every marked global source, and its counit transports the same markings. This proves the stated equivalence. The terminal source object of Theorem 10.4 therefore has a terminal atlas representative. Full faithfulness makes its universal arrow unique, including its actual initial spin lift. ∎

<div id="sec:common-cauchy-wave-families"></div>

## 13. Wave families on a common Cauchy manifold

Consider a smooth finite-dimensional family of metrics on one spacetime manifold with one hypersurface that is spacelike and Cauchy for every metric. The global estimates needed for this extension are local on compact sets of parameters and endpoints. A compact set of endpoints has a common compact Cauchy shadow, even when the common Cauchy hypersurface is noncompact. We first prove this support statement and then construct the scalar family by double Cauchy evolution of a uniformly classical family of complete initial kernels.

::: {.paper-block-heading}
**Common causal control.**
:::

<div id="def:common-cauchy-metric-family"></div>

**Definition 13.1 (A smooth family with a common Cauchy hypersurface).**

Let $B$ be a finite-dimensional parameter manifold, $M$ a fixed smooth connected four-manifold, and $\Sigma\subset M$ a fixed smooth embedded hypersurface. A common-Cauchy metric family is a jointly smooth family $g_\lambda$, $\lambda\in B$, of time-oriented Lorentzian metrics of signature $(+---)$ such that every $(M,g_\lambda)$ is globally hyperbolic and $\Sigma$ is spacelike and Cauchy for every member. The future coorientation of $\Sigma$ varies continuously, and hence is fixed on each connected parameter neighborhood. No compactness or completeness of the induced spatial metrics is assumed. The scalar results below do not require $\operatorname{Ric}(g_\lambda)=0$.

Fix smooth positive background densities to identify the distribution spaces while differentiating in $\lambda$. Physical volume densities and the field and future-normal half-density traces are then smooth coefficient factors in these identifications. The wave operator is $P_\lambda=\Box_{g_\lambda}$. Write $\gamma_{0,\lambda},\gamma_{1,\lambda}$ for the physical traces on the common $\Sigma$.

Every estimate is on compact parameter sets $L\Subset\operatorname{int}L'\Subset B$ and compact spacetime, spatial and angular sets with larger buffered parents. The family and those parents are fixed before the requested derivative or homogeneous coefficient orders. A constant may depend on finitely many stronger coefficient seminorms and on positive coordinate, hyperbolicity, noncharacteristic and phase-inverse margins. No uniform constant over all of a noncompact spacetime is required.

<div id="lem:family-compact-cauchy-parents"></div>

**Lemma 13.2 (Common compact Cauchy shadows and strips).**

Let $g_\lambda$ satisfy Definition 13.1. For compact $L\subset B$ and compact $K\subset M$, the union over $\lambda\in L$ of

$$
\begin{aligned}
&J^+_{g_\lambda}(K)\cap\Sigma,
\qquad J^-_{g_\lambda}(K)\cap\Sigma,\\
&J^+_{g_\lambda}(K)\cap J^-_{g_\lambda}(\Sigma),
\qquad J^-_{g_\lambda}(K)\cap J^+_{g_\lambda}(\Sigma)
\end{aligned}
$$ {#eq:family-common-causal-strips}

is contained in one compact subset of $M$. The compact parent can be enlarged to a compact neighborhood with a positive buffer. Near each parameter value, a smooth time function for the base metric with zero surface $\Sigma$ remains temporal for the nearby metrics on this enlarged parent. Moreover, near every $(\lambda_0,p)$ there is a fixed open point neighborhood $D$ that is causally convex and globally hyperbolic for every sufficiently nearby $g_\lambda$, with a fixed spacelike Cauchy disk. These choices do not depend on a subsequent differentiation order.

*Proof.* First fix $\lambda_0$. Choose an auxiliary Riemannian norm on $TM$. The set of $g_{\lambda_0}$-causal vectors of auxiliary norm one based at $K$ is compact. Include both time orientations and both timelike and null vectors, with the null boundary included. The maximal geodesic with any such initial vector meets $\Sigma$ exactly once. It is inextendible as an unparametrized causal curve: the endpoint argument in Theorem 3.2 applies to every nonzero causal tangent, using the compact closed ball of causal directions normalized by a local temporal differential. A causal endpoint in $M$ would give a finite nonzero limiting affine tangent and an extension of the geodesic. The Cauchy property therefore gives a hit at a finite affine parameter.

Every hit is transverse because $\Sigma$ is spacelike. Smooth dependence for the geodesic ordinary differential equation and the implicit function theorem give a smooth hit time on a neighborhood of each initial vector and of $\lambda_0$. This neighborhood can include vectors that are not causal for the base metric; transversality is an open condition. Shrink it with compact closure so that the entire segment from its initial point to its continued hit is defined on a compact flow domain. Finitely many such neighborhoods cover the compact normalized causal initial set. For all sufficiently nearby $\lambda$, every normalized $g_\lambda$-causal vector over $K$ lies in their union. Otherwise a convergent sequence of normalized vectors would limit to a $g_{\lambda_0}$-causal vector outside that union. The segment images from the finitely many compact flow domains lie in one compact subset of $M$.

These geodesic segments also control arbitrary causal strips. For example, if $z\in J^-_{g_\lambda}(K)\cap J^+_{g_\lambda}(\Sigma)$ and $z\ne p\in K$ with $z\le_{g_\lambda}p$, global hyperbolicity gives a maximizing causal geodesic from $z$ to $p$. We use the Avez–Seifert statement in Minguzzi, Theorem 4.123 ([Minguzzi 2019](#ref-Minguzzi2019)). Reverse this segment from $p$ and normalize its initial tangent in the auxiliary norm. Its continuation meets $\Sigma$ after it has passed $z$: a hit before $z$ would put $z$ on the past side of a Cauchy hypersurface, contrary to $z\in J^+(\Sigma)$. Equivalently, the two components of $M\setminus\Sigma$ are its chronological future and past, and a causal curve crosses $\Sigma$ only once. Thus $z$ lies on one of the controlled initial-to-hit segments. The case $z=p$ is included by adding $K$. Reversing time proves the other strip assertion, and their endpoints contain both Cauchy shadows.

A finite cover of the compact parameter set $L$ by the neighborhoods just obtained gives one compact union. Enlarge it slightly inside $M$ to obtain the stated buffer. Bär–Ginoux–Pfäffle, Theorem 1.3.13, supplies a Cauchy temporal function $t_0$ for $g_{\lambda_0}$ with $\Sigma=t_0^{-1}(0)$ ([Bär, Ginoux and Pfäffle 2007](#ref-BarGinouxPfaeffle2007)). Its differential is uniformly timelike on the enlarged compact parent. Joint smoothness preserves that positive margin for nearby $\lambda$. The function need not be temporal for those metrics outside this parent.

For the final local assertion, start with a compact neighborhood $K$ of $p$. Every causal curve between two points of $K$ lies in the union of the two strips just bounded: split it at its possible unique crossing of $\Sigma$. It is therefore contained in one common compact set $C$. On that set, after a parameter restriction there is $c>0$ such that $\mathrm dt_0(v)\ge c|v|_{\mathrm{aux}}$ for every future causal tangent. Its auxiliary length is at most $c^{-1}$ times the difference of the endpoint $t_0$ values. Choose a coordinate neighborhood $V$ of $p$, and then a smaller endpoint neighborhood $N\Subset V\cap\operatorname{int}K$ whose oscillation in $t_0$ is less than $c$ times its auxiliary distance to the complement of $V$. Every ambient causal curve with endpoints in $N$ consequently remains in $V$.

After reducing $V$ and the parameter neighborhood, choose one constant Lorentz cone in its coordinates strictly wider than all the $g_\lambda$ future cones. A sufficiently small double cone $D$ for this constant metric has closure in $N$. An ambient $g_\lambda$-causal curve between two points of $D$ first stays in $V$, by the preceding length estimate, and is then causal for the constant wider cone. Convexity of that cone's double cone forces it to stay in $D$. Thus $D$ is causally convex in every nearby spacetime. It is globally hyperbolic because the ambient spacetime is globally hyperbolic and its causal diamonds between points of $D$ remain in $D$.

Take the constant cone coordinates so that $D=\{|s|+|x|/a<\delta\}$ and the wider causal speed is $a$. Its middle disk $s=0$ is spacelike for all the narrower metrics. A future causal curve in the part $s<0$ has $|\mathrm dx/\mathrm ds|\le a$ and cannot reach the expanding side boundary before the middle disk: the positive gap $a(\delta+s)-|x|$ cannot decrease to zero. It has an interior limit at $s=0$ if it has not already extended there. The reverse argument applies in $s>0$. Hence every inextendible causal curve in $D$ meets the middle disk once. This supplies the common Cauchy disk. ∎

::: {.paper-block-heading}
**Evolution with parameters.**
:::

<div id="lem:family-smooth-cauchy-evolution"></div>

**Lemma 13.3 (Smooth Cauchy evolution with metric parameters).**

Suppose the Cauchy data $f_{0,\lambda},f_{1,\lambda}$ on $\Sigma$ and the forcing $F_\lambda$ on $M$ are jointly smooth, without support assumptions. Their unique smooth solutions of

$$
P_\lambda u_\lambda=F_\lambda,
\qquad
\gamma_{j,\lambda}u_\lambda=f_{j,\lambda}
\quad(j=0,1)
$$ {#eq:family-inhomogeneous-cauchy-problem}

are jointly smooth on $B\times M$. For every compact $L\Subset\operatorname{int}L'$ and compact output set $K$, each finite mixed output seminorm is bounded by finitely many input and metric seminorms on common compact parents, and the inverses of their retained positive margins. The statement also holds with further smooth passive variables.

*Proof.* For each fixed parameter, existence and uniqueness are Lemma 2.5. Fix a parameter $\lambda_0$ and enlarge the compact output set $K$ slightly. Lemma 13.2 gives a compact set $C$ containing the causal strips of this enlargement to $\Sigma$ for the parameters in a fixed compact neighborhood of $\lambda_0$. Choose compactly supported smooth cutoffs of the initial data and forcing that agree with them on neighborhoods of the corresponding shadows and strips. Choose $\chi\in C_c^\infty(M)$ with $0\le\chi\le1$, equal to one on a neighborhood of $C$ and of these cutoff supports. These choices are made before any derivative order is prescribed.

Put $g_0=g_{\lambda_0}$. Let $t_0$ be a smooth Cauchy temporal function for $g_0$ with $\Sigma=t_0^{-1}(0)$, as in Lemma 13.2. Cauchy temporal stability gives a smooth Lorentzian metric $\bar g$ whose future cones strictly contain those of $g_0$ and for which $t_0$ is still Cauchy temporal ([Minguzzi 2019](#ref-Minguzzi2019), Theorem 4.122). Define

$$
\widetilde g_\lambda
=g_0+\chi(g_\lambda-g_0).
$$ {#eq:family-auxiliary-metric}

On the compact support of $\chi$, Lorentzian signature and strict containment of the future cones in those of $\bar g$ persist for all sufficiently nearby $\lambda$. Outside this set $\widetilde g_\lambda=g_0$, so both properties hold globally. The differential $\mathrm dt_0$ is temporal for every auxiliary metric. An inextendible auxiliary causal curve has no endpoint in $M$ and is also $\bar g$-causal; the Cauchy property for $\bar g$ therefore makes its $t_0$ range all of $\mathbb R$. Thus every $S_t=t_0^{-1}(t)$ is a whole Cauchy surface for every $\widetilde g_\lambda$.

Let $\widetilde u_\lambda$ solve the auxiliary wave equation with the cutoff data and forcing, using their physical traces for $\widetilde g_\lambda$. On the region where the data cutoffs are supported, the auxiliary and original metrics agree. For each fixed $\lambda$, the difference between the original solution and $\widetilde u_\lambda$ has zero initial data on the relevant shadow and zero $P_\lambda$ forcing near the entire original strip. Finite propagation therefore identifies the two solutions on a fixed neighborhood of $K$. This argument uses the original strips; no containment of the wider metric's strips in $\operatorname{supp}\chi$ is required.

Choose $T>0$ so that the output set and the supports of the cutoff data and forcing lie in $t_0^{-1}((-T,T))$. Let $S$ be their compact union. Finite propagation for the auxiliary equations and cone inclusion put all their solution supports, on this slab, in

$$
Q=\bigl(J^+_{\bar g}(S)\cap t_0^{-1}([0,T])\bigr)
\cup\bigl(J^-_{\bar g}(S)\cap t_0^{-1}([-T,0])\bigr).
$$ {#eq:family-common-propagation-set}

This set is compact: apply Lemma 2.1 for $\bar g$ with the two Cauchy surfaces $S_{-T}$ and $S_T$, separating future and past propagation. Its future part is closed under further future propagation within the slab, and its past part has the corresponding past property. Thus the differentiated forcing used below has the same support control at every order. Enlarge $Q$ to a compact neighborhood for coefficient estimates. Integrate the wave energy over the entire slices $S_t$. The solutions are supported in $Q$, so integration by parts has no spatial boundary term. A fixed product trivialization of the Cauchy temporal foliation and a finite coordinate cover of $Q$ give, for every integer $s\ge0$,

$$
\mathcal E_s(\widetilde u;t)
\le C_s\left(
\mathcal E_s(\widetilde u;t_*)
+\int_{\min(t,t_*)}^{\max(t,t_*)}
\|\widetilde P_\lambda\widetilde u(r)\|_{H^s(S_r)}\,\mathrm dr
\right),
$$ {#eq:family-local-energy-estimate}

for either time direction, where $\widetilde P_\lambda=\Box_{\widetilde g_\lambda}$. On these compact supports, $\mathcal E_s$ is uniformly equivalent to the field's $H^{s+1}$ norm plus the $H^s$ norm of its coordinate-time derivative. The scalar energy identity, commutation with spatial derivatives and Gronwall's inequality give the estimate. Coordinate partitions contribute lower-order commutators that are included in the same estimate. Its constants use finitely many coefficient derivatives and inverse hyperbolicity margins on the fixed compact set. Increasing $s$ does not alter the slices, supports or cutoffs. This is the linear energy calculation of Paper 3, Lemma 2.13, now applied on full slices with common compact support ([Isthmus 2026c](#ref-IsthmusSmooth2026)).

Apply this estimate first to the difference of two auxiliary solutions. It gives continuity in every finite lower Sobolev norm once the required stronger spatial norms are retained. A first parameter difference quotient has a candidate limit solving

$$
\widetilde P_\lambda v_a
=\partial_{\lambda^a}\widetilde F_\lambda
-(\partial_{\lambda^a}\widetilde P_\lambda)
\widetilde u_\lambda,
$$

with differentiated initial data. Convert the physical traces to field and coordinate-time data before taking these differences; the conversion coefficients are smooth in $\lambda$ and uniformly nondegenerate on the initial support. Subtracting the candidate equation from the quotient equation makes its forcing and initial errors tend to zero in each required finite norm. The same energy estimate proves convergence of the quotient to $v_a$.

At higher parameter orders the differentiated auxiliary equation has the same triangular form, with operators of order at most two acting on lower parameter derivatives. At each fixed order only finitely many stronger spatial norms are required. The quotient argument and induction therefore give actual parameter derivatives at every order, on the same support set $Q$. Time derivatives are recovered from the equation, whose coordinate-time leading coefficient has a uniform positive lower bound on $Q$. Sobolev embedding yields joint smoothness and mixed $C^m$ estimates for $\widetilde u$.

Equality with the original solutions near $K$ now proves their joint smoothness there. In the original variables their differentiated equation is

$$
P_\lambda\partial_\lambda^\beta u_\lambda
=\partial_\lambda^\beta F_\lambda
 -\sum_{0<\alpha\le\beta}
  {\beta\choose\alpha}
  (\partial_\lambda^\alpha P_\lambda)
  \partial_\lambda^{\beta-\alpha}u_\lambda.
$$ {#eq:family-parameter-differentiated-wave}

Every finite auxiliary coefficient seminorm uses finitely many seminorms of the original metric family and $g_0$ on the chosen compact parents, together with the fixed cutoff derivatives. The energy estimates consequently give the asserted finite dependence for the original solution. Additional passive variables are included as parameters that do not change the wave operator. Finally, a finite cover of $L$ by these parameter neighborhoods gives the statement on the prescribed compact parameter set. ∎

<div id="lem:family-cauchy-kernels"></div>

**Lemma 13.4 (Cauchy kernels, test transposes and double evolution).**

Let $\mathcal U_\lambda=(\mathcal U_{0,\lambda},\mathcal U_{1,\lambda})$ denote exact Cauchy evolution from the physical half-density traces on $\Sigma$. Its kernels form a smooth distribution-valued family. On every common compact parent they have uniform classical Fourier integral representatives on the two null branches, modulo a remainder smooth jointly in the parameter and both kernel variables. Both spatial endpoint covectors of each branch are nonzero. Their parameter covectors are those of the varying phases and need not vanish.

Let $\phi_\lambda$ be a jointly smooth family of spacetime tests whose supports lie in a common compact subset of $M$ on each compact parameter set. Then the transpose $\mathcal U_\lambda^t\phi_\lambda$ is jointly smooth and supported, on each compact parameter set, in one compact subset of $\Sigma$. This map has finite seminorm bounds on those compact sets. Consequently a smooth distribution-valued initial matrix $A_\lambda$ has an exact double evolution

$$
\mathcal E_\lambda(A_\lambda)
=\sum_{i,j=0}^1
 (\mathcal U_{i,\lambda}\otimes\mathcal U_{j,\lambda})
 (A_\lambda)_{ij}.
$$ {#eq:family-double-cauchy-evolution}

It is a smooth distribution-valued family with that double Cauchy matrix. Double evolution takes a jointly smooth initial matrix to a jointly smooth spacetime kernel. No support or growth condition on that smooth matrix is required.

*Proof.* Lemma 13.3 gives smooth dependence of the exact solution on a fixed compactly supported smooth initial test and finite seminorm bounds for its parameter derivatives. The parameter version of the Schwartz kernel theorem, or its proof by testing on finite sums of tensor-product functions and using those bounds, gives a smooth distribution-valued kernel family on $M\times\Sigma$.

We give the uniform microlocal refinement. In a short cylinder over the initial hypersurface use the normal coordinates of the varying metric, obtained by a smooth geodesic flow with a fixed inverse margin. Paper 3, Theorem 6.6, constructs the selected normal operator $Q_+$ with physical principal symbol $iH$ and its field parametrix $E_+$. Its scalar construction applies to a smooth Lorentzian collar without the Einstein equation, as specified in that paper's §6.4. Since the scalar wave coefficients are real, physical kernel conjugation gives the opposite operators $Q_-=\overline{Q_+}$ and $E_-=\overline{E_+}$, with principal normal symbol $-iH$. The opposite full operator is not defined by the formula $Q_-=-Q_+$.

The two initialized field-normal columns form the matrix

$$
\begin{pmatrix}I&I\\-Q_+&-Q_-\end{pmatrix}.
$$

Its weighted principal determinant is $2iH$, so it has an inverse in the uniform complete matrix calculus. Composing the two field parametrices with this inverse produces the two columns of a full Cauchy parametrix, initialized by the identity modulo joint smoothing. The eikonal equations and initialized transport equations have coefficients smooth in the parameter. On compact unit-frequency patches, ordinary differential equations and the implicit function theorem give their phases on one common smaller time interval. The leading amplitude is initialized and nonzero. Every next amplitude solves a linear transport equation with forcing from finitely many earlier amplitudes and coefficient derivatives. Parameter-dependent asymptotic summation gives actual uniform classical kernels with jointly smoothing equation and initial errors. This uses the proof of Paper 3, Proposition 6.11, and its finite-calculus Lemma 6.4: their phase, transport and summation steps use smooth coefficients and the retained margins, which are supplied here by Lemma 13.2 and the local Gaussian flow. The source-collar hypothesis of that proposition is thus replaced here by these explicitly verified scalar hypotheses ([Isthmus 2026c](#ref-IsthmusSmooth2026)).

The difference between this parametrix and exact evolution is jointly smooth on the retained local Cauchy domain. Construct the correction there from its smooth kernel-valued forcing and initial errors using the localized energy construction of Lemma 13.3, retaining the initial-coordinate variable as passive. Every coordinate cutoff is one on the required domain of dependence. Its commutator may be singular outside that domain, but does not enter this correction or its retained output; it is not treated as a globally smooth forcing. At each fixed parameter, local distributional Cauchy uniqueness from Lemma 2.2 identifies the correction with the difference of the two kernels on the smaller domain. Testing on initial and spacetime variables verifies equality of the smooth distribution-valued families. This proves joint smoothness of the local remainder rather than inferring it from separate smoothness at each parameter.

For a compact output set, use the auxiliary common-Cauchy family of Lemma 13.3 on a parameter neighborhood. It agrees with $g_\lambda$ on a neighborhood of the original common causal strips and is dominated by one fixed globally hyperbolic metric $\bar g$ with Cauchy temporal function $t_0$. Multiply the initial variable by a compactly supported cutoff equal to one near the initial shadows of a slightly larger output set. Domain of dependence identifies the resulting exact kernels with the original kernels near the retained outputs. On a finite $t_0$ interval, the supports of all these compact-data solutions are contained in one compact $\bar g$-causal propagation set. Every whole level $\Sigma_t=t_0^{-1}(t)$ is a Cauchy hypersurface for the auxiliary family.

Subdivide the interval into finitely many short slabs, constructing each local parametrix on a slightly larger time interval. On each initial level, cover the relevant compact initial support by finitely many smaller coordinate disks inside larger disks and choose a partition of unity. Choose the time step so that the entire $\bar g$-causal propagation of each smaller support during that slab lies inside its larger coordinate cylinder. Construct the full two-branch Cauchy parametrix there, using the invertible field-normal matrix above. Multiply its output by a cutoff equal to one near that entire causal propagation and supported inside the cylinder. The cutoff commutator is jointly smoothing: the known canonical relations of the constructed short parametrix, with its initial partition factor, do not meet the derivative support of that cutoff. Its equation and initial errors are therefore jointly smooth on the whole short-slab product. Summing the finite partition gives the full short Cauchy parametrix for the retained compact initial support.

Extend these smooth error kernels from the larger time interval using a temporal cutoff equal to one on the retained closed slab. Apply Lemma 13.3 to the auxiliary family with that slab's initial whole slice as Cauchy surface and the initial kernel coordinate passive. Exact Cauchy uniqueness identifies this jointly smooth correction with the short exact-minus-parametrix difference. At each intermediate whole level insert a spatial cutoff equal to one near the common compact support of the propagated exact data. The exact Cauchy evolution factors through these whole levels, and replacing every short exact factor by its full parametrix plus the jointly smooth correction produces a finite product. Every term containing a correction is jointly smooth: all spatial supports in the compositions are compact, both spatial endpoint covectors of the short phase kernels are nonzero, and integration by parts retains that conclusion after every finite parameter derivative. The same construction with a variable last time gives the spacetime–initial kernel, rather than only its traces at the subdivision times.

The remaining finite product is decomposed conically, retaining both the field and normal rows of each Cauchy matrix. To identify its relations, let $Q_{k,+,\lambda}$ and $Q_{k,-,\lambda}$ be the complete normal operators in Gaussian collars of an intermediate whole slice. The Riccati factorization makes the two traces of an incoming branch equal, modulo joint smoothing, to the column $(I,-Q_{k,\pm,\lambda})^{\mathrm T}$ applied to its field kernel. With

$$
\mathsf B_{k,\lambda}
=\begin{pmatrix}I&I\\-Q_{k,+,\lambda}&-Q_{k,-,\lambda}\end{pmatrix},
\qquad
\mathsf B_{k,\lambda}^{-1}
 \begin{pmatrix}I\\-Q_{k,\pm,\lambda}\end{pmatrix}
=\iota_\pm,
\qquad
\iota_+=\begin{pmatrix}I\\0\end{pmatrix},\quad
\iota_-=\begin{pmatrix}0\\I\end{pmatrix},
$$ {#eq:family-intermediate-branch-splitting}

the full normal splitting annihilates the other component to every order. These are identities of smooth coefficient families, so the uniform classical remainder estimates remove all sign-switching terms jointly. The surviving compositions continue one of the two spacetime characteristic branches through every intermediate level. They therefore give the two full null-flow relations, with no additional broken-path relations. Uniform graph composition supplies their classical phase descriptions, and the compactly supported smoothing terms already treated give a jointly smooth remainder on the entire retained product. Caustics and multiple rays between base points require several conic phase charts; all their cotangent contributions are included. The auxiliary parent, spatial partitions, subdivision and cutoffs are fixed before the coefficient and derivative orders. A finite cover of the compact parameter set completes the construction.

Pair a local oscillatory kernel with a smooth compact spacetime test. Its nonzero spacetime covector makes the phase nonstationary in that test variable. Integration by parts gives arbitrary inverse powers of the frequency, uniformly on each compact parameter and initial-coordinate set. Any specified parameter derivative costs finitely many frequency powers, which are absorbed by further integrations. The paired kernel is consequently jointly smooth in the initial and parameter variables. Its exact support lies in $J_{g_\lambda}(\operatorname{supp}\phi_\lambda)\cap\Sigma$ by finite propagation. On a compact parameter set, apply Lemma 13.2 to the common compact spacetime support of the tests. This gives one compact initial support for all their transposes. The localized oscillatory estimates, together with the joint smooth remainder estimates, give the stated continuity in test-function seminorms.

To define the double evolution, apply the two transpose Cauchy operators to a spacetime test kernel. Their common compact support and smoothness put the result in the test-function space of $\Sigma\times\Sigma$, with smooth parameter dependence and finite seminorm bounds. Pair it with $A_\lambda$. This defines the displayed smooth distribution-valued family. The exact equations and the four trace identities hold for each parameter and hence as family identities. If the initial matrix is jointly smooth, Lemma 13.3 first evolves one variable with the other spatial variable passive, then the second variable with the first spacetime variable passive. Its common compact support control localizes each output product before either step. The resulting function is jointly smooth in all variables. ∎

A related formula is available under stronger support hypotheses. For metric variations supported in a fixed compact set between two Cauchy surfaces of a spatially compact spacetime, Strohmaier identifies the parameter covector of the Cauchy evolution kernel by integrating the metric variation along each null geodesic ([Strohmaier 2026](#ref-Strohmaier2026), §3.1).

::: {.paper-block-heading}
**The joint Cauchy and wave classes.**
:::

<div id="prop:family-global-cauchy-class"></div>

**Proposition 13.5 (A uniform global complete Cauchy class).**

There is a canonical family of complete Cauchy matrix classes on $\Sigma$, with orders

$$
\begin{pmatrix}-1&0\\0&1\end{pmatrix},
$$

and a jointly classical Hermitian representative $A_\lambda$ whose kernel support is proper in both spatial factors, uniformly on compact parameter sets. Its local complete class is the physical matrix of Paper 3, Theorem 6.10. Every two such constructions differ by a matrix smooth on all of $B\times\Sigma\times\Sigma$. Each prescribed finite list of homogeneous coefficients and its mixed derivatives is bounded by finitely many metric and coordinate seminorms on fixed larger compact parents and their positive margins.

*Proof.* Around a point of $B\times\Sigma$, choose fixed spatial coordinates on the common initial surface and the Gaussian normal coordinates of the metric family on a common short collar. Smooth geodesic dependence and a positive inverse margin give these coordinates on a retained parent. In those coordinates the Riccati and charge recursions of Paper 3, Theorem 6.6 and Proposition 6.7, produce smooth classical coefficient families $Q_\lambda,R_\lambda$ and the complete matrix

$$
A^{\mathrm{can}}_\lambda
=J_\lambda R_\lambda^{-1}J_\lambda^{\dagger},
\qquad J_\lambda=\begin{pmatrix}I\\-Q_\lambda\end{pmatrix}.
$$ {#eq:family-local-cauchy-factorization}

At each homogeneous degree the new coefficient is obtained by finitely many differentiations and division by the positive nonzero leading symbol. The Gaussian coordinate changes and the physical trace factors have finite differentiated ordinary differential equation bounds. Thus every finite coefficient list has the asserted finite dependence. The uniform symbol summation and finite-calculus statements are Paper 3, Lemma 6.4 and Proposition 6.11 ([Isthmus 2026c](#ref-IsthmusSmooth2026)). The common causal parents in Lemma 13.2 permit the local joint-kernel uniqueness argument on overlaps, or one may use the coordinate covariance of these complete Cauchy recursions. It identifies the local classes modulo joint smoothing, not merely pointwise smoothing.

Use a locally finite smooth partition on $B\times\Sigma$ subordinate to the resulting coordinate parents and apply the construction of Lemma 4.2 with these parameter-dependent coefficients. All spatial cutoffs can be multiplied by one fixed smooth cutoff equal to one near the diagonal and supported in a closed relation proper over both factors of $\Sigma\times\Sigma$. Such a relation can be chosen using bounded distance in a complete auxiliary Riemannian metric. Locally finite quantization then gives a global kernel family with that common support property. Near every diagonal point its full symbol is the canonical symbol, because the local class differences are jointly smoothing and the partition sums to one. Away from the diagonal every term is jointly smooth, and local finiteness preserves this property. The two conclusions show that any two resulting matrix families differ by a globally jointly smooth matrix. Hermitian symmetrization preserves the support and complete class.

The recursive formulas bound any fixed finite coefficient list and its derivatives in terms of finitely many input seminorms. The cutoff sequence realizing the entire symbol can depend on all its coefficients, so this bound concerns the complete class. ∎

<div id="thm:family-global-canonical-wave"></div>

**Theorem 13.6 (Canonical wave class modulo joint smoothing).**

For a common-Cauchy family there is a unique class

$$
[\Lambda]\in
\mathcal D'(B\times M\times M)\big/
C^\infty(B\times M\times M)
$$ {#eq:family-global-wave-class}

with the following admission properties. It has uniform classical oscillatory representatives on retained compact phase charts, its wave equations and commutator hold modulo jointly smooth kernels, and its joint wavefront set satisfies

$$
\operatorname{WF}(\Lambda)\subset
\left\{(\lambda,p,q;\sigma,\xi,-\eta):
(p,\xi;q,\eta)\in\mathcal C_{g_\lambda}^+\right\}.
$$ {#eq:family-global-joint-positive-relation}

Both spacetime endpoint covectors in this condition are nonzero. The parameter covector $\sigma$ is allowed to be nonzero; pure parameter singularities are excluded. The kernel equations are

$$
P_{\lambda,p}\Lambda,\ P_{\lambda,q}\Lambda
\in C^\infty(B\times M^2),
\qquad
\Lambda-\Lambda^T+iE_\lambda
\in C^\infty(B\times M^2),
$$ {#eq:family-global-wave-admission}

where $E_\lambda$ is the physical retarded-minus-advanced scalar kernel of the fiber metric. It is itself a smooth distribution-valued family. A representative of the admitted class is

$$
\Lambda_\lambda=\mathcal E_\lambda(A_\lambda),
$$ {#eq:family-global-wave-construction}

with $A_\lambda$ from Proposition 13.5. This representative is an exact Hermitian bisolution and depends smoothly on $\lambda$ as a distribution. The class is independent of the coordinate parents, partitions, symbol realizations and common Cauchy presentation used in its construction.

For the four-trace characterization, take a family $K_\lambda$ in the parameter-dependent oscillatory calculus used in Lemma 13.4, with the following local requirements. On retained compact phase charts its representatives, modulo a kernel smooth jointly in $(\lambda,p,q)$, are finite sums of oscillatory integrals with smoothly parameterized nondegenerate homogeneous phases and classical amplitudes. Smooth dependence of an amplitude is measured in the local classical symbol topology: the differentiated homogeneous coefficients and the remainder after each finite truncation satisfy their symbol estimates uniformly on compact parameter and coordinate sets, after every prescribed finite number of parameter derivatives. Differentiating the phase incurs the corresponding finite order loss. On the critical sets, the two spacetime endpoint covectors are nonzero and null for $g_\lambda$; no frequency sign or common bicharacteristic is prescribed for the two endpoints. Require both $P_{\lambda,p}K$ and $P_{\lambda,q}K$ to be smooth jointly in the parameters and endpoints. Then $K_\lambda$ has the admitted joint class if and only if its four traces on the entire common $\Sigma\times\Sigma$ have the canonical family class of Proposition 13.5 modulo joint smoothing.

The joint wavefront condition gives well-defined parameter fibers and smooth dependence into distributions: after multiplying by a compact point test and pushing forward the point variables, a nonsmooth parameter covector would require a joint wavefront covector with both spacetime components zero. Thus the family formulation and joint-distribution formulation agree for these admitted kernels. It is natural under supplied smooth families of physical isometric open embeddings with causally convex image between common-Cauchy families. Naturality is an equality modulo kernels smooth jointly in the parameters and both point variables.

*Proof.* Lemma 13.4 defines the double evolution on the whole product and makes it a smooth distribution-valued family. It has zero wave residuals and the initial matrix $A_\lambda$. Hermitian symmetry follows from the Hermitian initial matrix and real scalar Cauchy evolution. The physical volume and trace-density factors depend smoothly on the parameter and are retained in this statement.

First identify the commutator family without making a parameter-dependent choice of states. Its universal double Cauchy matrix is

$$
J_{\mathrm{KG}}=
\begin{pmatrix}0&-I\\I&0\end{pmatrix}.
$$

For each fixed metric, the causal propagator has this matrix and is an exact bisolution, by the Green normalization used in §4 and Paper 3, Lemma 6.8. Distributional Cauchy uniqueness therefore identifies

$$
E_\lambda=\mathcal E_\lambda(J_{\mathrm{KG}}).
$$ {#eq:family-causal-kernel-construction}

The right-hand side is a smooth distribution-valued family by Lemma 13.4. This proves the asserted family regularity of the actual causal kernels. In the initial matrix calculus, the local charge identities give

$$
A_\lambda-A_\lambda^{\mathrm T}+iJ_{\mathrm{KG}}
\in C^\infty(B\times\Sigma^2),
$$

where matrix transposition also exchanges its two spatial variables. The identity holds jointly near the diagonal by the uniform local construction and off the diagonal by the joint smoothness of the Cauchy kernels there. Double evolution of this matrix is jointly smooth by Lemma 13.4. This gives the global commutator equation.

We next prove the joint frequency condition on the entire spacetime product. Fix compact parameter and endpoint sets. Lemma 13.2 supplies the common original causal strips and initial shadows, and Lemmas 13.3–13.4 compare the exact evolutions with finite compositions of full two-branch short Cauchy parametrices on whole common Cauchy levels. Their remainder is smooth jointly on the entire retained products. The auxiliary and original metrics and physical traces agree on a neighborhood of the retained initial shadows. Their complete normal-root recursions therefore agree there; the inserted initial cutoffs are one on a larger neighborhood, so their commutators with those roots are smoothing on the retained initial conic sets. In the initial factorization of Proposition 13.5, the column $J_\lambda$ initializes only the selected spacetime branch. At each short step the two field-normal columns have separated elliptic normal roots. Expressing the incoming selected solution in this full Cauchy splitting gives zero opposite-branch coefficient at every homogeneous order. Equivalently, its opposite symbol solves the homogeneous transport recursion with zero initial values, as in Lemma 5.2. These equalities hold for the smooth coefficient families on the retained parameter neighborhood. Uniform classical asymptotic estimates therefore make the opposite remainder jointly smoothing. This branch argument is applied before an endpoint trace can make two projected carrier graphs intersect. The full-product remainder statement of Lemma 13.4 ensures that no additional wavefront points lie outside the composed relations.

For the paired kernel, stationary matching at the common initial carrier requires the same point and the same tangential covector in the two factors, since the intervening initial complete operator has the diagonal canonical relation. The selected lifts therefore give two nonzero spacetime covectors on one selected null bicharacteristic. On a retained phase patch their frequency is comparable to each nonzero endpoint covector. Parameter derivatives of the phases are homogeneous of degree one with bounded coefficients on the compact unit-frequency charts, so

$$
|\sigma|\le C(|\xi|+|\eta|)
$$ {#eq:family-parameter-frequency-control}

there, with a constant for that retained chart. In particular these phases produce no pure parameter covector.

The unmatched terms are jointly smoothing. Insert conic cutoffs on the initial and intermediate carriers before composition. On compact supports away from the matching equations, a rescaled phase gradient has a fixed nonzero lower bound. For comparable dyadic frequencies, integration by parts gives arbitrary inverse powers of their scale. For noncomparable neighboring frequencies, differentiation in their common spatial variable separates the two covectors, and one integrates first at the largest unmatched scale. Every prescribed endpoint or parameter derivative costs finitely many powers of frequency. More integrations absorb that loss, after which the dyadic sums converge with the required derivatives. These are the uniform composition and remainder arguments of Paper 3, Lemma 6.4 and the retained mixed-kernel construction following Proposition 6.11 ([Isthmus 2026c](#ref-IsthmusSmooth2026)). The finite compact cover proves the condition at all endpoint pairs, including pairs outside every single original local wave parent. Jointly smooth corrections from the exact Cauchy construction do not alter it.

For uniqueness, subtract two admitted joint kernels and call the difference $D$. The commutator equation makes $D-D^T$ jointly smooth. Hence $D$ and $D^T$ have the same joint wavefront set. The first lies in the selected relation displayed above; transposition carries that relation into the opposite spacetime frequency component. Both endpoint covectors are nonzero, so the two sets are disjoint regardless of the parameter covector. Thus $D$ is jointly smooth. This argument would not exclude a pure parameter singularity if the nonzero-spacetime-covector condition were omitted.

For the Cauchy characterization, the uniform characteristic phase calculus permits successive physical field and normal traces on the fixed spacelike $\Sigma$. A nonzero null endpoint covector cannot be its timelike conormal, and its tangential restriction is nonzero. Restricting the smooth phase families therefore gives smooth distribution-valued families of the one-sided and double traces, with uniform classical remainders. Suppose first that the four traces of $K_\lambda$ have the canonical family class, and subtract the constructed $\Lambda_\lambda$. The difference $D_\lambda$ has jointly smooth residuals $F_p=P_{\lambda,p}D_\lambda$ and $F_q=P_{\lambda,q}D_\lambda$, and jointly smooth four-trace matrix. Put $d_i=(\gamma_{i,\lambda}\otimes I)D_\lambda$. Its second-variable forcing is $(\gamma_{i,\lambda}\otimes I)F_q$, which is jointly smooth, and its two second-variable Cauchy data are the given smooth double traces.

Apply Lemma 13.3 with the first spatial variable passive to construct a jointly smooth kernel $w_i(\lambda,x,q)$ with those forcing and data. For each fixed $\lambda$, the fixed-metric distributional Cauchy uniqueness of Lemma 2.6, with $x$ passive, gives $d_{i,\lambda}=w_{i,\lambda}$. Both sides are smooth distribution-valued parameter families, so the equality holds jointly. Next use Lemma 13.3 in the first spacetime variable, with $q$ passive, to construct a jointly smooth $w(\lambda,p,q)$ from forcing $F_p$ and first-variable Cauchy data $w_0,w_1$. Fixed-parameter uniqueness again identifies $D_\lambda=w_\lambda$. Thus $D$ is jointly smooth, proving the forward implication. Conversely, an admitted family differs jointly smoothly from the constructed one by the preceding uniqueness proof, and taking its four traces gives the canonical family class. At no step is the parameter-dependent wave operator commuted through an integration in its metric parameter.

A different construction on the same Cauchy surface has initial difference jointly smooth by Proposition 13.5, and hence final difference jointly smooth by Lemma 13.4. A construction using another common Cauchy presentation satisfies the same global admission properties, so uniqueness identifies its class modulo joint smoothing with the one constructed above.

Finally, a supplied smooth family of causal isometric embeddings gives an open embedding of the total point manifolds over the parameter base. Pullback of the joint distribution is therefore defined. The differential may mix a parameter covector with the derivatives of the point embedding, which is permitted by the joint wavefront condition; its spacetime covectors remain the nonzero selected null covectors. Causal convexity identifies the intrinsic null relations and the physical causal kernels in each fiber. The latter identity holds as a smooth distribution-valued family by the causal-kernel construction above. Pullback consequently satisfies all the joint admission tests, and uniqueness proves naturality. ∎

::: {.paper-block-heading}
**Estimates at finite orders.**
:::

<div id="prop:family-wave-finite-estimates"></div>

**Proposition 13.7 (Finite coefficients on fixed common parents).**

Fix compact parameter and endpoint sets, a finite retained coordinate and phase cover of their null relations, and the common compact causal and initial parents of Lemma 13.2. These domains can be chosen before the homogeneous depth $J$, coordinate and angular derivative order $m$, and parameter derivative order $q$. For a prescribed finite list $\mathcal Y$ of canonical Cauchy coefficients, phase functions and wave-transport amplitude coefficients, there are a finite input order $N$ and a finite locally bounded function $F_{J,m,q}$ such that

$$
\|\mathcal Y\|_{J,m,q;L}
\le F_{J,m,q}\left(
\mathcal N_N(g;L'\times\text{larger parents}),
\mathfrak m^{-1}\right).
$$ {#eq:family-global-wave-finite-estimates}

The margins $\mathfrak m$ include the selected coordinate, hyperbolicity, spacelike, inverse, phase and domain-buffer margins. Fixed auxiliary partitions and coordinate maps are included among the chosen parent data. Increasing the requested orders changes the finite norms and bound, not the selected spacetime or parameter neighborhood.

*Proof.* On a retained Gaussian parent the complete Cauchy coefficients are finite recursive expressions from Proposition 13.5. Their prescribed derivatives therefore have finite bounds from the metric family and its inverse margins. The normalized null flows and transverse hits solve smooth ordinary differential equations on the compact segment domains of Lemma 13.2. Each finite variation obeys a linear variational equation with forcing from finitely many lower variations and metric derivatives. Gronwall's inequality and the retained transverse inverse give the finite phase bounds.

At each homogeneous depth the amplitude solves a linear transport equation along these same fixed rays. Its forcing uses finitely many previous coefficients and finite derivatives; differentiating the equation in the parameter and coordinate variables preserves this finite triangular structure. The finite sequence of short propagators uses finite-depth stationary phase and composition formulas, so each output coefficient still involves only finitely many input coefficients and derivatives. The coordinate and angular covers are already finite and buffered. Combining these bounds proves the estimate.

Parameter differentiation of an actual oscillatory kernel may raise its distributional order: differentiating $e^{i\phi_\lambda}a_\lambda$ contributes $i(\partial_\lambda\phi_\lambda)a_\lambda$, which has one higher frequency order. Thus the theorem estimates smooth phase and complete amplitude coefficients, with the finite derivative losses in the energy argument retained. It does not assert smooth dependence as bounded operators on one unchanging Sobolev space without those losses. Actual uniform asymptotic realizations exist by the parameter symbol calculus, but their noncanonical smoothing tails are outside this finite-coefficient estimate. ∎

<div id="ex:weak-smooth-kernel-family"></div>

**Example 13.8 (Fiberwise smooth remainders need not be jointly smooth).**

On fixed Minkowski space put $u=t-x^1$. For $s\in(-1,1)$ define

$$
D_s(p,q)=
\begin{cases}
\cos\bigl((u(p)-u(q))/s\bigr),&s>0,\\
0,&s\le0.
\end{cases}
$$ {#eq:family-fiberwise-smooth-counterexample}

This is a smooth distribution-valued family, flat at $s=0$ in that topology. Every fiber is a smooth symmetric exact bisolution. It is not a jointly smooth kernel in $(s,p,q)$. Therefore adding it to a constant canonical wave family preserves every fiber's kernel class and admission tests, and preserves smooth dependence into distributions, but does not preserve the joint class of Theorem 13.6.

*Verification.* Both endpoint gradients of $u$ are null and constant, so the two wave equations vanish. The cosine makes the kernel symmetric. For a compactly supported test in $(p,q)$, the phase $u(p)-u(q)$ is a submersion with a fixed nonzero derivative. Repeated integration by parts makes its pairing $O(s^N)$ for every $N$, uniformly on bounded sets of tests with fixed compact support. Every finite $s$ derivative introduces only finitely many negative powers of $s$ and polynomial phase factors. Further integrations give the same arbitrary decay, proving smooth distribution-valued dependence and flatness at zero. On the spacetime diagonal, however, $D_s(p,p)=1$ for $s>0$, whereas it is zero for $s\le0$. The joint distribution cannot have a smooth representative: in the open region $s>0$ that representative would equal the displayed smooth function, which has incompatible limits along nearby paths to $(0,p,p)$. Thus joint admission, rather than merely fiberwise admission and weak smoothness, is essential. ∎

<div id="sec:parameter-family-correspondence"></div>

## 14. Families of full comparisons and ordinary-pair atlases

We apply the joint scalar construction to Ricci-flat physical-spin families satisfying [Definition 13.1](#def:common-cauchy-metric-family) on a fixed smooth spacetime manifold, with a common smooth spacelike Cauchy hypersurface. The parameter base $B$ is a finite-dimensional smooth manifold; estimates are stated in its coordinate neighborhoods. An actual family of principal spin bundles means a smooth principal bundle over $B\times M$ covering the oriented and time-oriented vertical orthonormal frame bundle. A supplied comparison family includes a smooth actual principal map over its smooth point map. Pointwise existence of isometries between two families does not supply such a comparison family.

All parameter assertions are local on compact parameter, point and homogeneous direction sets. The global kernel is admitted in the joint quotient of §13. The finite estimates below concern its complete coefficient data and the corresponding full source comparisons; they do not bound an arbitrarily chosen exact smoothing remainder.

::: {.paper-block-heading}
**Families on a fixed manifold.**
:::

<div id="def:common-parent-source-families"></div>

**Definition 14.1 (Smooth full source families and finite seminorms).**

A smooth full source family over $B$ consists of full sources $S_\lambda$ of Definition 7.1 on a common smooth point manifold $M$, with the following joint data. The Cartan fields, physical density, actual principal spin bundle, finite-rank bundles, tensor fields and initial normalization maps are smooth on their parameterized domains. Their recognized metrics form a family admitted in §13, with a common Cauchy presentation $\Sigma$. The scalar kernel satisfies that section's joint admission conditions on $B\times M^2$. In fixed carrier coordinates the complete algebra coefficients, the phase functions and amplitude coefficients of the moving whole-sky modules, and all stored normalization maps and their inverses are smooth families in the complete calculus. Remainders in the point and kernel formulas are jointly smooth in the parameter, point and carrier variables on the stated domains.

The normalization, adjoint, evaluation, connection, root and stored-cell equations hold as joint complete-family identities. In particular, equality of scalar kernel representatives is taken modulo $C^\infty(B\times M^2)$, rather than by separately discarding a possibly nonsmooth family of fiberwise smoothing terms. Upper orders of general algebra and module sections are locally bounded on the retained parameter and conic charts.

Fix compact parameter sets $L\subset\operatorname{int}L'\subset B$, compact observation sets in the point and carrier variables, and finitely many compact unit-covector charts. A *retained parent* is a fixed larger coordinate and ray-tube neighborhood, with these compact sets in its interior, on which the relevant metrics, carrier maps, comparison maps and inverses are defined. Its positive margins include Lorentz nondegeneracy, spacelikeness, transverse intersections, phase inverses, nonzero principal roots, chart inverses and point or ray-domain buffers. The compact causal control and common causal cores of [Lemma 13.2](#lem:family-compact-cauchy-parents), together with Proposition 14.2 below, select these parents before any prescribed coefficient depth or derivative order.

For a finite list $\mathcal Y_J$ of coefficients through homogeneous depth $J$, write $\|\mathcal Y_J\|_{m,q}$ for the indicated coefficient seminorms through point and angular order $m$ and parameter order $q$, measured on these compact sets in the chosen smooth phase charts. The phases and their derivatives are included whenever the list involves a graph or a moving module. The general finite estimate has the form

$$
\|\mathcal Y_J\|_{m,q}
\le
F_{J,m,q}\bigl(
\mathcal N_N(\text{input fields and markings};L'\times\text{larger parents}),
\mathfrak m^{-1}\bigr),
$$ {#eq:family-full-comparison-estimate}

where $N$ is finite, $F_{J,m,q}$ is finite and locally bounded, and $\mathfrak m$ is the finite list of retained positive margins. Constants can depend on the fixed finite cover and compact sets. For stored comparisons the input list includes the supplied normalization maps and inverse maps; for a supplied physical comparison it includes that comparison, its inverse on the image and its actual spin map. Whole ordinary inputs, when present, are measured in the finite weighted seminorms of Paper 3, Proposition 5.8. Increasing $J,m,q$ may change $N$ and $F_{J,m,q}$, but not the selected parents, ordinary extension branch or geometric trajectories.

These are coefficient seminorms in smooth phase presentations. Differentiating an oscillatory representative in a moving external parameter can introduce additional powers of its frequency. No assertion that such differentiation preserves its fixed operator order is implicit in this notation.

<div id="prop:family-geometric-ray-comparisons"></div>

**Proposition 14.2 (Geometry and actual transport on common parents).**

For a Ricci-flat physical-spin family satisfying Definition 13.1, the null incidence, homogeneous ray maps between retained spacelike carriers, contact multipliers, affine changes of origin and finite-rank canonical diagrams are smooth families on every retained compact interior domain. The initialized comparison of Lemma 6.5 is a smooth family when its initial map and source fields are supplied smoothly. All these fields, their stipulated inverses and their finite variations satisfy estimates of the form in Definition 14.1, without an index $J$ for a finite-rank field.

The parents are chosen before the derivative orders. The assertion concerns interior ray segments and realized domains; it does not assert smooth dependence of omitted affine endpoints or a common domain for an entire family of maximal developments.

*Proof.* Fix a compact set of points and normalized null directions at a chosen parameter value. The common Cauchy property gives the transverse carrier hits used in §3 and §8. Lemma 13.2 and a finite cover of these hits give compact ray tubes and buffers, as well as common causally convex local parents when needed. The null Hamilton equations are finite smooth ordinary differential equations whose coefficients use the metric and its first derivatives. On a compact unit-direction section, positive spacelike and time-orientation margins keep the normalizations and transverse derivatives away from zero. Continuous dependence and the implicit function theorem therefore preserve the selected hits, their uniqueness on the retained domains and their positive margins after one parameter restriction. This restriction depends on low-order bounds and the domain buffers, not on later derivative orders.

Repeated differentiation of the Hamilton equations gives linear variational equations with forcing involving finitely many lower variations and finite metric jets. Their integral equations and Gronwall estimates give every prescribed mixed point and parameter bound on the same tubes. Differentiate the transverse-hit identity to obtain the corresponding inverse-function bounds, dividing by its retained nonzero derivative. The contact multipliers and affine origin changes are the actual formulas of Proposition 3.4; their variations use only these hit maps, finite metric jets and positive normalization factors. Compactness gives a finite angular cover even if one phase projection develops a caustic. The argument uses the nondegenerate phase chart on each member of that cover, not a globally regular sky projection. A compact parameter set is covered by finitely many of the selected parameter neighborhoods; their finite lists of buffered parents are fixed before the higher orders are specified.

The soldering, Levi-Civita connection and curvature are finite differential expressions in the admitted geometric fields. Their canonical tensor and spin constructions consequently have the stated regularity. Principal spin parallel transport is lifted from the actual frame transport with its specified initial map. In local principal charts its equation is a finite smooth system; its variations obey the same type of linear estimates. The initial central sign is preserved by path lifting and is not a scalar normalization freedom.

For an independently initialized finite-rank comparison, the formula of Lemma 6.5 is

$$
J_\lambda(z,s)
=P^{\mathrm s}_{\lambda,s,0}
 J_{0,\lambda}(z)
 \bigl(P^{\mathrm{can}}_{\lambda,s,0}\bigr)^{-1}.
$$ {#eq:family-initialized-finite-rank-comparison}

On each of the selected compact ray segments the transports and their inverses satisfy the preceding finite ODE estimates. The initial tangential and mixed-curvature tests imply the full connection identity fiberwise by Lemma 6.5. Both sides are now jointly smooth, so this is also a joint identity and may be differentiated in the parameters. Point-bundle descent uses the same constancy on each connected sky fiber. Compositions and inverses have their joint identities by initialized uniqueness. ∎

<div id="thm:family-relative-carrier-comparison"></div>

**Theorem 14.3 (Relative carriers in a varying metric family).**

Let $U_\lambda\subset M$ be a smooth family of causally convex globally hyperbolic open subspacetimes, presented by smooth embeddings $f_\lambda:N\to M$ from a fixed manifold $N$ with image $U_\lambda$, and suppose the ambient and pulled-back Ricci-flat metrics satisfy Definition 13.1. Choose common Cauchy presentations in these manifolds. On every compact interior subset of the parameterized relative ray domain, the relative comparisons of Theorem 8.3 form smooth complete graph families. They preserve all the structures in that theorem, including the full evaluation, internal adjoint, native roots, and both point connections on every section. Their inverse, nested restriction and change-of-carrier identities hold in the joint quotient.

Every stipulated finite list of their phase, amplitude and complete coefficient data has the estimate of Definition 14.1. The same assertion holds for any finite number $k$ of iterated point derivatives of the evaluation and comparison formulas, with $k$ included in the finite indices and the evaluation's filtration origin taken at degree $1+k$ before external parameter differentiation.

*Proof.* The parameterized embedding $(\lambda,x)\mapsto(\lambda,f_\lambda(x))$ has an invertible differential and is injective, hence identifies the source product with an open subset of the ambient product. The relative ray domain is open there: a retained ray has a hit in the image interior, and its hit and the image chart persist under small changes in the parameters. Proposition 14.2 gives the smooth homogeneous graph and its retained inverse charts.

Pullback and causal restriction carry the jointly admitted scalar class to the intrinsic class on the source family. To justify the joint assertion, pull back the wave equations and the causal commutator identity. The causal Green restriction is valid in every fiber, and the parameterized evolution of §13 supplies the joint kernel identities. On the compact phase charts, the derivatives of the supplied diffeomorphisms are bounded, and the nonzero endpoint covectors control any new parameter covectors contributed by pullback. Thus the joint wavefront admission is retained. Joint kernel uniqueness in [Theorem 13.6](#thm:family-global-canonical-wave) gives equality modulo jointly smooth kernels; fiberwise uniqueness alone would not give this conclusion.

The mixed traces have the uniform noncharacteristic margins of Proposition 14.2. In the following carrier subscripts $U$ denotes the image $U_\lambda=f_\lambda(N)$ at the indicated parameter. The positive-principal roots and normalized mixed traces give the formula of §8,

$$
T_{U,M,\lambda}
=W_{U,\lambda}C_{U,M,\lambda}W_{M,\lambda},
$$ {#eq:family-relative-carrier-formula}

now in smooth phase and coefficient families. On each retained compact graph choose inner and outer conic sets and proper cutoffs that work on one parameter neighborhood. Insert these cutoffs before composing. The local cancellation proof of Lemma 8.2 gives the inverse identities with jointly smoothing errors: the finite-depth composition has smooth coefficients, while the separated graph terms are jointly smoothing by the parameter-dependent phase and joint-smoothing argument of §13. All products are taken in the retained interiors. No global properness across the boundary of the relative ray domain is asserted.

The phase equations, transverse hit maps and leading amplitudes have the estimates of [Proposition 13.7](#prop:family-wave-finite-estimates) and Proposition 14.2. At depth $J$, the inverse and positive square-root recursions divide by the retained nonzero leading terms and use finitely many preceding coefficients and derivatives. The amplitude transport recursion is linear on the already selected trajectories. Differentiating a finite number of its equations in points and parameters gives finite Gronwall bounds. Finite-depth stationary phase uses finitely many additional jets and the fixed inverse-phase margins. These are the operations estimated in Paper 3, Propositions 6.11 and 6.17, now applied to the finite compact ray-tube cover ([Isthmus 2026c](#ref-IsthmusSmooth2026)). They give the stated estimate and do not change its geometric parents when the output orders increase.

The local carrier-factorization proof of Theorem 8.3 preserves the internal adjoint and native half-density and root diagrams with the same smooth short-carrier generators. Its point-column factorization gives the full evaluation identity in the joint quotient. Every compact parameter and point set has its entire sky covered by finitely many of these retained charts. Uniform classical symbol-family estimates on them show that the graph action preserves the whole module families and their jointly smooth remainders. The fixed-background graph at each $\lambda$ is independent of the evaluated point, so it commutes with the actual point connection on every section. Its dependence on $\lambda$ is permitted. The iterated point-derivative estimates are the coefficient rule of Paper 3, Proposition 6.22, on these same charts.

Finally, the localized cancellation giving Corollary 8.4 is an identity of these joint complete families. It proves nested restriction, inverse and carrier-change coherence. Formal coefficient identities hold at every parameter and every degree, and the smooth family calculus and joint kernel uniqueness identify their jointly smoothing remainders. ∎

<div id="thm:family-full-source-hom"></div>

**Theorem 14.4 (Full Hom and recognition for source families).**

Let $\mathsf{Vac}^{\infty,\mathrm{cc}}_{\mathrm{GH},0}(B)$ consist of the Ricci-flat physical-spin metric families satisfying Definition 13.1. Its arrows are supplied smooth parameter-preserving families of physical isometric open embeddings with causally convex images and actual principal spin lifts. Let $\mathsf{FullSrc}^{\infty,\mathrm{cc}}_{\mathrm{GH},0}(B)$ have the source families of Definition 14.1 and the joint versions of the full open comparisons of Definition 9.3. Then recognition and the native construction give an equivalence

$$
R_B:\mathsf{FullSrc}^{\infty,\mathrm{cc}}_{\mathrm{GH},0}(B)
\simeq
\mathsf{Vac}^{\infty,\mathrm{cc}}_{\mathrm{GH},0}(B).
$$ {#eq:family-full-source-equivalence}

Every supplied smooth physical-spin embedding family has a unique joint full lift. Its native vertices, stored vertices, overlap units, evaluations and all-section point comparisons satisfy the finite estimates of Definition 14.1 on retained compact sets. The equivalence commutes with parameter restriction and physical restriction on the admitted domains. Its natural unit and counit retain the full stored cells and both triangle identities.

*Proof.* Recognition is by the actual algebraic and differential readouts of §6, so it is smooth on the supplied families. Its image is Ricci-flat by Proposition 6.2 and satisfies the family geometric hypotheses by Definition 14.1. Conversely the scalar construction of §13, the geometric and finite-rank construction of Proposition 14.2, and identity native normalizations produce an admitted source family for every object on the right.

For a supplied embedding family $f_\lambda$, use Theorem 14.3 and actual physical half-density pushforward to form, on the relative image domain,

$$
F_{f,\lambda}
=T^{1,\lambda}_{\Sigma_1,f_\lambda(\Sigma_0)}C_{f_\lambda},
\qquad
J_{f,\lambda}=\operatorname{Ad}(F_{f,\lambda}).
$$ {#eq:family-native-embedding-comparison}

The maps and their inverses are smooth on every retained compact domain. For such a domain, source compact causal control bounds the segments to $\Sigma_0$, and the smooth image of those compact tubes is compact in the target family. Target compact causal control bounds the remaining segments to $\Sigma_1$. Thus the parents required by the relative comparison can be chosen before any output differentiation. This argument gives local finite control and uses no uniform bound over the entire noncompact spacetime.

The full stored formulas remain

$$
\begin{aligned}
k_{i,\lambda}
 &=(n_{i,\lambda}^1)^{-1}J_{f,\lambda}n_{i,\lambda}^0,\\
\Xi_{i,\lambda}
 &=(v_{i,\lambda}^1)^{-1}F_{f,\lambda}v_{i,\lambda}^0,\\
a_{ij,\lambda}
 &=(n_{i,\lambda}^1)^{-1}
 \left(J_{f,\lambda}(u_{ij,\lambda}^0)
       (u_{ij,\lambda}^1)^{-1}\right).
\end{aligned}
$$ {#eq:family-stored-full-comparison}

They are smooth coefficient families because their supplied normalizations and inverse maps are smooth and their products are taken on the common retained conic charts. The proofs of Theorems 7.7 and 9.4 apply to these formulas in the joint quotient: both raw associators occur, and all evaluations and connections are transported with the same normalized changes. The finite-rank maps are the actual smooth tensor and initialized spin comparisons of Proposition 14.2. Each operation at a fixed degree and derivative order has finite input order, giving the estimate.

For uniqueness, normalize two joint lifts on the restricted source Cauchy carrier and compare them there. The Euler recursion in Lemma 7.3 is smooth in the parameters at every finite depth and divides only by its nonzero integer weights and the retained symbol normalizations. The evaluation argument of Lemma 7.4 makes the residual local scalar and normalized inner unit identities on the entire retained incidence. Since their coefficients are jointly smooth, these are joint complete-family identities. The normalized center gives the same conclusion for the remaining presentation cells. Joint scalar kernel uniqueness is supplied by Theorem 13.6.

The Hom bijection follows. Identity, composition and restriction hold in the joint quotient by Theorem 14.3 and the same stored-cell equations as in Theorem 9.4. The units and counits are their unique joint lifts over the corresponding geometric and actual spin maps. Their naturality and triangle identities follow by faithfulness, as in Corollary 7.8. Choosing another common Cauchy presentation gives the smooth canonical whole-carrier comparison and hence the same equivalence up to that natural comparison. ∎

<div id="def:ordinary-pair-atlas-families"></div>

**Definition 14.5 (Ordinary-pair atlas families).**

A family of ordinary-pair atlases over $B$ is a parameter-preserving version of Definition 11.2 with the following additional data. For smooth supplied ordinary inputs, Paper 3, Theorem 4.18, gives the initial source family, Theorem 2.14 supplies its common local Cartan development, and Propositions 6.11, 6.17 and 6.22 give its local joint wave enrichment and finite estimates. These are the execution inputs for the fields used here. Its effective smooth quotient is supplied on $B\times M$. Each executed chart is defined over some open parameter set $B_i\subset B$, with a smooth family of whole ordinary pairs, scales, markings and actual executed fields on common local representatives. Each chart has its own retained parents and positive margins, chosen before the requested finite orders. The chart maps and actual overlap maps are smooth in the parameter, the principal spin cocycle is strict, and the complete overlap comparisons and normalized cells are joint complete-family identities.

The chart images form a countable locally finite cover of the total parameter-point manifold $B\times M$. The quotient and causal admission tests are imposed fiberwise, and the descended metric family must satisfy §13, including its supplied common Cauchy presentation. The whole input on chart $i$ is defined on $B_i$; it need not be extended to all of $B$. The parameter sets $B_i$ and the geometric widths may vary from chart to chart.

Arrows are smooth parameter-preserving versions of Definition 11.4, over supplied smooth physical embedding candidates, with locally represented full family comparisons on their actual common domains. Refinements restrict parameter domains and point cores and retain the same whole pair on each parent chart. Denote this category by $\mathsf{PairAtl}^{\infty,\mathrm{cc}}_{\mathrm{GH},0}(B)$. For estimates on a compact parameter-point set, local finiteness reduces the argument to finitely many chart parents; no common radius on a whole noncompact fiber is required.

<div id="thm:family-atlas-completion-correspondence"></div>

**Theorem 14.6 (Family atlas descent, completion and coverage).**

Let an atlas family satisfy Definition 14.5, including the requirement that its descended metric family admit the supplied common spacelike Cauchy hypersurface of Definition 13.1. Its charts descend to a smooth Ricci-flat physical-spin family with a joint full source completion. Between any two such completions there is a unique full family comparison preserving the atlas marking and local comparisons. Completion is fully faithful. These conclusions use execution, local family comparisons, §13, Proposition 14.2 and Theorems 14.3–14.4.

If Paper 3, Proposition 5.8 and Proposition 8.4, are also assumed, every object of $\mathsf{Vac}^{\infty,\mathrm{cc}}_{\mathrm{GH},0}(B)$ has an ordinary-pair atlas family. There are then equivalences

$$
\mathsf{PairAtl}^{\infty,\mathrm{cc}}_{\mathrm{GH},0}(B)
\simeq
\mathsf{FullSrc}^{\infty,\mathrm{cc}}_{\mathrm{GH},0}(B)
\simeq
\mathsf{Vac}^{\infty,\mathrm{cc}}_{\mathrm{GH},0}(B).
$$ {#eq:family-three-correspondences}

The comparisons, units and counits are smooth on their local parameter-point representatives and have every prescribed finite coefficient and derivative estimate on the same chosen compact parents.

*Proof.* For a supplied atlas family, the metric and principal spin gluing proof of Proposition 11.3 is parameter-preserving. All transition maps are jointly smooth, and the strict principal cocycle gives an actual smooth bundle over $B\times M$. The descended metric is Ricci-flat because the executed chart metrics are Ricci-flat and their transitions are physical isometries. The common Cauchy and geometric family conditions are explicit admission tests. The native construction of Theorem 14.4 therefore gives a full source family over this descended geometry.

Construct the local comparison from an executed chart exactly as in Theorem 12.2. Use the common causally convex cores of Lemma 13.2 and the uniform image and inverse margins to choose a causal refinement inside both actual comparison domains. Apply the successive source and target restrictions of §11.4 on these common cores. Choose a small auxiliary spacelike disk and its image there. Proposition 14.2 keeps their full-sky intersections, their inverse margins and all necessary ray segments on common parents near the chosen parameter. The full scalar comparison has the three factors in the proof of Theorem 12.2: a relative transport from the local image carrier to the global common Cauchy carrier, actual half-density pushforward on the auxiliary disk, and the executed chart's original carrier transport. The first factor has the family estimates of Theorem 14.3, the middle factor has ordinary finite pullback and positive-root estimates, and the last factor has Paper 3, Proposition 6.17, on its retained parent. Joint kernel uniqueness identifies the global and local classes on this common causal parent. The resulting maps preserve the full evaluation and all point directions of both connections, with the estimates of Paper 3, Proposition 6.22. The Cartan and finite-rank maps are the actual tensor and initialized spin comparisons.

Conjugate by the supplied smooth stored normalizations. The formulas of Theorem 12.2 retain the raw source associators, and their finite coefficient estimates follow from the preceding factors. On overlaps, compose two such local comparisons inversely to obtain a comparison between the two already executed charts. Paper 3, Theorem 7.11 and Proposition 7.12, identify it with the supplied family overlap comparison; the pointwise uniqueness acts on jointly smooth complete coefficients and hence gives the joint identity. The actual spin maps agree literally. Thus the comparisons satisfy the atlas compatibility, with their normalized cells and strict spin cocycle. Theorem 14.4 proves uniqueness of any two global completions, naturality on supplied atlas arrows, and full faithfulness.

For coverage, fix a point $(\lambda_0,p_0)$ in the total geometric family. Choose smooth local tangent-plane and spin markings near it. Paper 3, Propositions 5.8 and 8.4, provide a smooth selected ordinary-pair family, one positive radius and extension branch, and actual physical-spin identifications on one parameter neighborhood and buffered point parent. Their domain is chosen before any requested finite orders. This is a parameter-dependent selection theorem, not a consequence of making unrelated pointwise choices. Restrict its actual representatives to the common causally convex cores supplied by Lemma 13.2, using the common-neighborhood construction of §11.4 with uniform image and inverse margins. A fixed null-boundary diamond for one metric is not assumed to remain causally convex when the metric varies; the common cores use the wider-cone and trapping construction of Lemma 13.2.

These local family charts cover $B\times M$. Choose a countable locally finite refinement in the total manifold, with compact-closure shrinkings as in Proposition 11.6, and take smaller product representatives inside the original family charts. The selected whole pairs are restricted only in their parameter domains. On any compact parameter-point set only finitely many of these choices are used, so the common smaller neighborhoods and the finite list of buffered parents can be fixed before $J,m,q$. On noncompact fibers the charts retain their individual parameter neighborhoods; an infinite intersection of those neighborhoods is never taken.

The actual physical and spin identifications give smooth overlap maps. Their full local family lifts are Paper 3, Proposition 7.12, and their coherences follow from uniqueness in the same way as in Lemma 11.1. This supplies every datum of Definition 14.5. In particular the strict spin cocycle comes from actual compositions, and the effective quotient is the original $B\times M$.

Thus the family geometric recognition is essentially surjective. Its full faithfulness is the family argument just used: the input is a supplied smooth physical-spin map, its local full lifts exist on common parents, and uniqueness glues them. Combining with Theorem 14.4 proves the three equivalences. Choose the inverse atlas family through the local selections just constructed. Its identifications with a supplied independent full source are obtained by composing the completion comparisons with the unique full family lift of the geometric identification. Their naturality and both triangle identities follow from the family Hom bijections, as in Theorem 12.4. The finite estimates use only the local selection estimates, the actual geometric maps and inverses, and the complete comparison formulas on the already fixed finite parent cover. ∎

<div id="cor:family-controlled-compact-selections"></div>

**Corollary 14.7 (One finite selection near a compact observation set).**

Assume the ordinary family coverage inputs of Theorem 14.6, namely Paper 3, Propositions 5.8 and 8.4. Fix a parameter value and a compact point set in a physical-spin family of Theorem 14.4. After one parameter restriction there are finitely many selected ordinary display families, extension branches, positive radii and buffered parents covering that point set and carrying the inverse and completion comparisons. Every specified finite coefficient depth, point derivative order and parameter derivative order is estimated on these same selections. Raising those orders changes only the required finite input seminorms and the order-dependent estimate functions.

*Proof.* At the fixed parameter the local family charts constructed in Theorem 14.6 cover the compact set, so choose a finite subcover. Intersect their finitely many parameter neighborhoods and retain compactly contained parameter sets. Positive image and inverse margins preserve the cover on a smaller common neighborhood. The selected branches and radii in Paper 3, Proposition 5.8, and all geometric and carrier parents above were chosen before the output orders. The finitely many estimates combine by taking their maximum and their finite union of input seminorms. ∎

<div id="ex:family-affine-endpoint-jump"></div>

**Example 14.8 (A flat family with discontinuous affine endpoints).**

Choose a nonzero nonnegative smooth function $\chi$ of compact support on $\mathbb R$, and take $\lambda$ in a sufficiently small interval about zero. On $M=\mathbb R\times\mathbb R^3$ put

$$
a_\lambda(t)=
\begin{cases}
 e^{-t^2}+\chi(t-\lambda^{-2}),&\lambda\ne0,\\
 e^{-t^2},&\lambda=0,
\end{cases}
\qquad
g_\lambda=a_\lambda(t)^2\,\mathrm dt^2-|\mathrm dx|^2.
$$ {#eq:family-escaping-lapse-bump}

This is a jointly smooth flat globally hyperbolic family with the common spacelike Cauchy hypersurface $\Sigma=\{t=0\}$. Normalize a future null tangent at $\Sigma$ by $g_\lambda(K,n_\lambda)=1$. Its future affine endpoint, measured from that hypersurface, is

$$
b_\lambda=
\begin{cases}
 \sqrt\pi/2+\displaystyle\int_{\mathbb R}\chi(u)\,\mathrm du,
   &\lambda\ne0,\\
 \sqrt\pi/2,&\lambda=0.
\end{cases}
$$ {#eq:family-discontinuous-affine-endpoint}

Thus the endpoint function is discontinuous even in this Ricci-flat common-Cauchy family. The total realized flow domain is still open and the flow is smooth on it, as required by Proposition 14.2.

*Proof.* On any bounded $t$ interval the translated bump vanishes identically for all sufficiently small $|\lambda|$. Hence the displayed lapse is smooth jointly at every finite point with $\lambda=0$; elsewhere it is manifestly smooth and positive. Choose the parameter interval so that the bump vanishes at and below $t=0$. Then $a_\lambda(0)=1$ for all parameters. The coordinate

$$
T_\lambda(t)=\int_0^t a_\lambda(u)\,\mathrm du
$$

identifies each metric with a Minkowski slab, so it is flat and each constant-$t$ slice is Cauchy. In the normalized null direction, $T_\lambda$ is the affine parameter with zero at $\Sigma$. Taking its future endpoint gives the displayed formula. On every retained interior flow segment the smooth dependence statement is the ordinary differential equation argument of Proposition 14.2. ∎

<div id="rem:parameter-family-scope"></div>

**Remark 14.9 (Parameter derivatives and maximal developments).**

The connections in these statements are the point connections already defined on each source. External parameter differentiation is differentiation of the supplied family in chosen representatives. In particular

$$
\partial_\lambda(T_\lambda m_\lambda)
=(\partial_\lambda T_\lambda)m_\lambda
 +T_\lambda\partial_\lambda m_\lambda;
$$

the first term is generally present, and no canonical connection in parameter space has been introduced. A positive physical scale may depend smoothly on the parameter, with its derivatives and a positive lower bound included in the input estimates; it remains constant on each spacetime member.

The compact estimates apply inside the supplied common-Cauchy family. Applying Theorem 10.4 separately at each parameter gives neither a common domain for the entire maximal developments nor regularity of a moving singular boundary. Example 14.8 exhibits the endpoint issue within a smooth family.

<div id="sec:intrinsic-spacetime-families"></div>

### 14.1. Families on spacetime bundles

The local family constructions also apply when the point manifolds form a smooth bundle over the parameter space. Different parameter neighborhoods may use different Cauchy hypersurfaces and carrier presentations. We first specify this admission, then descend the joint wave class and the full comparison records. Compact Cauchy fibers make the local admission automatic.

<div id="def:locally-common-cauchy-bundles"></div>

**Definition 14.10 (Locally common-Cauchy spacetime bundles).**

Let $B$ be a finite-dimensional Hausdorff second-countable smooth manifold. A locally common-Cauchy spacetime bundle is a smooth locally trivial bundle $\pi:\mathfrak M\to B$ of connected four-manifolds without boundary, equipped with a smooth Lorentzian metric $g$ on the vertical tangent bundle $T_\pi\mathfrak M=\ker\mathrm d\pi$ and smooth vertical orientation and time orientation. Every fiber $(M_b,g_b)$ is globally hyperbolic. Require an open cover $\{U_i\}$ of $B$ and bundle trivializations

$$
\Phi_i:U_i\times M_i\longrightarrow\mathfrak M|_{U_i}
$$ {#eq:intrinsic-family-local-trivializations}

such that the pulled-back metric family has one fixed smooth spacelike Cauchy hypersurface $\Sigma_i\subset M_i$ throughout $U_i$. These are called adapted trivializations. The scalar conclusions require no Einstein equation.

A physical-spin vacuum bundle additionally has $\operatorname{Ric}(g_b)=0$ in every fiber, the specified physical metric scale, and an actual smooth principal $\operatorname{Spin}^+(1,3)$ bundle covering the oriented and time-oriented orthonormal frame bundle of $T_\pi\mathfrak M$. Denote its category by $\mathsf{VacBun}^{\infty,\mathrm{cc}}_{\mathrm{GH},0}(B)$. An arrow is a supplied smooth bundle map over $B$ whose fiber maps are physical isometric open embeddings with causally convex images, together with a smooth actual principal spin lift.

The adapted cover and its Cauchy hypersurfaces are presentation choices. On an overlap write $f_{ij,b}:M_j\to M_i$ for the point transition. It is an isometry between the two pulled-back metrics. Pulling back the actual vertical spin bundle gives smooth bundles over $U_i\times M_i$, exactly of the kind used in Definition 14.1. Their actual transition maps $\widetilde f_{ij}$ satisfy the strict principal cocycle. No product trivialization of a spin bundle in the parameter variable is required.

Write $\mathfrak M^{[2]}=\mathfrak M\times_B\mathfrak M$ and $\pi^{[2]}(p,q)=\pi(p)=\pi(q)$. Kernels are scalar distributions on this fiber product, with the physical vertical volume densities implementing the scalar pairing convention of §2. A positive density on a parameter chart may be used to identify a smooth distribution-valued family with a joint distribution; changing it changes only this test-density identification. Let $P_1$ and $P_2$ be the vertical wave operators in its two point variables.

<div id="lem:compact-spacelike-is-cauchy"></div>

**Lemma 14.11 (Compact spacelike hypersurfaces).**

In a connected globally hyperbolic spacetime, every nonempty compact connected smooth embedded spacelike hypersurface without boundary is a Cauchy hypersurface.

*Proof.* This is the smooth embedded case of Budic–Isenberg–Lindblom–Yasskin, Theorem 1 ([Budic, Isenberg, Lindblom and Yasskin 1978](#ref-BudicIsenbergLindblomYasskin1978)). We give a proof using the smooth Cauchy splitting of Bernal–Sánchez ([Bernal and Sánchez 2005](#ref-BernalSanchez2005), Theorem 1.1). Write the spacetime as $\mathbb R\times N$, with Cauchy temporal coordinate $t$ and future timelike vertical curves, and let $S$ be the stated hypersurface.

The projection $r:S\to N$ is a local diffeomorphism. Indeed, the kernel of the ambient projection is a timelike line and therefore has zero intersection with the spacelike tangent space of $S$. The map $r$ is proper because $S$ is compact. Its image is open by local invertibility and closed by compactness, hence equals the connected manifold $N$. Thus $r$ is a finite covering.

For each $x\in N$, order the finitely many points of $r^{-1}(x)$ by their distinct $t$ coordinates. On an evenly covered neighborhood these ordered heights are smooth, and their order cannot change without two points of the embedded hypersurface coinciding. The ordered sheets consequently define disjoint global graphs. Since $S$ is connected, there is one sheet, and $S=\{(s(x),x):x\in N\}$ for a smooth bounded function $s$.

Along an inextendible future causal curve the Cauchy coordinate takes every real value. Hence $t-s(x)$ changes sign and the curve meets $S$. On $S$ the covector $\mathrm d(t-s(x))$ is timelike and evaluates to $1$ on the future vertical vector $\partial_t$. It is therefore positive on every nonzero future causal vector, and remains future-positive timelike in a neighborhood of each intersection. Every crossing changes $t-s(x)$ from negative to positive. Two crossings would require a crossing from positive to negative between them, which is impossible. This argument also applies to locally Lipschitz causal curves, since a temporal function is strictly increasing along them in that neighborhood. Every inextendible causal curve therefore meets $S$ exactly once. ∎

<div id="prop:compact-fibers-local-cauchy-admission"></div>

**Proposition 14.12 (Automatic local admission for compact Cauchy fibers).**

Let $\pi:\mathfrak M\to B$ be a supplied smooth locally trivial bundle with smooth vertical Lorentzian metric and orientation data, whose connected fibers are globally hyperbolic. If every fiber has a compact Cauchy hypersurface, the bundle is locally common-Cauchy in the sense of Definition 14.10.

*Proof.* Fix $b_0$ and any bundle trivialization near it. Choose a compact smooth spacelike Cauchy hypersurface $\Sigma_0$ for the pulled-back metric $g_{b_0}$. On the compact unit sphere bundle of $T\Sigma_0$, measured in a fixed auxiliary Riemannian norm, $-g_{b_0}(v,v)$ has a positive minimum. Joint smoothness preserves a positive lower bound after one restriction of the parameter neighborhood. Thus the same embedded $\Sigma_0$ is spacelike for all metrics there. It remains compact, connected and without boundary. Each nearby metric is globally hyperbolic by hypothesis, so Lemma 14.11 makes $\Sigma_0$ Cauchy for each of them. The supplied time orientation gives its smoothly varying future unit normal. Repeating the argument near every parameter gives an adapted cover. ∎

<div id="thm:intrinsic-family-canonical-wave"></div>

**Theorem 14.13 (The joint wave class on a spacetime bundle).**

A locally common-Cauchy spacetime bundle has a unique class

$$
[\Lambda]\in\mathcal D'(\mathfrak M^{[2]})/C^\infty(\mathfrak M^{[2]})
$$ {#eq:intrinsic-joint-wave-class}

whose expression in every adapted trivialization satisfies the uniform classical admission of Theorem 13.6. It has an exact Hermitian bisolution representative. The class is independent of the adapted cover and Cauchy presentations, and is natural under supplied smooth fiberwise isometric open embeddings preserving the stipulated orientations and having causally convex images.

It is also natural under every smooth map $\beta:B'\to B$ between finite-dimensional parameter manifolds. If $\mathfrak M'=\beta^*\mathfrak M$ and $\widehat\beta:\mathfrak M'^{[2]}\to\mathfrak M^{[2]}$ is the induced map, then distributional pullback is defined and

$$
[\Lambda_{\mathfrak M'}]=\widehat\beta^{*}[\Lambda_{\mathfrak M}].
$$ {#eq:intrinsic-wave-base-change}

No rank condition on $\beta$ is required.

*Proof.* At $(p,q)\in\mathfrak M^{[2]}$ over $b$, the vertical tangent space is $T_pM_b\oplus T_qM_b$. Define the intrinsic joint positive relation by

$$
\mathfrak C^+
=\left\{(p,q;\zeta):
\zeta|_{T_pM_b\oplus T_qM_b}=(\xi,-\eta),\quad
(p,\xi;q,\eta)\in\mathcal C_{g_b}^+\right\}.
$$ {#eq:intrinsic-family-positive-relation}

Both $\xi$ and $\eta$ are nonzero. In a product chart this is the relation in Theorem 13.6, with unrestricted parameter component. A parameter-dependent change of bundle coordinates changes that component and carries the two vertical components by the fiber isometry. Thus the condition $\operatorname{WF}(\Lambda)\subset\mathfrak C^+$ is intrinsic.

In each adapted chart choose an exact Hermitian representative $\Lambda_i$ from Theorem 13.6 and transport it to $\mathfrak M^{[2]}|_{U_i}$. Its class is independent of the local Cauchy presentation. On $U_i\cap U_j$, joint naturality in that theorem gives

$$
\Lambda_i-\Lambda_j\in
C^\infty\bigl(\mathfrak M^{[2]}|_{U_i\cap U_j}\bigr).
$$ {#eq:intrinsic-local-wave-comparison}

The local causal propagator kernels agree exactly under these isometries: retarded and advanced Green uniqueness preserves their support and equation normalization. Lemma 13.4 gives their smooth distribution-valued dependence. They therefore define one joint kernel $E_\pi$ on the fiber product, with the actual retarded-minus-advanced kernel in every fiber.

Choose a locally finite smooth partition of unity $\{\psi_i\}$ on $B$ subordinate to an adapted refinement, with $\operatorname{supp}\psi_i\subset U_i$. Define

$$
\Lambda=\sum_i(\psi_i\circ\pi^{[2]})\Lambda_i.
$$ {#eq:intrinsic-wave-partition}

Each weighted distribution extends by zero outside its parameter chart, because its multiplier vanishes on a neighborhood of every point outside $U_i$; the sum is locally finite. The operators $P_1$ and $P_2$ are vertical and differentiate none of the weights. Hence $P_1\Lambda=P_2\Lambda=0$. Taking the weights real preserves Hermitian symmetry. Moreover

$$
\Lambda-\Lambda^{\mathrm T}+iE_\pi
=\sum_i(\psi_i\circ\pi^{[2]})
\bigl(\Lambda_i-\Lambda_i^{\mathrm T}+iE_\pi\bigr)
\in C^\infty(\mathfrak M^{[2]}).
$$ {#eq:intrinsic-wave-commutator}

Multiplication by a smooth weight and a locally finite sum preserve the stated wavefront containment. On any adapted chart, subtract its $\Lambda_j$ from the sum. Each difference $\Lambda_i-\Lambda_j$ is [jointly smooth on the overlap](#eq:intrinsic-local-wave-comparison), so the weighted sum differs from $\Lambda_j$ by a jointly smooth kernel there. Thus the global class has the local uniform classical admission and is independent of the partition. Two globally admitted classes agree on every adapted chart by Theorem 13.6, so their difference is globally smooth. The same uniqueness identifies constructions from different adapted covers on a common refinement. A supplied fiberwise isometric open embedding over $B$ is an open embedding of total spaces; its pullback preserves the local admission by Theorem 13.6 and therefore identifies the intrinsic classes.

For base change, the pullback bundle is smooth because $\pi$ is a submersion. Pulling back an adapted chart gives $\beta^{-1}(U_i)\times M_i$ with the same $\Sigma_i$. In these coordinates the induced map is

$$
(b',p,q)\longmapsto(\beta(b'),p,q).
$$

Its transpose differential sends $(\sigma,\xi,-\eta)$ to $((\mathrm d\beta)^t\sigma,\xi,-\eta)$. A conormal covector to this map must therefore have $\xi=\eta=0$. The joint admission excludes all such wavefront covectors. The distributional pullback criterion consequently applies and gives $\operatorname{WF}(\widehat\beta^{*}\Lambda)\subset\mathfrak C^+_{\mathfrak M'}$. The [commutator equation](#eq:intrinsic-wave-commutator) also gives $\operatorname{WF}(E_\pi)\subset\operatorname{WF}(\Lambda)\cup\operatorname{WF}(\Lambda^{\mathrm T})$. Its covectors again have both vertical endpoint components nonzero, so the same criterion defines $\widehat\beta^{*}E_\pi$.

The vertical equations commute with this pullback. The local causal kernels pull back to the actual causal kernels of the pulled-back fibers, and a jointly smooth remainder remains jointly smooth. In a local oscillatory representative, substitution $b=\beta(b')$ preserves the nondegeneracy of the phase in its fiber and frequency variables. On compact parameter sets the chain rule bounds every finite derivative by finitely many derivatives of the original coefficients and of $\beta$. Thus the uniform classical admission, not just the wavefront containment, is preserved. Theorem 13.6 now identifies the pulled-back class with the canonical class of $\mathfrak M'$. Composition and identity of base changes follow either from this uniqueness or from the same coefficient substitution. ∎

<div id="def:intrinsic-full-source-families"></div>

**Definition 14.14 (Intrinsic full sources and atlas families).**

An intrinsic full source family over $B$ consists of the following descent data. Its point charts give a supplied effective smooth locally trivial bundle $\mathfrak M\to B$. On an adapted parameter cover $\{U_i\}$ supply source families $S_i$ of Definition 14.1. Their actual point and principal spin transitions give the point bundle and an actual vertical spin bundle, with strict principal cocycle. On overlaps supply joint full comparison isomorphisms

$$
L_{ij}:S_j|_{U_i\cap U_j}\longrightarrow S_i|_{U_i\cap U_j},
\qquad
L_{ii}=I,\qquad L_{ij}L_{jk}=L_{ik},
$$ {#eq:intrinsic-full-source-cocycle}

over those actual transitions. The full comparisons and their equalities use the complete-family quotient and normalized presentation equivalences of Definitions 7.2 and 9.3. In particular they retain the native root maps, central specializations, whole modules, all-section point connections, initialized finite-rank maps and both stored associators. Each local source has the evaluation- and connection-compatible normalization records of Definition 7.1.

Two descriptions are identified by common parameter refinement and compatible full changes of local presentation over the identity of the same actual point and spin bundles. An arrow is locally a joint full open comparison over one supplied smooth point and actual spin bundle map, compatible with the displayed overlap comparisons. Its geometric fiber maps have causally convex images. Arrow representatives are identified only by common refinement and normalized presentation changes with these actual maps fixed. Denote the resulting category by $\mathsf{FullSrcBun}^{\infty,\mathrm{cc}}_{\mathrm{GH},0}(B)$. Cauchy carriers are local presentation data over $B$.

An intrinsic ordinary-pair atlas family has the executed local objects, full overlap comparisons and effective admission of Definition 14.5, with effective point quotient the supplied bundle $\mathfrak M$ in place of a global product. In each adapted trivialization its parameter and point charts are those of that definition; the total chart images form a countable locally finite cover of $\mathfrak M$. Its arrows are the compatible local atlas arrows. Write $\mathsf{PairAtlBun}^{\infty,\mathrm{cc}}_{\mathrm{GH},0}(B)$ for this category. Refinements restrict parameter neighborhoods and point cores while retaining each selected whole ordinary pair on its parent.

<div id="thm:intrinsic-full-family-correspondence"></div>

**Theorem 14.15 (Intrinsic family recognition and completion).**

On spacetime bundles with the local common-Cauchy presentations of Definition 14.10, recognition and the native construction give an equivalence

$$
\mathsf{FullSrcBun}^{\infty,\mathrm{cc}}_{\mathrm{GH},0}(B)
\simeq
\mathsf{VacBun}^{\infty,\mathrm{cc}}_{\mathrm{GH},0}(B).
$$ {#eq:intrinsic-full-family-equivalence}

Every supplied smooth physical-spin bundle embedding with causally convex fiber images has a unique full lift. The lift intertwines the complete algebras and whole-sky modules to every order, their evaluations and point connections, native root diagrams and normalized finite-rank fields. It retains the specified actual spin map and carries the stored normalization and overlap records through the comparison equations, including both source and target associators. The units and counits retain these data and satisfy both triangle identities.

Supplied admitted intrinsic ordinary-pair atlas families have full completions unique up to the unique full comparison preserving the given marking and local comparisons, and completion is fully faithful. If the ordinary family coverage inputs of Theorem 14.6, namely Paper 3, Propositions 5.8 and 8.4, are also assumed, there are equivalences

$$
\mathsf{PairAtlBun}^{\infty,\mathrm{cc}}_{\mathrm{GH},0}(B)
\simeq
\mathsf{FullSrcBun}^{\infty,\mathrm{cc}}_{\mathrm{GH},0}(B)
\simeq
\mathsf{VacBun}^{\infty,\mathrm{cc}}_{\mathrm{GH},0}(B).
$$ {#eq:intrinsic-family-three-correspondences}

The constructions are independent of adapted covers and carriers up to their unique full comparisons. They commute with refinement, admitted physical restriction and arbitrary smooth base change. The finite estimates of Definition 14.1 hold on retained compact sets in finitely many adapted charts, with their actual transition maps, inverse maps, spin maps and any base-change map included among the input seminorms.

*Proof.* Recognition on each $U_i$ is Theorem 14.4. A full overlap comparison reads out the supplied physical isometry $f_{ij}$ and actual spin map $\widetilde f_{ij}$. Thus the local metrics, physical densities, time orientations and spin bundles descend to the given point bundle. Ricci flatness is a local vertical equation. The common Cauchy hypersurface on each $U_i$ supplies precisely the admission in Definition 14.10. The Cartan and initialized finite-rank readouts also agree under these actual overlap maps. Theorem 14.13 identifies the local scalar classes with one intrinsic joint class.

Conversely, start with a physical-spin vacuum bundle and an adapted cover. Apply Theorem 14.4 in each chart to construct a native family $N_i$. Apply its full Hom theorem to $(f_{ij},\widetilde f_{ij})$ to obtain $L_{ij}:N_j\to N_i$. Since the actual point and spin maps obey the cocycle, $L_{ij}L_{jk}$ and $L_{ik}$ cover the same actual maps. Uniqueness in Theorem 14.4 proves [the full cocycle](#eq:intrinsic-full-source-cocycle).

The carrier and record descent can be seen directly. Each local homogeneous ray bundle is identified with $U_i\times(T^*\Sigma_i\setminus0)$. Proposition 14.2 gives smooth full homogeneous return maps on overlaps; their cocycle follows from the actual null geodesic and point transitions. They glue the homogeneous ray bundles, their positive quotients and the full labelled incidences. No missing affine endpoint is added: each transition maps the actual realized null interval by the affine change of Proposition 3.4.

Let $F_{ij}$ and $J_{ij}=\operatorname{Ad}(F_{ij})$ be the native whole-module and algebra comparisons supplied by Theorem 14.4. They have the joint identities $F_{ij}F_{jk}=F_{ik}$ and $J_{ij}J_{jk}=J_{ik}$. On a common ray refinement, compatible families of local algebra sections, respectively module sections, therefore define the descended sheaves. Their complete products, actions and filtrations are well-defined because the transition maps preserve them. The maps $F_{ij}$ preserve the entire evaluation family and intertwine every vertical point direction on every module section; $J_{ij}$ does the same for algebra sections. Hence the evaluations and point connections descend, including their Leibniz and commutator identities. The native half-density squares and their phase-transition factors are retained through those same actual graph comparisons. The Cartan, tractor, local-twistor, infinity, optical and screen records descend through their actual tensor and initialized spin maps. Their defining equations hold in each chart and hence globally.

For clarity, the stored records need not have identity raw associators. Use $\alpha,\beta,\gamma$ for internal ray-chart indices and $i,j,k$ for parameter charts. On a common ray refinement let $(n^i_\alpha,v^i_\alpha,u^i_{\alpha\beta})$ be the stored normalization records. Suppress the geometric pullbacks. The comparison from chart $j$ to chart $i$ is

$$
\begin{aligned}
k^{ij}_\alpha&=(n^i_\alpha)^{-1}J_{ij}n^j_\alpha,\\
\Xi^{ij}_\alpha&=(v^i_\alpha)^{-1}F_{ij}v^j_\alpha,\\
a^{ij}_{\alpha\beta}
&=(n^i_\alpha)^{-1}
\left(J_{ij}(u^j_{\alpha\beta})(u^i_{\alpha\beta})^{-1}\right).
\end{aligned}
$$ {#eq:intrinsic-family-stored-transition}

The normalization edge equations and the normalized triple equation of Lemma 7.5 give

$$
\begin{aligned}
k^{ij}_\alpha\varphi^j_{\alpha\beta}
&=\operatorname{Ad}(a^{ij}_{\alpha\beta})
\varphi^i_{\alpha\beta}k^{ij}_\beta,\\
a^{ij}_{\alpha\beta}
\varphi^i_{\alpha\beta}(a^{ij}_{\beta\gamma})
C^i_{\alpha\beta\gamma}
&=k^{ij}_\alpha(C^j_{\alpha\beta\gamma})
a^{ij}_{\alpha\gamma},\\
\Xi^{ij}_\alpha\tau^j_{\alpha\beta}
&=a^{ij}_{\alpha\beta}\tau^i_{\alpha\beta}\Xi^{ij}_\beta.
\end{aligned}
$$ {#eq:intrinsic-family-both-associators}

These are the equations checked in Theorem 7.7, now with jointly smooth coefficients as in Theorem 14.4. To check their parameter cocycle without suppressing its overlap units, use $J_{ij}J_{jk}=J_{ik}$. Applying $n^i_\alpha$ to the product $k^{ij}_\alpha(a^{jk}_{\alpha\beta})a^{ij}_{\alpha\beta}$ gives

$$
J_{ik}(u^k_{\alpha\beta})
J_{ij}(u^j_{\alpha\beta})^{-1}
J_{ij}(u^j_{\alpha\beta})
(u^i_{\alpha\beta})^{-1}
=n^i_\alpha(a^{ik}_{\alpha\beta}).
$$

Consequently the stored composition is exactly

$$
k^{ij}_\alpha k^{jk}_\alpha=k^{ik}_\alpha,
\qquad
\Xi^{ij}_\alpha\Xi^{jk}_\alpha=\Xi^{ik}_\alpha,
\qquad
k^{ij}_\alpha(a^{jk}_{\alpha\beta})a^{ij}_{\alpha\beta}
=a^{ik}_{\alpha\beta}.
$$ {#eq:intrinsic-stored-parameter-cocycle}

Associativity gives the fourfold compatibility. Point-dependent stored coordinates transport their connections with the derivative term of Definition 7.1, so the preceding all-section connection statement holds in those coordinates as well. Both raw associators remain in [the stored comparison equation](#eq:intrinsic-family-both-associators), and the strict principal spin cocycle remains separate from the scalar operator equations. This constructs all the descent data of Definition 14.14.

Now let a smooth physical-spin bundle embedding be supplied. Choose adapted source and target charts over a common parameter refinement. Theorem 14.4 gives its unique local full lift. On overlapping parameter charts, conjugating either local lift by the source and target transitions gives lifts of the same point and actual spin maps. Local full Hom uniqueness makes them equal. They therefore define a global full arrow. Conversely, a global full arrow is determined on the parameter cover, and the same local uniqueness proves faithfulness. This proves the Hom bijection, including the distinct central spin lifts. Identities and compositions agree locally and therefore globally.

The local recognition counits are the actual physical-spin identifications and descend under these comparisons. The global full Hom bijection gives the unit as the unique lift of the corresponding inverse geometric identification. Naturality follows by comparing arrows with the same geometric and spin labels. Applying recognition to either triangle gives its geometric identity, and faithfulness proves the full triangle identities. For two choices of adapted cover, intersect their parameter charts and use the same unique lift of the identity geometry and actual spin bundle. The resulting comparisons agree on further intersections, proving independence of covers and compatibility with refinement. The construction for different local Cauchy hypersurfaces is included in Theorem 14.4.

For a supplied ordinary-pair atlas family, apply Theorem 14.6 in each adapted trivialization. Its local completions recognize the same metric and actual spin bundle on overlaps. Their unique full comparisons give the cocycle just proved, so they form an intrinsic full completion. The local completion maps from the executed atlas charts agree after that comparison: their difference is a comparison of already executed local models over the identity geometry and spin map, and the local family full Hom input used in Theorem 14.6 makes it the identity. Thus the completion retains the original atlas transitions and cells. The same reasoning for arrows proves uniqueness and full faithfulness without using coverage.

With the additional Paper 3 coverage inputs, apply Theorem 14.6 near each point of the total bundle in an adapted parameter chart. The selected ordinary families, branches and positive radii are fixed before the output orders. Their point images cover $\mathfrak M$. A countable locally finite refinement in the Hausdorff second-countable total manifold, with smaller product representatives in the adapted charts as in Proposition 11.6, gives the required atlas family. Whole ordinary inputs are restricted only in their parameter domains. The actual identifications with the bundle give the point and strict principal spin transitions; their unique local full comparisons give the stored overlap coherence. Hence the effective quotient is the supplied $\mathfrak M$, and every physical-spin vacuum bundle has an ordinary-pair presentation. The equivalences follow from this essential surjectivity and the full faithfulness already proved.

For base change, pull back the actual point and principal bundles and the adapted local descriptions. The scalar assertion is Theorem 14.13. In each carrier chart, pullback of the complete algebra coefficients and the phases and amplitudes of the module and graph comparisons is substitution of $\beta$ in their smooth parameter dependence. Their uniform parametric classical representations have a nonzero carrier covector comparable to the retained frequency, so they exclude pure parameter wavefront covectors, just as in that theorem. Fiberwise phase nondegeneracy, uniform classical estimates and joint smoothing are preserved. Products, complete inverses, positive-root recursions and the displayed stored equations commute with this substitution. Physical finite-rank maps and native density-square diagrams commute with actual bundle pullback. Point derivatives commute with parameter substitution, so all vertical point-connection identities hold after pullback; central specialization is ordinary coefficient restriction and commutes as well. For an ordinary atlas, pull back its whole input families, executed representatives and supplied comparisons. The inverse images of a locally finite cover are locally finite, and all its effective and stored equations pull back. Thus supplied atlases require no new coverage choice for this operation. These pullbacks give the native construction and the unique full lifts of the pulled-back geometric maps, by full Hom uniqueness. Identity and composition of base changes hold under the canonical identifications of iterated pullback bundles. Local finite-dimensional parameter maps need neither be submersions nor be proper.

Finally, fix retained compact parameter, point and unit-covector sets. A finite collection of adapted charts and their larger buffered parents covers them. The estimates of Theorems 14.3–14.6 apply there. Their finitely many transitions, inverse maps, normalization maps and spin maps are supplied smooth inputs. Under base change, the chain rule adds finitely many derivatives of $\beta$ on a compact parent. Taking finite unions of required input seminorms and finite maxima of bounds gives Definition 14.1's estimates. Increasing coefficient depth or derivative orders does not change the selected cover, parents or ordinary extension branches. ∎

<div id="cor:compact-cauchy-bundle-correspondence"></div>

**Corollary 14.16 (Families with compact Cauchy fibers).**

Theorems 14.13 and 14.15 apply to every supplied smooth locally trivial physical-spin vacuum bundle over a finite-dimensional base whose connected globally hyperbolic fibers have compact Cauchy hypersurfaces. No common Cauchy presentation is an additional admission condition. Every supplied smooth fiberwise physical-spin isometric open embedding between such bundles is admitted; its fiber maps are Cauchy embeddings and have causally convex images.

*Proof.* Proposition 14.12 supplies an adapted cover. Let $f_b:M_b^0\to M_b^1$ be a fiber isometric open embedding and choose a compact smooth spacelike Cauchy hypersurface $\Sigma_b\subset M_b^0$. Its image is compact, connected, embedded and spacelike in the connected globally hyperbolic target. Lemma 14.11 makes $f_b(\Sigma_b)$ a Cauchy hypersurface of the target. It is also Cauchy in the open image $f_b(M_b^0)$, which is isometric to the source. Lemma 3.5 therefore makes that image causally convex. The smooth bundle and actual spin maps are already supplied, so Theorem 14.15 applies to the family. ∎

<div id="ex:torus-monodromy-family"></div>

**Example 14.17 (A flat family with nontrivial parameter monodromy).**

Let

$$
A=\begin{pmatrix}1&1&0\\0&1&0\\0&0&1\end{pmatrix}
\in\operatorname{SL}(3,\mathbb Z).
$$

Choose $\rho\in C^\infty([0,1])$ with values in $[0,1]$, equal to zero near $0$ and one near $1$, and set

$$
h_s=(1-\rho(s))I+\rho(s)A^{\mathrm T}A,
\qquad
g_s=\mathrm dt^2-h_s
\quad\text{on }\mathbb R\times T^3.
$$ {#eq:torus-monodromy-metric}

Each $h_s$ is a positive definite constant spatial metric. Each $g_s$ is therefore flat and globally hyperbolic, with compact Cauchy hypersurface $t=0$. Form the bundle over $S^1$ by

$$
(1,t,x)\sim(0,t,Ax).
$$ {#eq:torus-monodromy-clutching}

Since $h_1=A^*h_0$ and the path is constant near its endpoints, the fiber metrics glue smoothly with their orientation and time orientation. To supply the actual spin bundle, use the global oriented orthonormal frames whose spatial matrices are $h_s^{-1/2}$. At the clutching, the frame rotation is

$$
R=A(A^{\mathrm T}A)^{-1/2}\in\operatorname{SO}(3).
$$

Choose one of its two lifts $\widetilde R\in\operatorname{Spin}(3)$ and glue the product spin bundles by $(1,t,x,a)\sim(0,t,Ax,\widetilde R a)$. This is an actual smooth principal lift of the vertical frame identification. The sign of this chosen lift is retained.

The first-homology local system of the spacetime fibers has monodromy $A\ne I$. A product bundle over $S^1$ has identity monodromy, and a change of fiber identification only conjugates it. Thus this spacetime bundle has no global product trivialization over $S^1$. Corollary 14.16 nevertheless supplies its joint wave class, full source family and unique full lift of the clutching data. With the ordinary family coverage inputs, it also has an intrinsic ordinary-pair atlas family. ∎

Descent retains the geometric and spin monodromy of the supplied spacetime bundle. The point connections act in the spacetime directions.

<div id="sec:global-analytic-real-germs"></div>

## 15. Analytic sources along an entire real spacetime

The analytic comparison uses the fixed-domain global correspondence of Paper 2, rather than only its marked Cauchy category. The latter is stated for compact analytic initial hypersurfaces. The fixed-domain constructions and the complexification and embedding lemmas have a larger scope: they apply to an entire Hausdorff second-countable analytic point manifold, with complex neighborhoods whose widths may vary from point to point ([Isthmus 2026b](#ref-IsthmusGlobal2026), Proposition 3.1, Theorems 3.11, 4.6 and 5.6, and Lemma 7.3). We use these results to describe the unmarked real objects, their arrows and their restrictions.

Throughout this section the Einstein coefficient is zero. A physical metric has signature $(+---)$, specified orientation and time orientation, its actual scale, and an actual principal $\operatorname{Spin}^{+}(1,3)$ bundle. No quotient by a constant conformal rescaling or by the central spin sign is taken. Write $\mathsf{Vac}^{\omega,\mathrm{cc}}_{\mathrm{GH},0}$ for connected real analytic objects with these data and with globally hyperbolic underlying spacetime. Its arrows are analytic spin isometric open embeddings with causally convex images. An analytic or compact Cauchy hypersurface is not part of an object of this category.

<div id="sec:unmarked-analytic-source-category"></div>

### 15.1. Extension objects and whole-real germs

<div id="def:unmarked-analytic-source-germs"></div>

**Definition 15.1 (Unmarked analytic source germs).**

An analytic extension source is one of the independently admitted holomorphic source atlases, operator monodromy sources or geometric monodromy sources of Paper 2, at coefficient zero, with the following additional structure and tests.

1. Its connected Hausdorff second-countable complex point manifold $B$ has a compatible antiholomorphic involution $\sigma$. Its fixed locus is exactly a connected real four-manifold $M$. Every point restriction retains the whole compact complex quadric over each retained complex point.
2. The source has the compatible Lorentz reality and actual real spin identifications of Paper 2, §6. On its local whole-sky models the retained spin and tangent calibration has real form $\operatorname{diag}(1,-1,-1,-1)$. Supply orientation and time orientation on $M$. The real cone field determined by $\mathrm dp(K_{\mathbb R})$ is required to be globally hyperbolic. These conditions are tested on the supplied incidence and local recognition data, before the global metric is decoded.
3. All physical comparison germs carry the selected Einstein scale and actual spin lift. Their analytic symbol and comparison admission is the one restated in Paper 2, Propositions 2.1–2.3, with the local conditioned conventions of its §2. Operator presentations retain both associators, their root square identifications, any retained root base factors, whole-family module frames, and the weak Lorentz square equations. The classical incidence and principal spin cocycles are strict. The operator comparison equations remain those of Paper 2, Definition 4.4; they are not replaced by strict equations on arbitrary algebra representatives.
4. The designated real-path groupoid is $\operatorname{Mon}(K_{\mathbb R})$, formed from paths lying in the real phase. Its functor into the complex monodromy groupoid is retained. It is not defined as the full restriction of the complex groupoid to real objects.

For a source atlas the phase and its real structure are obtained by its source operations and physical overlap comparisons, as in Paper 2, Lemma 5.5. The quotient point topology must pass the atlas tests in its Definition 5.1. For an operator or geometric source the point manifold and full incidence are supplied in its independent admission. No initial hypersurface, initial data or initial marking is included here.

*Representative restrictions.* An allowed representative restriction is a connected conjugation-invariant open neighborhood $B_0\subset B$ of all of $M$. Restriction recomputes

$$
\mathcal G_{B_0}
=\operatorname{Mon}\bigl(K|_{p^{-1}(B_0)}\bigr)
$$ {#eq:analytic-real-germ-recomputed-groupoid}

and pulls the supplied actions back by the integrated inclusion into $\mathcal G_B$. Symbols, torsors, incidence modules, actual roots, frames, associators and their comparisons restrict simultaneously. A full subgroupoid on the old endpoints is not substituted for this recomputed groupoid.

*Morphisms.* A morphism is represented by a physical source embedding on such a source neighborhood,

$$
\mathcal A
\xleftarrow{\ r_{B_0}\ }
\mathcal A|^{\mathrm{mon}}_{B_0}
\xrightarrow{\ F\ }
\mathcal A',
$$ {#eq:analytic-real-germ-roof}

compatible with the Lorentz structures and their specified coherences. Its real point map $f:M\to M'$ preserves orientation and time orientation and has causally convex image. Equality is equality after a common allowed restriction, with the same actual spin lift. On operator presentations it also uses the normalized comparison isomorphisms of Paper 2, Definition 4.4. Denote the three resulting categories by

$$
\mathsf{AnAtl}^{\mathrm{germ},\mathrm{cc}}_{\mathrm{GH},0},
\qquad
\mathsf{AnOp}^{\mathrm{germ},\mathrm{cc}}_{\mathrm{GH},0},
\qquad
\mathsf{AnRay}^{\mathrm{germ},\mathrm{cc}}_{\mathrm{GH},0}.
$$ {#eq:unmarked-analytic-source-categories}

These definitions use the original two analytic classes of weights $2$ and $-6$ and their physical source law, or the independent operator and geometric admission tests. They do not define admission by membership in the image of a metric constructor. In the next section $\mathsf{AnOp}^{\mathrm{germ},\mathrm{cc}}_{\mathrm{GH},0}$ is the convenient realization for retaining the scalar module comparison; the other two source realizations have the same physical Hom classes through the equivalences below.

Recognition uses the whole-sky data above. Section 16 also uses calibrated local counits and their compatibility with the physical comparisons on restrictions and overlaps. Its version, admission and family requirements are collected in the [inputs for the analytic comparison](#sec:analytic-interface-input-contract).

*Roof composition.* The roof composition is well defined. If a second representative is defined on $B'_0$, replace the first domain by the component containing $M$ of $B_0\cap F^{-1}(B'_0)$, recompute monodromy there, and compose. This component exists and contains all of $M$ because $M$ is connected. It is invariant under conjugation. Two such choices have a common allowed restriction. The nested integrated inclusions send each path to the same path, so composition is associative on germs. Causal convexity is closed under composition: a causal segment between two points of the composite image first lies in the second image and then, on pullback, in the first image. Identity roofs give identities. These are the neighborhood localizations of Paper 2, Definition 7.2, with the initial-data markings omitted and the stated real image condition imposed.

<div id="thm:unmarked-global-analytic-recognition"></div>

**Theorem 15.2 (Unmarked analytic recognition and full Hom).**

Under the analytic local inputs and fixed-domain global correspondence of Paper 2, real recognition induces equivalences

$$
\mathsf{AnAtl}^{\mathrm{germ},\mathrm{cc}}_{\mathrm{GH},0}
\simeq
\mathsf{AnOp}^{\mathrm{germ},\mathrm{cc}}_{\mathrm{GH},0}
\simeq
\mathsf{AnRay}^{\mathrm{germ},\mathrm{cc}}_{\mathrm{GH},0}
\simeq
\mathsf{Vac}^{\omega,\mathrm{cc}}_{\mathrm{GH},0}.
$$ {#eq:unmarked-global-analytic-recognition}

In particular, every object of $\mathsf{Vac}^{\omega,\mathrm{cc}}_{\mathrm{GH},0}$ has an analytic source germ along its entire real point manifold. No compactness of a Cauchy hypersurface, uniform complexification radius, separated complex ray quotient, null completeness or trivial complex leafwise holonomy is required.

For each of the three source realizations $\mathsf{An}$ and for two admitted objects, recognition gives a bijection

$$
\operatorname{Hom}_{\mathsf{An}}(\mathcal A,\mathcal A')
\xrightarrow{\ \sim\ }
\operatorname{Emb}^{\omega,\mathrm{cc}}_{\mathrm{spin}}
\bigl(\mathcal R_\omega\mathcal A,
      \mathcal R_\omega\mathcal A'\bigr).
$$ {#eq:unmarked-global-analytic-full-hom}

Both inverse comparisons retain the entire real point manifold and its actual scale and spin. On common extension representatives they retain the full complex skies, prescribed local source operations, recomputed complete complex null-path actions, and actual calibrated roots and module comparisons. The weak operator and Lorentz coherences are carried through the same comparisons.

*Proof.* Consider first a geometric monodromy source. Paper 2, Theorem 3.11 reconstructs a holomorphic Einstein metric $g_B$ on its supplied point manifold, with the complete incidence and specified spin structure. Its Lemma 2.4 makes reconstruction natural for the supplied conjugation. Hence $\sigma^*\overline{g_B}=g_B$, and the metric $g=g_B|_M$ is real analytic. The tangent calibration gives signature $(+---)$. Local recognition identifies its real null directions with the supplied $\mathrm dp(K_{\mathbb R})$. Therefore the orientation, time orientation and global hyperbolicity tests in Definition 15.1 are exactly those of $(M,g)$. The coefficient zero and the selected scale are preserved by recognition. The resulting principal spin structure is the actual supplied one, including its central action.

An allowed complex restriction retains all real points and all these real data. Source embeddings restrict to the stated real spin isometric embeddings. Recognition therefore defines a functor $\mathcal R_\omega$ on the roof category.

For essential surjectivity, let $(M,g,P)$ be any object of $\mathsf{Vac}^{\omega,\mathrm{cc}}_{\mathrm{GH},0}$. Paper 2, Proposition 3.1 supplies a Hausdorff second-countable complexification with fixed locus exactly $M$, a nondegenerate holomorphic vacuum metric, and extensions of the orientation, actual spin and selected scale. The underlying complexification input is existence and neighborhood uniqueness along the entire paracompact analytic manifold ([Whitney and Bruhat 1959](#ref-WhitneyBruhat1959), §1, Proposition 1); second countability supplies paracompactness here. Neither this input nor Paper 2's extension proposition requires a compact Cauchy surface. Shrink only to a connected conjugation-invariant neighborhood of all of $M$. The canonical source of its Theorem 3.11 is independently admitted on that complex neighborhood. Theorems 4.6 and 5.6 give its operator and original-source realizations. The compatible Lorentz structures pass through the same local inverse comparisons by Propositions 6.4–6.5 and the original-source reality operation. The prescribed real metric supplies precisely the causal tests of Definition 15.1. All real points remain present, so this constructs an object over the entire $M$ in each source category.

For fullness, fix an analytic spin isometric embedding $f:M\to M'$ with causally convex image. Paper 2, Lemma 7.3 extends it to a compatible holomorphic spin isometric embedding $F:B_0\to B'$ on a neighborhood of all of $M$. That lemma allows noncompact $M$ and nonproper $f$. It retains the specified spin lift and permits a conjugation-invariant connected source neighborhood. Fixed-domain full faithfulness, first in Theorem 3.11 and then in Theorems 4.6 and 5.6, supplies the corresponding physical source morphism on the recomputed source over $B_0$. The comparisons with its Lorentz conjugate cover the same physical map and actual spin lift. The normalized uniqueness in the fixed-domain operator theorem gives their required coherence, including the framed module square; it does not require a strict reality action on the chosen algebra sheaves. Its roof recognizes to $f$.

For faithfulness, suppose two roofs recognize to the same real point embedding with the same actual spin lift. Paper 2, Lemma 7.3, makes their holomorphic point and spin germs equal on a common neighborhood of all of $M$. On the recomputed groupoid there, the fixed-domain full Hom theorem identifies their source morphisms. This includes the action on every path class: the phase and infinitesimal maps are fixed, and source-connected, source-simply-connected integration fixes the integrated functor. The functor is not required to be faithful on complex path classes. On operator sources the comparison also retains both associators and the framed module maps, as specified in Paper 2, Definition 4.4 and Theorem 4.6. Thus the roofs are equal in the stated physical Hom set. Distinct principal spin lifts remain distinct.

The fixed-domain source-atlas and operator equivalences commute with recomputed restriction by Paper 2, Proposition 7.1 and the restriction statements in its §3–§5. Their unit and counit therefore descend to the roof categories. The original-source unit returns the original two classes and overlap instructions; the operator counit uses the actual local counits and their normalized comparison equations, with both associators. The global phase and transport comparisons are fixed by complete-sky evaluation and integration. Paper 2, Theorem 4.8, Proposition 5.7 and Theorem 6.3 identify the retained module family, source-operation diagram, spin and optical data. These are the same comparisons used above, so they remain natural after real restriction and neighborhood localization.

Finally, choose two complex extensions of one analytic real spacetime with a specified identity of the real point and spin data. Fullness lifts that identity to a source-germ isomorphism, and faithfulness makes both composites the identities. This proves independence of the chosen extension and completes the equivalences. The proof repeats the recognition and localization argument with unmarked globally hyperbolic real loci; it does not apply the compact initial-data statement of Paper 2, Theorem 7.4 outside its hypotheses. ∎

<div id="lem:analytic-geometric-locus-fullness"></div>

**Lemma 15.3 (The analytic geometric locus is full).**

Forgetting analyticity gives a fully faithful functor

$$
\mathsf{Vac}^{\omega,\mathrm{cc}}_{\mathrm{GH},0}
\longrightarrow
\mathsf{Vac}^{\infty,\mathrm{cc}}_{\mathrm{GH},0}.
$$ {#eq:analytic-geometric-locus-inclusion}

Its essential image consists of smooth physical spin metrics admitting a compatible real analytic structure in which the metric is analytic. When such a structure exists, its maximal analytic atlas is unique. The actual principal spin covering then has a unique compatible analytic covering structure.

*Proof.* A smooth local isometry $f$ between analytic metrics preserves the Levi–Civita connection. On a sufficiently small normal neighborhood of each point,

$$
f\circ\exp_p^{g}
=\exp_{f(p)}^{g'}\circ\mathrm df_p.
$$ {#eq:analytic-embedding-normal-coordinate-proof}

Both exponential maps and their local inverses are analytic, so $f$ is analytic. This is Paper 3, Lemma 9.1, or Paper 2, Lemma A.4. It applies to every open isometric embedding, without surjectivity onto the target spacetime. An actual smooth spin lift of this analytic frame map is analytic because the spin projections are locally analytic covering isomorphisms. Thus the morphism sets, with their spin labels and causal image condition, are unchanged.

Apply the same exponential-map identity to the identity of a smooth metric written in two proposed analytic atlases. The atlases are analytically compatible in both directions and have the same maximal completion. For the spin assertion, the oriented orthonormal frame bundle is analytic. Lift its analytic charts through the given double covering to obtain the unique analytic structure making that covering locally analytic; the group action and its frame compatibility are analytic by local lifting. This retains the given smooth principal bundle and its central action. ∎

Write $\mathsf{Vac}^{\infty,\mathrm{cc}}_{\mathrm{GH},0;\omega}$ for this full analytic locus. The condition concerns the regularity of the actual metric. It neither requires an analytic choice of a Cauchy hypersurface nor modifies the independent admission of smooth full sources in §6–§7.

<div id="sec:analytic-source-real-restriction"></div>

### 15.2. Real restriction and intrinsic real rays

<div id="prop:analytic-source-real-point-restriction"></div>

**Proposition 15.4 (Restriction of the real point domain).**

Let $\mathcal A$ be an analytic source germ over $M$, and let $U\subset M$ be a connected causally convex globally hyperbolic open subset. There is a canonically determined analytic source germ $\mathcal A|_U$ whose recognized spacetime is $(U,g|_U)$, with the restricted physical and actual spin data. It has an inclusion morphism into $\mathcal A$. Iterated restriction is related to direct restriction by the unique comparison over the specified real identity and spin identification. These comparisons respect composition and are natural for the embedding arrows of Definition 15.1.

This operation changes the retained real point domain. It is distinct from an allowed representative restriction around all of $M$.

*Proof.* Represent $\mathcal A$ on $B$. Since $M$ is its closed fixed locus, $M\setminus U$ is closed in $B$. The invariant open set $B\setminus(M\setminus U)$ has fixed locus exactly $U$. Take its connected component containing $U$, and, if needed, a smaller connected invariant neighborhood of all of $U$ there. Call this complex point domain $B_U$.

Restrict the original atlas and all of its physical comparison germs, or restrict the independent geometric and operator local data. Recompute the complex monodromy as

$$
\operatorname{Mon}\bigl(K|_{p^{-1}(B_U)}\bigr)
$$ {#eq:analytic-source-real-domain-monodromy}

and pull the old actions back by its integrated inclusion. The fixed-domain restriction constructions of Paper 2, §3–§5, retain all the local equations, full quadrics, roots, frames and comparison cells. The same path argument as its Proposition 7.1 proves compatibility of the actions. This argument concerns point restriction itself; the requirement in that proposition to retain the old entire real locus is replaced here by retaining the new entire real locus $U$.

The restricted phase has the real cone of $g|_U$, with its original orientations and spin, so it satisfies Definition 15.1 for $U$. Two choices of $B_U$ have a common neighborhood of all of $U$ in their intersection. If a different representative of the original germ is used, first restrict the given germ comparison to such a common neighborhood of $U$. The resulting restricted objects are therefore canonically isomorphic with the fixed real identity and spin identification. Theorem 15.2 makes this comparison unique as a physical Hom class.

For $V\subset U\subset M$, the nested groupoid functors send each path to the same path in the original representative. Their action maps and restricted physical cells agree, and common restriction gives $(\mathcal A|_U)|_V\simeq\mathcal A|_V$. For an embedding represented by $F:B_0\to B'$ and real opens with $f(U)\subset U'$, intersect the source representative with $F^{-1}(B'_{U'})$. This contains all of $U$ and yields the required restricted morphism after recomputing monodromy. Its identity and composition laws follow from the same path and cell equations. ∎

<div id="prop:analytic-intrinsic-real-path-comparison"></div>

**Proposition 15.5 (Intrinsic real-path and affine comparison).**

Let $\mathcal A$ be an admitted analytic source germ, with recognized real metric $g$ on $M$. Its designated real phase and path groupoid identify canonically with

$$
F_{\mathbb R}
\simeq \mathbb P_+\mathcal N^*_{\mathrm{past}}M,
\qquad
\operatorname{Mon}(K_{\mathbb R})
\simeq F_{\mathbb R}\times_{\mathcal N(M)}F_{\mathbb R}.
$$ {#eq:analytic-real-intrinsic-path-comparison}

The quotient is the full smooth cooriented ray space of Theorem 3.2, with all point-labelled skies. The quadratic-affine representation descends by real-path transport to the canonical real ray bundle. With any smooth spacelike Cauchy hypersurface $\Sigma$, its position retains exactly the realized domain $D_{M,\Sigma}$ of Theorem 3.2. Actual principal spin and finite-rank point comparisons are retained throughout. These identifications are natural for the causal open embeddings and real restrictions above.

*Proof.* Whole-sky recognition identifies the real fixed quadric with the real projective null sphere at every point and identifies $K_{\mathbb R}$ with its geodesic line. Time orientation selects the future tangent on each projective line; metric duality with the sign in Definition 3.1 identifies it with the positive past-covector phase. This proves the first map globally and preserves the full point family.

Choose a smooth spacelike Cauchy hypersurface of $M$. Theorem 3.2 identifies the entire real phase with $D_{M,\Sigma}$, whose fibers over $\mathcal N(M)$ are open intervals. Each real null leaf is therefore simply connected and has a unique endpoint-fixed real path class between any two of its points. The endpoint map of the real monodromy groupoid gives the second isomorphism in the statement. Locally it is the endpoint map of a flow box; globally these maps agree by the uniqueness of the real path class. This uses a smooth Cauchy surface, with no appeal to the compact analytic Cauchy surface in Paper 2, Proposition 3.2.

The full complex groupoid may have further arrows between real phase points, represented by paths leaving the real phase. None of them is inserted into the displayed real pair groupoid. This is precisely the designated real-path convention of Paper 2, Proposition 3.9 and Propositions 6.4–6.5. Changing the complex representative recomputes complex paths but leaves every real path in $M$ available, so it leaves this real groupoid unchanged.

For the quadratic-affine representation, Paper 2, Theorem 3.11 identifies the supplied complete-sky evaluation bundle and its connection with the canonical tractor data. At coefficient zero their real Einstein-scale form is

$$
\begin{aligned}
\mathcal T&=\mathbb R\oplus TM\oplus\mathbb R,\\
D_v(\sigma,\mu,\rho)
&=\bigl(v\sigma-g(v,\mu),\,
        \nabla_v\mu+\rho v,\,v\rho\bigr),\\
\mathsf I&=(1,0,0),\qquad \mathsf X=(0,0,1).
\end{aligned}
$$ {#eq:analytic-real-zero-scalar-tractor}

Their quadratic pairing is

$$
H\bigl((\sigma,\mu,\rho),(\sigma',\mu',\rho')\bigr)
=\sigma\rho'+\rho\sigma'+g(\mu,\mu').
$$ {#eq:analytic-real-zero-scalar-pairing}

In particular $H(\mathsf I,\mathsf X)=1$, so the comparison carries the selected physical scale. Let $P_z(s)$ be tractor transport along the $\Sigma$-normalized geodesic $\gamma_z$. The canonical identities $D_k\mathsf X=\Theta(k)$ and $D_k\Theta(k)=0$ give

$$
P_z(s)^{-1}\mathsf X(\gamma_z(s))
=\mathsf X(\gamma_z(0))+s\,\Theta(\dot\gamma_z(0)).
$$ {#eq:analytic-real-affine-interval-comparison}

Thus real-path descent is the bundle obtained by pulling $\mathcal T|_\Sigma$ to its Cauchy ray coordinates, with affine line generated by the two terms on the right. The position image consists exactly of the parameters $s\in I_z$. The complete affine line is an ambient fiber; no point is added at a missing affine endpoint or outside the realized interval.

The rank-four spin connection, its exterior-square identification, flag, infinity and optical data are built from this same point metric and actual spin structure in Paper 2, Propositions 6.1–6.2 and Theorem 6.3. Their restriction to real paths is their actual parallel transport. It agrees with the corresponding real canonical point data, with selected states compared in the same initialization and generator convention. Explicitly, for the future Cauchy-normalized generator $K_\Sigma$, the contact-normal covector is $\ell=-g(\mathrm dp(K_\Sigma),\cdot)$. The optical generator is therefore $-K_\Sigma$, or $-cK_\Sigma$ after multiplication of the contact form by a positive ray function $c$, exactly as in §6.3. Optical value-and-slope and companion states are compared after this conversion; the selected value stays one, and the companion parameter has derivative $-c^{-1}$ with respect to the future affine parameter. This assertion retains the specified principal spin map; agreement on projective skies alone does not determine that map. The separate scalar module calibration is treated in §16.

Changing the smooth Cauchy section gives exactly the affine and contact changes of Proposition 3.4. For a causal open embedding identify its image with $U\subset M'$. Proposition 3.6 identifies its rays with the ambient rays meeting $U$ and identifies its incidence with the point restriction. In ambient affine coordinates its realized interval is

$$
\{s\in I_z^{M'}:\gamma_z(s)\in U\}.
$$ {#eq:analytic-real-restricted-affine-interval}

This interval is connected by causal convexity. Isometric pullback preserves the displayed connections and initialized transport, so the quadratic-affine and spin comparisons commute with restriction and composition. A Cauchy embedding can identify all ray labels while retaining a proper point and affine-interval domain, as in Corollary 9.5. ∎

The independent analytic source conditions require a Hausdorff point manifold, the full proper quadric family and the effective actual spin cocycle. They do not require a Hausdorff coarse complex ray space. The extra closedness, embeddedness and loop-transport tests in Paper 2, Lemma 3.12 concern an optional ordinary complex quotient. They play no role in Theorem 15.2. The real quotient in Proposition 15.5 is Hausdorff because of global hyperbolicity and its Cauchy description, without imposing those complex quotient tests.

<div id="sec:global-analytic-wave-bridge"></div>

## 16. The structured analytic comparison and global wave completion

The analytic source retains its complex extension germ, complex monodromy and calibrated local operator records. Its smooth completion is the independently admitted global wave source on the recognized real spacetime. To compare the two sources, we construct maps on the complete real sectors and on the incidence over each labelled point. The global scalar class is constructed on the entire real spacetime product; it is not obtained by extending a locally defined analytic two-point kernel.

<div id="sec:analytic-interface-input-contract"></div>

::: {.paper-block-heading}
**Inputs for the analytic comparison.**
:::

The structured comparison uses the following local inputs on the retained records of Definition 15.1 ([Isthmus 2026c](#ref-IsthmusSmooth2026); [Isthmus 2026a](#ref-IsthmusProjective2026)). Theorem 15.2 uses the analytic inputs restated in Paper 2; the calibrated comparison below additionally uses Paper 3, §9. The hypotheses apply on each whole-sky chart of every source under comparison and on common refinements for its overlap, restriction and physical arrow diagrams. For the inverse on the analytic metric locus they apply also to the models of the source furnished by Theorem 15.2. Bounds uniform in a varying family enter only in the conditioned assertion.

1. **Models, versions and actual counits.** Paper 3, §9, uses Paper 1, manuscript version 1.1 (Hexagon v2), Definition H.1 and the actual counit of Theorem 9.10. The independent local source and its counit use Lemma H.2, Proposition H.3 and Theorem H.4. Paper 2 restates its analytic inputs while citing an earlier local revision. Its restated inputs are retained for recognition; no identification of all statements in the two local versions is inferred. The structured comparison is used on the retained records with the actual calibrated counits, root maps and frame maps satisfying the cited hypotheses.
2. **Algebra and module comparisons.** Analytic quantization and normalized comparison use Paper 1, Theorem F.4 and Lemma F.8; the actual simple modules and physical-spin comparisons use Lemma G.2 and Theorem G.5. Paper 2, Proposition 2.3 and Definition 4.4, retain the corresponding whole-sky operator data, root squares, and specified nonzero frames of the rank-one local-system factors, together with their comparison maps, which its Theorems 4.8 and 5.6 carry through descent and the counit. Their real root and frame calibration and coupled Lorentz comparison are those of Paper 3, Propositions 9.3–9.6 and Theorem 9.7.
3. **Admitted parents and individual comparisons.** All local comparisons are used on their admitted parents and common finite refinements. A supplied bounded diagram retains coordinate and conic buffers, maps and inverse maps, nonzero root and frame margins, and factorial bounds on the actual operator coordinate images and inverse comparisons. On a strict conic compact, an image of order $m$ has terms bounded by $M A^j j!$ at degree $m-j$, uniformly on the specified retained parameter set. These are the analytic-symbol bounds of Paper 3, Proposition 9.2, in the actual admitted operator algebra. For an individual admitted comparison, its finitely many coordinate-image symbols have these local bounds after restriction to smaller retained sectors. That proposition constructs a controlled reference comparison and its inverse and uses the actual coordinate-image bounds to compare a supplied representative. A finite diagram admits a common refinement. Coefficientwise holomorphy of an arbitrary formal series does not supply these bounds.
4. **Conditioned families.** A family assertion additionally requires uniform bounds on the coordinate images and inverse comparisons, with the retained parent, root and frame margins, over its supplied parameter set. These are conditioned hypotheses, as in Proposition 16.6; they are not inferred from fiberwise analytic admission. The real common-Cauchy hypotheses of that proposition remain separate from this analytic input contract.

Write

$$
\mathsf{FullSrc}^{\infty,\mathrm{cc}}_{\mathrm{GH},0;\omega}
$$

for the full subcategory of the smooth source category whose recognized physical metric belongs to the analytic locus of Lemma 15.3. The stored wave coefficients and the presentation Cauchy hypersurface need not be analytic. The condition is imposed on the recognized metric, with its actual scale and spin structure.

<div id="sec:analytic-wave-completion-data"></div>

### 16.1. Local interfaces with a global target

<div id="def:analytic-admitted-wave-completion"></div>

**Definition 16.1 (An admitted analytic wave completion).**

Let $\mathcal A$ belong to $\mathsf{AnOp}^{\mathrm{germ},\mathrm{cc}}_{\mathrm{GH},0}$, and put $M=\mathcal R_\omega\mathcal A$. An admitted wave completion consists of an independently admitted smooth global full source $S$, an actual physical-spin isometry

$$
b:RS\longrightarrow M,
$$ {#eq:analytic-wave-completion-marking}

and a compatible system of calibrated local interfaces from the whole-sky operator models of $\mathcal A$ to the restricted fields of $S$. The interfaces are taken after sectorwise real restriction and complete formal enrichment as in Paper 3, Proposition 9.2. They have invertible algebra and semilinear module vertices on the tested real ray domains. They preserve the full homogeneous map, filtration, product, complex-linear internal adjoint, the original root and its square maps, central specialization and framed factors. They also carry the finite-rank, optical and actual principal-spin diagrams over $b^{-1}$.

The full evaluation and the connections in every point direction on the enriched analytic presentation are the pullbacks of the smooth target fields by the module and algebra vertices. They act on every complete section in the respective presentation. Compatibility means the three stored comparison equations, with both original associators, and their identity, inverse and composition cells. Comparisons are understood modulo simultaneous normalized changes of presentation and common refinement, including the transformed evaluation and connection records. In Definition 7.1 it is the corrected transitions that carry the transferred evaluation.

The interfaces are defined on a real point cover and cover the whole real sky over every retained point. On overlaps they use the actual physical and principal-spin maps of the analytic source. On a causal point restriction they use the relative carrier comparison of §8. Their module domains remain point-labelled incidence domains. The definition neither replaces the analytic source by a module on an unlabelled real ray quotient nor identifies the complex monodromy groupoid with the designated real-path groupoid.

A morphism between two such completions is a full smooth source isomorphism over the corresponding marking, together with its compatible normalized local comparison cells. In the physical comparison quotient, the requirement is that it carry one calibrated interface system to the other. A single raw analytic chart is not required to extend to all points on all rays meeting that chart. The global target $S$ itself has the whole-incidence normalization records required by Definition 7.1.

<div id="lem:analytic-local-global-carrier-interface"></div>

**Lemma 16.2 (A calibrated interface on a global Cauchy carrier).**

Let $X$ be an admitted local analytic Lorentz operator model at coefficient zero, with its actual physical-spin identification with a real open neighborhood in $M$. Choose a whole smooth spacelike Cauchy hypersurface $\Sigma_M$ of $M$. After restricting the local point core, there are complete algebra and semilinear module interface vertices, with their finite sector indices suppressed,

$$
K_X^\Sigma:\mathscr E_X^{\mathbb R,\wedge}
 \longrightarrow\mathcal A_{\Sigma_M},
\qquad
F_X^\Sigma:\mathscr M_X^{\mathbb R,\wedge}
 \longrightarrow\mathcal M_{\Sigma_M}
$$ {#eq:analytic-local-global-interface-vertices}

on the corresponding conic and point-labelled incidence domains. They have inverses on those domains and satisfy the calibration of Paper 3, Proposition 9.5. The enriched analytic presentation receives the full evaluation and both point connections by pullback from the smooth target along the corresponding vertices. With these fields, the vertices intertwine evaluation and covariant differentiation on every complete section. Changes of the local scalar disk, global Cauchy carrier and admitted analytic presentation have the coherent comparison maps of Paper 3, Theorem 9.7, and Corollary 8.4 above.

*Proof.* The analytic physical-spin identification is part of the source model. Its real restriction identifies the local metric with $g|_M$. Let $D_a$ be an analytic spacelike disk through the compared point, as in Paper 3, Lemma 9.1. That lemma permits a maximal disk, but the use here is its role as a scalar carrier. Paper 3, Proposition 9.2, gives actual analytic sector comparisons and their finite-jet extensions

$$
k_X^{D_a}:\mathscr E_X^{\mathbb R,\wedge}
 \longrightarrow\mathcal A_{D_a},
\qquad
F_X^{D_a}:\mathscr M_X^{\mathbb R,\wedge}
 \longrightarrow\mathcal M_{D_a}.
$$

At each homogeneous degree these maps use only finite jets of the input at the real endpoint of the homogeneous ray map. The intermediate analytic transport paths enter their coefficients, not the values of a general smooth input away from that real endpoint. This is the finite-jet extension established in that proposition; it is the reason the maps act on smooth complete symbols rather than only on holomorphic symbols.

Keep the actual relative module root. In the notation of Paper 3, Proposition 9.3, with $\pi$ the full complex sky projection,

$$
R_X=R_{g_X}\otimes\pi^*A_X,
\qquad R_{g_X}=\mathcal L_X^{-1},
\qquad q_{A_X}:A_X^{\otimes2}\longrightarrow\mathcal O.
$$ {#eq:analytic-bridge-relative-root}

The square on $R_{g_X}$ is the metric null-residue square, and the product square is the supplied square on $R_X$. Thus the original square and every retained base factor are present in this formula. Proposition 9.4 of that paper gives the initialized section $a_X$ with $q_{A_X}(a_X^2)=\varepsilon_0$, where $\varepsilon_0$ is the actual calibrated Lorentz sign. If $\nu_X$ is the original frame of the rank-one local-system factor, choose the unique module interface over $k_X^{D_a}$ satisfying

$$
\nu_X\longmapsto a_X^{-1}\otimes n_{\mathrm W,X}.
$$ {#eq:analytic-global-interface-framing}

Here $a_X^{-1}$ pairs to one with $a_X$. The native frame is fixed by the complete wave evaluation through

$$
\sigma^{\mathrm{for}}_1(e)
 =-i(2\pi)^{-3/2}w_g\otimes n_{\mathrm W},
\qquad w_g=1\text{ in }\mathcal L\otimes R_g.
$$ {#eq:analytic-bridge-native-leading-frame}

These formulas fix the module scalar, including its phase. They do not impose principal scalar one on an arbitrary framed module map. For example, replacing the framed input by $\nu'_X=u\nu_X$ changes its calibrated interface to $u^{-1}F_X^{D_a}$. The induced connection coefficient changes by the scalar one-form $-u^{-1}\mathrm du$ in that reframed presentation. This is the scalar distinction in Paper 3, Proposition 9.5.

We place this interface in the global Cauchy presentation. Let $\iota$ denote the given real physical-spin identification. Choose a smaller common wave parent whose image $V$ is causally convex and globally hyperbolic in $M$, and whose inverse image is causally convex in the retained local wave parent. Such parents are obtained by the two successive causal restrictions used in the proof of Theorem 12.2. Choose a whole Cauchy hypersurface $\Sigma_V$ of $V$ through the compared central point, and a disk $D_s$ around its preimage in the inverse-image hypersurface. Decrease the compared point core so that its whole sky meets the interiors of $D_a$ and $D_s$, with the intervening segments retained in the local wave neighborhood. Transversality at the common central point and compactness of the projective real sky provide these buffers.

In the local graph calculus put

$$
\begin{aligned}
L_X^\Sigma
 &=T^M_{\Sigma_M,\Sigma_V}\,
       C_\iota^{D_s}\,
       T^X_{D_s,D_a},\\
K_X^\Sigma
 &=\operatorname{Ad}(L_X^\Sigma)k_X^{D_a},
&F_X^\Sigma&=L_X^\Sigma F_X^{D_a}.
\end{aligned}
$$ {#eq:analytic-global-carrier-factorization}

The first factor is the inverse relative comparison for $V\subset M$, the second is the actual half-density pushforward on $D_s$, and the third is the local carrier comparison. Insert proper cutoffs on nested compact conic interiors before composing.

Corollary 4.6 identifies the restricted global scalar class on $V^2$ with its native local class. Paper 3, Definition 6.9 and Theorem 6.10, give the same local class used by the analytic-sector wave realization; its displaced-carrier formulas are those of Definition 6.23 and Theorem 6.14 of that paper. Theorem 8.3 consequently identifies all three factors with the corresponding native packet comparisons. They preserve the internal adjoint, homogeneous covector normalization, native half-density roots, central specializations and full evaluation. In particular,

$$
L_X^\Sigma e_{D_a}(x)=e_{\Sigma_M}(\iota(x)).
$$ {#eq:analytic-bridge-full-evaluation-transfer}

The carrier factors are independent of the evaluated point on the retained point core. Their action therefore commutes with point differentiation on every algebra and module section, using the same fixed retained cutoffs. The analytic interface itself may use point-dependent presentation coordinates. Define its full fields by

$$
\begin{aligned}
e_X^F
 &=(F_X^\Sigma)^{-1}(e_{\Sigma_M}\circ\iota),\\
\nabla_X^{F,\mathrm{mod}}
 &=(F_X^\Sigma)^{-1}\iota^*\nabla^{\mathrm{amb},M}F_X^\Sigma,\\
\nabla_X^{F,\mathrm{alg}}
 &=(K_X^\Sigma)^{-1}\iota^*\nabla^{\mathrm{alg},M}K_X^\Sigma.
\end{aligned}
$$ {#eq:analytic-bridge-transferred-full-fields}

These identities define the transported fields on every complete section of the enriched real presentation. In a changing gauge $G$, the connection coefficient has the full transformation $B_Y\mapsto GB_YG^{-1}-(YG)G^{-1}$.

The residue-root comparison and the native leading evaluation are natural under the same physical and carrier maps, so the calibration is unchanged by $L_X^\Sigma$. The actual positive pseudodifferential roots used to normalize mixed Cauchy kernels are constructed at their respective endpoints. This argument does not identify those roots by literal conjugation; the root comparison just retained is the native half-density and calibrated relative-root comparison.

The finite-rank diagrams are compared by their canonical metric and actual spin identifications from Proposition 15.5 and §6.3. The initialized finite-rank transports agree because their initial maps and equations agree.

Carrier inverses and changes follow from the localized inverse and cocycle formulas of §8 and Paper 3, Theorem 6.14. A different analytic algebra interface with the same graded map is related by the unique normalized unit of Paper 3, Lemma 7.8; its framed module map is changed by the action of that unit, by Proposition 9.5. These are simultaneous changes of the full fields. Thus the local comparison class is independent of the auxiliary choices. ∎

<div id="sec:analytic-interface-descent"></div>

### 16.2. Root calibration, stored descent and reality

<div id="prop:analytic-calibrated-interface-descent"></div>

**Proposition 16.3 (Descent of calibrated interfaces and stored cells).**

Apply Lemma 16.2 on a real point refinement of the actual whole-sky models of $\mathcal A$. Their interfaces form a compatible system over the entire real point manifold and its full point-labelled incidence. This assertion includes the actual quadratic root factors, whole-family frames, both stored associators, corrected full evaluations and all-section point connections. The system is natural for the actual physical-spin comparisons and their finite diagrams, and retains the original coupled Lorentz operation with its given square cell.

For a fixed global target and physical identification, any two such systems are related by the unique compatible normalized presentation comparison. This uniqueness follows from the calibrated overlap equations.

*Proof.* Write $X_i$ for the local analytic models and $f_{ij}:X_j\to X_i$ for the actual physical comparison on an overlap. Its point map is the identity after the two chart images have been identified with their open subsets of $M$. Its principal spin maps satisfy the strict cocycle in Paper 2, Definition 4.4. The operator representatives have their supplied normalized composition cells. All statements below are made after a common whole-sky sector refinement near the compared point.

First consider the relative root. Let $I_R(f)$ be the actual calibrated original root comparison and $I_g(f)$ the native residue-root comparison. For a local section $b$ of the relative quadratic line, Paper 3, Proposition 9.3, gives

$$
I_A(f)b=I_R(f)\circ b\circ I_g(f)^{-1}.
$$ {#eq:analytic-bridge-quadratic-line-map}

It preserves the quadratic form. The calibrated root comparisons compose with their actual squares, and a normalized comparison cell acts as one on degree zero while carrying the separate framed factor. Therefore $I_A(gf)=I_A(g)I_A(f)$, as proved immediately after that proposition. Proposition 9.4 of the same paper gives

$$
I_A(f_{ij})a_j=a_i.
$$ {#eq:analytic-bridge-initialized-root-cocycle}

The local $a_i$ consequently descend to a nowhere-zero section of the descended real relative quadratic line. The proof uses the actual initialized counits and calibrated root maps. It does not select a sign independently on each chart or infer triviality of a quadratic line from its local square roots. The original complex line, square and comparison maps remain on the analytic side; the assertion concerns their calibrated real descent.

The analytic module comparison carries $\nu_j$ to $\nu_i$ as a factor frame. The native residue and leading evaluation carry $n_{\mathrm W,j}$ to $n_{\mathrm W,i}$. Together with the preceding equation, this makes the two framing prescriptions in [the framing condition](#eq:analytic-global-interface-framing) identical on every overlap. Over a fixed algebra comparison, two module comparisons differ by a nonzero point-parameter scalar: the complete Hom calculation in Paper 3, Lemma 7.9 and Proposition 9.2, gives precisely that residual line. Evaluation on the identical nonzero framed factor makes this scalar exactly one. This is the global overlap mechanism that removes a possible residual Hom-line ambiguity. It applies to the admitted calibrated cocycle; it is not a statement about arbitrary unframed local systems or additional freely chosen two-torsion twists.

Express the target in the native global carrier for the moment. For an original analytic physical representative $(\alpha_{ij},\Xi_{ij})$, the local interfaces satisfy

$$
K_i\alpha_{ij}=\operatorname{Ad}(U_{ij})K_j,
\qquad
F_i\Xi_{ij}=U_{ij}F_j,
$$ {#eq:analytic-global-physical-overlap}

where $U_{ij}$ is the unique normalized internal-adjoint-unitary implementer. The algebra equality follows from the common full homogeneous map and normalized inner rigidity. The module equality is the framed scalar calculation just made. Paper 3, Proposition 9.5, supplies this calculation before the carrier changes, and the coherent carrier factors of Lemma 16.2 preserve it.

If the original composition cell is $D_{ijk}$, so that $\Xi_{ij}\Xi_{jk}=D_{ijk}\Xi_{ik}$, composition of these identities gives

$$
U_{ij}U_{jk}=K_i(D_{ijk})U_{ik}.
$$ {#eq:analytic-global-physical-overlap-cell}

Both sides have the same inner action; normalization makes the implementers equal, and the same unit acts in the module equality. Set $P_{ij}=K_i^{-1}(U_{ij})$ and use the simultaneous corrected representative

$$
\alpha^{\mathrm W}_{ij}
 =\operatorname{Ad}(P_{ij}^{-1})\alpha_{ij},
\qquad
\Xi^{\mathrm W}_{ij}=P_{ij}^{-1}\Xi_{ij}.
$$ {#eq:analytic-global-corrected-physical-overlaps}

Then $K_i\alpha^{\mathrm W}_{ij}=K_j$ and $F_i\Xi^{\mathrm W}_{ij}=F_j$. The original cell equation gives exact composition for these corrected representatives. They carry the transferred full evaluation and intertwine the transported algebra and module connections on every section. The raw representatives and $D_{ijk}$ are retained as the comparison data relating them to this presentation.

There is also an independent operator-chart descent inside and between these whole-sky models. Use a common multi-index for all source and target chart refinements. Write $(\varphi^A_{ij},C^A_{ijk},\tau^A_{ij})$ and $(\varphi^S_{ij},C^S_{ijk},\tau^S_{ij})$ for their raw records. The actual vertices $(k_i,F_i)$ and normalized edge units $b_{ij}$ obey

$$
\begin{aligned}
k_i\varphi^A_{ij}
 &=\operatorname{Ad}(b_{ij})\varphi^S_{ij}k_j,\\
b_{ij}\varphi^S_{ij}(b_{jk})C^S_{ijk}
 &=k_i(C^A_{ijk})b_{ik},\\
F_i\tau^A_{ij}
 &=b_{ij}\tau^S_{ij}F_j.
\end{aligned}
$$ {#eq:analytic-global-three-stored-comparisons}

These are the equations of Paper 2, Definition 4.4, and Paper 3, Proposition 9.2 and Theorem 9.7, transported by the carrier factors. For completeness, in native target coordinates write their edge units as $U^{\Sigma}_{ij}$. If $n_i^S,v_i^S,u_{ij}^S$ are any stored normalization records of the smooth target, the actual representatives are

$$
\begin{aligned}
k_i&=(n_i^S)^{-1}K_i^\Sigma,
&F_i&=(v_i^S)^{-1}F_i^\Sigma,\\
b_{ij}
 &=(n_i^S)^{-1}
       \bigl(U^{\Sigma}_{ij}(u_{ij}^S)^{-1}\bigr).
\end{aligned}
$$ {#eq:analytic-global-stored-target-formula}

Substitution into the two normalization edge identities of Definition 7.1 gives the first and third equations. Expanding a triple and using the source and target descent equations gives the middle equation; normalized-inner uniqueness identifies the resulting implementers. In particular, identity native target cells do not set $C^A_{ijk}$ to one. A changed target presentation $V_i$ transforms these representatives by

$$
k'_i=\operatorname{Ad}(V_i)k_i,
\qquad F'_i=V_iF_i,
\qquad b'_{ij}=V_i b_{ij}\varphi^S_{ij}(V_j^{-1}),
$$ {#eq:analytic-global-interface-presentation-change}

with the full fields transformed at the same time. Both raw associators still occur in the triple identity. The algebra units are determined uniquely, and the factor framing fixes the module scalar. These facts prove the quadruple, inverse, identity and refinement compatibilities. The sheaf comparison equations therefore give one compatible local interface system over all the real point charts. There is no assertion that any particular raw vertex extends outside its original point domain.

The supplied short-ray algebroid comparisons in clause 5 of Paper 2, Definition 4.4, are retained in this system. On a common short-ray presentation the classical comparison is the same homogeneous real null map used in Lemma 16.2; changing its quantization is the normalized comparison just described. A compact real null segment is covered by finitely many such presentations. Their composition and refinement cells compare the corresponding finite chains. Proposition 15.5 identifies the designated real paths with interval-leaf paths, so subdivisions introduce no additional real path class. This verifies compatibility with the supplied real-path descent.

We finally record the coupled operation. Write $J_X,j_X$ for the algebra and module representatives of Lorentz conjugation and $Z_X$ for their normalized square cell. Transport them by the interfaces, using the vertices of the conjugate object $\mathfrak cX$ for the target and the conjugates of the vertices of $X$ for the source:

$$
\widehat J_X=K_{\mathfrak cX}J_X\overline{K_X}^{-1},
\qquad
\widehat j_X=F_{\mathfrak cX}j_X\overline{F_X}^{-1}.
$$ {#eq:analytic-global-coupled-interface}

Let $\kappa_X,j_X^0$ be the coefficient-conjugation maps in compatible native real formal presentations. Here $e_X$ denotes the native target evaluation. Paper 3, Proposition 9.6 and Theorem 9.7, give a unique normalized unit $V_X$ such that

$$
\begin{aligned}
\widehat J_X&=\operatorname{Ad}(V_X)\kappa_X,
&\widehat j_X&=V_Xj_X^0,\\
V_{\mathfrak cX}\kappa_{\mathfrak cX}(\overline{V_X})
 &=K_X(Z_X),
&\widehat j_X(\overline e_X)&=-V_Xe_{\mathfrak cX}.
\end{aligned}
$$ {#eq:analytic-global-coupled-square-and-vector}

The minus sign holds at every complete homogeneous degree. The strict native coefficient conjugation is not a strictification of the original stored weak square: the original $Z_X$ is the right side of the square equation. For a real point vector field $Y$, in fixed native carrier coordinates,

$$
\nabla_Y^{\mathfrak cX}\widehat j_X
 -\widehat j_X\overline{\nabla_Y^X}
 =(YV_X)V_X^{-1}\widehat j_X.
$$ {#eq:analytic-global-coupled-connection-defect}

In other charts $YV_X$ is the corresponding transported covariant derivative. Thus one either retains this defect or transports the target connection by $V_X$ along with the target vector. The odd conjugate marking is $-\overline e$; equivalently $ie$ is a Real full vector for the strict native coefficient conjugation. The original transported weak operation still carries $V_X$ and its square cell. Two applications recover that original square on the original representatives. Formal coefficient conjugation is over the same real ray; physical distributional conjugation reverses frequency and is a different operation.

Every equation restricts on a common point and sector refinement. Uniqueness of its normalized algebra unit and framed module comparison makes the local equations agree there, proving the stated global compatibility and uniqueness of the interface system. Both chiral operations and their original operator coefficients are carried through these simultaneous presentations, as in Paper 3, Theorem 9.7 and Paper 2, Proposition 5.7. ∎

<div id="sec:analytic-wave-global-equivalence"></div>

### 16.3. Global completion, restrictions and families

<div id="thm:global-analytic-wave-comparison"></div>

**Theorem 16.4 (Global comparison on the analytic locus).**

Under the [inputs for the analytic comparison](#sec:analytic-interface-input-contract), with the calibrated local counits and physical comparisons on every admitted model, arrow and causal restriction, every object of $\mathsf{AnOp}^{\mathrm{germ},\mathrm{cc}}_{\mathrm{GH},0}$ has an admitted wave completion. Its completion groupoid is nonempty and has exactly one arrow between any two objects. Choosing these completions gives an equivalence

$$
\mathcal W_\omega:
\mathsf{AnOp}^{\mathrm{germ},\mathrm{cc}}_{\mathrm{GH},0}
\simeq
\mathsf{FullSrc}^{\infty,\mathrm{cc}}_{\mathrm{GH},0;\omega}.
$$ {#eq:global-analytic-wave-equivalence}

The equivalence has both inverse comparisons and their unit and counit triangles. The local interfaces preserve the analytic root and its square, framed base factors, physical and optical scale, both original chiral records, finite-rank diagrams and spin labels. Their comparison cells relate the source and target associators. The smooth target supplies the full evaluation and point connections. Their pullbacks to the enriched analytic presentation intertwine under changes of presentation, on overlaps and along arrows, on every complete section. The interface system carries the coupled operation with the square and derivative law of Proposition 16.3. Original-source atlases and geometric monodromy sources give the same equivalence through Theorem 15.2 and their actual operator comparisons.

*Proof.* Let $M=\mathcal R_\omega\mathcal A$ and take $S=N M$. Sections 3–7 construct its actual global rays and realized affine domains, normalized finite-rank fields and native complete packet. In particular, Theorem 4.4 supplies its unique globally admitted scalar class on $M^2$, and the native source has normalization records over the entire incidence above every one of its global carrier charts. Lemma 16.2 constructs the local calibrated comparisons with the given analytic models, and Proposition 16.3 proves their compatibility with the actual overlap data. Together these give an admitted completion.

Let $(S_0,b_0,\eta^0)$ and $(S_1,b_1,\eta^1)$ be two completions. The global physical-spin map $b_1^{-1}b_0$ has a unique full source lift by Theorem 7.7. On a common real point refinement, compare its composite with $\eta^0$ to $\eta^1$. The two local algebra maps have the same full homogeneous map, hence their quotient has the unique normalized implementer. Their module maps have the same relative root calibration and factor frame, hence the residual scalar is exactly one. These are precisely the compatible comparison cells of Proposition 16.3. Thus the full source lift is the unique arrow of completion groupoids.

For an analytic source embedding $f:\mathcal A\to\mathcal B$, let $f_{\mathbb R}:M\to M'$ be its recognized causal physical-spin embedding. Theorem 9.4 gives its unique full smooth lift between native completions; denote its native scalar graph vertex by $F_f^{\mathrm W}$. We verify that this lift realizes the actual analytic records. On a common source and target point refinement, write $(\alpha_f,\Xi_f)$ for an original analytic representative and $\mathcal J_f=\operatorname{Ad}(F_f^{\mathrm W})$ in native coordinates. The local scalar calculation gives

$$
K_Y\alpha_f=\operatorname{Ad}(U_f)\mathcal J_fK_X,
\qquad
F_Y\Xi_f=U_fF_f^{\mathrm W}F_X.
$$ {#eq:analytic-global-arrow-interface}

The unit $U_f$ is normalized; equality of module scalars follows from the actual root and whole-factor-frame maps. Correcting the analytic representative by $P_f=K_Y^{-1}(U_f)$ gives exact intertwining with $F_f^{\mathrm W}$ and the transported full fields. For composable representatives, with original normalized cell $D_{g,f}$ and final target $Z$, the actual equation is

$$
U_g\mathcal J_g(U_f)=K_Z(D_{g,f})U_{gf}.
$$ {#eq:analytic-global-arrow-composition-cell}

It follows by expanding [the arrow interface identities](#eq:analytic-global-arrow-interface) and normalized-inner uniqueness. The module comparison uses the same unit by framing. The identity, inverse and finite coherence diagrams follow by the same calculation. Hence the native lift defines a functor realizing the supplied analytic comparison class through its calibrated interfaces, not merely a map on the recognized metrics.

Full faithfulness now follows with its record-level meaning. By Theorem 15.2, an analytic source Hom class is determined by, and realizes, exactly its analytic causal physical-spin embedding. By Lemma 15.3 every smooth such embedding between the recognized analytic metrics is analytic, with the specified principal spin lift. Theorem 9.4 identifies the corresponding smooth full Hom set. The local formula just proved shows that this bijection is the one carried by the actual analytic algebra, module and stored comparison vertices.

For essential surjectivity, take an admitted smooth full source $S$ whose recognized metric has a compatible analytic atlas. Lemma 15.3 makes this atlas unique and gives the compatible analytic structure on its actual spin bundle. The existence direction of Theorem 15.2 supplies an analytic source germ $\mathcal A$ along all of $RS$. On the independently admitted models of this source, the pinned local counits and physical comparisons of the interface hypotheses allow Lemma 16.2 and Proposition 16.3 to construct compatible local interfaces. The unique full comparison $NRS\to S$ of §7 gives an admitted completion with the original stored target records. This constructs an inverse object without requiring analytic coefficients in the supplied smooth wave charts.

Choose these inverses and the unique corresponding Hom lifts. The smooth-side counit is the full comparison just constructed, with its actual stored-cell formulas. On the analytic side use the source-germ comparison of Theorem 15.2. On each whole-sky model choose the actual local counit of the pinned bridge input, Paper 1, Theorem 9.10, with its root and frame components. It is this counit that defines $a_X$ in Paper 3, Proposition 9.4. The retained descent equations of Paper 2, Theorem 5.6, compare and glue these local counits to the supplied analytic records, with their specified root maps and framed module components. Applying [the arrow interface identities](#eq:analytic-global-arrow-interface) to these very arrows compares the original operator records and the transferred full fields.

Naturality and both triangles hold on physical maps by the two full Hom statements. At the representative level, [the composition-cell identity](#eq:analytic-global-arrow-composition-cell) and the three stored comparison equations give their normalized cells; calibrated module uniqueness gives their module components. These are the required unit and counit triangles with all the retained records. The same argument compares any two choices of completion and proves the stated uniqueness. ∎

<div id="cor:analytic-wave-causal-restriction"></div>

**Corollary 16.5 (Compatibility with causal restriction).**

For a connected causally convex globally hyperbolic open subset $U\subset M$, there is a canonical full comparison

$$
\mathcal W_\omega(\mathcal A|_U)
\simeq
\operatorname{Res}_U\mathcal W_\omega(\mathcal A).
$$ {#eq:analytic-wave-causal-restriction}

It intertwines the calibrated local interface systems, their roots, frames, both associators, full evaluation and all-section point connections. It is natural for causal embeddings and has the exact nested-restriction coherence in the normalized comparison quotient.

*Proof.* The analytic restriction is the recomputed point restriction of Proposition 15.4. Its complex monodromy is formed anew on the selected complex neighborhood of $U$, and the old action is pulled back by the integrated inclusion.

The two sides recognize to the same physical-spin metric on $U$. Theorem 8.3 identifies their native packets by the relative graph comparison $T_{U,M}$, and Corollary 4.6 identifies their globally admitted kernel classes on all of $U^2$. In native coordinates the local interface relation is

$$
F_X^{\Sigma_U}
=T_{U,M}F_X^{\Sigma_M},
\qquad
K_X^{\Sigma_U}
=\operatorname{Ad}(T_{U,M})K_X^{\Sigma_M},
$$ {#eq:analytic-interface-relative-carrier}

after the simultaneous normalized presentation comparisons already specified. The formulas use localized graph products on the ray domain of $U$. Native residue roots and evaluation frames are transported by this same map, so the relative framing condition remains unchanged. All point derivatives commute with the fixed-carrier action on every complete section.

For nested causal opens, Corollary 8.4 gives the exact carrier cocycle, while Proposition 15.4 gives the analytic recomputed-restriction cocycle. Applying the displayed equations and the three stored comparison identities shows that the two local routes have identical normalized units and framed module maps. They therefore give the same full comparison globally. The same argument with a supplied causal embedding proves naturality. ∎

<div id="prop:analytic-wave-conditioned-families"></div>

**Proposition 16.6 (Conditioned analytic families and finite jets).**

Suppose a coherent holomorphic family of analytic sources is supplied in the sense stated after Paper 2, Theorem 5.6, with the conditioned local operator hypotheses at the start of this section. Restrict its parameters to an admitted real parameter manifold. Suppose its real geometries are identified with a common smooth manifold and satisfy Definition 13.1, with a supplied common spacelike Cauchy hypersurface and actual smoothly identified spin bundles. Then the local calibrated interfaces and the global completions form joint complete smooth families of §13–§14. They commute with admitted physical and parameter restrictions and with finite parameter jets on every retained finite diagram.

On the common conditioned parents of the supplied family, each stipulated finite set of complete coefficients and point and parameter derivatives has a finite bound. The original analytic inputs and their analytic comparisons retain their factorial estimates. The new real wave interfaces and transferred full evaluations are asserted in the complete smooth formal calculus and its joint smoothing quotient. On the wave side a finite parameter jet means the Taylor restriction of this constructed smooth family in its real parameters; no convergence of its Taylor series or holomorphic family of whole Cauchy kernels is asserted.

*Proof.* Choose a compact parameter, point and angular subsystem of one of the supplied finite diagrams. Its analytic hypotheses give a finite buffered cover, controlled coordinate and inverse images, root and frame margins, and the actual holomorphic comparisons and counits. Paper 3, Proposition 9.2, expresses each complete real-sector output coefficient through finitely many input jets and the actual endpoint maps. Its Proposition 9.4 constructs $a_X$ by the initialized square equation; differentiating that equation uses finitely many derivatives of its coefficient and divisions controlled by the retained root margin. The factor-frame normalization divides by the retained nonzero Hom-frame value. Thus these operations have smooth parameter dependence and the stated finite bounds. Their actual analytic construction commutes with finite parameter jets on the supplied diagrams, as in Paper 2, Proposition 5.7.

The common-Cauchy assumption supplies the compact causal parents of Lemma 13.2. Theorems 13.6 and 14.3 provide the joint global scalar class and the relative carrier factors in [the global carrier factorization](#eq:analytic-global-carrier-factorization). Choose their retained conic cutoffs on these parents before the derivative orders are prescribed. Proposition 13.7 and Theorem 14.3 then bound every prescribed phase, amplitude and complete-coefficient derivative with finite input order. Parameter differentiation of an oscillatory representative can raise its order, as in §13; the assertion concerns the stated complete family calculus. All remainders discarded from these family comparisons are jointly smooth.

Composition, inversion and the normalized-unit recursions use only finitely many earlier coefficients at each prescribed depth. The same is true of the differentiated connection gauge law, the square identity and each stored-cell equation. Their finite parameter jets therefore agree on every admitted comparison diagram. The original identities hold before truncation, so their restrictions give identity, composition, inverse and triangle laws at every finite order. Higher output orders change the required finite input seminorms, not the chosen conditioned parents.

On a noncompact real spacetime the comparison systems use local parameter-point charts; each chart retains its own positive buffers. Compact subsystems have finite such covers. No intersection of infinitely many local parameter widths is used. Theorem 13.6 supplies the global joint kernel class, independently of whether the complex source monodromy can be organized as a single smooth global groupoid family.

The point connections differentiate in spacetime. Differentiation in a parameter also differentiates the chosen interface; the finite-jet comparison is made in the supplied conditioned family. ∎

<div id="sec:analytic-smooth-terminal-comparison"></div>

### 16.4. The marked terminal comparison

For the compact connected analytic initial data of §10, we first construct a marked inclusion into the smooth terminal development (Corollary 16.7). Analytic persistence in Appendix A identifies the full point domains through Theorem 16.8. Corollary 16.9 then compares the terminal sources on that common domain.

<div id="cor:analytic-smooth-terminal-source-inclusion"></div>

**Corollary 16.7 (Analytic and smooth marked terminal sources).**

Let $\mathfrak d=(\Sigma,h,K,P_\Sigma)$ be the compact connected analytic vacuum constraint data of Paper 2, Appendix A, at coefficient zero, with its prescribed initial spin identification. Let $\mathcal A^{\max}_\omega$ be its terminal analytic source germ of Paper 2, Corollary 7.5, and let $S^{\max}_\infty$ be its terminal smooth full source of Theorem 10.4. After retaining the initial marking on the wave completion, there is a unique marked full Cauchy embedding

$$
\mathcal W_\omega(\mathcal A^{\max}_\omega)
\longrightarrow S^{\max}_\infty.
$$ {#eq:analytic-smooth-terminal-full-embedding}

Its point map is the canonical open inclusion $M_\omega\subset M_{\mathrm{sm}}$. It identifies all ray labels and retains the inclusion of their realized affine intervals. It is an isomorphism precisely when that point inclusion is onto.

*Proof.* Paper 2, Proposition A.2 and Theorem A.7, supply the analytic maximal development and identify its underlying smooth spacetime with the union of the analytic developments inside the smooth maximal development. The initial hypersurface is Cauchy on both sides. The actual spin inclusion is the unique lift extending the prescribed initial identification, by its Lemma A.6 and the relative spin argument of §10 above.

Lemma 3.5 makes this point inclusion causally convex. Theorem 9.4 therefore gives its unique full source lift. Theorem 16.4 identifies its source with the wave completion of the terminal analytic source, including the calibrated local records, and uniqueness preserves the initial marking. The common Cauchy hypersurface gives the ray identification and affine-domain inclusion by Proposition 3.6 and Proposition 8.6. A full source embedding is an isomorphism exactly when its physical point map is a spin isometry onto the target, proving the final assertion. ∎

<div id="sec:analytic-smooth-marked-development-equivalence"></div>

### 16.5. Analytic and smooth marked developments

Let $\mathfrak d=(\Sigma,h,K,P_\Sigma)$ be the marked vacuum constraint data of Definition 10.1, with $\Sigma$ compact, connected and real analytic and with $h$ and $K$ real analytic. Equip the given spatial spin bundle $P_\Sigma$ with its unique analytic covering structure over the analytic oriented orthonormal frame bundle, obtained by lifting frame charts. Write $\mathsf{Dev}^{\omega}_{\mathrm{geom}}(\mathfrak d)$ and $\mathsf{Dev}^{\infty}_{\mathrm{geom}}(\mathfrak d)$ for the analytic and smooth geometric spin development categories, with the actual initial point and spin markings of Definition 10.1. The analytic category requires its initial embedding and spin identification to be analytic; the smooth category is the geometric development category defined there.

<div id="thm:analytic-smooth-marked-development-equivalence"></div>

**Theorem 16.8 (Analytic and smooth marked development categories).**

Forgetting analyticity gives an equivalence

$$
\mathsf{Dev}^{\omega}_{\mathrm{geom}}(\mathfrak d)
\simeq
\mathsf{Dev}^{\infty}_{\mathrm{geom}}(\mathfrak d).
$$ {#eq:analytic-smooth-marked-development-equivalence}

Its inverse equips a smooth development with the unique analytic metric atlas and spin covering structure of Theorem A.4. Both comparisons preserve the entire point manifold and the actual initial markings. The equivalence is natural under isomorphisms of the analytic constraint data with their specified spatial spin lifts.

*Proof.* Theorem A.4 supplies an analytic structure for every smooth development, with the same metric, point domain, initial embedding and actual spin identification. This proves essential surjectivity. A smooth marked isometric embedding between analytic developments is analytic, and so is its prescribed spin lift, by Lemma 15.3. Its initial marking equations are unchanged. Thus forgetting analyticity is fully faithful.

The unique maximal analytic atlas makes the inverse construction independent of local gauge choices. The same smooth maps give its arrows, with their uniquely determined analytic regularity, so identity and composition are preserved. An isomorphism of the initial data acts by reparametrizing the initial embedding and transporting the prescribed initial spin identification. Neither operation changes the maximal analytic atlas of the developed metric. The resulting comparison functors therefore commute with forgetting analyticity and its inverse. In particular, the classical smooth maximal development, with the actual spin marking of Lemma 10.2, acquires a compatible analytic structure by Theorem A.4. Every marked smooth embedding into it is analytic by Lemma 15.3, so the same object is terminal in the analytic geometric development category. ∎

<div id="cor:analytic-smooth-maximal-source-isomorphism"></div>

**Corollary 16.9 (Compatibility of analytic and smooth maximal sources).**

Under the analytic interface input contract of §16, let $\mathcal A^{\max}_\omega(\mathfrak d)$ and $S^{\max}_\infty(\mathfrak d)$ be the terminal sources of Corollary 16.7. Its canonical marked comparison is an isomorphism

$$
\mathcal W_\omega\bigl(\mathcal A^{\max}_\omega(\mathfrak d)\bigr)
\xrightarrow{\ \sim\ }
S^{\max}_\infty(\mathfrak d).
$$ {#eq:analytic-smooth-maximal-source-isomorphism}

It identifies the entire maximal point domains and their realized affine intervals, and preserves the actual spin maps, both Weyl chiralities, finite-rank fields, complete evaluation and point connections, calibrated roots, module frames and stored associators through the comparisons of Theorem 16.4. It is natural under analytic initial-data isomorphisms with their specified spatial spin lifts.

More generally, the analytic source-germ development categories of Paper 2, Theorem 7.4, at coefficient zero are equivalent to $\mathsf{Dev}_{\mathrm{src}}(\mathfrak d)$. In the operator realization this equivalence is the marked restriction of $\mathcal W_\omega$.

*Proof.* Equip the smooth maximal development $M_{\mathrm{sm}}$ with the analytic structure of Theorem A.4. It is then an analytic development of the prescribed marked data. The analytic terminal property of Paper 2, Theorem A.7, gives an embedding $j:M_{\mathrm{sm}}\to M_\omega$. The existing inclusion of Corollary 16.7 is denoted by $i:M_\omega\to M_{\mathrm{sm}}$. Both preserve the initial point and actual spin markings. Marked geometric uniqueness gives

$$
ij=I_{M_{\mathrm{sm}}},
\qquad
ji=I_{M_\omega}.
$$ {#eq:analytic-smooth-terminal-inverses}

Thus the inclusion is onto. Its full lift in Corollary 16.7 is an isomorphism by Theorem 9.4. The construction is the calibrated comparison of Theorem 16.4, so it retains all the stated structures. Equality of point domains gives equality of the realized intervals, not only a bijection of their ray labels.

For the general category assertion, use Paper 2, Theorem 7.4, for analytic marked source germs, Theorem 16.8 for marked geometric developments, and Corollary 10.5 for smooth marked full sources. On operator presentations, Theorem 16.4 identifies the composite with $\mathcal W_\omega$, including its local root and module comparisons and the two stored associators. Initial-data-preserving embeddings have causally convex images by Lemma 3.5, so they are precisely the admitted arrows needed for these restrictions.

Finally, transport the initial markings by an isomorphism of the data. The two paths in the proposed naturality square are full comparisons over the same marked geometric isometry with the same actual spin lift. The full Hom theorem makes them equal. ∎

<div id="sec:dependencies-and-scope"></div>

## 17. Dependencies and scope of the correspondence

<div id="sec:proof-dependencies"></div>

### 17.1. Proof dependencies

The table lists the local results used in each global construction. The geometric, hyperbolic and maximal-development theorems used alongside them are identified in the respective proofs.

| Conclusion of this paper | Series input used by its proof | Additional dependence or scope |
| --- | --- | --- |
| Global scalar class, whole Cauchy characterization and real null incidence, §2–§4 | The local scalar normal forms and singularity conventions of Paper 3, §6, where invoked; the geometric and global propagation arguments are given here | None from the analytic correspondence or ordinary-pair coverage |
| Native construction, normalized full sources, recognition, full Hom and causal restriction, §5–§9 | Paper 3's full Cartan equations in Theorem 2.9, smooth complete calculus and carrier identities in §6, finite-rank models in Propositions 7.4–7.5, and normalization and rigidity in Definitions 6.23 and 7.7 and Lemmas 7.8–7.10 | The global full Hom theorem uses the evaluation- and connection-compatible normalization records of Definition 7.1 |
| Terminal smooth marked source developments, §10 | The preceding full embedding correspondence, together with the classical smooth maximal-development theorem and the actual initial spin extension | An ordinary-pair presentation of that terminal object additionally uses the coverage input below |
| Effective descent, comparison and completion of a supplied admitted ordinary-pair atlas, §11–§12 | Paper 3's executed ordinary displays in Definition 8.1, Theorems 2.9 and 4.18, scale restoration in Proposition 5.6, and full local comparisons in Theorem 7.11; completion uses the global construction of §§3–9 and the local wave comparisons of Paper 3, §6 | Essential surjectivity for every smooth physical metric adds Paper 3, Theorem 5.7, including its protected extension in Appendix B |
| Joint kernels and full source comparisons for supplied common-Cauchy families, §13–§14 | Paper 3's energy argument in Lemma 2.13, uniform calculus in Lemma 6.4, complete positive normal symbol in Theorem 6.6, and kernel, carrier and point-connection estimates in Propositions 6.11, 6.17 and 6.22; the common causal control and joint propagation are proved here | The hypotheses concern supplied common-Cauchy representatives and joint smoothing classes |
| Completion and comparison of supplied ordinary-pair atlas families, Theorem 14.6 | The preceding family results, Paper 3's execution theorem, common family collars in Theorem 2.14 and full comparison estimates in Proposition 7.12 | Universal family coverage additionally uses Paper 3, Propositions 5.8 and 8.4, with their selected extension branch and common-parent quantifiers |
| Intrinsic scalar and full families on spacetime bundles, Theorems 14.13–14.15 | The preceding common-Cauchy family construction and full Hom theorem, applied in adapted local bundle charts | Local common-Cauchy admission is automatic for compact Cauchy fibers by Proposition 14.12; arbitrary smooth base change uses the joint wavefront condition. Universal ordinary-family coverage retains the separate input above |
| Unmarked analytic source-germ correspondence, §15 | Paper 2's stated local inputs in Propositions 2.1–2.3, its fixed-domain global full Hom theorems, and its complexification and whole-real embedding lemmas | Existence of an analytic source for every analytic metric uses the existence direction of the analytic correspondence |
| Calibrated analytic-to-global-wave comparison, §§16.1–16.4 | The preceding analytic correspondence and Paper 3, Propositions 9.2–9.6 and Theorem 9.7, including the pinned Paper 1 analytic admission and actual counit | Conditioned-family compatibility requires the supplied holomorphic finite diagrams and their bounds; it is not inferred from separate analytic fibers |
| Geometric analytic persistence and marked development equivalence, Theorem A.4 and Theorem 16.8 | No series correspondence input | Compact connected analytic vacuum data. Appendix A constructs the classical analytic Cauchy collar and uses smooth geometric uniqueness, Grauert approximation, local wave energy estimates and Alinhac–Métivier analytic propagation. Lemmas 10.2 and 15.3 handle the actual spin marking and analytic lifts |
| Analytic and smooth terminal source isomorphism, Corollary 16.9 | Paper 2’s marked analytic source correspondence, the smooth full source correspondence, and the calibrated analytic interface recorded above | The geometric equivalence of Theorem 16.8 supplies equality of the maximal point domains; the source inputs supply the comparison preserving the complete records |

The three predecessor manuscripts are used as named, unrefereed inputs in the pinned versions ([Isthmus 2026a](#ref-IsthmusProjective2026); [Isthmus 2026b](#ref-IsthmusGlobal2026); [Isthmus 2026c](#ref-IsthmusSmooth2026)).

The analytic realizations have distinct input requirements within Paper 2. Its independent geometric recognition in Theorem 3.11 uses the whole-sky recognition and physical Hom input of Proposition 2.2. The operator equivalence and incidence modules in Theorems 4.6 and 4.8 additionally use the normalized quantization and framed-module input of Proposition 2.3. The original two-class atlas equivalence in Theorem 5.6 uses the constructor, decoder and actual counit input of Proposition 2.1. Theorem 15.2 retains these requirements when it compares the three whole-real analytic realizations.

<div id="sec:classical-domain-and-further-structures"></div>

### 17.2. Classical domain and further structures

For the two-chirality vacuum correspondence, the smooth ordinary inputs are the local executed pairs of Paper 3, whereas the analytic source atlases retain the original analytic classes and their physical overlap law. Their relationship is the structured correspondence of §16 on the analytic locus. These are different presentations with a proved comparison under the stated inputs; they are not obtained by identifying their initial cohomology classes degree by degree.

The wave class and operator algebras in this correspondence are auxiliary classical source structures. A physical quantum state and its smooth two-point remainder are not source data, and the scalar auxiliary commutator is not an identification of the Einstein gravitational phase space or its quantum commutator. A quantization application would require additional results on gravitational variations, gauge equivalence, the relevant symplectic or Poisson structures, and their compatibility with the source correspondence.

<span class="paper-leadin">**Computational supplement.**</span> The [supplement guide](../computations/README.md) gives exact finite checks for the translated Fourier modes in Example 4.7, the carrier and evaluation identities in Theorems 5.3 and 5.5, and the change of frame in Lemma 16.2. The guide records the inputs, negative controls and limits of each check. The version 1.0 supplement is [smooth-global-twistor-sources-computations-v1.0.zip](https://github.com/lioristhmus/smooth-global-twistor-sources/releases/download/v1.0/smooth-global-twistor-sources-computations-v1.0.zip). The version 1.0 release is available at [https://github.com/lioristhmus/smooth-global-twistor-sources/releases/tag/v1.0](https://github.com/lioristhmus/smooth-global-twistor-sources/releases/tag/v1.0).

On a Kasner torus we compare scalar transport between Cauchy surfaces with axis-mode Hankel solutions. At an off-surface point the evaluation error against Hankel is $2.41\times10^{-8}$, and the covariance residual within the numerical transport is $3.08\times10^{-9}$. Localized frequency tests distinguish the two time branches, and pairings with smooth tests detect the translated singularities of Example 4.7. A final experiment compares three scalar presentations on overlapping Kasner slabs. The [additional supplement guide](../additional-computations/paper4-global-wave-additional-computations-2026-11-24-r2/README.md) accompanies [paper4-global-wave-additional-computations-2026-11-24-r2.zip](https://github.com/lioristhmus/smooth-global-twistor-sources/releases/download/v1.1/paper4-global-wave-additional-computations-2026-11-24-r2.zip).

<div id="sec:googly-literature-scope"></div>

### 17.3. The contribution to the googly programme

The term “googly problem” has been used for distinct mathematical targets. Sharma constructs a twistor action equivalent to Euclidean general relativity at zero cosmological constant, using a partially integrable almost complex twistor geometry ([Sharma 2021](#ref-Sharma2021), Proposition 2). That variational result includes the non-self-dual sector; its boundary conventions and Euclidean setting are part of the comparison. Adamo, Araneda, Seet and Sharma give a Schwarzschild construction and state a more specific solution-generating criterion: data on one twistor space, holomorphic restrictions on those data, and an Einstein metric obtained from the construction without separately solving field equations on twistor space ([Adamo, Araneda, Seet and Sharma 2026](#ref-AdamoAranedaSeetSharma2026), §1). These are the respective authors' formulations and results, not interchangeable definitions.

The present smooth theorem uses the real CR input and Cauchy execution of Paper 3, and its comparison with the analytic source category is Theorem 16.4 under the additional analytic inputs. The construction extends the local smooth records across the globally hyperbolic spacetime by real wave propagation. Its holomorphic input enters at the calibrated comparison of §16.

Noncommutative twistor structures and classical spacetime can coexist. Marcolli and Penrose explicitly study quantized twistor-space constructions that retain a classical underlying spacetime, and distinguish their twistor programme from the ordinary ambitwistor route ([Marcolli and Penrose 2021](#ref-MarcolliPenrose2021), §1.1–§1.2). The auxiliary wave structures used here have that same classical status at the level of the recognized metric.

<div id="sec:compact-analytic-persistence"></div>

## Appendix A. Analytic persistence for compact Cauchy data

Starting with the classical analytic Cauchy collar, we identify a neighborhood of the marked initial surface in the given smooth development. Grauert's finite-order approximation theorem ([Grauert 1958](#ref-Grauert1958), Proposition 8) supplies analytic spacelike surfaces approaching an intermediate Cauchy slice. On these surfaces, finitely many smooth bounds give wave-coordinate neighborhoods of uniform real width. The analytic propagation theorem for nonlinear symmetric hyperbolic systems ([Alinhac and Métivier 1984](#ref-AlinhacMetivier1984), Theorem 1.2.2) carries analyticity across the slice within these neighborhoods, even if the analytic radii of the approaching data shrink.

We use signature $(+---)$ and the convention $K(X,Y)=-g(\nabla_Xn,Y)$ for the future unit normal. All developments and initial hypersurfaces in this appendix are connected. Compact hypersurfaces have no boundary.

<div id="sec:classical-analytic-cauchy-collars"></div>

::: {.paper-block-heading}
**Classical analytic Cauchy collars.**
:::

Let $\mathfrak d=(\Sigma,h,K,P_\Sigma)$ satisfy Definition 10.1, with $\Sigma$ compact and real analytic and with $h$ and $K$ real analytic. The classical analytic Einstein Cauchy problem gives an analytic vacuum collar of these data; see Fourès-Bruhat ([Fourès-Bruhat 1952](#ref-FouresBruhat1952), Chapter IV, §1). We give the Gaussian-coordinate construction, including the passage to a collar of the entire initial hypersurface and its prescribed spin marking.

*Construction.* Seek $g=\mathrm dt^2-h_t$ on $(-\varepsilon,\varepsilon)\times\Sigma$, put $K_t=\tfrac12\partial_t h_t$ and $\tau_t=\operatorname{tr}_{h_t}K_t$, and impose

$$
\partial_t h_t=2K_t,\qquad
\partial_t K_t=-\operatorname{Ric}(h_t)-\tau_tK_t
+2K_th_t^{-1}K_t,
\qquad (h_0,K_0)=(h,K).
$$ {#eq:classical-analytic-gaussian-evolution}

Eliminating $K_t$ gives the second-order system

$$
\partial_t^2h_t=-2\operatorname{Ric}(h_t)
-\tfrac12\operatorname{tr}_{h_t}(\partial_t h_t)\,\partial_t h_t
+(\partial_t h_t)h_t^{-1}(\partial_t h_t),
\qquad h_0=h,\quad \partial_t h_0=2K.
$$ {#eq:classical-analytic-gaussian-ck}

Its right side is analytic in the positive metric, its first derivatives and its spatial derivatives of order two, and contains no second normal derivative. Thus $t=0$ is noncharacteristic for the second-order Cauchy–Kowalevski theorem. It gives a unique analytic germ in each analytic spatial chart. The equations are covariant under time-independent spatial coordinate changes, so uniqueness identifies these germs on overlaps. Choose a finite cover of $\Sigma$ by chart domains whose closures lie inside larger construction charts. Compactness and germ uniqueness allow one common smaller time interval on the closures and their overlaps. The local solutions therefore give an analytic $h_t$ on a product collar. Decreasing $\varepsilon$ makes $h_t$ positive and uniformly comparable with $h$ on the closed smaller collar.

For these conventions the spatial Ricci components are

$$
\operatorname{Ric}(g)_{ij}
=\operatorname{Ric}(h_t)_{ij}+\partial_t(K_t)_{ij}
+\tau_t(K_t)_{ij}-2(K_t)_i{}^q(K_t)_{qj}=0.
$$ {#eq:classical-analytic-spatial-ricci}

Set $H=\operatorname{Ric}(g)_{00}$ and $M_i=\operatorname{Ric}(g)_{0i}$. The Gaussian curvature formulas and the contracted Bianchi identity, with the spatial Ricci components zero, give

$$
\begin{aligned}
H|_{t=0}&=R_h+(\operatorname{tr}_hK)^2-|K|_h^2=0,\\
M_i|_{t=0}&=\nabla^jK_{ij}-\partial_i\operatorname{tr}_hK=0,\\
\partial_tH&=2\nabla^iM_i-2\tau_tH,\\
\partial_tM_i&=\tfrac12\partial_iH-\tau_tM_i.
\end{aligned}
$$ {#eq:classical-analytic-constraint-propagation}

Here the spatial derivatives and contractions at time $t$ use $h_t$. The last two equations are a homogeneous analytic first-order Cauchy system. Uniqueness with the displayed zero initial data gives $H=M_i=0$ after restriction to a smaller collar. Thus $\operatorname{Ric}(g)=0$ and the induced initial data are exactly $(h,K)$.

The coordinate $t$ is temporal, with future normal $\partial_t$. For a causal curve parametrized by $t$, uniform comparison of $h_t$ and $h$ bounds its spatial speed in $h$. If an inextendible causal curve had an endpoint of its $t$ range in the interior of $(-\varepsilon,\varepsilon)$, compactness of $\Sigma$ and that speed bound would give a limit point in the collar, where the curve could be extended. Consequently every inextendible causal curve meets $t=0$ exactly once. The collar is globally hyperbolic with the entire $\Sigma$ as a Cauchy hypersurface.

Use the prescribed orientation and extend the given spatial spin bundle with its actual initial marking by Lemma 10.2. The analytic oriented orthonormal frame bundle supplies analytic charts on this spin covering by local lifting, as in the proof of Lemma 15.3. The lifted group action and initial marking are analytic because their frame maps are analytic and the covering maps are local analytic diffeomorphisms. This produces an analytic marked spin development on the same collar.

<div id="lem:analytic-cauchy-slice-approximation"></div>

**Lemma A.1 (Analytic approximation of intermediate Cauchy hypersurfaces).**

Let $(M,g)$ be a smooth globally hyperbolic spacetime with compact Cauchy hypersurfaces. Let $t:M\to\mathbb R$ be a smooth Cauchy temporal function, and write $S_b=t^{-1}(b)$. Suppose that an open subset $W\subset M$ carries a compatible analytic structure in which $g|_W$ is analytic, and that

$$
t^{-1}((b-\varepsilon,b))\subset W
$$

for some $\varepsilon>0$. For every finite integer $m$, there are compact analytic spacelike Cauchy hypersurfaces $S_n\subset W$ lying in $\{t<b\}$ and converging to $S_b$ in $C^m$, as graphs in a fixed smooth product neighborhood of $S_b$.

*Proof.* Use the temporal splitting to identify a neighborhood of $S_b$ with a product of an interval and a fixed compact three-manifold. Choose $b_n\uparrow b$ and positive $\delta_n\downarrow0$ such that

$$
K_n=t^{-1}([b_n-2\delta_n,b_n+2\delta_n])
\subset t^{-1}((b-\varepsilon,b)).
$$

The sets $K_n$ are compact. Apply Grauert's proposition on the analytic manifold $W$ to the smooth real function $t$. It gives an analytic real function $a_n$ whose difference from $t$ is arbitrarily small in $C^m$ on $K_n$. The proposition states its derivative estimates in analytic coordinate charts. A finite covering of $K_n$ converts them to the fixed smooth product norm. The conversion constants may depend on $n$; the approximation errors can be chosen after these constants and can be arbitrarily small.

Choose those errors so that $\|a_n-t\|_{C^0(K_n)}<\delta_n/2$, $\partial_ta_n>1/2$, and $\|a_n-t\|_{C^m(K_n)}\to0$. For $m<1$, carry out the construction in $C^1$ as well. Since $\mathrm dt$ is uniformly timelike on a fixed compact neighborhood of $S_b$, the approximation can also ensure that $\mathrm da_n$ is timelike with the same time orientation throughout $K_n$.

On each product line, $a_n-b_n$ has opposite signs at $t=b_n-\delta_n$ and $t=b_n+\delta_n$, and is strictly increasing. Its zero set in this band is therefore a single graph

$$
S_n=\{(s_n(x),x):x\in S_b\},
\qquad
\|s_n-b_n\|_{C^m}\longrightarrow0.
$$ {#eq:analytic-cauchy-slice-graphs}

The finite-order implicit-function estimates here use $\partial_ta_n>1/2$. The graph is compact and spacelike. It is an analytic hypersurface in $W$, because it is a regular level of $a_n$.

Every inextendible causal curve in $M$ crosses the lower and upper boundary of the displayed temporal band. Along its intervening segment, $a_n$ is strictly monotone, so it crosses $S_n$ exactly once. Monotonicity of $t$ prevents another visit to that band. Hence $S_n$ is Cauchy in $M$. Since $b_n\to b$, the graphs converge to $S_b$ in $C^m$. ∎

<div id="lem:uniform-local-wave-coordinate-collars"></div>

**Lemma A.2 (Uniform local wave-coordinate collars).**

Let $S_n$ be compact smooth spacelike Cauchy hypersurfaces converging in $C^{12}$, as graphs in a temporal product neighborhood, to a compact smooth spacelike Cauchy hypersurface $S_*\subset(M,g)$, where $g$ is smooth. There are $r,a>0$ such that, for all sufficiently large $n$, one can choose finitely many intrinsic geodesic normal charts $z=(z^1,z^2,z^3)$ on $S_n$, defined on $B_{4r}$, whose $B_r$ images cover $S_n$. The number of charts is independent of $n$. They have local wave coordinates $y=(y^0,y^1,y^2,y^3)$ satisfying

$$
\begin{aligned}
&\Box_g y^\alpha=0,\qquad y^0|_{S_n}=0,
\qquad n_n y^0|_{S_n}=1,\\
&y^i|_{S_n}=z^i,\qquad n_n y^i|_{S_n}=0
\end{aligned}
$$ {#eq:analytic-persistence-wave-coordinate-data}

on $B_{3r}$. Here $n_n$ is the future unit normal. The wave-coordinate images contain a neighborhood of $[-a,a]\times\overline B_{2r}$. The coordinates have uniform real collar widths, uniform bounds for their first two derivatives and inverse first derivatives, and a uniform positive lower bound for $g^{-1}(\mathrm dy^0,\mathrm dy^0)$.

The choices and bounds require only finitely many smooth norms of the hypersurface embeddings and the fixed metric on a compact neighborhood of $S_*$. If the induced metric on $S_n$ is analytic, its intrinsic normal coordinates are analytic on their real chart domains. No uniform complex extension radius is required.

*Proof.* Identify $S_n$ with $S_*$ by their graph projections. The induced Riemannian metrics converge in $C^{11}$ and the second fundamental forms in $C^{10}$. These finite orders suffice to choose common real coordinate domains and to obtain the $C^2$ wave-coordinate bounds from the energy estimates below. Smooth dependence of the Riemannian geodesic equation gives a common real normal-coordinate radius and uniform inverse and finite derivative bounds. Fix $r$ with $4r$ smaller than that radius. Now choose finitely many centers on $S_*$ with a covering margin at radius $r$, and orthonormalize transported frames for the induced metrics on $S_n$. For large $n$, their $B_r$ images cover $S_n$. The radius $r$ is fixed from this point onward. If an induced metric is analytic, analytic dependence of its geodesic equation makes the normal chart analytic on $B_{4r}$.

The normal exponential map of the fixed Lorentz metric gives a tubular neighborhood of the compact hypersurface $S_*$. The normal fields of $S_n$ converge to that of $S_*$, so the corresponding maps, expressed on the fixed product with $S_*$, converge in $C^1$ on a smaller closed collar. Decreasing its width makes all these maps embeddings. In each intrinsic chart they give Gaussian coordinates $(s,z)$ with

$$
g=\mathrm ds^2-h_{n,s},
$$

on fixed smaller cylinders. The coefficient bounds and strict hyperbolicity constants on these cylinders are uniform in $n$.

Construct the scalar wave solutions in the statement by the smooth Cauchy theorem of §2. Give the time coordinate $y^0$ data $(0,1)$ on all of $S_n$. Fix a cutoff $\chi\in C^\infty_c(B_{4r})$ equal to one on $B_{3r}$ in the common chart domains. For each spatial coordinate use data $(\chi z^i,0)$, extended by zero. For the local energy estimate also solve the wave equation with time data $(0,\chi)$.

By the uniform bound on causal coordinate speeds, choose a common time width for which the cylinder over $B_{5r/2}$ lies in the domain of dependence of the initial $B_{3r}$. There the auxiliary time solution equals $y^0$ by Cauchy uniqueness. Since $\operatorname{supp}\chi$ has positive distance from $\partial B_{4r}$, the same speed bound, after shrinking the common width if necessary, keeps the auxiliary and spatial solutions supported inside $B_{4r}$ throughout the estimate. The two coordinate constructions give uniform coefficient bounds through at least order eight on these cylinders. The scalar energy identity, commutation with spatial derivatives and Gronwall’s inequality give the local energy estimate (in the form displayed in Lemma 13.3), hence uniform bounds for the solutions and their first time derivatives in $H^5\oplus H^4$ on smaller cylinders. Their constants depend only on finitely many of the coefficient and data norms already controlled. The wave equation expresses the second time derivative in terms of spatial derivatives of order at most two and lower terms. Sobolev embedding in three space dimensions therefore gives a uniform $C^2$ bound for all four solutions. No parameter differentiability theorem is needed for this sequence of problems.

At $s=0$ the map $(s,z)\mapsto y$ has derivative the identity. Its uniform $C^2$ bound implies

$$
\|\mathrm dy-I\|\le C|s|
$$

on a common cylinder over $B_{5r/2}$. Decrease its time width until the right-hand side is less than $1/2$. On convex coordinate cylinders the resulting lower Lipschitz bound gives injectivity as well as invertibility of the derivative. The value and derivative estimates imply that their images contain a neighborhood of $[-a,a]\times\overline B_{2r}$ for a common smaller $a>0$. Only time widths have been decreased after fixing the covering by $B_r$ balls. The initial timelikeness of $\mathrm dy^0$ and the same finite bounds give its uniform timelike margin. This proves all the assertions. ∎

<div id="lem:analytic-propagation-through-limiting-slice"></div>

**Lemma A.3 (Propagation through a limiting smooth hypersurface).**

Assume in Lemma A.2 that $g$ is Ricci-flat, that each $S_n$ is an analytic hypersurface in an analytic metric region, and that its graph lies strictly below $S_*$ in the temporal product. Then $g$ admits compatible analytic metric charts on an open neighborhood of $S_*$.

*Proof.* Work in one of the wave-coordinate charts supplied by Lemma A.2. Let $h$ and $K$ denote the induced tensors on $S_n$ in its intrinsic analytic coordinates. On the initial coordinate plane $y^0=0$,

$$
g_{00}=1,
\qquad g_{0i}=0,
\qquad g_{ij}=-h_{ij},
\qquad \partial_0g_{ij}=-2K_{ij}.
$$ {#eq:analytic-persistence-initial-metric-data}

The harmonic coordinate identities $g^{\alpha\beta}\Gamma^\mu_{\alpha\beta}=0$ determine the other normal derivatives:

$$
\partial_0g_{00}=2\operatorname{tr}_hK,
\qquad
\partial_0g_{0\ell}
=-h_{\ell i}h^{jk}\Gamma(h)^i_{jk}.
$$ {#eq:analytic-persistence-initial-gauge-data}

Indeed, at the initial plane $\Gamma^0_{ij}=K_{ij}$, $\Gamma^0_{00}=\tfrac12\partial_0g_{00}$, $\Gamma^i_{00}=-h^{ij}\partial_0g_{0j}$ and $\Gamma^i_{jk}=\Gamma(h)^i_{jk}$. Contracting gives the displayed equations. Thus the initial metric and its complete first jet are analytic. This conclusion uses the coordinate Cauchy data and the harmonic identities directly; it does not require analyticity of the newly constructed wave-coordinate map in a previously fixed smooth chart.

For clarity, we give the symmetric hyperbolic reduction to which the analytic propagation theorem applies. Write $u=(g_{\alpha\beta})$ for the ten metric components. In harmonic coordinates the vacuum equations have the form

$$
g^{\mu\nu}\partial_\mu\partial_\nu u
=F(u,\partial u),
$$ {#eq:analytic-persistence-reduced-einstein-equation}

where $F$ is analytic on the open set of nondegenerate metrics. Define

$$
\beta^i=\frac{g^{0i}}{g^{00}},
\qquad
a^{ij}=\beta^i\beta^j-\frac{g^{ij}}{g^{00}},
\qquad
D=\partial_0+\beta^i\partial_i,
\qquad
v=Du,\quad w_i=\partial_i u.
$$ {#eq:analytic-persistence-symmetric-variables}

The matrix $(a^{ij})$ is positive definite because $\mathrm dy^0$ is timelike. The equations for $U=(u,v,w_1,w_2,w_3)$ can be written

$$
\begin{aligned}
Du&=v,\\
Dv-a^{ij}\partial_iw_j&=G(U),\\
a^{ij}(Dw_j-\partial_jv)&=G^i(U).
\end{aligned}
$$ {#eq:analytic-persistence-symmetric-system}

Here $G$ and $G^i$ are analytic: derivatives of $\beta(u)$ are expressed using $\partial_i u=w_i$ and $Du=v$. In matrix form the principal part is $A^0(U)\partial_0+A^i(U)\partial_i$, with symmetric matrices and

$$
A^0=\operatorname{diag}(I,I,(a^{ij})\otimes I)>0.
$$

The only off-diagonal spatial blocks couple $v$ and $w_j$ through the matching entries $-a^{ij}$. Thus this is an analytic symmetric hyperbolic system in the precise sense used by Alinhac and Métivier. The solution is already smooth and solves the full vacuum equations, so no new reduced-solution or constraint-propagation argument is being assumed.

The coordinate and cone bounds from Lemma A.2 give positive constants, independent of $n$ and of the finite chart index, for the smallest eigenvalue of $A^0$ and upper bounds for the spatial matrices. Retain the radii $r,2r$ of that lemma, and choose a small $a_0>0$ below its common time width. Set

$$
\phi(\zeta)=a_0\left(1-\frac{|\zeta|^2}{4r^2}\right),
\qquad
D_n=\{(y^0,y'):y'\in\overline B_{2r},\ 0\le y^0\le\phi(y')\}.
$$ {#eq:analytic-persistence-lens}

Choose $a_0$ so that this lens lies in the common box and

$$
A^0-\mu\sum_i(\partial_i\phi)A^i>0
\qquad (0\le\mu\le1)
$$ {#eq:analytic-persistence-spacelike-sweep}

throughout it. The compact lens is swept from its initial disk by the spacelike hypersurfaces $y^0=\mu\phi(y')$, with their common boundary on $y^0=0$. It is therefore a domain of influence of the form required in Alinhac–Métivier, §1.1(c). Its initial data are analytic on a larger disk by the two initial-jet formulas. Their Theorem 1.2.2 makes $U$, and hence the metric components, analytic in the interior of the lens.

The lenses contain a common positive part of the normal collar. Indeed, in the Gaussian coordinates $(s,z)$ used to construct a wave chart, the initial data and uniform $C^2$ bound give

$$
\tfrac12s\le y^0(s,z)\le2s,
\qquad
|y'(s,z)-z|\le Cs^2
\qquad (s>0)
$$

after a common shrinking. For $|z|<r$ and $0<s<c$, choose $c>0$ so that $Cc^2<r/2$ and $2c<a_0/4$. Then $|y'|<3r/2$ and $\phi(y')\ge7a_0/16$, so the point is in the lens interior. The number $c$ is independent of $n$ and of the finite chart index. The smaller normal balls cover $S_n$.

Since the hypersurfaces converge as graphs from the past, $S_*$ lies in this positive normal collar for all sufficiently large $n$. Its positive normal coordinates tend uniformly to zero: the tubular maps and their inverses converge, and a point of $S_*$ is in $I^+(S_n)$ by the temporal product lines. Hence every point of $S_*$ lies in one of the lens interiors. Finitely many charts cover $S_*$ and supply analytic metric charts on an open neighborhood of it.

On overlaps, including overlaps with the former analytic region, the transition is a smooth local isometry between analytic metric expressions. Lemma 15.3 makes it analytic. The charts are consequently compatible. ∎

<div id="thm:compact-analytic-vacuum-persistence"></div>

**Theorem A.4 (Analytic persistence on a smooth development).**

Let $\mathfrak d=(\Sigma,h,K,P_\Sigma)$ be the marked vacuum constraint data of Definition 10.1, with $\Sigma$ compact, connected and real analytic, $h$ and $K$ real analytic, and the given $P_\Sigma$ equipped with its analytic frame-covering structure. Every smooth globally hyperbolic vacuum development $(M,g,\iota,P)$ of these data has a unique compatible maximal real analytic atlas in which the metric and initial embedding are analytic. Its given principal spin bundle has the unique compatible analytic covering structure, and the prescribed initial spin identification is analytic.

*Proof.* The [classical analytic Cauchy construction above](#sec:classical-analytic-cauchy-collars) gives an analytic marked vacuum collar of the data. Smooth geometric uniqueness identifies a neighborhood of its initial hypersurface with a neighborhood of $\iota(\Sigma)$ in the given development: embed both developments in their common smooth maximal development and restrict to the intersection of their open images ([Sbierski 2016](#ref-Sbierski2016), Theorem 2.8). Lemma 10.2 supplies the unique compatible spin comparison with the prescribed initial marking. Push forward the analytic collar atlas. Thus $g$ is analytic in some compatible atlas on a neighborhood of the entire initial hypersurface.

Let $\mathcal O\subset M$ be the set of points admitting a neighborhood with an analytic metric atlas compatible with the smooth structure. It is open. Lemma 15.3 makes all such atlases compatible on intersections, so $\mathcal O$ has one maximal analytic atlas and $g|_{\mathcal O}$ is analytic.

Choose a smooth Cauchy temporal function $t$ with $\iota(\Sigma)=t^{-1}(0)$, using Bernal–Sánchez ([Bernal and Sánchez 2006](#ref-BernalSanchez2006), Theorem 1.2). Its temporal splitting identifies $M$ with $\mathbb R\times\Sigma$; every closed finite time slab is compact. The initial analytic neighborhood therefore contains a slab $t^{-1}([-\delta,\delta])$ for some $\delta>0$.

Suppose that

$$
T=\sup\{b\ge0:t^{-1}([0,b])\subset\mathcal O\}
$$ {#eq:analytic-persistence-first-slice}

is finite. It is positive, and $t^{-1}([0,T))\subset\mathcal O$. Lemma A.1, with $m=12$, supplies analytic spacelike Cauchy hypersurfaces $S_n\subset\mathcal O$ approaching $t^{-1}(T)$ from its past in $C^{12}$. Lemmas A.2 and A.3 put $t^{-1}(T)$ in $\mathcal O$. Compactness of this hypersurface and openness of $\mathcal O$ give an additional time band beyond $T$ contained in $\mathcal O$. Together with the already admitted earlier slab this contradicts the definition of $T$.

Hence every nonnegative time slab is analytic. The same argument with reversed time proves the assertion on negative time slabs, so $\mathcal O=M$. The proof uses the nonlinear analytic propagation theorem on uniformly controlled real wave-coordinate domains. It does not require a lower bound for the analytic radius of the intermediate data.

The maximal analytic atlas is unique by Lemma 15.3. The local smooth isometry from the analytic Cauchy collar is analytic for this atlas, again by that lemma; consequently $\iota$ is analytic with its prescribed initial analytic structure. The orthonormal frame bundle is now analytic. Lift its charts through the given principal spin covering to obtain its unique analytic covering structure. The group action and the prescribed initial identification are analytic by local lifting of their analytic frame maps, since the spin covering is locally an analytic diffeomorphism. The initial marking fixes the lift as in Lemma 10.2, preserving the original principal spin bundle and its central sign. ∎

<div id="rem:compact-analytic-persistence-scope"></div>

**Remark A.5 (Scope of persistence).**

Analyticity is relative to the compatible atlas on the interior of the given smooth development. The proof uses compactness to approximate an entire intermediate Cauchy hypersurface and cross it in finitely many uniform coordinate domains. The local analytic radii can shrink near a maximal boundary; the argument gives no such crossing theorem for noncompact initial data.

<div id="sec:ai-and-tool-use-disclosure"></div>

## AI and tool use disclosure

AI systems were used extensively throughout this research and the preparation of this manuscript. The models used were GPT-6 Pro, gpt-6.2-astra (high), Claude Fable 5.2 (xhigh), Claude Opus 5.5 (xhigh), and Gemini 4 Carbon (high). We used Python for the exact finite checks and for numerical experiments on wave propagation and transport. The computational supplements document the software versions, execution environments, and reproduction steps.

<div id="sec:references"></div>

## References

<div id="ref-AdamoAranedaSeetSharma2026"></div>

Tim Adamo, Bernardo Araneda, Sean Seet and Atul Sharma (2026). *Schwarzschild black holes from twistor space*. Preprint, [arXiv:2607.06236v2](https://arxiv.org/abs/2607.06236v2), 30 September 2026.

<div id="ref-AlinhacMetivier1984"></div>

Serge Alinhac and Guy Métivier (1984). “Propagation de l’analyticité des solutions de systèmes hyperboliques non-linéaires.” *Inventiones Mathematicae* **75**, 189–204. [DOI](https://doi.org/10.1007/BF01388563). The analytic system theorem is Theorem 1.2.2, with domains of influence defined in §1.1(c).

<div id="ref-BarGinouxPfaeffle2007"></div>

Christian Bär, Nicolas Ginoux and Frank Pfäffle (2007). *Wave Equations on Lorentzian Manifolds and Quantization*. ESI Lectures in Mathematics and Physics, European Mathematical Society, 2007. [DOI](https://doi.org/10.4171/037) and [author version](https://arxiv.org/abs/0806.1036v1).

<div id="ref-BarStrohmaier2019"></div>

Christian Bär and Alexander Strohmaier (2019). “An index theorem for Lorentzian manifolds with compact spacelike Cauchy boundary.” *American Journal of Mathematics* **141**(5), 1421–1455. [DOI](https://doi.org/10.1353/ajm.2019.0037) and [author version](https://arxiv.org/abs/1506.00959v3). The cited Appendix A and Theorem A.1 are in arXiv:1506.00959v3.

<div id="ref-BernalSanchez2005"></div>

Antonio N. Bernal and Miguel Sánchez (2005). “Smoothness of time functions and the metric splitting of globally hyperbolic spacetimes.” *Communications in Mathematical Physics* **257**, 43–50. [DOI](https://doi.org/10.1007/s00220-005-1346-1) and [author text, arXiv:gr-qc/0401112v3](https://arxiv.org/abs/gr-qc/0401112v3).

<div id="ref-BernalSanchez2006"></div>

Antonio N. Bernal and Miguel Sánchez (2006). “Further results on the smoothability of Cauchy hypersurfaces and Cauchy time functions.” *Letters in Mathematical Physics* **77**, 183–197. [DOI](https://doi.org/10.1007/s11005-006-0091-5); [author version, arXiv:gr-qc/0512095v1](https://arxiv.org/abs/gr-qc/0512095v1). Theorem 1.2 gives a Cauchy temporal function adapted to a prescribed spacelike Cauchy hypersurface.

<div id="ref-BrunettiFredenhagenVerch2003"></div>

Romeo Brunetti, Klaus Fredenhagen and Rainer Verch (2003). “The Generally Covariant Locality Principle – A New Paradigm for Local Quantum Field Theory.” *Communications in Mathematical Physics* **237**, 31–68. [DOI](https://doi.org/10.1007/s00220-003-0815-7); [author version, arXiv:math-ph/0112041v1](https://arxiv.org/abs/math-ph/0112041v1). Definition 2.1 and Theorem 2.2 refer to this author version.

<div id="ref-BudicIsenbergLindblomYasskin1978"></div>

Robert Budic, James Isenberg, Lee Lindblom and Philip B. Yasskin (1978). “On the Determination of Cauchy Surfaces from Intrinsic Properties.” *Communications in Mathematical Physics* **61**, 87–95. [DOI](https://doi.org/10.1007/BF01609469); [author-hosted article](https://ccom.ucsd.edu/~lindblom/Publications/10_CommMathPhys.61.87.pdf). Theorem 1 is used in its smooth embedded form.

<div id="ref-ChernovNemirovski2018"></div>

Vladimir Chernov and Stefan Nemirovski (2018). “Redshift and contact forms.” *Journal of Geometry and Physics* **123**, 379–384. [DOI](https://doi.org/10.1016/j.geomphys.2017.09.017); [author version, arXiv:1709.01741v1](https://arxiv.org/abs/1709.01741v1).

<div id="ref-ChernovRudyak2008"></div>

Vladimir V. Chernov (Tchernov) and Yuli B. Rudyak (2008). “Linking and Causality in Globally Hyperbolic Space-times.” *Communications in Mathematical Physics* **279**, 309–354. [DOI](https://doi.org/10.1007/s00220-008-0414-8); [author version, arXiv:math/0611111v3](https://arxiv.org/abs/math/0611111v3).

<div id="ref-ChoquetBruhatGeroch1969"></div>

Yvonne Choquet-Bruhat and Robert Geroch (1969). “Global aspects of the Cauchy problem in general relativity.” *Communications in Mathematical Physics* **14**, 329–335. [DOI](https://doi.org/10.1007/BF01645389).

<div id="ref-Duistermaat1972"></div>

J. J. Duistermaat (1972). “Applications of Fourier integral operators.” *Séminaire Goulaouic–Schwartz* (1971–1972), Exposé XXVII, 1–24. [Primary text](https://www.numdam.org/article/SEDP_1971-1972____A27_0.pdf); [errata](https://www.numdam.org/item/SEDP_1971-1972____A33_0.pdf).

<div id="ref-FouresBruhat1952"></div>

Yvonne Fourès-Bruhat (1952). “Théorème d’existence pour certains systèmes d’équations aux dérivées partielles non linéaires.” *Acta Mathematica* **88**, 141–225. [DOI](https://doi.org/10.1007/BF02392131); [original article](https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/5764-11511_2006_Article_BF02392131.pdf). Chapter IV, §1 records analytic vacuum Cauchy existence and geometric uniqueness.

<div id="ref-FullingNarcowichWald1981"></div>

S. A. Fulling, F. J. Narcowich and R. M. Wald (1981). “Singularity structure of the two-point function in quantum field theory in curved spacetime, II.” *Annals of Physics* **136**(2), 243–272. [DOI](https://doi.org/10.1016/0003-4916(81)90098-1).

<div id="ref-GerardWrochna2014"></div>

Christian Gérard and Michał Wrochna (2014). “Construction of Hadamard states by pseudo-differential calculus.” *Communications in Mathematical Physics* **325**, 713–755. [DOI](https://doi.org/10.1007/s00220-013-1824-9) and [arXiv:1209.2604v4](https://arxiv.org/abs/1209.2604v4).

<div id="ref-Grauert1958"></div>

Hans Grauert (1958). “On Levi’s Problem and the Imbedding of Real-Analytic Manifolds.” *Annals of Mathematics* **68**(2), 460–472. [DOI](https://doi.org/10.2307/1970257); [original article](https://www.math.ens.psl.eu/~benoist/refs/Grauert.pdf). Proposition 8, p. 471, supplies approximation in any prescribed finite differentiability order.

<div id="ref-IsthmusProjective2026"></div>

Lior Isthmus (2026a). *A projective twistor correspondence for local analytic Einstein germs*. Unrefereed preprint, [Hexagon 2611.00123v2](https://hexagonmath.org/2611.00123v2); [manuscript version 1.1](https://doi.org/10.5281/zenodo.24197319), dated 13 November 2026. [Archived manuscript source](https://github.com/lioristhmus/projective-twistor-einstein-germs/blob/f866c0e88025753273d3a51cb80947cb9ccdd181/release/paper-v1.1/manuscript.md), commit `f866c0e88025753273d3a51cb80947cb9ccdd181`.

<div id="ref-IsthmusGlobal2026"></div>

Lior Isthmus (2026b). *Global twistor sources for analytic Einstein spacetimes*. Unrefereed preprint, [Hexagon 2611.00425v2](https://hexagonmath.org/2611.00425v2), posted 15 November 2026; [manuscript version 1.0.1](https://doi.org/10.5281/zenodo.24239028), dated 13 November 2026. [Archived manuscript source](https://github.com/lioristhmus/global-twistor-sources/blob/cac46b4ee6c551d2ebf9401a5a73b3e37230ac6e/paper/manuscript.md), commit `cac46b4ee6c551d2ebf9401a5a73b3e37230ac6e`.

<div id="ref-IsthmusSmooth2026"></div>

Lior Isthmus (2026c). *A two-chirality twistor correspondence for smooth Lorentzian Ricci-flat germs*. Unrefereed preprint, [Hexagon 2611.00698v2](https://hexagonmath.org/2611.00698v2), posted 20 November 2026; [manuscript version 1.0](https://doi.org/10.5281/zenodo.24385872), dated 19 November 2026. [Archived manuscript source](https://github.com/lioristhmus/smooth-twistor-germs/blob/5e3c45910dc3441386e81a171ef74330f2217b5f/paper/smooth-twistor-germs-en-v1.0.md), commit `5e3c45910dc3441386e81a171ef74330f2217b5f`. The v2 posting updates the bibliography format.

<div id="ref-MarcolliPenrose2021"></div>

Matilde Marcolli and Roger Penrose (2021). “Gluing Non-commutative Twistor Spaces.” *The Quarterly Journal of Mathematics* **72**(1–2), 417–454. [DOI](https://doi.org/10.1093/qmath/haab024); [author repository](https://authors.library.caltech.edu/records/a1a3t-zxy51); [author text, arXiv:2012.02823v1](https://arxiv.org/abs/2012.02823v1).

<div id="ref-Minguzzi2019"></div>

Ettore Minguzzi (2019). “Lorentzian causality theory.” *Living Reviews in Relativity* **22**, article 3. [DOI and publisher text](https://doi.org/10.1007/s41114-019-0019-x); [published text](https://s3.cern.ch/inspire-prod-files-7/7a575d682fd15aaad8463a778fac1609).

<div id="ref-Penrose2015"></div>

Roger Penrose (2015). “Palatial twistor theory and the twistor googly problem.” *Philosophical Transactions of the Royal Society A* **373**(2047), article 20140237. [DOI](https://doi.org/10.1098/rsta.2014.0237); [PubMed abstract](https://pubmed.ncbi.nlm.nih.gov/26124255/). The abstract states the interacting opposite-helicity target within the same twistor conventions and the proposed role of holomorphic differential operators.

<div id="ref-RadzikowskiVerch1996"></div>

Marek J. Radzikowski (1996), with an appendix by Rainer Verch. “A local-to-global singularity theorem for quantum field theory on curved space-time.” *Communications in Mathematical Physics* **180**, 1–22. [DOI and publisher text](https://doi.org/10.1007/BF02101180).

<div id="ref-Sbierski2016"></div>

Jan Sbierski (2016). “On the Existence of a Maximal Cauchy Development for the Einstein Equations: A Dezornification.” *Annales Henri Poincaré* **17**(2), 301–329. [Accepted author manuscript, arXiv:1309.7591v3](https://arxiv.org/abs/1309.7591v3); [DOI](https://doi.org/10.1007/s00023-015-0401-5). The theorem numbering refers to this accepted author manuscript.

<div id="ref-Sharma2021"></div>

Atul Sharma (2021). *Twistor action for general relativity*. Preprint, [arXiv:2104.07031v2](https://arxiv.org/abs/2104.07031v2), 28 July 2021. Proposition 2 and the discussion give the Euclidean zero-cosmological-constant action comparison, with the stated boundary conventions.

<div id="ref-Strohmaier2026"></div>

Alexander Strohmaier (2026). *Microlocal properties of Cauchy evolution under metric variations*. Preprint, [arXiv:2611.12488v1](https://arxiv.org/abs/2611.12488v1), 9 November 2026.

<div id="ref-WhitneyBruhat1959"></div>

Hassler Whitney and François Bruhat (1959). “Quelques propriétés fondamentales des ensembles analytiques-réels.” *Commentarii Mathematici Helvetici* **33**, 132–160. [Primary text](https://www.math.ens.psl.eu/~benoist/refs/WhitneyBruhat.pdf); [DOI](https://doi.org/10.1007/BF02565913).
