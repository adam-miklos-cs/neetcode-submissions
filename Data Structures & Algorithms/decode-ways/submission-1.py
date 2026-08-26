class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        
        d_before = '0'
        count_single = 1
        count_double = 1

        for d in s:
            count = 0

            single = (d != '0')

            double = (
                d_before == '1' or
                (d_before == '2' and d <= '6')
            )

            if single:
                count += count_single
            if double:
                count += count_double
            if not single and not double:
                return 0

            count_double, count_single = count_single, count
            d_before = d

        return count
            


            

                    

