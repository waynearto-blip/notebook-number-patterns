#!/usr/bin/env python3
"""
Generate number groups similar to the notebook pattern.

Each section:
- Choose a target sum S
- Generate 3 groups of 3 positive integers that each sum to S
- Compute total = 3 * S
- Show successive doublings of the total

Also supports auditing cumulative sums against a target (e.g. 6185).
"""

import random
from typing import List, Tuple, Dict


def generate_group(target_sum: int) -> Tuple[int, int, int]:
    """Generate three positive integers that sum to target_sum."""
    if target_sum < 3:
        raise ValueError("target_sum must be at least 3")
    
    # Pick two random positive integers, the third is determined
    a = random.randint(1, target_sum - 2)
    b = random.randint(1, target_sum - a - 1)
    c = target_sum - a - b
    # Shuffle so order is random
    nums = [a, b, c]
    random.shuffle(nums)
    return tuple(nums)


def generate_section(target_sum: int, label: str = "") -> Dict:
    """Generate one section of the pattern."""
    groups = [generate_group(target_sum) for _ in range(3)]
    total = 3 * target_sum
    doublings = [total]
    for _ in range(3):  # three successive doublings, matching the notebook style
        doublings.append(doublings[-1] * 2)
    
    return {
        "label": label,
        "target_sum": target_sum,
        "groups": groups,
        "total": total,
        "doublings": doublings,
    }


def section_sum(section: Dict) -> int:
    """Sum of all numbers displayed in a section (groups + doublings)."""
    group_sum = sum(sum(g) for g in section["groups"])
    doubling_sum = sum(section["doublings"])
    return group_sum + doubling_sum


def print_section(section: Dict) -> None:
    """Pretty-print a section in a style similar to the notebook."""
    label = section["label"]
    if label:
        print(f"{label}")
    
    for g in section["groups"]:
        print(f"  {g[0]:3d} {g[1]:3d} {g[2]:3d}    {section['target_sum']}")
    
    d = section["doublings"]
    print(f"           {d[0]:4d} {d[1]:4d} {d[2]:4d} {d[3]:4d}")
    print()


def audit_sections(sections: List[Dict], target: int = 6185) -> None:
    """Audit the cumulative sum of all generated numbers against a target."""
    cumulative = 0
    print("=" * 50)
    print(f"AUDIT against target {target}")
    print("=" * 50)
    
    for i, section in enumerate(sections, 1):
        s = section_sum(section)
        cumulative += s
        label = section["label"] or f"section {i}"
        print(f"{label:10s}  section sum: {s:6d}   cumulative: {cumulative:7d}")
    
    diff = cumulative - target
    print("-" * 50)
    print(f"Grand total of all numbers: {cumulative}")
    print(f"Target:                     {target}")
    print(f"Difference (total - target): {diff:+d}")
    if diff == 0:
        print("✓ Exact match")
    elif abs(diff) < 100:
        print("~ Close match")
    else:
        print("✗ Not matching — adjust target sums or number of sections")
    print()


def main():
    random.seed()  # use system time for randomness
    
    # Example sections matching the notebook style
    examples = [
        (15, ""),
        (12, "to9"),
        (24, "to17"),
        (48, "to24"),
    ]
    
    print("Generated number groups (notebook style)\n")
    print("=" * 50)
    
    sections = []
    for target, label in examples:
        section = generate_section(target, label)
        sections.append(section)
        print_section(section)
    
    # Custom examples
    print("=" * 50)
    print("Custom generation examples:\n")
    
    for s in [10, 20, 30, 36]:
        section = generate_section(s, f"sum={s}")
        sections.append(section)
        print_section(section)
    
    # Audit all generated numbers against 6185
    audit_sections(sections, target=6185)


if __name__ == "__main__":
    main()
