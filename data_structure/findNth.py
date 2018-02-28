def partition(seq):
    pi, seq = seq[0], seq[1:]                   # Pick and remove the pivot
    lo = [x for x in seq if x <= pi]            # All the small elements
    hi = [x for x in seq if x > pi]             # All the large ones
    return lo, pi, hi                           # pi is "in the right place"

def select(seq, k):
    lo, pi, hi = partition(seq)                 # [<= pi], pi, [> pi]
    m = len(lo)
    if m == k: return pi                        # We found the kth smallest
    elif m < k:                                 # Too far to the left
        return select(hi, k-m-1)                # Remember to adjust k
    else:                                       # Too far to the right
        return select(lo, k)                    # Just use original k here

seq = [3, 4, 1, 6, 3, 7, 9, 13, 93, 0, 100, 1, 2, 2, 3, 3, 2]
print partition(seq) #([1, 3, 0, 1, 2, 2, 3, 3, 2], 3, [4, 6, 7, 9, 13, 93, 100])
print select([5, 3, 2, 7, 1], 3) #5
print select([5, 3, 2, 7, 1], 4) #7
ans = [select(seq, k) for k in range(len(seq))]
seq.sort()
print ans == seq #True

