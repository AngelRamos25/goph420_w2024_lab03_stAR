import numpy as np
from matplotlib import pyplot as plt
from goph420_lab03 import regression as rgr


def main():

    t, y = np.loadtxt('M_data.txt', float, unpack=True)
    # a, e, rsq = rgr.multi_regress(y, Z)

    # Plotting raw data:
    plt.figure(figsize=(20, 6))
    plt.plot(t, y, '.')
    plt.grid(min)
    plt.ylabel('Magnitude', fontsize=20)
    plt.xlabel('Hours', fontsize=20)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.title('Seismic events over the whole week.', fontsize=20)
    # Saving the image on the directory /figures. This section is commented since it could be an error if run in other computer:
    # plt.savefig(
    #    'C:/Users/mange/Desktop/UoC/Winter 2024/GOPH_420/goph420_w2024_lab03_stAR/figures/raw_data.pdf')
    # plt.show()

    # Plotting raw data divided by days:
    plt.figure(figsize=(20, 20))
    plt.subplot(5, 1, 1)
    plt.plot(t[0:3928], y[0:3928], '.')
    plt.grid(min)
    plt.ylabel('M - Day 1', fontsize=20)
    plt.title('Seismic events of each day.', fontsize=30)
    plt.ylim([-1.5, 1.5])

    plt.subplot(5, 1, 2)
    plt.plot(t[3929:5684], y[3929:5684], '.')
    plt.grid(min)
    plt.ylabel('M - Day 2', fontsize=20)
    plt.ylim([-1.5, 1.5])

    plt.subplot(5, 1, 3)
    plt.plot(t[5685:6974], y[5685:6974], '.')
    plt.grid(min)
    plt.ylabel('M - Day 3', fontsize=20)
    plt.ylim([-1.5, 1.5])

    plt.subplot(5, 1, 4)
    plt.plot(t[6975:9536], y[6975:9536], '.')
    plt.grid(min)
    plt.ylabel('M - Day 4', fontsize=20)
    plt.ylim([-1.5, 1.5])

    plt.subplot(5, 1, 5)
    plt.plot(t[9537:13390], y[9537:13390], '.')
    plt.grid(min)
    plt.xlabel('Time (hours)', fontsize=30)
    plt.ylabel('M - Day 5', fontsize=20)
    plt.ylim([-1.5, 1.5])

    # Saving the image on the directory /figures. This section is commented since it could be an error if run in other computer:
    # plt.savefig(
    #    'C:/Users/mange/Desktop/UoC/Winter 2024/GOPH_420/goph420_w2024_lab03_stAR/figures/raw_data_days.pdf')
    # plt.show()

    # Making a graph to show how we can separate the intervals
    plt.figure(figsize=(20, 6))
    plt.plot(t, y, '.')
    plt.grid(min)
    plt.ylabel('Magnitude', fontsize=20)
    plt.title('Seismic events over the whole week.', fontsize=20)
    plt.axvline(34, color='k')
    plt.axvline(46, color='k')
    plt.axvline(72, color='k')
    plt.axvline(96, color='k')
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.text(10, 1.55, "Section 1", fontsize=15)
    plt.text(35, 1.55, "Section 2", fontsize=15)
    plt.text(57, 1.55, "Section 3", fontsize=15)
    plt.text(80, 1.55, "Section 4", fontsize=15)
    plt.text(100, 1.55, "Section 5", fontsize=15)
    # Saving the image on the directory /figures. This section is commented since it could be an error if run in other computer:
    # plt.savefig(
    #    'C:/Users/mange/Desktop/UoC/Winter 2024/GOPH_420/goph420_w2024_lab03_stAR/figures/raw_data_cuts.pdf')
    # plt.show()

    # Plotting histograms to construct M vs N for each interval of time.
    y1 = (y[0:3928])
    y2 = (y[3929:5684])
    y3 = (y[5685:6974])
    y4 = (y[6975:9536])
    y5 = (y[9537:13390])

    M = np.arange(-0.5, 1.3, 0.1)

    # Calculating graphs M vs N for section 1:
    N1 = np.zeros(len(M))

    for j in range(0, len(M), 1):
        count = 0
        for i in range(0, len(y1), 1):
            if y1[i] > M[j]:
                count += 1
        N1[j] = count
    plt.figure(figsize=(20, 7))
    plt.semilogy(M, N1, 'o', label="Measured events")
    plt.xlabel("Magnitude order - M", fontsize=20)
    plt.ylabel("Number of events - N", fontsize=20)
    plt.title("Graph M vs N - Section 1", fontsize=20)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.grid(min)

    # Building matrix A for Section 1:
    Z1 = np.ones([len(N1), 2])
    Z1[:, 1] = Z1[:, 1]*(-M)

    # Solving for a and b for Section 1:
    a1, e1, R21 = rgr.multi_regress(np.log10(N1), Z1)
    print(f"Values of a and b for Section 1 are: {a1}")
    print(f"Coefficient of determination for Section 1 is: {R21}")

    # Plotting results for Section 1:
    N1_est = np.matmul(Z1, a1)
    plt.plot(M, 10**N1_est, '-r',
             label=f"LSQR | $a$ = {np.round(a1[0], 3)}, $b$ = {np.round(a1[1], 3)}, $R^2$ = {R21}")
    plt.legend(fontsize=20)
    # Saving the image on the directory /figures. This section is commented since it could be an error if run in other computer:
    # plt.savefig(
    #    'C:/Users/mange/Desktop/UoC/Winter 2024/GOPH_420/goph420_w2024_lab03_stAR/figures/MvsN_S1.pdf')
    # plt.show()


# Calculating graphs M vs N for section 2:
    N2 = np.zeros(len(M))

    for j in range(0, len(M), 1):
        count = 0
        for i in range(0, len(y2), 1):
            if y2[i] > M[j]:
                count += 1
        N2[j] = count
    plt.figure(figsize=(20, 7))
    plt.semilogy(M, N2, 'o', label="Measured events")
    plt.xlabel("Magnitude order - M", fontsize=20)
    plt.ylabel("Number of events - N", fontsize=20)
    plt.title("Graph M vs N - Section 2", fontsize=20)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.grid(min)

    # Building matrix A for Section 2:
    Z2 = np.ones([len(N2), 2])
    Z2[:, 1] = Z2[:, 1]*(-M)

    # Solving for a and b for Section 2:
    a2, e2, R22 = rgr.multi_regress(np.log10(N2), Z2)
    print(f"Values of a and b for Section 2 are: {a2}")
    print(f"Coefficient of determination for Section 2 is: {R22}")

    # Plotting results for Section 2:
    N2_est = np.matmul(Z2, a2)
    plt.plot(M, 10**N2_est, '-r',
             label=f"LSQR | $a$ = {np.round(a2[0], 3)}, $b$ = {np.round(a2[1], 3)}, $R^2$ = {R22}")
    plt.legend(fontsize=20)
    # Saving the image on the directory /figures. This section is commented since it could be an error if run in other computer:
    # plt.savefig(
    #    'C:/Users/mange/Desktop/UoC/Winter 2024/GOPH_420/goph420_w2024_lab03_stAR/figures/MvsN_S2.pdf')
    # plt.show()


# Calculating graphs M vs N for section 3:
    N3 = np.zeros(len(M))

    for j in range(0, len(M), 1):
        count = 0
        for i in range(0, len(y3), 1):
            if y3[i] > M[j]:
                count += 1
        N3[j] = count
    plt.figure(figsize=(20, 7))
    plt.semilogy(M, N3, 'o', label="Measured events")
    plt.xlabel("Magnitude order - M", fontsize=20)
    plt.ylabel("Number of events - N", fontsize=20)
    plt.title("Graph M vs N - Section 3", fontsize=20)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.grid(min)

    # Building matrix Z for Section 3:
    Z3 = np.ones([len(N3), 2])
    Z3[:, 1] = Z3[:, 1]*(-M)

    # Solving for a and b for Section 3:
    a3, e3, R23 = rgr.multi_regress(np.log10(N3), Z3)
    print(f"Values of a and b for Section 3 are: {a3}")
    print(f"Coefficient of determination for Section 3 is: {R23}")

    # Plotting results for Section 3:
    N3_est = np.matmul(Z3, a3)
    plt.plot(M, 10**N3_est, '-r',
             label=f"LSQR | $a$ = {np.round(a3[0], 3)}, $b$ = {np.round(a3[1], 3)}, $R^2$ = {R23}")
    plt.legend(fontsize=20)
    # Saving the image on the directory /figures. This section is commented since it could be an error if run in other computer:
    # plt.savefig(
    #    'C:/Users/mange/Desktop/UoC/Winter 2024/GOPH_420/goph420_w2024_lab03_stAR/figures/MvsN_S3.pdf')
    # plt.show()

    # Calculating graphs M vs N for section 4:
    N4 = np.zeros(len(M))

    for j in range(0, len(M), 1):
        count = 0
        for i in range(0, len(y4), 1):
            if y4[i] > M[j]:
                count += 1
        N4[j] = count
    plt.figure(figsize=(20, 7))
    plt.semilogy(M, N4, 'o', label="Measured events")
    plt.xlabel("Magnitude order - M", fontsize=20)
    plt.ylabel("Number of events - N", fontsize=20)
    plt.title("Graph M vs N - Section 4", fontsize=20)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.grid(min)

    # Building matrix Z for Section 4:
    Z4 = np.ones([len(N4), 2])
    Z4[:, 1] = Z4[:, 1]*(-M)

    # Solving for a and b for Section 4:
    a4, e4, R24 = rgr.multi_regress(np.log10(N4), Z4)
    print(f"Values of a and b for Section 4 are: {a4}")
    print(f"Coefficient of determination for Section 4 is: {R24}")

    # Plotting results for Section 4:
    N4_est = np.matmul(Z4, a4)
    plt.plot(M, 10**N4_est, '-r',
             label=f"LSQR | $a$ = {np.round(a4[0], 3)}, $b$ = {np.round(a4[1], 3)}, $R^2$ = {R24}")
    plt.legend(fontsize=20)
    # Saving the image on the directory /figures. This section is commented since it could be an error if run in other computer:
    # plt.savefig(
    #    'C:/Users/mange/Desktop/UoC/Winter 2024/GOPH_420/goph420_w2024_lab03_stAR/figures/MvsN_S4.pdf')
    # plt.show()

 # Calculating graphs M vs N for section 5:
    N5 = np.zeros(len(M))

    for j in range(0, len(M), 1):
        count = 0
        for i in range(0, len(y5), 1):
            if y5[i] > M[j]:
                count += 1
        N5[j] = count
    plt.figure(figsize=(20, 7))
    plt.semilogy(M, N5, 'o', label="Measured events")
    plt.xlabel("Magnitude order - M", fontsize=20)
    plt.ylabel("Number of events - N", fontsize=20)
    plt.title("Graph M vs N - Section 5", fontsize=20)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.grid(min)

    # Building matrix Z for Section 5:
    Z5 = np.ones([len(N5), 2])
    Z5[:, 1] = Z5[:, 1]*(-M)

    # Solving for a and b for Section 5:
    a5, e5, R25 = rgr.multi_regress(np.log10(N5), Z5)
    print(f"Values of a and b for Section 5 are: {a5}")
    print(f"Coefficient of determination for Section 5 is: {R25}")

    # Plotting results for Section 5:
    N5_est = np.matmul(Z5, a5)
    plt.plot(M, 10**N5_est, '-r',
             label=f"LSQR | $a$ = {np.round(a5[0], 3)}, $b$ = {np.round(a5[1], 3)}, $R^2$ = {R25}")
    plt.legend(fontsize=20)
    # Saving the image on the directory /figures. This section is commented since it could be an error if run in other computer:
    # plt.savefig(
    #    'C:/Users/mange/Desktop/UoC/Winter 2024/GOPH_420/goph420_w2024_lab03_stAR/figures/MvsN_S5.pdf')
    # plt.show()

    # Plotting the residuals
    plt.figure(figsize=(20, 7))
    plt.plot(M, e1, '-', label="Residual of Section 1")
    plt.plot(M, e2, '-', label="Residual of Section 2")
    plt.plot(M, e3, '-', label="Residual of Section 3")
    plt.plot(M, e4, '-', label="Residual of Section 4")
    plt.plot(M, e5, '-', label="Residual of Section 5")
    plt.ylabel("Residual of N [r]", fontsize=20)
    plt.xlabel("Magnitude [M]", fontsize=20)
    plt.title("Graph of residuals for each section", fontsize=20)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.grid(min)
    plt.legend()
    # plt.savefig(
    #    'C:/Users/mange/Desktop/UoC/Winter 2024/GOPH_420/goph420_w2024_lab03_stAR/figures/Residuals.pdf')

    # To plot all the plots, if you don't want to see them all, comment this plt.show().
    # plt.show()


if __name__ == "__main__":
    main()
