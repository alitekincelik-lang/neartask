import numpy as np, wave
sr=44100; bpm=126; beat=60/bpm; dur=20.0
N=int(sr*dur); out=np.zeros(N)
D4=293.66
def f(semi,cents=0): return D4*2**((semi+cents/100)/12)
# Ussak-like scale degrees (semitones from D): D, E(-quarter), F, G, A, Bb, C, D'
S={0:f(0),1:f(2,-35),2:f(3),3:f(5),4:f(7),5:f(8),6:f(10),7:f(12),8:f(14,-35),9:f(15)}
def zurna(freq,t0,d,amp=.22):
    n=int(d*sr); t=np.arange(n)/sr
    vib=1+0.006*np.sin(2*np.pi*5.5*t)
    ph=2*np.pi*np.cumsum(freq*vib)/sr
    sig=sum((1/k**0.9)*np.sin(k*ph) for k in range(1,9))
    env=np.minimum(1,t/0.015)*np.minimum(1,(d-t)/0.03).clip(0,1)
    i=int(t0*sr); e=min(N,i+n); out[i:e]+=amp*(sig*env)[:e-i]
def drum(t0,amp=.6,low=True):
    n=int(.35*sr); t=np.arange(n)/sr
    fr=55 if low else 180
    sig=np.sin(2*np.pi*fr*t*(1+1.5*np.exp(-t*30)))*np.exp(-t*(9 if low else 25))
    if not low: sig=0.6*sig+0.4*np.random.randn(n)*np.exp(-t*40)
    i=int(t0*sr); e=min(N,i+n); out[i:e]+=amp*sig[:e-i]
# melody phrases (degree, eighths)
A=[(4,1),(5,1),(4,1),(3,1),(2,1),(3,1),(4,2),(4,1),(5,1),(6,1),(5,1),(4,1),(3,1),(2,2),
   (3,1),(2,1),(1,1),(2,1),(3,1),(2,1),(1,1),(0,1),(1,1),(2,1),(1,1),(0,1),(0,4)]
B=[(7,1),(6,1),(7,1),(8,1),(7,1),(6,1),(5,2),(6,1),(5,1),(4,1),(5,1),(4,1),(3,1),(2,2),
   (4,1),(3,1),(2,1),(3,1),(2,1),(1,1),(0,2),(2,1),(1,1),(0,1),(1,1),(0,4)]
seq=A+B+A+B
t=0.6; e8=beat/2
for deg,l in seq:
    if t>dur-1: break
    zurna(S[deg],t,l*e8*0.95); t+=l*e8
# drone
n=N; tt=np.arange(n)/sr
out+=0.05*np.sin(2*np.pi*D4/2*tt)*np.minimum(1,tt/1.5)
# davul: 2/4  - DUM . tek tek
b=0.0
while b<dur-0.3:
    drum(b,.55,True); drum(b+beat*0.75,.25,False); drum(b+beat,.35,False); drum(b+beat*1.5,.25,False)
    b+=2*beat
fade=np.ones(N); fl=int(1.5*sr); fade[-fl:]=np.linspace(1,0,fl); fade[:int(.3*sr)]=np.linspace(0,1,int(.3*sr))
out*=fade
out=out/np.max(np.abs(out))*0.28   # quiet (~ -11 dBFS peak)
pcm=(out*32767).astype(np.int16)
w=wave.open('bar_music.wav','w'); w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr); w.writeframes(pcm.tobytes()); w.close()
