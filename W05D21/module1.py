
def freq(test_str):
    all_freq = {}
  
    for i in test_str:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1
    return all_freq
    print(all_freq)