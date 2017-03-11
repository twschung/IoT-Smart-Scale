import matplotlib.pyplot as plt
#import matplotlib.figure as Figure
import numpy as np
import db_access
import datetime, os
fig_size = plt.rcParams['figure.figsize']
fig_size[0] = 6.5
fig_size[1] = 2.7
plt.rcParams['figure.figsize'] = fig_size
    
def plot_and_save_weekly_graph(this_week_list, last_week_list, weekday):
	y_prev_week = last_week_list
	y_curr_week = this_week_list
	days=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
	days[weekday] = 'Today'
	plt.style.use(['ggplot'])

	N = 7 
	ind = np.arange(N)
	width = 0.35

	ax1 = plt.subplot(111)

	prev_week_series = ax1.bar(ind, y_prev_week, width, align='center')
	curr_week_series = ax1.bar(ind+width, y_curr_week, width, align='center')

	# adding labels, wxis and ticks
	ax1.set_ylabel('Calorie Comsumption/ kcal', fontsize=9)
	ax1.set_xticks(ind + width / 2)
	ax1.set_xticklabels(days, fontsize=9)
	ax1.legend((prev_week_series[0], curr_week_series[0]), ('Previous Week','Current Week'), fontsize=9)
	bar_value(prev_week_series)
	bar_value(curr_week_series)
	plt.savefig('plot.png', bbox_inches='tight') #, dpi=95)
	#plt.show()
	ax1.clear()
    
def bar_value(series):
	# Labels the value above the chart
	for x in series:
		height = x.get_height()
		plt.text(x.get_x() + x.get_width()/2., 1.03*height, '%d' %int(height),ha='center', va='bottom', fontsize=8)
	
def plot_weekly_label(self, date, currentUserInfo):#,  currentUserInfo):
	# print("barchart.py:date %s" %(str(date.strftime("%Y-%m-%d"))))
	userId = currentUserInfo.id
	weekday = date.weekday()
	thisweek = [0]*7
	lastweek = [0]*7

	## block can be removed - was used to check if the dates are passed correctly
	##start date from myTrackingMenu
	#currentWeek_startDate = (date - (datetime.timedelta(days=weekday))).strftime("%Y-%m-%d")
	##strtDate = (date - (datetime.timedelta(days=(date.weekday()+7)))).strftime("%Y-%m-%d")
	#print("barchart.py:currentWeek_startDate \t%s" %(str(currentWeek_startDate)))
	#currentWeek_endDate = date.strftime("%Y-%m-%d") #aka today
	#print("barchart.py:currentWeek_endDate \t%s" %(str(currentWeek_endDate)))

	# use getDailyIntake instead of getRangeDailyIntake
	# was: entries = db_access.user_getRangeDailyIntake(userId,strtDate,endDate)[1]
	# now: db_access.user_getDailyIntake(userId, date)
	for i in range(0,(weekday+1)):
		dateToPlot = date - (datetime.timedelta(days=weekday-i))
		# print(dateToPlot.strftime("%Y-%m-%d"))
		entry = db_access.user_getDailyIntake(userId, dateToPlot.strftime("%Y-%m-%d"))
		if (entry[0] == False):
			thisweek[i] = float(0)
			# print(thisweek) # to check for error
		else:
			# print(int(entry[1].energy)) # to check for error
			thisweek[i] = float(entry[1].energy)

	for j in reversed(range(0,7)):
		dateToPlot = date + (datetime.timedelta(days=j-weekday-7))
		# print(dateToPlot.strftime("%Y-%m-%d"))
		entry = db_access.user_getDailyIntake(userId, dateToPlot.strftime("%Y-%m-%d"))
		if (entry[0] == False):
			lastweek[j] = float(0)
		else:
			# print(int(entry[1].energy)) # to check for error
			lastweek[j] = float(entry[1].energy)


	###following two lines check if the data is correct
	#print('barchart.py: thisweek: %s' %thisweek)
	#print('barchart.py: lastweek: %s' %lastweek)
	plot_and_save_weekly_graph(thisweek, lastweek, weekday)
	#return figure1
