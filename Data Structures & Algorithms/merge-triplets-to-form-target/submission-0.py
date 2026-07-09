class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        validTriplets = set()
        ta, tb, tc = target[0], target[1], target[2]
        numValid = 0
        for a, b, c in triplets:
            if a > ta or b > tb or c > tc:
                continue
            elif a == ta or b ==  tb or c == tc:
                validTriplets.add((a, b, c))
                numValid += 1
        
        while numValid > 1:
            if tuple(target) in validTriplets:
                return True
            triplet1, triplet2 = validTriplets.pop(), validTriplets.pop()
            newTriplet = (max(triplet1[0], triplet2[0]), max(triplet1[1], triplet2[1]), max(triplet1[2], triplet2[2]))
            validTriplets.add(newTriplet)    
            numValid -= 1
        
        if tuple(target) in validTriplets:
            return True
        return False

