class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        MAX_HAND = 1000
        count = [0] * (MAX_HAND + 1)
        for card in hand:
            count[card] += 1
        
        groups_closed_at = [0] * (MAX_HAND + groupSize)
        currently_open_groups = 0
        for i in range(0, MAX_HAND + 1):
            print(count[i])
            print(currently_open_groups)
            if count[i] < currently_open_groups:
                return False
            
            newly_opened_groups = count[i] - currently_open_groups
            groups_closed_at[i + groupSize - 1] = newly_opened_groups
            currently_open_groups = currently_open_groups + newly_opened_groups - groups_closed_at[i]
        
        return True

        
        
        