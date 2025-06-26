# Reinforcement Learning
## RL loss  
## policy gradient
### version 0
reward delay and short sight problem
### version 1
cumulative reward
$A_k=\sum_{i=k}^{n}r_i$
### version 2
$A_k=r_k+\gamma r_{k+1}+\gamma^2 r_{k+2}+\cdots=\sum_{i=k}^{n}\gamma^{i-k}r_i$  
where $\gamma\in[0,1)$ is the discount factor
### version 3
Good or bad reward is relative 