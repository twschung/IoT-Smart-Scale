# py.sign_in('xuenhoong', 'wmmlV25sNcqQGdiOeMgt')

# Get this figure: fig = py.get_figure("https://plot.ly/~xuenhoong/3/")
# Get this figure's data: data = py.get_figure("https://plot.ly/~xuenhoong/3/").get_data()
# Add data to this figure: py.plot(Data([Scatter(x=[1, 2], y=[2, 3])]), filename ="text-hover-bar", fileopt="extend"))
# Get y data of first trace: y1 = py.get_figure("https://plot.ly/~xuenhoong/3/").get_data()[0]["y"]

# Get figure documentation: https://plot.ly/python/get-requests/
# Add data documentation: https://plot.ly/python/file-options/

# If you're using unicode in your file, you may need to specify the encoding.
# You can reproduce this figure in Python with the following code!

# Learn about API authentication here: https://plot.ly/python/getting-started
# Find your api_key here: https://plot.ly/settings/api

import plotly.plotly as py
import plotly.offline as offline

from plotly.graph_objs import *

import barchart, db_access
import datetime

# py.sign_in('xuenhoong', 'wmmlV25sNcqQGdiOeMgt')
def plot_and_save_weekly_graph(this_week_list, previous_week_list, weekday):
    y_prev_week = previous_week_list
    y_curr_week = this_week_list
    x_today=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    x_today[weekday] = 'Today'
    current_week = Bar(
        x=x_today,
        y=y_curr_week,
        marker=Marker(
            color='rgb(158,202,225)',
            line=Line(
                color='rgb(8,48,107)',
                width=1.5
            )
        ),
        name='This Week',
        opacity=0.6,
        # uid='f9ad87',
        # xsrc='xuenhoong:4:d1e5b1',
        # ysrc='xuenhoong:4:57c379'
    )
    previous_week = Bar(
        x=x_today,
        y=y_prev_week,
        name='Last Week',
        # uid='afc8b8',
        # xsrc='xuenhoong:4:d1e5b1',
        # ysrc='xuenhoong:5:ed6d43'
    )

    data = Data([current_week, previous_week])

    layout = {
      "autosize": False,
      "height": 265,
      "hovermode": "x",
      "legend": {
        "orientation": "h",
        "traceorder": "normal"
      },
      "margin": {
        "t": 50,
        "b": 50,
        "l": 80
      },
      "showlegend": False,
      "title": "<br>",
      "width": 670,
      "xaxis": {
        "autorange": True,
        "fixedrange": True,
        "range": [-0.5, 6.5],
        "title": "",
        "type": "category",
        "zeroline": False
      },
      "yaxis": {
        "autorange": True,
        "fixedrange": True,
        "range": [0, 2631.57894737],
        "title": "Calorie Consumption/kcal",
        "type": "linear"
      }
    }

    #username = str(userId)
    fig = Figure(data=data, layout=layout)
    plot_url = offline.plot((fig), auto_open=False)
	# py.image.save_as((fig), filename='%s_weekly.png' %(today_date))
    # py.image.save_as((fig), filename='weekly.png')

def plot_weekly_label(self,date,userId):#,  currentUserInfo):
    # print("barchart.py:date %s" %(str(date.strftime("%Y-%m-%d"))))
    #userId = currentUserInfo.id # uncomment when using on RPi, replace userId with currentUserInfo
    weekday = date.weekday()
    """
    # block can be removed - was used to check if the dates are passed correctly
    #start date from myTrackingMenu
    currentWeek_startDate = (date - (datetime.timedelta(days=weekday))).strftime("%Y-%m-%d")
    #strtDate = (date - (datetime.timedelta(days=(date.weekday()+7)))).strftime("%Y-%m-%d")
    print("barchart.py:currentWeek_startDate \t%s" %(str(currentWeek_startDate)))
    currentWeek_endDate = date.strftime("%Y-%m-%d") #aka today
    print("barchart.py:currentWeek_endDate \t%s" %(str(currentWeek_endDate)))
    """
    # use getDailyIntake instead of getRangeDailyIntake
    # was: entries = db_access.user_getRangeDailyIntake(userId,strtDate,endDate)[1]
    # now: db_access.user_getDailyIntake(userId, date)
    thisweek = [0]*7
    lastweek = [0]*7
    for i in range(0,(weekday+1)):
        dateToPlot = date - (datetime.timedelta(days=weekday-i))
        # print(dateToPlot.strftime("%Y-%m-%d"))
        entry = db_access.user_getDailyIntake(userId, dateToPlot.strftime("%Y-%m-%d"))
        if (entry[0] == False):
            thisweek[i] = 0
            # print(thisweek) # to check for error
        else:
            # print(int(entry[1].energy)) # to check for error
            thisweek[i] = entry[1].energy

    for j in range(0,7):
        dateToPlot = date - (datetime.timedelta(days=abs((weekday-14+1+j))))
        # print(dateToPlot.strftime("%Y-%m-%d"))
        entry = db_access.user_getDailyIntake(userId, dateToPlot.strftime("%Y-%m-%d"))
        if (entry[0] == False):
            lastweek[j] = 0
        else:
            # print(int(entry[1].energy)) # to check for error
            lastweek[j] = entry[1].energy

    # following two lines check if the data is correct
    # print('barchart.py: thisweek: %s' %thisweek)
    # print('barchart.py: lastweek: %s' %lastweek)

    barchart.plot_and_save_weekly_graph(thisweek, lastweek, weekday)
