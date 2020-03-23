# Outbreak Model
# dS/dt=-λS
# dE/dt=λS-kE
# dI/dt=kE-αI
# dJ/dt=αI-δJ
# dQ/dt=δJ-γQ
# dR/dt=γQ

# initial value of susceptible people
S = 190000000
# initial value of latent people
E = 0
# initial value of infected people
I = 2
# initial value of quarantined people
J = 0
# initial value of removed people
Q = 0
# initial value of dead people
R = 0

# parameters
# incubation period
k = 1 / 11
# Period of symptom onset to hospitalization of community members 1/α(use paper parameter])
α = 1/  4
# Period of hospitalization to isolation(paper value)
δ = 1 / 2
# Period of isolation to recovery
γ = 1 / 14
#λ = .2
beta_com =  0.1352 # (Pre_value) #0.1082 (Post-intervention value)
beta_jc =  0.0405 # (Pre_value) #0.0324 (Post-intervention value)
# initial time in days
t = 0

FINAL_SLIQRD = open("westafrica_covid_19.csv", "w")  # open file for writing
FINAL_SLIQRD.write("time, S,E, I, J, Q, R\n")  # write headers to file

for i in range(0, 100):
    FINAL_SLIQRD.write(
        str(t) + "," + str(S) + "," + str(E) + "," + str(I) + "," + str(J) + "," + str(Q) + "," + str(R) + "\n")
    print(str(t) + "," + str(S) + "," + str(E) + "," + str(I) + "," + str(J) + "," + str(Q) + "," + str(R) + "\n")
    t = t + 1

    λ =(beta_com *I) + (beta_jc * J)

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
FINAL_SLIQRD.write(
    str(t) + "," + str(S) + "," + str(E) + "," + str(I) + "," + str(J) + "," + str(Q) + "," + str(R) + "\n")

FINAL_SLIQRD.close()