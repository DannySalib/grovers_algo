___
The same as the NOT gate in classical computer logic
### ***Circuit Representation***
$\alpha{\ket{0}}+\beta{\ket{1}}$ ---X--- $\alpha{\ket{1}}+\beta{\ket{0}}$
```
|1>---X---|0>

|0>---X---|1>
```
### ***Matrix Representation***
$$X=\begin{pmatrix}0&1 \\ 1&0\end{pmatrix}$$
$$
\begin{align}
X \lvert0 \rangle&=\begin{pmatrix}0&1 \\ 1&0\end{pmatrix}\begin{pmatrix}1 \\ 0\end{pmatrix} \\
&=\begin{pmatrix}0 \\ 1\end{pmatrix} \\ &=\lvert1 \rangle \\ \\

X \lvert1 \rangle&=\begin{pmatrix}0&1 \\ 1&0\end{pmatrix}\begin{pmatrix}0 \\ 1\end{pmatrix} \\
&=\begin{pmatrix}1 \\ 0\end{pmatrix} \\ &=\lvert0 \rangle \\ \\
\end{align}
$$


$$X \lvert \phi = \begin{pmatrix}0&1 \\ 1&0\end{pmatrix} \begin{pmatrix}a \\ b\end{pmatrix}=\begin{pmatrix}b \\ a \end{pmatrix}$$


### **Constraints***
$\ket{\psi'}=\alpha'\ket{0}+\beta'\ket{1}$
