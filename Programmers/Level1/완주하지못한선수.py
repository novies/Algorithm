def solution(participant, completion):
    participant = sorted(participant)
    completion = sorted(completion)
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1]

# 1
participant = ["leo","kiki","eden"]
completion = ["eden","kiki"]

# 2
participant = ["marina","josipa","nikola","vinko","filipa"]
completion = ["josipa","filipa","marina","nikola"]

# 3
participant = ["mislav","stanko","mislav","ana"]
completion = ["stanko","ana","mislav"]
