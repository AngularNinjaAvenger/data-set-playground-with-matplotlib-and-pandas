import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb




class Births:
    def __init__(self):
        self.data = pd.read_csv('data/births.csv')

    def main(self):
        pass
        # self.g_month_birth(10,2002)
    def validation(self,month=1,day=1,year=2000):
        if month > 12 or month < 1:
            return False
        if year > 2014 or year < 2000:
            return False
        if day > 31 or day < 1:
            return False
        return True
    def g_dwmb(self):
        print("GET DAY WITH THE MOST BIRTH")
        x = self.data
        mi = x.describe()
        d_m_b = 0
        for i in mi.loc["max"].keys():
            d_m_b = mi.loc["max"][i]
        birth = x.keys()[-1]
        return x[x[birth] == d_m_b]
    def g_dwmib(self):
        print("GET DAY WITH THE LOWEST BIRTH")
        x = self.data
        mi = x.describe()
        d_m_b = 0
        for i in mi.loc["min"].keys():
            d_m_b = mi.loc["min"][i]
        birth = x.keys()[-1]
        print(x[x[birth] == d_m_b])

    def g_month_birth(self,month,year):
        x = self.data
        vali = self.validation(month=month,year=year)
        if not vali:
            return 
        x = self.gmy_data_set(month,year)
    def cmbiy(self,months,year):
        if not self.validation(year=year):
            return False
        for i in months:
            if not self.validation(month=i):
                return False
        get_year = self.data[(self.data["year"] == year)] 
        months_list = []
        for i in months:
            month1 = get_year[(get_year["month"] == i)]
            months_list.append(month1)
        print(months_list)
        return months_list
    def cdbim(self,days,month,year):
        # ARRAYS OF DAYS
        if not self.validation(year=year,month=month):
            return False
        for i in days:
            if not self.validation(day=i):
                return False
        get_month = self.gmy_data_set(month,year)
        days_list = []
        for i in days:
            get_day1 = get_month[(get_month["date_of_month"] == i)]
            days_list.append(get_day1)
        return days_list
    def g_week_wtmb_(self,month):
        print("""
        ENTER 1 AND ENTER A SPECIFIC YEAR
        ENETER 2 TO GET THE WEEK WITH THE MOST BIRTH FROM 2000-2014
        ENTER CHOICE 3 TO GET THE DAY WITH THE MOST BRITH OF A SPECIC YEAR AND ANOTHER YEAR
        ENTER CHOICE 4 TO GET THE DAY WITH THE MOST BIRTHS BETWEEN AND [ OF YEARS TO COMPARE WITH]
            """)
        what_year = input("Choice: ")
        choice  = None
        try:
            choice = int(what_year)
        except:
            return False        
        if choice == 1:
            self.for_specific_year()
        if choice == 2:
            self.all_year()
        if choice == 3:
            self.fromYear_to_year()
            pass
        if choice == 4:
            self.arrays_of_years()
            pass
        else:
            return False
    def for_specific_year(self):
        year = input("enter the specific year you want between 2000-2014: ")
        month = input("enter a specific month: ")
        try:
            year = int(year)
            month = int(month)
        except:
            return False
        if not self.validation(month=month,year=year):
            return False
        # GET THE DATA
        data = self.gmy_data_set(month,year)
        max_ = data.describe().loc["max"]
        birth = max_[max_.keys()[-1]]
        x = data[(data[max_.keys()[-1]] == birth)]
        return x
    def arrays_of_years(self):
        years = []
        while continue_entry:
            year = input("enter year: ")
            try:
                year = int(year)
            except:
                break
            # if not self.validation(year=year):
            #     print("validation error")
            #     break
            stop = input("would you like to stop enter [Y/N]: ")
            if stop.lower() == "y":
                print("y stop")
                break
            # if years and year in years:
            #     print("year in year already")
            #     continue
            years.append(year)
        new_year = []
        print(years,"<----")
        for i in years:
            print(i)
            print(self.plot_year_birth(i))         
    def plot_year_birth(self,year):
        x = self.data[(self.data["year"] == year)]
        print(x)
    def all_year(self):
        x = self.data.describe().loc["max"]
        birth = x[x.keys()[-1]]
        x = self.data[(self.data[x.keys()[-1]] == birth)]
        print(x)
        return x
        pass
    def fromYear_to_year(self):
        year1 = input("ENTER YEAR 1: ")
        year2 = input("ENTER YEAR 2: ")
        try:
            year1 =int(year1)
            year2 =int(year2)
        except:
            return False
       
        x = self.validation
        if not x(year = year1) and not x(year = year2):
            return False
        if year1 > year2:
            temp = year1
            year1 = year2
            year2 = temp
        get_year1 = self.data[(self.data["year"] >= year1)]
        new_year = get_year1[(get_year1["year"] <= year2)]
        x = new_year.describe().loc["max"]
        birth = x.keys()[-1]
        highest_birth = x[birth]
        print(new_year[new_year[birth] == highest_birth])
        return new_year[new_year[birth] == highest_birth]
    def g_month_wtmb_(self):
        pass
    def g_year_wtmb_(self):
        pass
    def gmy_data_set(self,month,year):
        year = self.data[(self.data["year"] == year)]
        month = year[year["month"] == month]
        return month
birth = Births().g_month_birth(10,2001)
print(birth)
# birth.g_week_wtmb_(10)

plt.show()

# birth.g_dwtmb_week(10,2002)

# between years

# week :
    # month
    # year

# month
# year





# get top number of births in a day in a year
# get top number of births in a day in a month
# get top number of births in a month in a year



# get least number of births in a day in a year
# get least number of births in a day in a month
# get least number of births in a month in a year


# get and plot week with the most birth
# get and plot month with the most birth
# get and plot year with the most birth
# get and plot the top 5 years of birth


# get and plot day with the least birth
# get and plot week with the least birth
# get and plot month with the least birth
# get and plot year with the least birth
# get and plot the top 5 leaset years with the most birth


# plot months and thier birth
# pass as an argument 2 months and thier years  get the birth
# pass as an argument 2 years and thier years  get the birth compare to see which one has the most births
# pass as an argument 2 days of a year and thier days of a year  get the birth compare to see which one has the most births


# allow you to pass in multiple months of a year to see a graph of the child births and to s
# allow  user to see a plot of multiple years passed in and to get thier birth counts or months or days
# allow users to see the total number of child birth accross all years 
# allow users to get the addition of mutiple years and get thier the total child birth count
# allow users to add months together to get total births for those months

#get and plot day of the months with the hight birth of a particular year
#get and plot week of the months with the hight birth of a particular year
# get and plot month with hight birth of a particular year

#get and plot day of the months with the lowest birth of a particular year
#get and plot week of the months with the lowest birth of a particular year
# get and plot month with lowest birth of a particular year


