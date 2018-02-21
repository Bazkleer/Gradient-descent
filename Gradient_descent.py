
x=[1,2,3,4]
y=[1,2,3,4]

def calc_cost_fun(theta_0,theta_1,feature):
    sum=0
    for i in range(0,len(x)-1):
        cost_fun=((theta_0 +theta_1*x[i])-y[i])
        if(feature!=0):
            cost_fun=cost_fun*x[i]
        sum=sum+cost_fun
    return sum

def gradrient_desc(x,y,alpah,theta_0,theta_1):
    theta_0_temp=0
    theta_1_temp=0
    m=len(x)
    for i in range(0,2000):
        theta_0_temp= theta_0 -((alpah/m)*calc_cost_fun(theta_0,theta_1,0))
        theta_1_temp= theta_1 -((alpah/m)*calc_cost_fun(theta_0,theta_1,1))
        theta_0=theta_0_temp
        theta_1=theta_1_temp
    return (theta_0,theta_1)


print(gradrient_desc(x,y,0.01,0.1,0.1))
