___
# Definition
The uncertainty of a Qbit, being that it is neither 0 (up) or 1 (down), making it both up AND down.

___
# Linear Combination Representation Of Qbits
*Representation of a qbit's quantum state*
$\lvert \phi \rangle = a\lvert0\rangle+b\lvert1\rangle$
$\text{given }\lvert{a}\lvert^2+\lvert{b}\lvert^2=1$
$:|a|^2=P(\lvert0\rangle)$
$:\lvert{b}\lvert^2=P(\lvert1\rangle)$

*My notes: Proof  that the sums of  probabilities 1 or 0 is 1*
$$
\begin{align}
P(\lvert0\rangle) =\not P(\lvert1\rangle)=1-P(\lvert1\rangle)
\implies1-P(\lvert1\rangle)\lor P(\lvert1\rangle)&=1\quad\lvert0<=P(X)<=1\quad\forall{X}\in \Omega \\
P(\lvert0\rangle)+P(\lvert1\rangle)&=1 \\ 
1-P(\lvert1\rangle)+P(\lvert1\rangle)&=1\implies 1=1 \\
[P(\lvert0\rangle)+P(\lvert1\rangle)]^2&=1^{2}\\
P(\lvert0\rangle)^2+2P(\lvert1\rangle)P(\lvert0\rangle)+P(\lvert1\rangle)^2&=1^{2}\\
P(\lvert0\rangle)^2+2(1-P(\lvert1\rangle)+P(\lvert1\rangle))+P(\lvert1\rangle)^2&=1^{2}\\
P(\lvert0\rangle)^2+2-2P(\lvert1\rangle)+2P(\lvert1\rangle)+P(\lvert1\rangle)^2&=1^{2}\\
P(\lvert0\rangle)^2+P(\lvert1\rangle)^2&=-1??? \\
\text{Either wrong or involves imaginary numbers given that} \\
\text{these probabilities are the square of the absolute values of a and b }
%& \therefore P(\lvert0\rangle)^2+P(\lvert1\rangle)^2=1
\end{align}$$


**references**
- $\lvert \phi \rangle$: represents a quantum state, where ϕ is the label or name of the state.
- $a,b \in \mathbb{c}$
- $\mathbb{c}$: Set of [[complex numbers]]
- $\lvert0\rangle,\lvert1\rangle$: The ground state and excited state (0 or 1 in classical logic)
___
# Matrix Representation Of Qbits
$$
\begin{align}
\lvert0\rangle&=\begin{pmatrix}0 \\ 1\end{pmatrix} \\
\lvert1\rangle&=\begin{pmatrix}1 \\ 0\end{pmatrix} \\ \\
\lvert\phi\rangle&={a}\lvert0\rangle+{b}\lvert1\rangle \\
&={a}\begin{pmatrix}0 \\ 1\end{pmatrix}+b\begin{pmatrix}1 \\ 0\end{pmatrix} \\
&=\begin{pmatrix} a \\ 0\end{pmatrix}+\begin{pmatrix} 0 \\ b\end{pmatrix} \\
&=\begin{pmatrix} a \\ b \end{pmatrix}
\end{align}
$$


