################################
### Author: Devin Hunt
### Created: June 8, 2025
### DS510 Assignment 2 Part A
### Description: This program calculates compounded interest.
### Inputs: P = Pricipal investment amount
###         APR = Annual percentage rate in %
###         T = time in years
###         N = number of periods per year (1, 4, or 12)
### Output: Interest table displaying the final total investment amount on a single deposit
### References: Sample Code from Dr. Loren Rhodes for right alignment of text
##################################

### Ask user for inputs as noted above

P = float(input("Enter the inital balance to invest: "))
APR = float(input("Enter the Anual Percentage Rate (APR) as percentage: "))
T = float(input("Enter the number of years to invest: "))
N = int(input("Enter the number of compounding periods per year: "))

# Convert APR to decimal
APR_dec = APR/100

# Convert APR to period percentage rate by dividing by numbers of periods in year to compound over
PPR = APR_dec / N

# Print header to console
print("Beginning Balance | Interest Earned | Ending Balance")
print("="*17,"+","="*15, "+", "="*14)

inter = int(T * N)    # calculate the number of iterations
startBalance = P       # set starting balance to input P
endBalance = float(0)  # initialize ending balance as float

# Loop through compounding interest calculation
for i in range(0, inter):
    interest = startBalance * PPR     # Calculate interest as starting balance * PPR
    endBalance = startBalance + interest   # calculate ending balance as starting balance plus interest

    # print starting balance, interest, and ending balance formatted as decimeal with comma seperators
    print(f'${startBalance:,.2f}'.rjust(17)+ ' | ' + f'${interest:,.2f}'.rjust(15) + ' | ' + f'${endBalance:,.2f}'.rjust(14))

    # set starting balance to ending balance for next loop
    startBalance = endBalance

# print divider line
print("="*52)

# Double check calculation by second independent formula
finalBalance = P * (1 + APR_dec / N) ** (N*T)

# Output the exact answer via direct calculation
print("The exact answer is: " f'${finalBalance:,.2f}')


""" Test runs

>>> %run "c:\\Users\\devin\\OneDrive\\Documents\\positron\\DS510\\Assignment 2\\Assignment 2A - Hunt.py"
Enter the inital balance to invest: 
25000
Enter the Anual Percentage Rate (APR) as percentage: 
3.6
Enter the number of years to invest: 
10
Enter the number of compounding periods per year: 
4
Beginning Balance | Interest Earned | Ending Balance
================= + =============== + ==============
       $25,000.00 |         $225.00 |     $25,225.00
       $25,225.00 |         $227.03 |     $25,452.03
       $25,452.03 |         $229.07 |     $25,681.09
       $25,681.09 |         $231.13 |     $25,912.22
       $25,912.22 |         $233.21 |     $26,145.43
       $26,145.43 |         $235.31 |     $26,380.74
       $26,380.74 |         $237.43 |     $26,618.17
       $26,618.17 |         $239.56 |     $26,857.73
       $26,857.73 |         $241.72 |     $27,099.45
       $27,099.45 |         $243.90 |     $27,343.35
       $27,343.35 |         $246.09 |     $27,589.44
       $27,589.44 |         $248.30 |     $27,837.74
       $27,837.74 |         $250.54 |     $28,088.28
       $28,088.28 |         $252.79 |     $28,341.08
       $28,341.08 |         $255.07 |     $28,596.15
       $28,596.15 |         $257.37 |     $28,853.51
       $28,853.51 |         $259.68 |     $29,113.19
       $29,113.19 |         $262.02 |     $29,375.21
       $29,375.21 |         $264.38 |     $29,639.59
       $29,639.59 |         $266.76 |     $29,906.34
       $29,906.34 |         $269.16 |     $30,175.50
       $30,175.50 |         $271.58 |     $30,447.08
       $30,447.08 |         $274.02 |     $30,721.10
       $30,721.10 |         $276.49 |     $30,997.59
       $30,997.59 |         $278.98 |     $31,276.57
       $31,276.57 |         $281.49 |     $31,558.06
       $31,558.06 |         $284.02 |     $31,842.08
       $31,842.08 |         $286.58 |     $32,128.66
       $32,128.66 |         $289.16 |     $32,417.82
       $32,417.82 |         $291.76 |     $32,709.58
       $32,709.58 |         $294.39 |     $33,003.97
       $33,003.97 |         $297.04 |     $33,301.00
       $33,301.00 |         $299.71 |     $33,600.71
       $33,600.71 |         $302.41 |     $33,903.12
       $33,903.12 |         $305.13 |     $34,208.25
       $34,208.25 |         $307.87 |     $34,516.12
       $34,516.12 |         $310.65 |     $34,826.77
       $34,826.77 |         $313.44 |     $35,140.21
       $35,140.21 |         $316.26 |     $35,456.47
       $35,456.47 |         $319.11 |     $35,775.58
====================================================
The exact answer is: $35,775.58


>>> %run "c:\\Users\\devin\\OneDrive\\Documents\\positron\\DS510\\Assignment 2\\Assignment 2A - Hunt.py"
Enter the inital balance to invest: 
100000
Enter the Anual Percentage Rate (APR) as percentage: 
3.1
Enter the number of years to invest: 
20
Enter the number of compounding periods per year: 
4
Beginning Balance | Interest Earned | Ending Balance
================= + =============== + ==============
      $100,000.00 |         $775.00 |    $100,775.00
      $100,775.00 |         $781.01 |    $101,556.01
      $101,556.01 |         $787.06 |    $102,343.07
      $102,343.07 |         $793.16 |    $103,136.22
      $103,136.22 |         $799.31 |    $103,935.53
      $103,935.53 |         $805.50 |    $104,741.03
      $104,741.03 |         $811.74 |    $105,552.77
      $105,552.77 |         $818.03 |    $106,370.81
      $106,370.81 |         $824.37 |    $107,195.18
      $107,195.18 |         $830.76 |    $108,025.94
      $108,025.94 |         $837.20 |    $108,863.14
      $108,863.14 |         $843.69 |    $109,706.83
      $109,706.83 |         $850.23 |    $110,557.06
      $110,557.06 |         $856.82 |    $111,413.88
      $111,413.88 |         $863.46 |    $112,277.34
      $112,277.34 |         $870.15 |    $113,147.49
      $113,147.49 |         $876.89 |    $114,024.38
      $114,024.38 |         $883.69 |    $114,908.07
      $114,908.07 |         $890.54 |    $115,798.61
      $115,798.61 |         $897.44 |    $116,696.04
      $116,696.04 |         $904.39 |    $117,600.44
      $117,600.44 |         $911.40 |    $118,511.84
      $118,511.84 |         $918.47 |    $119,430.31
      $119,430.31 |         $925.58 |    $120,355.89
      $120,355.89 |         $932.76 |    $121,288.65
      $121,288.65 |         $939.99 |    $122,228.64
      $122,228.64 |         $947.27 |    $123,175.91
      $123,175.91 |         $954.61 |    $124,130.52
      $124,130.52 |         $962.01 |    $125,092.54
      $125,092.54 |         $969.47 |    $126,062.00
      $126,062.00 |         $976.98 |    $127,038.98
      $127,038.98 |         $984.55 |    $128,023.54
      $128,023.54 |         $992.18 |    $129,015.72
      $129,015.72 |         $999.87 |    $130,015.59
      $130,015.59 |       $1,007.62 |    $131,023.21
      $131,023.21 |       $1,015.43 |    $132,038.64
      $132,038.64 |       $1,023.30 |    $133,061.94
      $133,061.94 |       $1,031.23 |    $134,093.17
      $134,093.17 |       $1,039.22 |    $135,132.39
      $135,132.39 |       $1,047.28 |    $136,179.67
      $136,179.67 |       $1,055.39 |    $137,235.06
      $137,235.06 |       $1,063.57 |    $138,298.63
      $138,298.63 |       $1,071.81 |    $139,370.45
      $139,370.45 |       $1,080.12 |    $140,450.57
      $140,450.57 |       $1,088.49 |    $141,539.06
      $141,539.06 |       $1,096.93 |    $142,635.99
      $142,635.99 |       $1,105.43 |    $143,741.42
      $143,741.42 |       $1,114.00 |    $144,855.41
      $144,855.41 |       $1,122.63 |    $145,978.04
      $145,978.04 |       $1,131.33 |    $147,109.37
      $147,109.37 |       $1,140.10 |    $148,249.47
      $148,249.47 |       $1,148.93 |    $149,398.40
      $149,398.40 |       $1,157.84 |    $150,556.24
      $150,556.24 |       $1,166.81 |    $151,723.05
      $151,723.05 |       $1,175.85 |    $152,898.91
      $152,898.91 |       $1,184.97 |    $154,083.87
      $154,083.87 |       $1,194.15 |    $155,278.02
      $155,278.02 |       $1,203.40 |    $156,481.43
      $156,481.43 |       $1,212.73 |    $157,694.16
      $157,694.16 |       $1,222.13 |    $158,916.29
      $158,916.29 |       $1,231.60 |    $160,147.89
      $160,147.89 |       $1,241.15 |    $161,389.03
      $161,389.03 |       $1,250.77 |    $162,639.80
      $162,639.80 |       $1,260.46 |    $163,900.26
      $163,900.26 |       $1,270.23 |    $165,170.48
      $165,170.48 |       $1,280.07 |    $166,450.56
      $166,450.56 |       $1,289.99 |    $167,740.55
      $167,740.55 |       $1,299.99 |    $169,040.54
      $169,040.54 |       $1,310.06 |    $170,350.60
      $170,350.60 |       $1,320.22 |    $171,670.82
      $171,670.82 |       $1,330.45 |    $173,001.27
      $173,001.27 |       $1,340.76 |    $174,342.03
      $174,342.03 |       $1,351.15 |    $175,693.18
      $175,693.18 |       $1,361.62 |    $177,054.80
      $177,054.80 |       $1,372.17 |    $178,426.97
      $178,426.97 |       $1,382.81 |    $179,809.78
      $179,809.78 |       $1,393.53 |    $181,203.31
      $181,203.31 |       $1,404.33 |    $182,607.64
      $182,607.64 |       $1,415.21 |    $184,022.84
      $184,022.84 |       $1,426.18 |    $185,449.02
====================================================
The exact answer is: $185,449.02

"""