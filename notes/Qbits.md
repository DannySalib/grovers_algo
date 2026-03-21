___
# Definition
Short for quantum bit. Represents the data value 0, 1, or the [[quantum superposition]] of both 0 & 1. 

--- start-multi-column
```column-settings
Column Size:[65%, 30%]
```
# Bloc Sphere Representation

$$
\begin{align}
\lvert \psi \rangle= \alpha \lvert0 \rangle + \beta \lvert1 \rangle \implies
\lvert \psi \rangle= \cos(\frac{\theta}{2})\lvert0 \rangle+e^{i\phi}\sin({\frac{\theta}{2}})\lvert1 \rangle

\end{align}
$$

--- end-column ---

![[360_F_469735502_AElrx3dqrucXJ3rx3CfVg94jkIhlXLMk.webp|170]]
--- end-multi-column

- Getting information on a Qbit is restricted and limited 
- When measuring a Qbit we see that it is either
	- $\ket{0}$ w/ $P(\ket{0})=\lvert \alpha \lvert^2$
	- $\ket{1}$ w/ $P(\ket{1}) = \lvert \beta \lvert^2$
	- given $\lvert \alpha \lvert^{2}+ \lvert \beta \lvert ^{2} = 1$
- A Qbit is always in a state between $\ket{0}$ and $\ket{1}$ - **until observed** 
### ***Example***
$\frac{1}{\sqrt{2}}\ket{0}+ \frac{1}{\sqrt{2}}\ket{1}$
*When measured* gives the result 0,1 50% of the time $(\lvert \frac{1}{\sqrt{2}}\lvert^2)$ (denoted as $\ket{+}$)

$\ket{\psi}=\left(\cos{\frac{\theta}{2}}\ket{0}+e^{i \phi}\sin{\frac{\theta}{2}\ket{1}}\right)\quad \theta,\gamma,\phi\in R$
![[640px-Bloch_sphere.svg.webp|200]]
