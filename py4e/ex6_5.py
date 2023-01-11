text = "X-DSPAM-Confidence:    0.8475"
pos0=text.find('0')
print(float(text[pos0:]))
