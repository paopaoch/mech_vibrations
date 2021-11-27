from theoretical import theoretical_analysis 
from matplotlib import pyplot as plt
import pandas as pd
from numpy import pi, polyfit
import os

def data_plot(load_type):
    m = 1.82
    DIR_PATH = os.path.dirname(os.path.realpath(__file__))

    """ Get Simulation Data """
    df_sim = pd.read_csv("{0}\data\l{1}.csv".format(DIR_PATH, load_type))
    # print(df_sim.head())
    df_sim["m"] = m * df_sim["l{0}".format(load_type)]

    df_sim["w1"] = df_sim["w1"] / (2* pi)
    df_sim["w2"] = df_sim["w2"] / (2* pi)
    df_sim["w3"] = df_sim["w3"] / (2* pi)

    m_sim = df_sim["m"].to_numpy()

    w1_sim = df_sim["w1"].to_numpy()
    w2_sim = df_sim["w2"].to_numpy()
    w3_sim = df_sim["w3"].to_numpy()
    frequencies_sim = [w1_sim, w2_sim, w3_sim]

    """ Get Theoretical Data """
    m_theo, frequencies_theo = theoretical_analysis(lambda_number=load_type, plot=False)

    """ Get Experimetal Data """
    df_exp = pd.read_csv("{0}\data\\real_data_l{1}.csv".format(DIR_PATH, load_type))
    df_exp["m"] = m + df_exp["d{0}".format(load_type)]
    m_exp = df_exp["m"].to_numpy()
    w1_exp = df_exp['w1'].to_numpy()
    w2_exp = df_exp['w2'].to_numpy()
    w3_exp = df_exp['w3'].to_numpy()
    frequencies_exp = [w1_exp, w2_exp, w3_exp]

    """ Plot data """
    for i in range(len(frequencies_theo)):
        f_sim = frequencies_sim[i]
        f_theo = frequencies_theo[i]
        f_exp = frequencies_exp[i]
        plt.xlabel('mass (kg)')
        plt.ylabel('Natural frequency (Hz)')
        plt.title('Natural frequency against mass, Load type {0}, Frequency mode {1}'.format(load_type, i+1))
        plt.plot(m_sim, f_sim, 'r', label='Simulation')
        plt.plot(m_theo, f_theo, 'b', label='Theoretical')
        plt.scatter(m_exp, f_exp, c='gold', label='Experimental points')
        m, b = polyfit(m_exp, f_exp, 1)
        plt.plot(m_exp, m*m_exp + b, 'g', label='Experiment best fit line')
        plt.legend()
        plt.show()

if __name__ == '__main__':
    data_plot(4) # change the parameter 1,2,3,4 for each load type