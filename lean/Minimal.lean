/-
FreeNumKernel / Minimal.lean
Free Numbers Lean minimal kernel v0.2-pre.2

Scope:
  - restricted rewriting core only
  - no mathlib dependency intended
  - pure transport declared but excluded from Red

Axiom and deferred component list for v0.2-pre.2.

A1. LocalMul
    Abstract local multiplication relation.
    Intended later replacement:
      concrete multiplication table for local quaternionic closure.

A2. ExistingBoundary
    Abstract relation indicating that a generated boundary can fold
    into an existing normalized boundary.

A3. FreshBoundary
    Abstract relation indicating that a generated boundary cannot fold
    into an existing boundary and must be retained as normGen.

A4. PureMove
    Abstract admissible transport relation.
    Declared in v0.2-pre.2 but excluded from Red.
    It will be restored only after adding either:
      - transportCost, or
      - TransportNormal, or
      - a preprocessing relation separate from Red.

A5. BoundaryIso
    Deferred boundary isomorphism relation.

A6. ResidualPurity
    Deferred residual purity criterion.

A7. EqAdm
    Deferred admissible equivalence relation.

A8. WeakConfluence
    Deferred weak confluence modulo EqAdm.

A9. EffectiveMagProjection
    Deferred admissible, non-constant, residual-sensitive projection.

A10. TransportNormalizedReduction
     Deferred restoration of admissible transport into reduction.

The restricted kernel proves only:
  Red X Y -> weight Y < weight X

This establishes termination for the restricted Gen-normalization core,
not for the full admissible transport system.
-/

namespace FreeNumKernel

/-- Chart identifier.
Provisional Nat representation.

Important:
  this minimal kernel uses Nat only as a syntactic chart label.
  It does not yet enforce chart distinctness, disjoint-copy semantics,
  or boundary isomorphism at the kernel level.
  These are deferred to later versions.
-/
abbrev Chart := Nat

/-- Local element identifier. Provisional Nat representation. -/
abbrev LocalId := Nat

/-- Generated chart boundary. -/
structure Boundary where
  leftChart  : Chart
  leftId     : LocalId
  rightChart : Chart
  rightId    : LocalId
deriving Repr, DecidableEq

/-- Local element inside a chart. -/
structure LocalElem where
  chart : Chart
  id    : LocalId
deriving Repr, DecidableEq

/--
Finite generated terms.

atom    : local element
mul     : syntactic product; global associativity is not assumed
star    : conjugation / return operation
gen     : unresolved generated chart boundary
normGen : normalized generated chart boundary
-/
inductive Term where
  | atom    : LocalElem -> Term
  | mul     : Term -> Term -> Term
  | star    : Term -> Term
  | gen     : Boundary -> Term
  | normGen : Boundary -> Term
deriving Repr, DecidableEq

/-- Count open, unresolved generated chart nodes. -/
def openGenCount : Term -> Nat
  | Term.atom _       => 0
  | Term.mul t1 t2    => openGenCount t1 + openGenCount t2
  | Term.star t       => openGenCount t
  | Term.gen _        => 1
  | Term.normGen _    => 0

/-- Syntactic tree size. -/
def termSize : Term -> Nat
  | Term.atom _       => 1
  | Term.mul t1 t2    => 1 + termSize t1 + termSize t2
  | Term.star t       => 1 + termSize t
  | Term.gen _        => 1
  | Term.normGen _    => 1

/-- Restricted termination weight.

The paper uses the same repeated-addition form:

  openGenCount t + openGenCount t + termSize t

This is mathematically equal to:

  2 * openGenCount t + termSize t

but the repeated-addition form is used here to keep the restricted
Nat expression syntactically minimal.
-/
def weight (t : Term) : Nat :=
  openGenCount t + openGenCount t + termSize t

/-- Abstract local multiplication relation. -/
axiom LocalMul : LocalElem -> LocalElem -> LocalElem -> Prop

/-- Abstract admissible transport, declared but excluded from Red in v0.2-pre.2. -/
axiom PureMove : LocalElem -> LocalElem -> LocalElem -> Prop

/-- Abstract relation for folding a generated boundary into an existing boundary. -/
axiom ExistingBoundary : Boundary -> Boundary -> Prop

/-- Abstract relation for retaining a fresh generated boundary as normalized. -/
axiom FreshBoundary : Boundary -> Prop

/--
Restricted one-step reduction.

G1_local:
  local atom multiplication

G3_existing:
  generated boundary folds into an existing normalized boundary

G4_mark:
  fresh generated boundary is retained as normalized

Pure transport is intentionally excluded from Red in v0.2-pre.2.
-/
inductive Red : Term -> Term -> Prop where
  | G1_local {x y z : LocalElem} :
      LocalMul x y z ->
      Red
        (Term.mul (Term.atom x) (Term.atom y))
        (Term.atom z)

  | G3_existing {B B' : Boundary} :
      ExistingBoundary B B' ->
      Red
        (Term.gen B)
        (Term.normGen B')

  | G4_mark {B : Boundary} :
      FreshBoundary B ->
      Red
        (Term.gen B)
        (Term.normGen B)

/-- Red seen in the decreasing direction for well-founded recursion. -/
def RedRel : Term -> Term -> Prop :=
  fun Y X => Red X Y

/-- Reflexive-transitive closure of Red. -/
inductive RedStar : Term -> Term -> Prop where
  | refl {X : Term} :
      RedStar X X

  | step {X Y Z : Term} :
      Red X Y ->
      RedStar Y Z ->
      RedStar X Z

/-- A normal form is a term with no outgoing Red step. -/
def NormalForm (X : Term) : Prop :=
  Not (Exists (fun Y : Term => Red X Y))

/-- N is a normal form reached from X. -/
def IsNFOf (X N : Term) : Prop :=
  RedStar X N ∧ NormalForm N

/-- Existing-boundary fold decreases open generated nodes. -/
theorem red_G3_decreases
  {B B' : Boundary} (_h : ExistingBoundary B B') :
  openGenCount (Term.normGen B') < openGenCount (Term.gen B) := by
  simp [openGenCount]

/-- Fresh-boundary normalization decreases open generated nodes. -/
theorem red_G4_decreases
  {B : Boundary} (_h : FreshBoundary B) :
  openGenCount (Term.normGen B) < openGenCount (Term.gen B) := by
  simp [openGenCount]

/-- Restricted Red never increases open generated nodes. -/
theorem red_openGen_noninc
  {X Y : Term} (h : Red X Y) :
  openGenCount Y <= openGenCount X := by
  cases h <;> simp [openGenCount]

/-- Restricted Red strictly decreases the termination weight. -/
theorem red_weight_decreases
  {X Y : Term} (h : Red X Y) :
  weight Y < weight X := by
  cases h <;> simp [weight, openGenCount, termSize]

/-- Same decrease expressed in the RedRel direction. -/
theorem redRel_weight_decreases
  {X Y : Term} (h : RedRel Y X) :
  weight Y < weight X := by
  exact red_weight_decreases h

end FreeNumKernel
