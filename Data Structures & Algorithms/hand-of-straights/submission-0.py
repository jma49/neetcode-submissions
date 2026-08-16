class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = Counter(hand)
        if len(hand) % groupSize != 0:
            return False
        # key: num / value: freq
        for start in sorted(count):
            if count[start] == 0:
                continue 
            need = count[start]
            for card in range(start, start + groupSize):
                if count[card] < need:
                    return False
                count[card] -= need
        return True


