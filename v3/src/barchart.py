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
from plotly.graph_objs import *
#import datetime

import datetime
import db_access

# from IPython.display import Image
py.sign_in('xuenhoong', 'wmmlV25sNcqQGdiOeMgt')
def plot_and_save_weekly_graph(self, this_week_list, previous_week_list, weekday, today_date):
    y_prev_week = previous_week_list
    y_curr_week = this_week_list
    x_today=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    #i=(datetime.datetime.utcnow())
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

    layout = Layout(
        hovermode='closest',
        showlegend=True,
        title='Calorie Intake (This week v. Last Week)',
        xaxis=XAxis(
            autorange=True,
            range=[-0.5, 6.5],
            title='',
            type='category'
        ),
        yaxis=YAxis(
            autorange=True,
            range=[0, 2631.5789473684213],
            title='Calorie Consumption/kcal',
            type='linear'
        )
    )
    #username = str(userId)
    fig = Figure(data=data, layout=layout)
    # plot_url = offline.plot((fig),image='png', )
    #py.image.save_as((fig), filename='%s_weekly.png' %(today_date))
    py.image.save_as((fig), filename='weekly.png')

def plot_weekly_label(self,  currentUserInfo):
    date = datetime.datetime.utcnow() #-datetime.timedelta(days=2)
    userId = currentUserInfo.id

    strtDate = (date - (datetime.timedelta(days=(date.weekday()+7)))).strftime("%Y-%m-%d")
    print('Start date: %s '%(strtDate))
    endDate = date.strftime("%Y-%m-%d")
    print('End date: %s'%(endDate))

    weekday = date.weekday()

    (vrai, entries) = db_access.user_getRangeDailyIntake(currentUserInfo.id,strtDate,endDate)
    print("No. of Entries Found: %s"%(str(len(entries))))
    for i in range(0,len(entries)):
        print("Entry dates: %s" %(entries[i].date))
    thisweek = [0]*7
    lastweek = [0]*7
    # updates the array with energy from sql (this week)
    for i in range(0,(date.weekday())+1):
        thisweek[i] = int(entries[-i+date.weekday()].energy)
    # updates the array with energy from sql (last week)
    for j in range(date.weekday()+1, len(entries)):
        lastweek[(date.weekday()-j)] = int(entries[j].energy)

    print('thisweek: %s' %thisweek)
    print('lastweek: %s' %lastweek)

    plot_and_save_weekly_graph(self, thisweek, lastweek, weekday, endDate)
