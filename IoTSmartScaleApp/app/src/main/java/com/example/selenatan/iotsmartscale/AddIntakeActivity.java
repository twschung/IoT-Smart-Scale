package com.example.selenatan.iotsmartscale;

import android.app.AlertDialog;
import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.app.DatePickerDialog;
import android.widget.DatePicker;

import java.util.Calendar;
import java.util.Locale;
import java.text.SimpleDateFormat;

public class AddIntakeActivity extends AppCompatActivity {

    userCache CurrentUserCache;
    user currentUser;

    EditText editText_foodItemVal, editText_calorieContentVal, editText_dateConsumedVal;

    Button button_addIntake;

    final Calendar myCalendar = Calendar.getInstance();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_add_intake);

        CurrentUserCache = new userCache(this);
        currentUser = CurrentUserCache.getCurrentUser();

        editText_foodItemVal = (EditText)findViewById(R.id.editText_foodItemVal);
        editText_calorieContentVal = (EditText)findViewById(R.id.editText_calorieContentVal);

        String myFormat = "yyyy-MM-dd";
        SimpleDateFormat sdf = new SimpleDateFormat(myFormat, Locale.UK);
        myCalendar.get(Calendar.YEAR);
        myCalendar.get(Calendar.MONTH);
        myCalendar.get(Calendar.DAY_OF_MONTH);
        editText_dateConsumedVal = (EditText)findViewById(R.id.editText_dateConsumedVal);
        editText_dateConsumedVal.setText(sdf.format(myCalendar.getTime()));
        editText_dateConsumedVal.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v) {
                // TODO Auto-generated method stub
                new DatePickerDialog(AddIntakeActivity.this, date, myCalendar
                        .get(Calendar.YEAR), myCalendar.get(Calendar.MONTH),
                        myCalendar.get(Calendar.DAY_OF_MONTH)).show();
            }
        });

        button_addIntake = (Button) findViewById(R.id.button_addIntake);
        button_addIntake.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v){
                String foodItemVal = editText_foodItemVal.getText().toString();
                String calorieContentVal = editText_calorieContentVal.getText().toString();
                String dateConsumedVal = editText_dateConsumedVal.getText().toString();
                addIntake(currentUser.id,foodItemVal,calorieContentVal,dateConsumedVal);
            }
        });

    }

    @Override
    public void onBackPressed()
    {
        super.onBackPressed();
        Intent intent = new Intent(getApplicationContext(),MainMenuActivity.class);
        intent.addFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP); // Will clear out your activity history stack till now
        startActivity(intent);
    }

    DatePickerDialog.OnDateSetListener date = new DatePickerDialog.OnDateSetListener(){
        @Override
        public void onDateSet(DatePicker view, int year, int monthOfYear, int dayOfMonth) {
            // TODO Auto-generated method stub
            myCalendar.set(Calendar.YEAR, year);
            myCalendar.set(Calendar.MONTH, monthOfYear);
            myCalendar.set(Calendar.DAY_OF_MONTH, dayOfMonth);
            updateLabel();
        }

    };

    private void updateLabel(){
        String myFormat = "yyyy-MM-dd";
        SimpleDateFormat sdf = new SimpleDateFormat(myFormat, Locale.UK);
        editText_dateConsumedVal.setText(sdf.format(myCalendar.getTime()));
    }

    private void addIntake(int id,final String foodItem,final String calorieContent, final String dateConsumed){
        DB_user_request db_user_request = new DB_user_request(this);
        db_user_request.addUserIntake(id,foodItem,calorieContent,dateConsumed, new updateDBCallBack() {
            @Override
            public void done(String result) {
                if (result == "SUCCESS") {
                    showSuccessMessage();
                    Intent intent = new Intent(AddIntakeActivity.this, AddIntakeActivity.class);
                    startActivity(intent);
                } else {
                    showErrorMessage(result);
                }
            }
        });
    }

    private void showErrorMessage(String errorMessage) {
        AlertDialog.Builder dialogBuilder = new AlertDialog.Builder(AddIntakeActivity.this);
        dialogBuilder.setMessage(errorMessage);
        dialogBuilder.setPositiveButton("OK", null);
        dialogBuilder.show();
    }

    private void showSuccessMessage(){
        AlertDialog.Builder dialogBuilder = new AlertDialog.Builder(AddIntakeActivity.this);
        dialogBuilder.setMessage("SUCCESS: Intake Added");
        dialogBuilder.setPositiveButton("Ok", null);
        dialogBuilder.show();
    }
}
