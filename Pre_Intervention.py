# Outbreak Model
# dS/dt=-λS
# dE/dt=λS-kE
# dI/dt=kE-αI
# dJ/dt=αI-δJ
# dQ/dt=δJ-γQ
# dR/dt=γQ
# Total populatio
N = 206139589
# initial value of susceptible people
S = (90 / 100) * N
# initial value of exposed people
E = (9 / 100) * N
# initial value of infected people
I = (.7 / 100) * N
# initial value of hospitalized people
J = (.3 / 100) * N
# initial value of isolation treated people
R = (0 / 100) * N
# initial value of dead people
D = (0 / 100) * N

# parameters
# incubation period
k = 1 / 6.4
# Period of symptom onset to hospitalization of community members 1/α(use paper parameter])
α = 1 / 7
# Period of isolation to recovery
γ = 1 / 10
# mortaliy rate among hospitalized
η = .043
# (Preintervention_value)
beta_com = 0.99
# (Preintervention_value)
beta_jc = 0.99
# initial time in days
t = 1
λ = ((beta_com * I) + (beta_jc * J)) / N
FINAL_SLIQRD = open("preintervention.csv", "w")  # open file for writing
FINAL_SLIQRD.write("time, Susceptible, Exposed, Infected, Hospitalized, Recovered, Death\n")  # write headers to file

for i in range(0, 30000):
    FINAL_SLIQRD.write(
        str(t) + "," + str(S) + "," + str(E) + "," + str(I) + "," + str(J) + "," + str(R) + "," + str(D) + "\n")
    # print(str(t) + "," + str(S) + "," + str(E) + "," + str(I) + "," + str(J) + "," + str(Q) + "," + str(R) + "\n")
    t = t + 1
    dS_dt = -λ * S
    dE_dt = λ * S - k * E
    dI_dt = k * E - α * I
    dJ_dt = α * I - γ * J - η * J
    dR_dt = γ * J
    dD_dt = η * J

    S = S + dS_dt
    E = E + dE_dt
    I = I + dI_dt
    J = J + dJ_dt
    R = R + dR_dt
    D = D + dD_dt

FINAL_SLIQRD.write(
    str(t) + "," + str(S) + "," + str(E) + "," + str(I) + "," + str(J) + "," + str(R) + "," + str(D) + "\n")

FINAL_SLIQRD.close()