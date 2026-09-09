# RT-BBN-001 — Lithium-7 Surrogate Retest

**Scientific status:** theoretical candidate; historical toy calculation; not cosmology validation.

## Preserved historical claim

A surrogate calculation used a baseline abundance of (5.38\times10^{-10}) and a suppression factor (e^{-1.23}\approx0.292), yielding approximately (1.57\times10^{-10}).

The original integral did not independently reproduce (\Xi_\gamma=1.23). A corrected (q_\gamma) was therefore required. That correction is part of the failure history, not a validated derivation.

## Frozen retest requirements

1. Recover the exact original source, code, constants, and output.
2. Reproduce the historical result without silently repairing it.
3. Record the failing integral and corrected branch separately.
4. Derive or explicitly parameterize (\Xi_\gamma); do not fit it after observing the target.
5. Integrate through a recognized BBN solver such as AlterBBN.
6. Compare lithium and all other predicted abundances with accepted observational datasets.
7. Reject the candidate if improvement in lithium damages other abundances beyond preregistered tolerances.
8. Preserve numerical failures, nulls, sensitivity results, and competing explanations.

## Current blockers

Original executable and raw output are not yet in this repository. Full AlterBBN integration, Standard-Model reduction, tensor/operator derivation, and a first-principles (\Xi_\gamma) derivation are absent.
