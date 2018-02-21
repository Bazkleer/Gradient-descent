#Hossam Elbahrawy

import matplotlib.pyplot as plt

x=[[.5],
   [1],
   [1.5],
   [2],
   [3],
   [3.5],
   [4]]

y=[[1],
   [.5],
   [1.5],
   [1],
   [2],
   [3],
   [3.5]]

cost_arr=[]

def calc_func(theta_0,theta_1,feature):
    sum=0
    for i in range(0,len(x)-1):
        cost_fun=((theta_0 +theta_1*x[i][0])-y[i][0])
        if(feature!=0):
            cost_fun=cost_fun*x[i][0]
        sum=sum+cost_fun
    return sum

def calc_cost_func(theta_0,theta_1):
    cost=0
    for i in range(0,len(x)-1):
        cost=cost+((theta_0+theta_1*x[i][0])-y[i][0])**2;
    return cost

    
def gradrient_desc(x,y,alpah,theta_0,theta_1):
    theta_0_temp=0
    theta_1_temp=0
    m=len(x)
    for i in range(0,200):
        theta_0_temp= theta_0 -((alpah/m)*calc_func(theta_0,theta_1,0))
        theta_1_temp= theta_1 -((alpah/m)*calc_func(theta_0,theta_1,1))
        cost_arr.append(calc_cost_func(theta_0_temp,theta_1_temp))
        theta_0=theta_0_temp
        theta_1=theta_1_temp
    return (theta_0,theta_1)


def plot_data():
    plt.grid()
    plt.axis([0,5,0,5])
    for i in range(0,len(x)):
        plt.scatter(x[i][0],y[i][0],c='r')
        
def plot_cost_func():
    plt.grid()
    plt.axis([0,200,.5,10])
    plt.ylabel("Cost Function")
    plt.plot(cost_arr,c='r')
    
def plot_hyp(theta_0,theta_1):
    #plt.grid()
    plt.axis([0,5,0,5])
    res=[]
    for i in range(0,len(x)):
        res.append(theta_0+(theta_1*i))
    plt.plot(res)
    
    
plot_data()
t0,t1=gradrient_desc(x,y,0.01,0.1,0.1)
print("Theta_0:",t0)
print("Theta_1:",t1)
plot_hyp(t0,t1)
#plot_cost_func()      # un comment to plot the cost function