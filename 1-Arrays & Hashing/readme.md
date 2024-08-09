# Arrays & Hashing

## Arrays

Arrays are a fundamental data structure in programming and are used to store multiple values in a single variable , that collects elements of the same data type and stores them in contiguous and adjacent memory locations. Arrays work on an index system starting from 0 to (n-1), where n is the size of the array.

There are basically two types of arrays:

**Static Array:**

A static array is an array whose memory is allocated at compile time, and it has a fixed size. This means that the size of a static array cannot be altered or updated after it has been declared. Static arrays are simple to use and have a predictable memory usage, but their fixed size can be a limitation.

```c

int arr[10]; // max size is 10

```

**Dynamic Array:**

A dynamic array, on the other hand, is an array whose size can be changed during runtime. This allows for greater flexibility as the array can grow or shrink as needed. Dynamic arrays are implemented using pointers and dynamic memory allocation functions such as malloc, calloc, and realloc in C.

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int *arr;
    int size;
    int capacity; 
} Array;

Array* initArray(int capacity) {
    Array *newArray = malloc(sizeof(Array));
    newArray->arr = malloc(sizeof(int) * capacity);
    newArray->size = 0;
    newArray->capacity = capacity;
    return newArray;
}

void addElement(Array *myArray, int element) {
    if (myArray->size == myArray->capacity) {
        myArray->capacity *= 2;
        myArray->arr = realloc(myArray->arr, sizeof(int) * myArray->capacity);
    }
    myArray->arr[myArray->size] = element;
    myArray->size++;
}

int main() {
    Array *example_array = initArray(20);
	   
    addElement(example_array, 10);
    addElement(example_array, 20);
    addElement(example_array, 30);
    printf("Elements of the array: ");
    for (int i = 0; i < example_array->size; i++) {
        printf("%d ", example_array->arr[i]);
    }
    printf("\n");
    return 0;
}

```

## Hash Table and Hashing

A hash table is a data structure that efficiently inserts, looks up, and removes key-value pairs. It uses a hash function to translate each key into a distinct array index, where the corresponding value is stored, effectively mapping keys to values.

### Types of Hash Functions

**Division Method:**
- **Formula:** `h(K) = K mod M`  
  Where `K` is the key value, and `M` is the size of the hash table.
- **Example:**
  - For a hash table of size `M=10` and a key value of `K=75`, the hash value is calculated as `h(K) = 75 mod 10 = 5`. Thus, the key `75` would be stored at index `5` of the hash table.
- **Advantages:**
  - Effective for all values of `M`.
  - Requires only one operation, making it quick.
- **Disadvantages:**
  - Consecutive keys might result in successive hash values, leading to poor performance.

**Mid-Square Method:**
- This method squares the key value and then extracts the middle digits of the result to use as the hash value.
- **Example:**
  - For a key value of `K=1234`, squaring it results in `1522756`. Extracting the middle digits (e.g., `227`) gives the hash value. So, the key `1234` would be stored at index `227` of the hash table.
- **Advantages:**
  - Produces a random distribution of keys, reducing clustering.
- **Disadvantages:**
  - Hash value quality depends on the key choice.
  - Requires more computational resources due to the squaring operation.

**Multiplication Method:**
- **Formula:** `h(K) = ⌊M × ((K × A) mod 1)⌋`  
  Where `K` is the key, `A` is a constant (0 < A < 1), `M` is the hash table size, and `⌊⋅⌋` denotes the floor function.
- **Example:**
  - For `K=42`, `A=0.6180339887`, and `M=10`:
    1. Multiply `K` by `A`: `42 × 0.6180339887 = 25.9380253514`.
    2. Extract the fractional part: `0.9380253514`.
    3. Multiply by `M`: `0.9380253514 × 10 = 9.380253514`.
    4. Apply the floor function: `⌊9.380253514⌋ = 9`.
  - The key `42` would be stored at index `9`.
- **Advantages:**
  - Wide Distribution of Keys: Provides a good spread of keys across the table.
  - Less Sensitive to Table Size: Less dependent on the choice of table size `M`, making it easier to select without detailed key analysis.
- **Disadvantages:**
  - Computational Complexity: More complex to compute compared to simpler methods.
  - Dependence on Constant A: The effectiveness of the hash function depends on the choice of the constant `A`.


**Folding Method:**
- The folding method breaks the key into smaller parts, adds these parts together, and then applies a modulo operation with the hash table size.
- **Example:**
  - For a key `123456`, divide it into two parts: `123` and `456`. Sum them: `123 + 456 = 579`. Apply modulo with the hash table size `M=10`: `579 mod 10 = 9`.

**Cryptographic Hash Function:**
- Cryptographic hash functions produce a fixed-size output (hash) that looks random but is deterministic for a given input. They're used in cryptography for secure hashing.

### Collision Resolution Techniques

When two keys hash to the same index, a collision occurs. Various methods can handle these collisions:

#### Open Addressing (Closed Hashing)

**Linear Probing:**
- **Example:**
  - Given a hash table of size `M=10` and the hash function `h(K) = K mod 10`, inserting keys `27`, `18`, `29`, `28`, `39`, `13`, `16`:
    - After inserting `27`, `18`, and `29`, the table looks like:

      ```plaintext
      Index: 0 1 2 3 4 5 6 7  8  9
      Keys:  - - - - - - - 27 18 29
      ```

    - Attempting to insert `28` (which hashes to index `8`) results in a collision. Linear probing finds the next available slot (starting at index `9`, wrapping around to index `0`), and inserts `28` at index `0`:

      ```plaintext
      Index: 0  1 2 3 4 5 6 7  8  9
      Keys:  28 - - - - - - 27 18 29
      ```

- **Disadvantages:**
  - **Clustering:** contiguous blocks of occupied slots slow down insertion and lookup.
  - It can take longer to find an empty slot.

**Quadratic Probing:**
- **Example:**
  - Hash function `h(K) = K mod 10`, inserting keys `20`, `12`, `22`, `32`, `42`:
    1. `h(20) = 20 mod 10 = 0`: Insert `20` at index `0`.
    2. `h(12) = 12 mod 10 = 2`: Insert `12` at index `2`.
    3. `h(22) = 22 mod 10 = 2`: Collision! Quadratic probing checks `2 + 1^2 = 3`, index `3` is empty, insert `22`.
    4. `h(32) = 32 mod 10 = 2`: Collision! Quadratic probing checks `2 + 2^2 = 6`, index `6` is empty, insert `32`.
    5. `h(42) = 42 mod 10 = 2`: Collision! Quadratic probing checks `2 + 3^2 = 1`, insert `42` at index `1`.
  - Resulting hash table:

    ```plaintext
    Index:  0   1   2   3   4   5   6   7   8   9
    Keys:  20  42  12  22  -   -  32   -   -   -
    ```

#### Separate Chaining (Open Hashing)

In this technique, each index in the hash table contains a linked list of elements. Colliding elements are added to the list, allowing multiple elements to hash to the same index without conflict.

```python 

class MyHashTable:
    def __init__(self, size=10):
        self.size = size
        self.arr = [None for _ in range(self.size)] 

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.size

    def __getitem__(self, key):
        hash = self.get_hash(key)
        return self.arr[hash]

    def __setitem__(self, key , value):
        hash = self.get_hash(key)
        if self.arr[hash] is None:
            self.arr[hash] = value
        else : 
            # Linear probing 
            new_hash = self.get_hash(key) + 1
            new_hash = new_hash % self.size 
            while self.arr[new_hash] is not None:
                new_hash += 1
                new_hash = new_hash % self.size
            self.arr[new_hash] = value
            # Quadratic probing
            new_hash = self.get_hash(key)
            i = 1
            while self.arr[new_hash] is not None:
                new_hash = self.get_hash(key) + i**2
                i += 1
                new_hash = new_hash % self.size
            self.arr[new_hash] = value

    def __delitem__(self, key):
        hash = self.get_hash(key)
        self.arr[hash] = None

def main():
    ht = MyHashTable()
    ht["march 6"] = 120
    ht["march 20"] = 230
    ht["march 17"] = 20
    ht["march 26"] = 200
    ht["march 35"] = 2907
    ht["march 44"] = 2024
    print(ht.arr)

if __name__ == "__main__":
    main()


```