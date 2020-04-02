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
S = (65/100)*N
#initial value of population restricted for travel
TR=(25/100)*N

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
tr_rate=.01
#travel restriction efficacy
tr_efficacy=.5486
#initial value of reproduction number
R0= 2.5
# (Postintervention_value) 
beta_com =  0.1082
# (Postintervention_value) 
beta_jc =  0.0324
#(Post-intervention value)
# beta_jc =  60
# initial time in days
t = 0
λ =((beta_com *I) + (beta_jc * J))/N*tr_rate
print(λ)
FINAL_SLIQRD = open("nig_covid_19(postintervention).csv", "w")  # open file for writing
FINAL_SLIQRD.write("time, Susc,TR, Exposed, Infec, J, Q, Recovered, R0\n")  # write headers to file

for i in range(0, 30000):
    FINAL_SLIQRD.write(
        str(t) + "," + str(S) + "," +  str(TR) + "," + str(E) + "," + str(I) + "," + str(J) + "," + str(Q) + "," + str(R) + "," + str(R0) + "\n")
    # print(str(t) + "," + str(S) + "," + str(E) + "," + str(I) + "," + str(J) + "," + str(Q) + "," + str(R) + "\n")
    t = t + 1
   

    dS_dt = -λ * S-tr_rate*S
    dTR_dt= tr_rate*S 
    dE_dt = λ * S - k * E
    dI_dt = k * E - α * I
    dJ_dt = α * I - δ * J
    dQ_dt = δ * J - γ * Q
    dR_dt = γ * Q + tr_rate*S
   
    dR0_dtTR=R0*tr_rate

    S = S + dS_dt
    E = E + dE_dt
    I = I + dI_dt
    J = J + dJ_dt
    Q = Q + dQ_dt
    R = R + dR_dt
    TR=TR+dTR_dt
    R0=R0 - dR0_dtTR

FINAL_SLIQRD.write(
    str(t) + "," + str(S) + "," + str(TR) + "," + str(E) + "," + str(I) + "," + str(J) + "," + str(Q) + "," + str(R) + "," + str(R0) + "\n")

FINAL_SLIQRD.close()