
#Total population
N=206139589
# initial value of susceptible people
S = (65/100)*N
#initial value of population socially distanced
SD=(20/100)*N

# initial value of exposed people
E = (7/100)*N
# initial value of infected people
I = (2/100)*N
# initial value of hospitalized people
J = (.7/100)*N
# initial value of isolation treated people
Q = (.3/100)*N
# initial value of dead people
R = (0/100)*N
#initial value of infected people outside border
BC = (5/100)*N

# parameters
# incubation period
k = 1 / 6.4
# Period of symptom onset to hospitalization of community members 1/α(use paper parameter])
α = 1/  4
# Period of hospitalization to isolation(paper value)
δ = 1 / 2
# Period of isolation to recovery
γ = 1 / 19
#travel restriction rate
SD_rate=.75

#initial value of reproduction number
R0SD =2.5
R0BC= 2.5
# (Postintervention_value) 
beta_com =  0.1082
# (Postintervention_value) 
beta_jc =  0.0324
#(Post-intervention value)
# beta_jc =  60
# initial time in days
t = 1
#border closure rate
BC_rate=.061
#average duration of border closure days
AD_BC= 15

λ =((beta_com *I) + (beta_jc * J))/N*SD_rate*BC_rate

FINAL_SLIQRD = open("covid_19(postintervention(75%){Social distancing+borderclosure}).csv", "w")  # open file for writing
FINAL_SLIQRD.write("time, Susceptible, Socially_distanced, Border_closed, Exposed, Infectious, Hospitalized, Isolation_treated, Recovered, R0SD, R0BC\n")  # write headers to file

for i in range(0, 30000):
    FINAL_SLIQRD.write(
        str(t) + "," + str(S) + "," +  str(SD) + "," + str(BC) + "," + str(E) + "," + str(I) + "," + str(J) + "," + str(Q) + "," + str(R) + "," + str(R0SD) + "," + str(R0BC) + "\n")
    # print(str(t) + "," + str(S) + "," + str(E) + "," + str(I) + "," + str(J) + "," + str(Q) + "," + str(R) + "\n")
    t = t + 1
    dS_dt = -λ * S-SD_rate*S - BC_rate*S
    dSD_dt= SD_rate*S 
    dE_dt = λ * S - k * E
    dI_dt = k * E - α * I
    dJ_dt = α * I - δ * J
    dQ_dt = δ * J - γ * Q
    dR_dt = γ * Q + SD_rate*S + BC_rate*S
    dBC_dt=BC_rate*S 
    dR0_dtBC= R0BC*AD_BC*BC_rate
    dR0_dtSD=R0SD*SD_rate
    S = S + dS_dt
    E = E + dE_dt
    I = I + dI_dt
    J = J + dJ_dt
    Q = Q + dQ_dt
    R = R + dR_dt
    SD=SD+dSD_dt
    BC=BC+ dBC_dt
    R0SD=R0SD - dR0_dtSD
    R0BC=R0BC - dR0_dtBC

FINAL_SLIQRD.write(
    str(t) + "," + str(S) + "," + str(SD) + "," + str(BC) + "," + str(E) + "," + str(I) + "," + str(J) + "," + str(Q) + "," + str(R) + "," + str(R0SD) + "," + str(R0BC) + "\n")

FINAL_SLIQRD.close()