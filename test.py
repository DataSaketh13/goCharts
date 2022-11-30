import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import re


print("Welcome to goCharts. Embrace the world of visual presentations, at your fingertips.")
print("Developed by Saketh Velagaleti, CEO and founder of goCharts. Copyright, 2022.")
print("Please select from one of the following charts to create: Pie Chart, Bar Graph, Histogram, Scatterplot, or Line Graph.")
      
type_of_chart = input("Which chart do you want to create today? Type it in here:")


if (type_of_chart == 'Pie Chart'):
        input_null = input("How many sections do you want your pie chart to have? (Minimum is 2 sections, maximum is 6 sections).")
        input1 = input("Please enter the names of the labels on the pie chart, separated by a comma. DO NOT ADD A SPACE.")
        input2 = input("Please enter the size (percents) of the labels on the pie chart. Please make sure the percent and the label is corresponding. ") 
    



        array1 = input1.split(",")
        array2 = input2.split(",")


        
        if(input_null == 2):
             explode = (0,0)

        elif(input_null == 3):
            explode = (0,0,0)

        elif(input_null == 4):
            explode = (0,0,0,0)

        elif(input_null == 5):
            explode = (0,0,0,0,0)

        else:
            explode = (0,0,0,0,0,0)
                
    
                           
        
        
        
        array2=list(map(int, array2))

       

    
        fig1, ax1 = plt.subplots()
        ax1.pie(array2, explode=None, labels=array1,autopct='%1.1f%%',
        shadow=True, textprops={'fontsize':9}, startangle=90,)
        plt.legend(array1, loc="best")
        ax1.axis('equal')  
        plt.show()
        
elif (type_of_chart == "Bar Graph"):

        type_bar = input("Are both the axies going to be numerical values, or is only the y-axis going to be a numerical value? Type YES if the answer is yes.")

        if(type_bar == 'YES'):
                input_bar_1 = input("What do you want your x-axis values to be? Separate them with a comma, please.")
                input_bar_2 = input("What do you want your y-axis values to be? Separate them with a comma, please.")            
                input_bar_3 = input("What do you want your x-axis to be labeled as?")
                input_bar_4 = input("What do you want your y-axis to be labeled as?")
                input_bar_5 = input("What do you want as the title of your bar graph?")
                input_bar_6 = input("What color do you want your bars to be?")
       

                array_bar_1 = input_bar_1.split(",")
                array_bar_2 = input_bar_2.split(",")
                array_bar_1 = list(map(int, array_bar_1))
                array_bar_2 = list(map(int, array_bar_2))

                x = array_bar_1
                y = array_bar_2
       

                plt.bar(x, y, color = input_bar_6, width = 0.4)
        
  
                plt.xlabel(input_bar_3)
                plt.ylabel(input_bar_4)
                plt.title(input_bar_5)
                plt.show()

        else:


                input_bar_1 = input("What do you want your x-axis values to be? Separate them with a comma, please. Please enter non-decimal values.")
                input_bar_2 = input("What do you want your y-axis values to be? Separate them with a comma, please.")            
                input_bar_3 = input("What do you want your x-axis to be labeled as?")
                input_bar_4 = input("What do you want your y-axis to be labeled as?")
                input_bar_5 = input("What do you want as the title of your bar graph?")
                input_bar_6 = input("What color do you want your bars to be?")
       

                array_bar_1 = input_bar_1.split(",")
                array_bar_2 = input_bar_2.split(",")
                array_bar_2=list(map(int, array_bar_2))

                x = array_bar_1
                y = array_bar_2

                plt.bar(x, y, color = input_bar_6, width = 0.4)
        
  
                plt.xlabel(input_bar_3)
                plt.ylabel(input_bar_4)
                plt.title(input_bar_5)
                plt.show()

elif (type_of_chart == 'Histogram'):

        input_his_1 = input("Please enter the data (the numbers), each separated by a comma.")
        input_his_2 = input("What do you want as the tile for your histogram?")
        input_his_3 = input("What do you want to label the x-axis on your histogram?")
        input_his_4 = input("What do you want to label the y-axis on your histogram?")
        input_his_5 = input("What do you want the color of your bars to be?")


        array_his_1 = input_his_1.split(",")
        array_his_2 = input_his_2.split(",")
        array_his_1 = list(map(int, array_his_1))
        array_his_2 = list(map(int, array_his_1))

        array_his_sorted = sorted(array_his_1)
        plt.hist(array_his_sorted, edgecolor='black',color=input_his_5)
        plt.xlabel(input_his_3)
        plt.ylabel(input_his_4)
        plt.title(input_his_2)
        plt.show()

elif(type_of_chart == 'Scatterplot'):

                input_scat_1 =  input("What do you want the x-axis values to be?")
                input_scat_2 =  input("What do you want the y-axis values to be?")
                input_scat_3 = input("What do you want to label the x-axis?")
                input_scat_4 = input("What do you want to label the y-axis?")
                input_scat_5 = input("What do you want to title your scatterplot?")
                input_scat_color = input("What color do you want for your dots?")

                array_scat_1 = input_scat_1.split(",")
                array_scat_2 = input_scat_2.split(",")
                array_scat_1 = list(map(int, array_scat_1))
                array_scat_2 = list(map(int, array_scat_2))

                plt.scatter(array_scat_1, color=input_scat_color)
                plt.xlabel(input_scat_3)
                plt.ylabel(input_scat_4)
                plt.title(input_scat_5)

                pltshow()

elif(type_of_chart == 'Line Graph'):

                        input_line_1 = input("What do you want the x-axis values to be?")
                        input_line_2 = input("What do you want the y-values to be?")
                        input_line_3 = input("What do you want to label the x-ais?")
                        input_line_4 = input("What do you want to label the y-axis?")
                        input_line_5 = input("What do you want to title your line graph?")
                        input_line_6 = input("What do you want to have the color of your line?")

                        array_lines_1 = input_line_1.split(",")
                        array_lines_2 = input_line_2.split(",")
                        print(array_lines_1, array_lines_2)

                        array_lines_11 = list(map(int, array_lines_1))
                        array_lines_12 = list(map(int, array_lines_2))

                        plt.plot(array_lines_11, array_lines_12, color=input_line_6)
                        plt.grid()
                        plt.xlabel = (input_line_3)
                        plt.ylabel = (input_line_4)
                        plt.title = (input_line_5)
                        plt.show()
                       
                


           
                

        
        
                                

    
        
