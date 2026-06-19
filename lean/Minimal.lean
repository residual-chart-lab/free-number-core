/-
FreeNumKernel / Minimal.lean
Free Numbers Lean minimal kernel v0.2-pre

Scope:
  - restricted rewriting core only
  - no mathlib dependency intended
  - pure transport declared but excluded from Red
-/

namespace FreeNumKernel

abbrev Chart := Nat
abbrev LocalId := Nat

structure Boundary where
  leftChart  : Chart
  leftId     : LocalId
  rightChart : Chart
  rightId    : LocalId
deriving Repr, DecidableEq

structure LocalElem where
  chart : Chart
  id    : LocalId
deriving Repr, DecidableEq

inductive Term where
  | atom    : LocalElem -> Term
  | mul     : Term -> Term -> Term
  | star    : Term -> Term
  | gen     : Boundary -> Term
  | normGen : Boundary -> Term
deriving Repr, DecidableEq

def openGenCount : Term -> Nat
  | Term.atom _       => 0
  | Term.mul t1 t2    => openGenCount t1 + openGenCount t2
  | Term.star t       => openGenCount t
  | Term.gen _        => 1
  | Term.normGen _    => 0

def termSize : Term -> Nat
  | Term.atom _       => 1
  | Term.mul t1 t2    => 1 + termSize t1 + termSize t2
  | Term.star t       => 1 + termSize t
  | Term.gen _        => 1
  | Term.normGen _    => 1

def weight (t : Term) : Nat :=
  openGenCount t + openGenCount t + termSize t

axiom LocalMul : LocalElem -> LocalElem -> LocalElem -> Prop
axiom PureMove : LocalElem -> LocalElem -> LocalElem -> Prop
axiom ExistingBoundary : Boundary -> Boundary -> Prop
axiom FreshBoundary : Boundary -> Prop

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

def RedRel : Term -> Term -> Prop :=
  fun Y X => Red X Y

inductive RedStar : Term -> Term -> Prop where
  | refl {X : Term} :
      RedStar X X

  | step {X Y Z : Term} :
      Red X Y ->
      RedStar Y Z ->
      RedStar X Z

def NormalForm (X : Term) : Prop :=
  Not (Exists (fun Y : Term => Red X Y))

def IsNFOf (X N : Term) : Prop :=
  RedStar X N /\ NormalForm N

theorem red_G3_decreases
  {B B' : Boundary} (_h : ExistingBoundary B B') :
  openGenCount (Term.normGen B') < openGenCount (Term.gen B) := by
  simp [openGenCount]

theorem red_G4_decreases
  {B : Boundary} (_h : FreshBoundary B) :
  openGenCount (Term.normGen B) < openGenCount (Term.gen B) := by
  simp [openGenCount]

theorem red_openGen_noninc
  {X Y : Term} (h : Red X Y) :
  openGenCount Y <= openGenCount X := by
  cases h <;> simp [openGenCount]

theorem red_weight_decreases
  {X Y : Term} (h : Red X Y) :
  weight Y < weight X := by
  cases h <;> simp [weight, openGenCount, termSize]

theorem redRel_weight_decreases
  {X Y : Term} (h : RedRel Y X) :
  weight Y < weight X := by
  unfold RedRel at h
  exact red_weight_decreases h

end FreeNumKernel
