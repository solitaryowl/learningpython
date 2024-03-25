import math

"""
Basic Operations:
1. Peek
2. Insert
3. Pop
4. Delete
5. Replace 
"""

heap = None


def peek(heap):
    if size(heap) == 0:
        print("EMPTY")
        return None
    else:
        print(heap[0])
        return heap[0]


def insert(heap, key):
    print("Inserting:" + str(key))
    heap.append(key)
    heapify_up(heap)
    print(heap)


def heapify_down(heap, curr_ind=0):
    size = len(heap)
    leftchild = 2 * curr_ind + 1
    rightchild = leftchild + 1
    largest = curr_ind

    if leftchild < len(heap) and heap[leftchild] > heap[largest]:
        largest = leftchild

    if rightchild < len(heap) and heap[rightchild] > heap[largest]:
        largest = rightchild

    if not largest == curr_ind:
        print("heapify_down:" + str(heap))

        swap(heap, largest, curr_ind)
        heapify_down(heap, largest)


def pop(heap):
    if isempty(heap):
        return None
    if len(heap) > 1:
        swap(heap, 0, len(heap) - 1)
    head = heap.pop(len(heap) - 1)
    heapify_down(heap)
    print("Popped:" + str(head) + " : after : " + str(heap))
    return head


def delete(heap):
    print()


def replace(heap, key):
    print()


"""
Creation Operations:
1. CreateEmpty
2. Heapify
3. Merge
4. Meld
"""


def createempty():
    return []


def swap(heap, x, y):
    z = heap[x]
    heap[x] = heap[y]
    heap[y] = z


"""
As We Always Insert At the End, we ll need to perform sift-up to maintain heap property
"""


def heapify_up(heap):
    print()
    last_ind = len(heap) - 1

    while math.floor((last_ind - 1) / 2) >= 0:

        parent_ind = math.floor((last_ind - 1) / 2)
        if heap[parent_ind] < heap[last_ind]:
            swap(heap, parent_ind, last_ind)
            last_ind = parent_ind
        else:
            break


"""
Inspection Operations:
1. Size
2. IsEmpty
"""


def size(heap):
    print("Length:" + str(len(heap)))


def isempty(heap):
    return len(heap) == 0


if __name__ == "__main__":
    heap = createempty()
    insert(heap, 15)
    insert(heap, 17)
    insert(heap, 11)
    insert(heap, 8)
    insert(heap, 29)
    insert(heap, 22)
    insert(heap, 3)
    insert(heap, 13)
    insert(heap, 24)
    insert(heap, 10)
    insert(heap, 26)
    print(str(heap))
    while not isempty(heap):
        pop(heap)
