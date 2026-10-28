# Notebook Number Patterns

Generator for notebook-style number groups: three groups of three positive integers that each sum to a target S, followed by the 3× total and three successive doublings.

Also includes cumulative audit against targets such as **6185**.

## Quick start

```bash
python3 generate_notebook_numbers.py
```

## Pattern structure

Each section produces:

- 3 groups × 3 numbers, each group summing to S
- Total = 3 × S
- Doublings: total, 2×, 4×, 8×

Section sum used for audit = sum of all group numbers + sum of the four doubling values.

## 6185 vs 6192 vs 6195

Sample cumulative audit (one random run):

| Section     | Section sum | Cumulative |
|-------------|-------------|------------|
| (15)        | 720         | 720        |
| to9 (12)    | 576         | 1296       |
| to17 (24)   | 1152        | 2448       |
| to24 (48)   | 2304        | 4752       |
| sum=10      | 480         | 5232       |
| **sum=20**  | **960**     | **6192**   |
| sum=30      | 1440        | 7632       |
| sum=36      | 1728        | 9360       |

- **6192** appears immediately after introducing the `sum=20` section.
- **6185** is 7 below that cumulative.
- **6195** is 3 above the same cumulative (and 10 above 6185).

### What the 20 introduced

Adding the `sum=20` section contributes a fixed section sum of 960 (independent of the random group values, because group sums are constrained to 3×20 = 60 and the doublings are determined by the total).

Before it: cumulative ≈ 5232  
After it: cumulative ≈ 6192  

The jump of +960 moves the running total from well below the audit band into the narrow window containing 6185, 6192 and 6195. In that sense the introduction of 20 is the step that first makes the audit targets reachable; without it the cumulative stays at 5232.

Because the section sum itself is deterministic for a given S, the only variability comes from which earlier sections are included. Adjusting or omitting the `sum=20` section (or changing an earlier S) is the practical lever for landing exactly on 6185 rather than 6192 or 6195.

## Continuing the pattern

The same structure can be extended with further target sums. The audit function accepts any target, so new sections can be added and the cumulative re-checked against 6185, 6192, 6195 or other reference values.

## License

MIT (or use as you wish).
