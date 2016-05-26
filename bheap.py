def cmp_lt(x, y):
    # Use __lt__ if available; otherwise, try __le__.
    # In Py3.x, only __lt__ will be called.
    return (x < y) if hasattr(x, '__lt__') else (not y <= x)


def heappush(heap, item, heapmap):
    """Push item onto heap, maintaining the heap invariant."""
    heap.append(item)
    heapmap[item] = len(heap)
    _siftdown(heap, 0, len(heap)-1, heapmap)


def heappop(heap, heapmap):
    """Pop the smallest item off the heap, maintaining the heap invariant."""
    lastelt = heap.pop()    # raises appropriate IndexError if heap is empty
    if heap:
        returnitem = heap[0]

        heapmap.pop(returnitem)

        heap[0] = lastelt

        heapmap[lastelt] = 0

        _siftup(heap, 0, heapmap)
    else:
        returnitem = lastelt
    return returnitem


def _siftdown(heap, startpos, pos, heapmap):
    newitem = heap[pos]
    # Follow the path to the root, moving parents down until finding a place
    # newitem fits.
    while pos > startpos:
        parentpos = (pos - 1) >> 1
        parent = heap[parentpos]
        if cmp_lt(newitem, parent):
            heap[pos] = parent

            heapmap[parent] = pos

            pos = parentpos
            continue
        break
    heap[pos] = newitem

    heapmap[newitem] = pos


def _siftup(heap, pos, heapmap):
    endpos = len(heap)
    startpos = pos
    newitem = heap[pos]
    # Bubble up the smaller child until hitting a leaf.
    childpos = 2*pos + 1    # leftmost child position
    while childpos < endpos:
        # Set childpos to index of smaller child.
        rightpos = childpos + 1
        if rightpos < endpos and not cmp_lt(heap[childpos], heap[rightpos]):
            childpos = rightpos
        # Move the smaller child up.
        heap[pos] = heap[childpos]

        heapmap[heap[childpos]] = pos

        pos = childpos
        childpos = 2*pos + 1
    # The leaf at pos is empty now.  Put newitem there, and bubble it up
    # to its final resting place (by sifting its parents down).
    heap[pos] = newitem

    heapmap[newitem] = pos

    _siftdown(heap, startpos, pos, heapmap)


def heapreplace(heap, old, new, heapmap):
    index = heapmap[old]
    heap[index] = new
    heapmap.pop(old)
    heapmap[new] = index
    _siftdown(heap, 0, index, heapmap)