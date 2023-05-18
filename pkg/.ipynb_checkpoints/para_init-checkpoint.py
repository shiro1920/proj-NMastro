def paraInit(M_halo):
    """
    Use serval scaling relations to estimate various galaxy's properties from its halo mass.
    
    parameters
    -----------
    
    M_halo: Given Halo mass usually refer to M_200. It is used to estimate the steallar mass through
    the Abundance match method (Xu+2023), adopting the Double-powerlaw model.
    
    Returns
    -----------
    logM_200: viral halo mass in unit Msun
    R_200: viral halo radius
    c_200: concentrition of halo 
    logMstar(err): derived stellar mass and its error 
    logMgas(err): gas mass and its error
    log_Vmax(err): maximum rotational velocity and its error
    
    References
    -----------
    Xu+2023: https://ui.adsabs.harvard.edu/abs/2023ApJ...944..200X/abstract
    McGaughl+2000: https://ui.adsabs.harvard.edu/abs/2000ApJ...533L..99M/abstract
    V Parkash+2018: https://iopscience.iop.org/article/10.3847/1538-4357/aad3b9

    """
    # import package
    import numpy as np
    from astropy.io import ascii
    from astropy.table import Table
    
    
    # stellar mass
    k = 10**10.303
    M0 = 10**11.732
    alpha = 0.299
    beta = 1.917
    
    M_star = lambda x: 2*k/((x/M0)**(-alpha) + (x/M0)**(-beta))
    log_Mstar = np.log10(M_star(M_halo))
    log_Mstar_err = 0.23
    
    # gas (HI) mass
    log_MHI = lambda log_Mstar: 0.51 * (log_Mstar-10) + 9.71
    log_Mgas = log_MHI(log_Mstar)
    log_Mgas_err = 0.51*log_Mstar_err
    
    # maximum rotational velocity 
    gamma = 3.98
    f_A = np.log10(1.57)
    f_A_err = 0.25/1.57/np.log(10)
    M_d = np.log10(10**log_Mstar + 10**log_Mgas)
    Md_err = 0.32
    log_Vmax = lambda M_d: (M_d-f_A)/gamma
    log_Vmax = log_Vmax(M_d)
    log_Vmax_err = np.sqrt((f_A_err/gamma)**2+(0.32/(M_d-f_A))**2)
    
    # halo properties
    G = 4.301*10**(-6)
    H = 67.4*10**(-3)
    M_200 = np.log10(M_halo)
    c_halo = 9.60*(M_halo/(10**12/0.674))**(-0.075)
    R_halo = (M_halo * G / (100 * H**2))**(1/3)
    
    # results
    dT = dict()
    dT["logM_200/Msun"] = M_200
    dT["R_200/kpc"]     = R_halo
    dT["c_200"]         = c_halo
    dT["logMstar/Msun"] = log_Mstar
    dT["logMstar_err"]  = log_Mstar_err
    dT["logMgas/Msun"]  = log_Mgas
    dT["logMgas_err"]   = log_Mgas_err
    dT["log_Vmax/km/s"] = log_Vmax
    dT["log_Vmax_err"]  = log_Vmax_err
    
    return dT
    