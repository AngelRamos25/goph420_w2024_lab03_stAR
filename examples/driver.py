import numpy as np
from matplotlib import pyplot as plt
from goph420_lab03 import regression as rgr


def main():

    nD = 50
    t, y = np.loadtxt('M_data.txt', float, unpack=True)
    # a, e, rsq = rgr.multi_regress(y, Z)

    # Plotting raw data:
    plt.figure(figsize=(20, 6))
    C = plt.plot(t, y, '.')
    plt.grid(min)
    plt.ylabel('Magnitude')
    plt.xlabel('Hours')
    plt.title('Seismic events over the whole week.')
    # Saving the image on the directory /figures. This section is commented since it could be an error if run in other computer:
    # plt.savefig(
    #    'C:/Users/mange/Desktop/UoC/Winter 2024/GOPH_420/goph420_w2024_lab03_stAR/figures/raw_data.pdf')
    plt.show()

    # Plotting raw data divided by days:
    plt.figure(figsize=(30, 20))
    C2 = plt.subplot(5, 1, 1)
    plt.plot(t[0:3928], y[0:3928], '.')
    plt.grid(min)
    plt.ylabel('Magnitude - Day 1')
    plt.title('Seismic events of each day.')
    plt.ylim([-1.5, 1.5])
    plt.axvline(0, color='r')

    plt.subplot(5, 1, 2)
    plt.plot(t[3929:5684], y[3929:5684], '.')
    plt.grid(min)
    plt.ylabel('Magnitude - Day 2')
    plt.ylim([-1.5, 1.5])
    plt.axvline(34, color='r')
    plt.axvline(34.05, color='b')
    plt.axvline(46, color='b')
    plt.axvline(46.05, color='g')

    plt.subplot(5, 1, 3)
    plt.plot(t[5685:6974], y[5685:6974], '.')
    plt.grid(min)
    plt.ylabel('Magnitude - Day 3')
    plt.ylim([-1.5, 1.5])
    plt.axvline(72, color='g')

    plt.subplot(5, 1, 4)
    plt.plot(t[6975:9536], y[6975:9536], '.')
    plt.grid(min)
    plt.ylabel('Magnitude - Day 4')
    plt.ylim([-1.5, 1.5])
    plt.axvline(72, color='k')
    plt.axvline(96, color='k')

    plt.subplot(5, 1, 5)
    plt.plot(t[9537:13390], y[9537:13390], '.')
    plt.grid(min)
    plt.xlabel('Time (hours)')
    plt.ylabel('Magnitude- Day 5')
    plt.ylim([-1.5, 1.5])
    plt.axvline(96, color='m')
    plt.axvline(120, color='m')

    # Saving the image on the directory /figures. This section is commented since it could be an error if run in other computer:
    # plt.savefig(
    #    'C:/Users/mange/Desktop/UoC/Winter 2024/GOPH_420/goph420_w2024_lab03_stAR/figures/raw_data_cuts.pdf')
    plt.show()

    # Making a graph to show how we can separate the intervals by using abs()
    plt.figure(figsize=(20, 6))
    C3 = plt.plot(t, np.abs(y), '.')
    plt.grid(min)
    plt.ylabel('|Magnitude|')
    plt.title('Seismic events over the whole week.')
    plt.axvline(34, color='k')
    plt.axvline(46, color='k')
    plt.axvline(72, color='k')
    plt.axvline(96, color='k')
    plt.text(10, 1.55, "Section 1", fontsize=15)
    plt.text(36, 1.55, "Section 2", fontsize=15)
    plt.text(57, 1.55, "Section 3", fontsize=15)
    plt.text(80, 1.55, "Section 4", fontsize=15)
    plt.text(100, 1.55, "Section 5", fontsize=15)
    # Saving the image on the directory /figures. This section is commented since it could be an error if run in other computer:
    # plt.savefig(
    #    'C:/Users/mange/Desktop/UoC/Winter 2024/GOPH_420/goph420_w2024_lab03_stAR/figures/raw_data_cuts_abs.pdf')
    plt.show()

    # Plotting histograms to construct M vs N for each interval of time.
    y1 = np.abs(y[0:3928])
    y2 = np.abs(y[3929:5684])
    y3 = np.abs(y[5685:6974])
    y4 = np.abs(y[6975:9536])
    y5 = np.abs(y[9537:13390])

    t1 = t[0:3928]
    t2 = t[3929:5684]
    t3 = t[5685:6974]
    t4 = t[6975:9536]
    t5 = t[9537:13390]

    plt.figure(figsize=(20, 20))
    C4 = plt.subplot(5, 1, 1)
    counts1, M1, bar1 = plt.hist(y1, edgecolor='white', bins=nD)
    plt.title('Histograms of seismic events per magnitude')
    plt.ylabel('Frecuency - Day 1')
    plt.grid(min)

    plt.subplot(5, 1, 2)
    counts2, M2, bars2 = plt.hist(y2, edgecolor='white', bins=nD)
    plt.ylabel('Frecuency - Day 2')
    plt.grid(min)

    plt.subplot(5, 1, 3)
    counts3, M3, bars3 = plt.hist(y3, edgecolor='white', bins=nD)
    plt.ylabel('Frecuency- Day 3')
    plt.grid(min)

    plt.subplot(5, 1, 4)
    counts4, M4, bars4 = plt.hist(y4, edgecolor='white', bins=nD)
    plt.ylabel('Frecuency - Day 4')
    plt.grid(min)

    plt.subplot(5, 1, 5)
    counts5, M5, bars5 = plt.hist(y5, edgecolor='white', bins=nD)
    plt.xlabel('Magnitude')
    plt.ylabel('Frecuency - Day 5')
    plt.grid(min)

    # Saving the image on the directory /figures. This section is commented since it could be an error if run in other computer:
    # plt.savefig(
    #    'C:/Users/mange/Desktop/UoC/Winter 2024/GOPH_420/goph420_w2024_lab03_stAR/figures/histograms.pdf')
    plt.show()

    # Plotting graphs M vs N:

    # For Section 1:
    N1 = np.zeros([len(M1)-1, 1])

    for i in range(0, len(M1)-1, 1):
        N1[i] = sum(counts1[(0 + i):(len(M1)-1)])
    M1 = M1[0:-1]

    plt.figure(figsize=(30, 20))
    C4 = plt.subplot(3, 2, 1)
    plt.semilogy(M1, N1, '.')
    plt.xlabel('M')
    plt.ylabel('log(N)')
    plt.title('M vs N graph for section 1')
    plt.grid(min)

    # For Section 2:
    N2 = np.zeros([len(M2)-1, 1])

    for i in range(0, len(M2)-1, 1):
        N2[i] = sum(counts2[(0 + i):(len(M2)-1)])
    M2 = M2[0:-1]

    plt.subplot(3, 2, 2)
    plt.semilogy(M2, N2, '.')
    plt.xlabel('M')
    plt.ylabel('log(N)')
    plt.title('M vs N graph for section 2')
    plt.grid(min)

    # For Section 3:
    N3 = np.zeros([len(M3)-1, 1])

    for i in range(0, len(M3)-1, 1):
        N3[i] = sum(counts3[(0 + i):(len(M3)-1)])
    M3 = M3[0:-1]

    plt.subplot(3, 2, 3)
    plt.semilogy(M3, N3, '.')
    plt.xlabel('M')
    plt.ylabel('log(N)')
    plt.title('M vs N graph for section 3')
    plt.grid(min)

    # For Section 4:
    N4 = np.zeros([len(M4)-1, 1])

    for i in range(0, len(M4)-1, 1):
        N4[i] = sum(counts4[(0 + i):(len(M4)-1)])
    M4 = M4[0:-1]

    plt.subplot(3, 2, 4)
    plt.semilogy(M4, N4, '.')
    plt.xlabel('M')
    plt.ylabel('log(N)')
    plt.title('M vs N graph for section 4')
    plt.grid(min)

    # For Section 5:
    N5 = np.zeros([len(M5)-1, 1])

    for i in range(0, len(M5)-1, 1):
        N5[i] = sum(counts5[(0 + i):(len(M5)-1)])
    M5 = M5[0:-1]

    plt.subplot(3, 2, 5)
    plt.semilogy(M5, N5, '.')
    plt.xlabel('M')
    plt.ylabel('log(N)')
    plt.title('M vs N graph for section 5')
    plt.grid(min)
    # Saving the image on the directory /figures. This section is commented since it could be an error if run in other computer:
    # plt.savefig(
    #    'C:/Users/mange/Desktop/UoC/Winter 2024/GOPH_420/goph420_w2024_lab03_stAR/figures/MvN.pdf')

    # Calculating the parameters a and b for section 1:
    N1 = np.log10(N1)
    N2 = np.log10(N2)
    N3 = np.log10(N3)
    N4 = np.log10(N4)
    N5 = np.log10(N5)

    Z1 = np.ones(len(N1))
    Z1 = np.array([Z1,
                   -1*M1])
    Z1 = np.transpose(Z1)

    a1, e1, rsq1 = rgr.multi_regress(N1, Z1)
    N1a = np.matmul(Z1, a1)
    plt.subplot(3, 2, 1)
    plt.plot(
        M1, 10**N1a, label=f'BFL: a = {np.round(a1[0], 3)}, b = {np.round(a1[1], 3)}, R^2 = {rsq1} ')
    plt.legend(fontsize=17)

    # Calculating the parameters a and b for section 2:
    Z2 = np.ones(len(N2))
    Z2 = np.array([Z2,
                   -1*M2])
    Z2 = np.transpose(Z2)

    a2, e2, rsq2 = rgr.multi_regress(N2, Z2)
    N2a = np.matmul(Z2, a2)
    plt.subplot(3, 2, 2)
    plt.plot(
        M2, 10**N2a, label=f'BFL: a = {np.round(a2[0], 3)}, b = {np.round(a2[1], 3)}, R^2 = {rsq2} ')
    plt.legend(fontsize=17)

    # Calculating the parameters a and b for section 3:
    Z3 = np.ones(len(N3))
    Z3 = np.array([Z3,
                   -1*M3])
    Z3 = np.transpose(Z3)

    a3, e3, rsq3 = rgr.multi_regress(N3, Z3)
    N3a = np.matmul(Z3, a3)
    plt.subplot(3, 2, 3)
    plt.plot(
        M3, 10**N3a, label=f'BFL: a = {np.round(a3[0], 3)}, b = {np.round(a3[1], 3)}, R^2 = {rsq3} ')
    plt.legend(fontsize=17)

    # Calculating the parameters a and b for section 4:
    Z4 = np.ones(len(N4))
    Z4 = np.array([Z4,
                   -1*M4])
    Z4 = np.transpose(Z4)

    a4, e4, rsq4 = rgr.multi_regress(N4, Z4)
    N4a = np.matmul(Z4, a4)
    plt.subplot(3, 2, 4)
    plt.plot(
        M4, 10**N4a, label=f'BFL: a = {np.round(a4[0], 3)}, b = {np.round(a4[1], 3)}, R^2 = {rsq4} ')
    plt.legend(fontsize=17)

    # Calculating the parameters a and b for section 5:
    Z5 = np.ones(len(N5))
    Z5 = np.array([Z5,
                   -1*M5])
    Z5 = np.transpose(Z5)

    a5, e5, rsq5 = rgr.multi_regress(N5, Z5)
    N5a = np.matmul(Z5, a5)
    plt.subplot(3, 2, 5)
    plt.plot(
        M5, 10**N5a, label=f'BFL: a = {np.round(a5[0], 3)}, b = {np.round(a5[1], 3)}, R^2 = {rsq5} ')
    plt.legend(fontsize=17)

    # Saving the image on the directory /figures. This section is commented since it could be an error if run in other computer:
    # plt.savefig(
    #    'C:/Users/mange/Desktop/UoC/Winter 2024/GOPH_420/goph420_w2024_lab03_stAR/figures/MvN_results.pdf')
    plt.show()

    # Plotting the residuals for each day:
    # Day 1:
    plt.figure(figsize=(20, 6))
    C5 = plt.plot(e1, '-', label='Section 1 residuals')
    plt.xlabel('Data index')
    plt.ylabel('Residual')
    plt.title('Graphs of residuals for each day')
    plt.grid(min)

    # Day 2:
    plt.plot(e2, '-', label='Section 2 residuals')
    plt.grid(min)

    # Day 3:
    plt.plot(e3, '-', label='Section 3 residuals')
    plt.grid(min)

    # Day 4:
    plt.plot(e4, '-', label='Section 4 residuals')
    plt.grid(min)

    # Day 5:
    plt.plot(e5, '-', label='Section 5 residuals')
    plt.grid(min)

    plt.legend()
    # Saving the image on the directory /figures. This section is commented since it could be an error if run in other computer:
    # plt.savefig(
    #   'C:/Users/mange/Desktop/UoC/Winter 2024/GOPH_420/goph420_w2024_lab03_stAR/figures/residuals.pdf')
    plt.show()


if __name__ == "__main__":
    main()
