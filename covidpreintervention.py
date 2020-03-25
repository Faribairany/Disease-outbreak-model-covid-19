# Outbreak Model
# dS/dt=-λS
# dE/dt=λS-kE
# dI/dt=kE-αI
# dJ/dt=αI-δJ
# dQ/dt=δJ-γQ
# dR/dt=γQ
#Total population
N=206139589
# initial value of susceptible people
S = (97/100)*N
# initial value of exposed people
E = (1/100)*N
# initial value of infected people
I = (.9/100)*N
# initial value of hospitalized people
J = (.6/100)*N
# initial value of isolation treated people
Q = (.5/100)*N
# initial value of dead people
R = (0/100)*N


# parameters
# incubation period
k = 1 / 6.4
# Period of symptom onset to hospitalization of community members 1/α(use paper parameter])
α = 1/  4
# Period of hospitalization to isolation(paper value)
δ = 1 / 2
# Period of isolation to recovery
γ = 1 / 19
# (Preintervention_value) 
beta_com =  .89
# (Preintervention_value) 
beta_jc =  .840
# initial time in days
t = 0
#No of contact
c=100
λ =(((beta_com *I) + (beta_jc * J))/N)*c
print(λ)
FINAL_SLIQRD = open("westafrica_covid_19(preintervention).csv", "w")  # open file for writing
FINAL_SLIQRD.write("time, S,E, I, J, Q, R\n")  # write headers to file

for i in range(0, 500):
    FINAL_SLIQRD.write(
        str(t) + "," + str(S) + "," + str(E) + "," + str(I) + "," + str(J) + "," + str(Q) + "," + str(R) + "\n")
    # print(str(t) + "," + str(S) + "," + str(E) + "," + str(I) + "," + str(J) + "," + str(Q) + "," + str(R) + "\n")
    t = t + 1


    dS_dt = -λ * S
    dE_dt = λ * S - k * E
    dI_dt = k * E - α * I
    dJ_dt = α * I - δ * J
    dQ_dt = δ * J - γ * Q
    dR_dt = γ * Q


    S = S + dS_dt
    E = E + dE_dt
    I = I + dI_dt
    J = J + dJ_dt
    Q = Q + dQ_dt
    R = R + dR_dt
    N=S+E+I+J+Q+R
FINAL_SLIQRD.write(
    str(t) + "," + str(S) + "," + str(E) + "," + str(I) + "," + str(J) + "," + str(Q) + "," + str(R) + "\n")

FINAL_SLIQRD.close()