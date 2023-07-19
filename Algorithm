l# Algorithm
'''
### Notations
### A_b - price of the best bid in the order book (Sberbank)
### A_s - price of the best ask in the order book (Sberbank)
### B_b - price of the best bid in the order book (Sberbank-P)
### B_s - price of the best ask in the order book (Sberbank-P)
### All A and B are counted at the current moment (at moments of opening and closing)
### K_A_b - commission on buying Sberbank
### K_B_b - commission on buying Sberbank-P
### S - average spread (at market price)
### m - a parameter greater than zero (it should be:))

#
#
# 1) If A-B>0, S =(A-B)/2
# A) When the spread is larger than average
### If (A_s-B_b)-m1-S -  2*(K_A_b +K_B_b)>0 then:
###     Sell Sberbank
###     Buy Sberbank-P
### Close positions when (A_b-B_s)-m2 <= S - K_A_b - K_B_b
# B) When the spread is less than average
###  If (A_b-B_s)+ 2*(K_A_b + K_B_b)+m3-S<0 then:
###     Buy Sberbank
###     Sell Sberbank-P
### Close positions when (A_s-B_b) +m4 > S + K_A_b + K_B_b

#
#
# 2) If A-B<0, S=(B-A)/2
# A) When the spread is less than average
### If A_b-B_s+m5 + 2*(K_A_b + K_B_b)+S<0 then:
###     Buy Sberbank
###     Sell Sberbank-P
### Close positions when (A_s-B_b) + m6 > S + K_A_b + K_B_b
# B) When the spread is larger than average
###  If A_s-B_b-m7 - 2*(K_A_b + K_B_b)-S>0 then:
###     Sell Sberbank
###     Buy Sberbank-P
### Close positions when (A_b-B_s) - m8 <= S - K_A_b - K_B_b
'''
