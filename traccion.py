def traccion(mu,W,b,L,h,g,v,vmaxtot)
[P,T]=potencia(v,vmaxtot);
Fx=P/(v);[Fx,P,T]
Fxmax=traccionmax(mu,W,b,L,h);
if(Fx>Fxmax)
 Fx=Fxmax;
end
