# Todo
▪️ 用Python 包内有无其他求解方法；Scipy etc.  

▪️ 其他阶数的龙格-库塔方法求解，自适应网格求解

▪️ 方法稳定性分析，精确度，解域空间分布，std，冯-诺伊曼稳定性分析

▪️ 画一个帅气的图。

## Have a try, (maybe
▪️ 同时求解二元二阶方程？

▪️ 有没有办法同时求解二元二次方程组

# Ongoing
1. 冯-诺伊曼稳定性分析方法调研
2. Scipy内求解方法调研

# Complete
✅ 8阶龙格-库塔方法求解完成

✅ 分布求解

✅ Toy model，构造简单的物理模型

## LX
1. 课程报告
2. Runge-Kutta 方法自适应步长和截断误差分析
3. 收敛性分析

▪️ 使用包 scipy.integrate.solve_ivp

▪️ 如果没有自定义stepsize,程序会自己选择stepsize，并且不是固定步长

▪️ 选择不同的初始步长会严重影响解的形式(见ode853_stepsize.ipynb)

Question 如何定量的分析？

✦ 程序的步长选择是自适应的：看image adaptive_stepsize.png



## ZZY
✅ 不同质量星系的速度弥散，有效半径，恒星质量，DMH质量.  

▪️ DMH mass to Stellar mass: SHMF [Xu+2023](https://ui.adsabs.harvard.edu/abs/2023ApJ...944..200X/abstract)

使用DP(double power-law)模型来把给定的halo mass转到stellar mass，用abundance mathch的方法，这样的误差大约在0.23dex

$M_* = [\frac{2k}{(M_{vir} / M_{0})^{-\alpha} + (M_{vir} / M_{0})^{-\beta}}] $

对于local的星系使用他们拟合得到的z<0.2的参数：$log10(M_0)=11.732, \alpha=0.299, \beta=1.917, log10(k)=10.303$

▪️ Stellar mass to max rotation velocity: MTF relation [McGaughl+2000](https://ui.adsabs.harvard.edu/abs/2000ApJ...533L..99M/abstract)

用R波段的质光比，假设了Salpeter IMF，误差大约在0.22dex

$M_* = M_{100} V_{rot}^{\alpha}$

参数范围：$log10(M_*/M_{100})=9.51, \alpha=4.34$

▪️ gas mass (HI)：GSMF [V Parkash+2018](https://iopscience.iop.org/article/10.3847/1538-4357/aad3b9)

$log10(M_{HI} = 0.51 \cdot (log10(M_*)-10) + 9.71$


▪️ velocity dispersion: 10-100 km/s
   

▪️ effective radius: 1-10 kpc

## NJB
1. Rechardson 外推方法的代码实现


# Discussion

# model 
假设

流体静力学平衡；固定半径出的速度一致；重子物质运动带来的离心力；盘为等温盘；无磁场；恒星，气体面密度都是指数分布；DMH中心星系， i.e. 大（小）质量Halo host 大（小）质量星系

$\Sigma_{DMH}$ profile：NFW模型，球对称

R: 星系平面上的一个固定半径位置

$d\Phi/dR/R$: 旋转曲线

左端：速度弥散，恒星，气体压强带来的效应

$\Sigma_*$ profile: 未知量

$\sigma_{gas}$ profile: 未知量

# 求解
需要假设恒星盘，气体盘的面密度轮廓，需要设置参数上下限

针对不用质量星系求解，dwarfs，massive。
