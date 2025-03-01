import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore", message="invalid value")
warnings.filterwarnings("ignore", message="divide by zero")

###Computation of epsilon^S
def calculate_V1(F,m,M):
    """By multiplying a1 by the following value, we will ensure that all values are 'nan' 
    if m==M or F==1, which avoids a division by 0. Function outputs 1 if values are valid
    and 'nan' otherwise."""
    ensure_no_division_by_zero = np.where(m==M,float('nan'),np.where(np.isclose(F,1),float('nan'),1))
    a1 = (F-1) * (M/m) * (np.power((M-m), 2))*ensure_no_division_by_zero
    b1 = -((M-m)/m) * ((np.power(m,2)-4*M*m +2*M)*(F-1) + F*M)
    c1 = ((1-m)/m)* ( (F-1) * (2* np.power(m, 2)-4*M*m-m) + (3*F-1)*M )
    d1 = -(1-m) *( (F-1) * (m-2) + (F/m) )

    D10 = np.power(b1,2)-3*a1*c1
    D11 = (2*np.power(b1,3)) - (9*a1*b1*c1) + (27*np.power(a1, 2)* d1)
    case = np.power(D11, 2)-4*np.power(D10, 3)
    R1 = np.where(D10>0,float('nan'),np.sqrt(np.power(D10,3)))
    V1 = np.where(case>0, 
        -1/(3*a1)*(b1+np.cbrt((D11+np.sqrt(case))/2)+np.cbrt((D11-np.sqrt(case))/2)),
        -1/(3*a1)*(b1+2*np.sqrt(D10)*np.cos(1/3*np.arccos(D10/(2*R1)))) )

    return V1

def calculate_V2(F,m,M):
    """By multiplying a1 by the following value, we will ensure that all values are 'nan' 
    if m==M or F==1, which avoids a division by 0. Function outputs 1 if values are valid
    and 'nan' otherwise."""
    ensure_no_division_by_zero = np.where(m==M,float('nan'),np.where(F==1,float('nan'),1))
    a2 = (F-(F-1)*m)/m*ensure_no_division_by_zero
    b2 = -(6*F-(F-1)*(M+5*m))/m
    c2 = (1/(m*(1-M))) * (m*((F-1)*(m+9*M-9)-F)+4*M*((F-1)*M-4*F+1)+12*F)
    d2 = -(2*F-(F-1)*(M+m))*((4-m-4*M)/(m*(1-M)))+2*(F-1)
    D20 = np.power(b2, 2)-3*a2*c2
    D21 = 2*np.power(b2, 3) - 9*a2*b2*c2+27*np.power(a2, 2)*d2
    R2 = np.sqrt(np.power(D20,3))
    V2 = -1/(3*a2)*(b2+2*np.sqrt(D20)*np.cos((1/3)*np.arccos(D21/(2*R2))))
    
    return V2

def theoretical_eps(eps,m,M):
    F=np.exp(eps)
    V1=np.where(eps==0,((1-m)/(M-m))-np.sqrt(M*m*(1-m)*(1-M))/(M*(M-m)),calculate_V1(F,m,M))
    p1=np.where(V1>1,1,np.where(V1<0,0,V1))
    V2=np.where(eps==0,2-(np.sqrt(m*(1-M)))/(1-M),calculate_V2(F,m,M))
    p2=np.where(V2>1,1,np.where(V2<0,0,V2))
          
    #Maximums of each individual function:
    L1 = np.log( F-(F-1)*(p1*M+ (1-p1)*m) ) + p1*(M/m) + (1-p1)*(1-m)/(1-(p1*M+(1-p1)*m))-1
    L2 = np.log( F-(F-1)*(p2*M+(1-p2)*(M+m-p2*M)/(2-p2)) ) + p2*(M/m) +(1-p2)*(1-((M+m-p2*M)/(2-p2)))/(1-M)-1
    L3 = -(np.log(1/F + (1-1/F)*M)) + (1- (1-M)/(1-m))

    return np.where(L1>=L2,np.where(L1>=L3,L1,L3),np.where(L2>=L3,L2,L3))

def theoretical_eps_all(eps,m,M): 
    F=np.exp(eps)
    return np.where(m>M,float('nan'),np.where(m==M,np.log(F-(F-1)*m), theoretical_eps(eps,m,M)))





### Plot suppression
def generate_plot_suppression(plot_path_start, csv_path, plot_values, list_m_and_M, file_name_m_and_M, plots_limits, statistic, epsilon, include_title=True):
    ## Select points to plot
    df_all = pd.read_csv(csv_path)
    Points=[]

    ##We restrict the database to only those points (m,M) in list_m_and_M
    df_all["combined_m_and_M"] = df_all[["m","M"]].values.tolist() #Add column of (m,M) values into the dataframe
    df = df_all[df_all["combined_m_and_M"].isin(list_m_and_M)]
    ## Restrict database to the chosen plot_values
    plot_df = df.filter(["m","M",plot_values],axis=1)
    ##Delete all rows with a NaN value
    plot_df.dropna(inplace=True)

    ## Decide title and file name
    title_end = statistic
    file_name_end = "_"+plot_values+"_"+title_end+"_"+file_name_m_and_M+".pdf"
    
    if(plot_values=="difference_error_M_minus_MoS"):
        title = "Clustering mechanism: Difference of NICV (" + title_end +")"
        epsilon_text_M = "$\\mathcal{M}$ is $"+str(epsilon)+"$-DP"
        epsilon_text_MoS = "$\\mathcal{M}\\circ\\mathcal{S}$ is $(\\varepsilon^{\\mathcal{S}}("+str(epsilon)+",m,M))$-DP"
    elif(plot_values=="difference_error_M_minus_MoSChangeEpsDelta"):
        title = "Clustering mechanism: Difference of NICV (" + title_end +")"
        epsilon_text_M = "$\\mathcal{M}$ is $"+str(epsilon)+"$-DP"
        epsilon_text_MoS = "$\\mathcal{M}\\circ\\mathcal{S}$ is $"+str(epsilon)+"$-DP"  
    elif(plot_values=="difference_error_MChangeEpsDelta_minus_MoS"):
        title = "Clustering mechanism: Difference of NICV (" + title_end +")"
        epsilon_text_M = "$\\mathcal{M}$ is $(\\varepsilon^{\\mathcal{S}}("+str(epsilon)+",m,M))$-DP"
        epsilon_text_MoS = "$\\mathcal{M}\\circ\\mathcal{S}$ is $(\\varepsilon^{\\mathcal{S}}("+str(epsilon)+",m,M))$-DP"   

    ## Generate list of plot points
    x = plot_df["m"]
    y = plot_df["M"]
    z = plot_df[plot_values]
    for i in range(plot_df.shape[0]):
        Points.append([x.iloc[i],y.iloc[i],z.iloc[i]])

    ## Ensure that there are at least three points, otherwise the plot cannot be generated
    if len(x)<3:
        print("Plot "+ title + " for epsilon=" + str(epsilon) +" cannot be generated as there are less than three support values")
        return 0

    ## Specify colors of plot: Ensure that 0 will be yellow, negative numbers will be red and positive numbers will be green
    norm = mpl.colors.TwoSlopeNorm(vmin=min(-1e-10,z.min()), vcenter=0, vmax=max(1e-10,z.max()))

    ## Start plot
    fig, ax = plt.subplots()
    graph=ax.tricontourf(x, y, z, norm=norm, levels=30, cmap="RdYlGn", antialiased=True)
    # Colorbar
    fig.colorbar(graph)
    # Set axis and axis labels
    ax.set_xlim(plots_limits[0])
    ax.set_ylim(plots_limits[1])
    ax.set(xlabel='$m$', ylabel='$M$')

    # Print title
    if include_title==True:
        ax.set_title(title)

    # Add the text showing privacy parameters of M and MoS
    plt.text(0.65,0.3,epsilon_text_M,ha="center",va="center",fontsize=13,transform=ax.transAxes)
    plt.text(0.65,0.2,epsilon_text_MoS,ha="center",va="center",fontsize=13,transform=ax.transAxes)

    ### Plot implicitly when eps^S(eps,m,M)=eps with respect to m and M
    # Granularity
    delta = 0.0025*min(plots_limits[0][1]-plots_limits[0][0],plots_limits[1][1]-plots_limits[1][0])
    x = np.arange(plots_limits[0][0]+delta, plots_limits[0][1]-delta, delta)
    y = np.arange(plots_limits[1][0]+delta, plots_limits[1][1]-delta, delta)
    p, q = np.meshgrid(x, y)

    eps_suppression = lambda n, x, y: theoretical_eps_all(eps=n,m=x,M=y)
    
    z=eps_suppression(epsilon,p,q)

    my_blue = "dodgerblue"
    CSblue_line = plt.contour(p, q, z, [epsilon], colors=my_blue)
    ax.clabel(CSblue_line, [epsilon], inline=1, fontsize=10, fmt = "$\\varepsilon^{\\mathcal{S}}=%g$")

    ##Add labels for points
    for i in range(len(Points)):
        plt.text(Points[i][0],Points[i][1],np.format_float_positional(float(Points[i][2]), precision=3),fontsize=7,ha="center",va="center")

    plt.savefig(plot_path_start+file_name_end,bbox_inches='tight')
    plt.close()





### Plot of uniform Poisson sampling
def generate_plot_uniform_Poisson_sampling(plot_path_start, csv_path_list_M, csv_path_list_MoSChange, epsilon_list, statistic, include_title=True):
    fig, ax = plt.subplots()

    ##Filter the csv files that contain the statistic we consider (either Average or Variance)
    #csv_path_list_M = filter(lambda x: x.endswith(statistic+".csv"), csv_path_list_M)
    #csv_path_list_MoSChange = filter(lambda x: x.endswith(statistic+".csv"), csv_path_list_MoSChange)
    
    colors = iter(mpl.colors.TABLEAU_COLORS.values())

    for eps, csv_path_M, csv_path_MoSChange in zip(epsilon_list, csv_path_list_M, csv_path_list_MoSChange):
        df_M_all = pd.read_csv(csv_path_M)
        df_MoSChange_all = pd.read_csv(csv_path_MoSChange)
        Points_M=[]
        Points_MoSChange = []

        ##We restrict the database to the points m==M
        df_M = df_M_all[df_M_all["m"]==df_M_all["M"]]
        df_MoSChange = df_MoSChange_all[df_MoSChange_all["m"]==df_MoSChange_all["M"]]

        df_M_plot = df_M.filter(["m","stat_NICV"],axis=1).sort_values(by=["m"])
        df_MoSChange_plot = df_MoSChange.filter(["m","stat_NICV"],axis=1).sort_values(by=["m"])

        ##Delete all rows with a NaN value
        df_M_plot.dropna(inplace=True)
        df_MoSChange_plot.dropna(inplace=True)
        if df_M_plot.shape[0]==0:
            continue

        DP_label = str(eps)+"-DP"

        color = next(colors)
        plt.plot(1-df_M_plot["m"],df_M_plot["stat_NICV"], color=color, linestyle = "solid", label = "$\\mathcal{M}$ satisfying "+DP_label)
        plt.plot(1-df_MoSChange_plot["m"],df_MoSChange_plot["stat_NICV"], color=color, linestyle = "dotted", label = "$\\mathcal{M}\\circ\\mathcal{S}$ satisfying "+DP_label)

    #Axis limits and legend
    ax.set_xlim([0,1])
    ax.set_yscale('log')
    ax.legend()
    ax.set(xlabel='Sampling rate',ylabel= statistic + " of NICV (log scale)")

    #Print Title
    title = "Clustering mechanism"
    if include_title==True:
        ax.set_title(title)

    file_name_end = "_"+statistic+".pdf"
    plt.savefig(plot_path_start+file_name_end,bbox_inches='tight')
    plt.close()