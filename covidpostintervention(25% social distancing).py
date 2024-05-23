#Total population
N=2000000.0
# initial value of susceptible people
S = (90/100)*N
#socially distance people people
SD=(0/100)*N
# initial value of exposed people
E = (8/100)*N
# initial value of infected people
I = (1/100)*N
# initial value of hospitalized people
H = (.7/100)*N
# initial value of isolation treated people
R = (.2/100)*N
# initial value of dead people
D = (.1/100)*N
#natural death rate
η=.014
#social distancing 25%(w1)
SD_rate=.09
# parameters
# incubation period
k = 1 / 5.3891 
# Period of symptom onset to hospitalization of community members 1/α(use paper parameter])
α = 1/  7
# mortaliy rate
μ = 0.0255
# (Preintervention_value) 
beta_com =  0.8643
# (Preintervention_value) 
beta_hc =  0.63
# initial time in days
t = 1
#primary reproduction  umber
R0SD=2.42
λ =(((beta_com *I) + (beta_hc * H))/N)*SD_rate
FINAL_SLIQRD = open("westafrica_covid_19(postintervention75%).csv", "w")  # open file for writing
FINAL_SLIQRD.write("time, Susceptible, Socially_distanced, Exposed, Infected, Hospitalized, Recovered, Death, R0SD\n")  # write headers to file

for i in range(0, 30000):
    FINAL_SLIQRD.write(
        str(t) + "," + str(S) + "," +  str(SD) + "," + str(E) + "," + str(I) + "," + str(H) + "," + str(R) + "," + str(D) + "," + str(R0SD) + "\n")
    # print(str(t) + "," + str(S) + "," + str(E) + "," + str(I) + "," + str(H) + "," + str(Q) + "," + str(R) + "\n")
    t=t + 1
    dS_dt = -λ * S-SD_rate*S
    dE_dt = λ * S - k * E
    dI_dt = k * E - α * I -μ*I
    dH_dt = α * I - (1-μ)*H - μ*H
    dR_dt = (1-μ)*H + SD_rate*S
    dD_dt = μ*H + μ*I + η*N
    dSD_dt= SD_rate*S
    dR0SD_dt=R0SD*SD_rate
 

    S = S + dS_dt
    E = E + dE_dt
    I = I + dI_dt
    H = H + dH_dt
    R = R + dR_dt
    D = D + dD_dt
    SD=SD + dSD_dt
    R0SD=R0SD-dR0SD_dt
  
FINAL_SLIQRD.write(
    str(t) + "," + str(S) + "," + str(SD) + "," + str(E) + "," + str(I) + "," + str(H) + "," + str(R) + "," + str(D) + "," + str(R0SD) + "\n")

FINAL_SLIQRD.close()