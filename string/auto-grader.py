text = "X-DSPAM-Confidence:    0.8475 "

fin = text.find("0.8475")

result = text[fin-1:]

word = float(result)

print(word)

x = 'From marquard@uct.ac.za'
print(x[14:17])