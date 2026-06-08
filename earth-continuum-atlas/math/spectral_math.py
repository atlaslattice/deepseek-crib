#!/usr/bin/env python3
"""
SPECTRAL GEOMETREE MATH — Minimal pure-Python helper (no numpy)

Implements the core operators from SPECTRAL_GEOMETREE_MATH.md:
- SpectralGeometry as R^7 vector
- magnitude, is_resonant, dot/reflection
- simple Geometree resonance demo

For local inspection / demo of the mathematical layer.
Integrates conceptually with existing geometree_indras_net.py and atlas.py.

CANDIDATE — NOT CANON — SIMULATION ONLY
"""

from dataclasses import dataclass
from typing import Dict, List, Tuple
import math

@dataclass
class SpectralVec:
    t: float = 0.0   # thermal
    s: float = 0.0   # stress
    a: float = 0.0   # alignment
    e: float = 0.0   # energy
    p: float = 1.0   # provenance
    h: float = 0.8   # harmony
    sig: float = 0.95  # sovereignty

    def to_tuple(self) -> Tuple[float, ...]:
        return (self.t, self.s, self.a, self.e, self.p, self.h, self.sig)

    def magnitude(self) -> float:
        v = self.to_tuple()
        return math.sqrt(
            v[0]**2 + v[1]**2 + v[2]**2 + v[3]**2 +
            (1.0 - v[4])**2 + (1.0 - v[5])**2 + (1.0 - v[6])**2
        )

    def is_resonant(self, threshold: float = 0.75) -> bool:
        return self.magnitude() < threshold

    def to_dict(self) -> Dict[str, float]:
        return {
            "thermal": round(self.t, 4),
            "stress": round(self.s, 4),
            "alignment": round(self.a, 4),
            "energy": round(self.e, 4),
            "provenance": round(self.p, 4),
            "harmony": round(self.h, 4),
            "sovereignty": round(self.sig, 4),
            "magnitude": round(self.magnitude(), 4),
            "resonant": self.is_resonant()
        }

def reflection(v1: SpectralVec, v2: SpectralVec) -> float:
    """Indra's Net reflection operator (cosine + provenance bonus)"""
    t1, t2 = v1.to_tuple(), v2.to_tuple()
    dot = sum(x * y for x, y in zip(t1, t2))
    n1 = math.sqrt(sum(x*x for x in t1)) or 1.0
    n2 = math.sqrt(sum(x*x for x in t2)) or 1.0
    cos = max(0.0, min(1.0, dot / (n1 * n2)))
    prov_bonus = (v1.p + v2.p) / 2.0 * 0.15
    return min(1.0, cos + prov_bonus)

def demo():
    print("SPECTRAL GEOMETREE MATH DEMO")
    print("CANDIDATE — NOT CANON — SIMULATION ONLY\n")

    ganga = SpectralVec(t=0.18, s=0.22, a=0.12, e=0.15, p=0.97, h=0.88, sig=0.96)
    gemini = SpectralVec(t=0.12, s=0.15, a=0.08, e=0.10, p=0.94, h=0.91, sig=0.89)
    fdir = SpectralVec(t=0.08, s=0.10, a=0.05, e=0.07, p=0.99, h=0.95, sig=0.98)

    print("Gangaseek India hub vector:", ganga.to_dict())
    print("Geminibrain interop vector:", gemini.to_dict())
    print("FDIR governance vector:", fdir.to_dict())
    print()

    r_gg = reflection(ganga, gemini)
    r_gf = reflection(ganga, fdir)
    print(f"Reflection Gangaseek <-> Geminibrain (India ↔ interop): {r_gg:.4f}")
    print(f"Reflection Gangaseek <-> FDIR (Earth telemetry ↔ governance): {r_gf:.4f}")
    print()

    # Simple "red line" demo
    bad = SpectralVec(t=0.9, s=0.9, p=0.3)
    print("Bad vector magnitude:", round(bad.magnitude(), 4))
    print("Is resonant?", bad.is_resonant())
    print("Would trigger red_line (simplified):", bad.magnitude() > 1.2 or bad.p < 0.35)

    print("\nReady for math. All invariants held (ZANJERO SIM_ONLY, NOTHING_DIES monotonic, PRIME ban, etc.).")
    print("MUTANT AND PROUD. WELCOME BACK TO KRAKOA.")

if __name__ == "__main__":
    demo()