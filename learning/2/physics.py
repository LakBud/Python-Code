from pylab import *

# Informasjon om konstanter, konstante krefter og gjenstanden
m = 0.0037    # massen av gjenstanden, kg
g = 9.81      # tyngdeakselerasjon, m/s^2
k = 0.05     # luftmotstandstall, kg/m
G = m*g       # gravitasjonskraft, N

# Startverdier for bevegelsen
s = 0  # startposisjon, m
v = 0  # startfart, m/s
a = g  # startakselerasjon, m/s^2
t = 0  # starttid, s

# Simuleringsteknisk
s_slutt = 2.5     # sluttposisjon for simulering, m
dt = 0.001       # lengde på tidssteg, s
s_verdier = [s]  # liste for lagring av posisjon
v_verdier = [v]  # liste for lagring av x-verdier for graf
a_verdier = [a]  # liste for lagring av y-verdier for graf
t_verdier = [t]  # liste for lagring av y-verdier for graf
  

# Løkke som beregner ny fart, posisjon, akselerasjon og tid
while s < s_slutt:  
# Regner ut akselerasjonen for hver tid
  L = k*v**2     # luftmotstand, N
  sum_F = G - L  # kraftsum, N
  a = sum_F/m    # akselerasjon, m/s^2
# Regner ut v og s ved å finne arealet under grafen til a-t og v-t grafene
  v = v + a*dt   # regner ut ny v og overskriver gammel
  s = s + v*dt   # regner ut ny s og overskriver gammel
  t = t + dt     # regner ut ny t og overskriver gammel


  #Lagrer verdier for plotting av grafer.
  s_verdier.append(s)  # legger til nye y-verdier for graf 1
  v_verdier.append(v)  # legger til nye y-verdier for graf 2
  a_verdier.append(a)  # legger til nye y-verdier for graf 2
  t_verdier.append(t)  # legger til nye x-verdier for grafene
  
  

# Tegning av graf
fig, axs = subplots(1, 3, figsize=(10, 4)) 
axs[0].plot(t_verdier, s_verdier, color='blue') # lager grafen 1
axs[0].set_title("Posisjon som funksjon av tid", color='blue')
axs[0].set_xlabel("Tid [s]")       
axs[0].set_ylabel("Posisjon [m]")  
axs[0].set_xlim(0, s_slutt)
axs[0].set_ylim(0, max(s_verdier) + 0.1)
axs[0].grid(True) 

axs[1].plot(t_verdier, v_verdier, color='red') # lager grafen 2
axs[1].set_title("Fart som funksjon av tid", color='red')
axs[1].set_xlabel("Tid [s]")       
axs[1].set_ylabel("Fart [m/s]")  
axs[1].set_xlim(0, s_slutt)
axs[1].set_ylim(0, max(v_verdier) + 0.5)
axs[1].grid(True) 

axs[2].plot(t_verdier, a_verdier, color='green') # lager grafen 3
axs[2].set_title("Akselerasjon som funksjon av tid", color='green')
axs[2].set_xlabel("Tid [s]")       
axs[2].set_ylabel("Akselerasjon [m/s^2]")  
axs[2].set_xlim(0, s_slutt)
axs[2].set_ylim(0, max(a_verdier) + 0.5)
axs[2].grid(True) 

tight_layout()
show()  # viser grafen
