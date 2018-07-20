# caesar-cipher
Encrypt, decrypt or brute-force a Caesar cipher

***

### Example

```python
import caesar

print('encrypted text: {}'.format(caesar.encrypt('python', 9)))
print('decrypted text: {}'.format(caesar.decrypt('yhcqxw', 9)))

print('brute force candidates:\n')
for i, e in enumerate(caesar.brute_force('QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD')):
    print('{}: {}'.format(i, ''.join(e)))

```
