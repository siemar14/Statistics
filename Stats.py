#Calculate the sample mean and sample variance


#create an array of numbers from user input
int_list=list()
sum_sample=0
Calculation = 0

#while loop to ask user input to calculate mean and variance
while Calculation >=0:
    user_input=float(raw_input('Enter a number: '))
    #append the user's raw input into the list of numbers
    int_list.append(user_input)
    #the number of numbers in the list
    n = float(len(int_list))
    samp_variance = 0.0
    sum_sqr=0.0
    #if the user's input is a nonnegative number, continue the program
    if user_input >=0:
        for x in int_list:
            sum_sample= sum(int_list)
            #calculate the mean
            sample_mean = sum_sample / n
            sum_sqr = (x-sample_mean)**2
            if n<=1:
                samp_variance += sum_sqr / n
            else:
                samp_variance += sum_sqr / (n-1)
                
        if str(samp_variance).endswith('0') or str(samp_variance).endswith('5'):
            print 'Mean is: %.1f       variance is: %.1f' % (sample_mean, samp_variance)
        else:
            print 'Mean is: %.1f       variance is: %f' % (sample_mean, samp_variance)
            
#end the program
    else:
        print ""
        break;
        




 