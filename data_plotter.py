from theoretical import theoretical_analysis 
from matplotlib import pyplot as plt
import pandas as pd
from numpy import pi, polyfit
import os

M = 1.82
DIR_PATH = os.path.dirname(os.path.realpath(__file__))

def data_plot(load_type, on_one_graph=True):

    """ Get Simulation Data """
    df_sim = pd.read_csv("{0}\data\l{1}.csv".format(DIR_PATH, load_type))
    # print(df_sim.head())
    df_sim["m"] = M * df_sim["l{0}".format(load_type)]

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
    df_exp["m"] = M + df_exp["d{0}".format(load_type)]
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
        plt.plot(m_sim, f_sim, label='Simulation mode {0}'.format(i+1))
        plt.plot(m_theo, f_theo, label='Theoretical mode {0}'.format(i+1))
        plt.scatter(m_exp, f_exp, label='Experimental points mode {0}'.format(i+1))
        m, b = polyfit(m_exp, f_exp, 1)
        plt.plot(m_exp, m*m_exp + b, label='Experiment best fit line mode {0}'.format(i+1))
        plt.tight_layout()
        plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')

        if not on_one_graph:
            plt.title('Natural frequency against mass, Load type {0}, Frequency mode {1}'.format(load_type, i+1))
            plt.show()
    
    if on_one_graph:
        plt.title('Natural frequency against mass, Load type {0}'.format(load_type))
        plt.show()

PLT_COLORS = ['red', 'gold', 'lime', 'mediumblue']
def compare_load_type(mode_type, plot_type=["theoretical"], range_load_type=[1,2,3,4]):
    """ Get Simulation Data """
    color_index = 0
    for load_type in range_load_type:
        df_sim = pd.read_csv("{0}\data\l{1}.csv".format(DIR_PATH, load_type))
        df_sim["m"] = M * df_sim["l{0}".format(load_type)]

        df_sim["w{0}".format(mode_type)] = df_sim["w{0}".format(mode_type)] / (2* pi)

        m_sim = df_sim["m"].to_numpy()
        w1_sim = df_sim["w{0}".format(mode_type)].to_numpy()

        """ Get Theoretical Data """
        m_theo, frequencies_theo = theoretical_analysis(lambda_number=load_type, plot=False)
        w1_theo = frequencies_theo[mode_type-1]

        """ Get Experimetal Data """
        df_exp = pd.read_csv("{0}\data\\real_data_l{1}.csv".format(DIR_PATH, load_type))
        df_exp["m"] = M + df_exp["d{0}".format(load_type)]
        m_exp = df_exp["m"].to_numpy()
        w1_exp = df_exp['w{0}'.format(mode_type)].to_numpy()

        if "simulation" in plot_type:
            plt.plot(m_sim, w1_sim, color=PLT_COLORS[color_index], linestyle=':', label='Simulation type {0}'.format(load_type))
        if "theoretical" in plot_type:
            plt.plot(m_theo, w1_theo, color=PLT_COLORS[color_index], linestyle='-.', label='Theoretical type {0}'.format(load_type))
        if "experimental" in plot_type:
            plt.scatter(m_exp, w1_exp, color=PLT_COLORS[color_index], label='Experimental points tyzpe {0}'.format(load_type))
            # m, b = polyfit(m_exp, w1_exp, 1)
            # plt.plot(m_exp, m*m_exp + b, color=PLT_COLORS[color_index],  linestyle='--', label='Experiment best fit line type {0}'.format(load_type))

        plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
        color_index += 1

    plt.title('Natural frequency against mass, Frequency mode {0}'.format(mode_type))
    plt.xlabel('mass (kg)')
    plt.ylabel('Natural frequency (Hz)')
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    # data_plot(4, on_one_graph=True) # change the parameter 1,2,3,4 for each load type
    compare_load_type(mode_type=3, plot_type=["theoretical", "simulation", "experimental"], range_load_type=[1,2,3,4])