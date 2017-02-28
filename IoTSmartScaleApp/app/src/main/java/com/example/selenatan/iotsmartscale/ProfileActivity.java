
package com.example.selenatan.iotsmartscale;

import android.graphics.Color;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.TextView;
import android.widget.ProgressBar;
import android.widget.TabHost;

import com.github.mikephil.charting.charts.BarChart;
import com.github.mikephil.charting.data.BarData;
import com.github.mikephil.charting.data.BarDataSet;
import com.github.mikephil.charting.data.BarEntry;
import com.github.mikephil.charting.interfaces.datasets.IBarDataSet;
import com.github.mikephil.charting.utils.ColorTemplate;

import java.util.ArrayList;
import java.util.Calendar;
import java.lang.Integer;
import java.lang.Double;
import java.text.DecimalFormat;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;
import java.lang.String;

public class ProfileActivity extends AppCompatActivity {

    userCache CurrentUserCache;
    user currentUser;
    userIntakeCache CurrentUserIntakeCache;
    userIntake currentUserIntake;

    TextView textView_ageVal, textView_bmiVal, textView_bmrVal, textView_fatVal, textView_satVal, textView_carbVal, textView_sugarVal, textView_fibreVal, textView_proteinVal, textView_saltVal, textView_progressBar,textView_progress;

    ProgressBar progressBar_targetIntake;

    BarChart barChart_weekly, barChart_monthly;

    Map<String,List> weeklyData, monthlyData;

    int year = Calendar.getInstance().get(Calendar.YEAR);

    int age;

    DecimalFormat df = new DecimalFormat("#.00");

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_profile);

        CurrentUserCache = new userCache(this);
        currentUser = CurrentUserCache.getCurrentUser();

        CurrentUserIntakeCache = new userIntakeCache(this);
        currentUserIntake = CurrentUserIntakeCache.getCurrentUserIntake();

        weeklyData = new HashMap();

        TabHost host = (TabHost)findViewById(R.id.tabHost);
        host.setup();

        //Tab 1
        TabHost.TabSpec spec = host.newTabSpec("Tab One");
        spec.setContent(R.id.daily);
        spec.setIndicator("Daily");
        host.addTab(spec);

        //Tab 2
        spec = host.newTabSpec("Tab Two");
        spec.setContent(R.id.weekly);
        spec.setIndicator("Weekly");
        host.addTab(spec);

        //Tab 3
        spec = host.newTabSpec("Tab Three");
        spec.setContent(R.id.monthly);
        spec.setIndicator("Monthly");
        host.addTab(spec);

        // Daily Tab

        textView_progress = (TextView)findViewById(R.id.textView_progress);
        textView_progress.setText(currentUserIntake.energy+"/"+currentUser.targetIntake);

        textView_progressBar = (TextView)findViewById(R.id.textView_progressBar);

        progressBar_targetIntake = (ProgressBar)findViewById(R.id.progressBar_targetIntake);
        progressBar_targetIntake.setMax(Integer.parseInt(currentUser.targetIntake));
        if(Integer.parseInt(currentUserIntake.energy) < Integer.parseInt(currentUser.targetIntake)){
            progressBar_targetIntake.setProgress(Integer.parseInt(currentUserIntake.energy));
            textView_progressBar.setText("You have consumed " + ((double)Integer.parseInt(currentUserIntake.energy)/Integer.parseInt(currentUser.targetIntake))*100 + "% of your target intake!");
        }
        else{
            progressBar_targetIntake.setProgress(Integer.parseInt(currentUser.targetIntake));
            textView_progressBar.setText("You have consumed " + ((double)Integer.parseInt(currentUserIntake.energy)/Integer.parseInt(currentUser.targetIntake))*100 + "% of your target intake!");
        }

        textView_ageVal = (TextView)findViewById(R.id.textView_ageVal);
        age = year-Integer.parseInt(currentUser.dob);
        textView_ageVal.setText(Integer.toString(age));

        textView_bmiVal = (TextView)findViewById(R.id.textView_bmiVal);
        textView_bmiVal.setText(df.format(Double.parseDouble(currentUser.weight)/(Double.parseDouble(currentUser.height)*Double.parseDouble(currentUser.height))));

        textView_bmrVal = (TextView)findViewById(R.id.textView_bmrVal);
        if(currentUser.gender=="m") {
            textView_bmrVal.setText(df.format(66 + (13.7*Double.parseDouble(currentUser.weight)) + (500*Double.parseDouble(currentUser.height)) - (6.8*age)));
        }
        else{
            textView_bmrVal.setText(df.format(655 + (9.6*Double.parseDouble(currentUser.weight)) + (180*Double.parseDouble(currentUser.height)) - (4.7*age)));
        }

        textView_fatVal = (TextView)findViewById(R.id.textView_fatVal);
        textView_fatVal.setText(currentUserIntake.fat);

        textView_satVal = (TextView)findViewById(R.id.textView_satVal);
        textView_satVal.setText(currentUserIntake.saturates);

        textView_carbVal = (TextView)findViewById(R.id.textView_carbVal);
        textView_carbVal.setText(currentUserIntake.carbohydrate);

        textView_sugarVal = (TextView)findViewById(R.id.textView_sugarVal);
        textView_sugarVal.setText(currentUserIntake.sugars);

        textView_fibreVal = (TextView)findViewById(R.id.textView_fibreVal);
        textView_fibreVal.setText(currentUserIntake.fibre);

        textView_proteinVal = (TextView)findViewById(R.id.textView_proteinVal);
        textView_proteinVal.setText(currentUserIntake.protein);

        textView_saltVal = (TextView)findViewById(R.id.textView_saltVal);
        textView_saltVal.setText(currentUserIntake.salt);

        // Weekly Tab
        barChart_weekly = (BarChart) findViewById(R.id.chart_weekly);
        barChart_weekly.setDescription("");
        DB_user_request db_user_request = new DB_user_request(this);
        db_user_request.getUserIntakeWeeklydata(currentUser.id, new getUserIntakeWMCallBack() {
            @Override
            public void done(Map returnedUser) {
                if (returnedUser == null) {
                    // Error catching
                } else {
                    weeklyData = new TreeMap(returnedUser);
                    weeklyGraph();
                }
            }
        });

        // Monthly Tab
        barChart_monthly = (BarChart) findViewById(R.id.chart_monthly);
        barChart_monthly.setDescription("");
        db_user_request.getUserIntakeMonthlydata(currentUser.id, new getUserIntakeWMCallBack() {
            @Override
            public void done(Map returnedUser) {
                if (returnedUser == null) {
                    // Error catching
                } else {
                    monthlyData = new TreeMap(returnedUser);
                    monthlyGraph();
                }
            }
        });
    }

    public void weeklyGraph(){
        ArrayList<BarEntry> bar = new ArrayList<>();
        ArrayList<String> labels = new ArrayList<>();
        for (Map.Entry entry : weeklyData.entrySet()) {
            System.out.println(entry.getKey() + ", " + entry.getValue());
            if(entry.getKey().equals("energyList")) {
                List value = (List) entry.getValue();
                for(int i = 0; i < value.size(); i++) {
                    bar.add(new BarEntry(Integer.parseInt((String)value.get(i)), i));
                }
            }
            else if(entry.getKey().equals("weekList")){
                List value = (List) entry.getValue();
                for(int i = 0; i < value.size(); i++) {
                    if(value.get(i).equals("Monday")){
                        labels.add("Mon");
                    }else if(value.get(i).equals("Tuesday")){
                        labels.add("Tue");
                    }else if(value.get(i).equals("Wednesday")){
                        labels.add("Wed");
                    }else if(value.get(i).equals("Thursday")){
                        labels.add("Thu");
                    }else if(value.get(i).equals("Friday")){
                        labels.add("Fri");
                    }else if(value.get(i).equals("Saturday")){
                        labels.add("Sat");
                    }else{
                        labels.add("Sun");
                    }
                }
            }
        }
        BarDataSet barDataSet = new BarDataSet(bar, "Intake (kcal) from past 7 days");
        barDataSet.setColors(ColorTemplate.COLORFUL_COLORS);
        ArrayList<IBarDataSet> dataSets = new ArrayList<>();
        dataSets.add(barDataSet);
        BarData data = new BarData(labels, dataSets);
        barChart_weekly.setData(data);
    }

    public void monthlyGraph(){
        ArrayList<BarEntry> bar = new ArrayList<>();
        ArrayList<String> labels = new ArrayList<>();
        for (Map.Entry entry : monthlyData.entrySet()) {
            System.out.println(entry.getKey() + ", " + entry.getValue());
            if(entry.getKey().equals("energyList")) {
                List value = (List) entry.getValue();
                for(int i = 0; i < value.size(); i++) {
                    bar.add(new BarEntry(Integer.parseInt((String)value.get(i)), i));
                }
            }
            else if(entry.getKey().equals("monthList")){
                List value = (List) entry.getValue();
                for(int i = 0; i < value.size(); i++) {
                    switch(Integer.parseInt((String)value.get(i))){
                        case 1:
                            labels.add("Jan");
                            break;
                        case 2:
                            labels.add("Feb");
                            break;
                        case 3:
                            labels.add("Mar");
                            break;
                        case 4:
                            labels.add("Apr");
                            break;
                        case 5:
                            labels.add("May");
                            break;
                        case 6:
                            labels.add("June");
                            break;
                        case 7:
                            labels.add("Jul");
                            break;
                        case 8:
                            labels.add("Aug");
                            break;
                        case 9:
                            labels.add("Sept");
                            break;
                        case 10:
                            labels.add("Oct");
                            break;
                        case 11:
                            labels.add("Nov");
                            break;
                        case 12:
                            labels.add("Dec");
                            break;
                    }
                }
            }
        }
        BarDataSet barDataSet = new BarDataSet(bar, "Intake (kcal) from past 6 months");
        barDataSet.setColors(ColorTemplate.COLORFUL_COLORS);
        ArrayList<IBarDataSet> dataSets = new ArrayList<>();
        dataSets.add(barDataSet);
        BarData data = new BarData(labels, dataSets);
        barChart_monthly.setData(data);
    }
}

