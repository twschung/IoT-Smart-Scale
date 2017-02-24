package com.example.selenatan.iotsmartscale;

import android.app.AlertDialog;
import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Spinner;
import android.widget.ArrayAdapter;
import android.widget.AdapterView;

import java.util.Calendar;
import java.util.ArrayList;

public class EditAccountActivity extends AppCompatActivity {

    userCache CurrentUserCache;
    user currentUser;

    EditText editText_firstNameVal, editText_lastNameVal, editText_dobVal, editText_heightVal, editText_weightVal, editText_targetWeightVal,
            editText_targetIntakeVal;

    TextView textView_emailVal;

    Button button_saveChanges;

    Spinner spinner_genderVal, spinner_dobVal;

    String selGender, selDob;

    private String[] state = { "Male", "Female"};

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_edit_account);

        CurrentUserCache = new userCache(this);
        currentUser = CurrentUserCache.getCurrentUser();

        editText_firstNameVal = (EditText)findViewById(R.id.editText_firstNameVal);
        editText_firstNameVal.setHint(currentUser.firstName);

        editText_lastNameVal = (EditText)findViewById(R.id.editText_lastNameVal);
        editText_lastNameVal.setHint(currentUser.lastName);

        textView_emailVal = (TextView)findViewById(R.id.textView_emailVal);
        textView_emailVal.setText(currentUser.email);

        spinner_dobVal = (Spinner)findViewById(R.id.spinner_dobVal);
        ArrayList<String> years = new ArrayList<String>();
        int thisYear = Calendar.getInstance().get(Calendar.YEAR);
        for (int i = 1900; i <= thisYear; i++) {
            years.add(Integer.toString(i));
        }
        ArrayAdapter<String> adapter_years = new ArrayAdapter<String>(this, android.R.layout.simple_spinner_item, years);
        adapter_years.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        spinner_dobVal.setAdapter(adapter_years);
        for(int i=0;i<years.size();i++){
            if(years.get(i).equals(currentUser.dob)){
                spinner_dobVal.setSelection(i);
                selDob = years.get(i);
            }
        }
        spinner_dobVal.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener(){
            @Override
            public void onItemSelected(AdapterView<?> parent, View view, int position, long id){
                spinner_dobVal.setSelection(position);
                selDob = (String)spinner_dobVal.getSelectedItem();
            }
            @Override
            public void onNothingSelected(AdapterView<?> arg0) {
                // TODO Auto-generated method stub
            }
        });

        spinner_genderVal = (Spinner)findViewById(R.id.spinner_genderVal);
        ArrayAdapter<String> adapter_state = new ArrayAdapter<String>(this, android.R.layout.simple_spinner_item, state);
        adapter_state.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        spinner_genderVal.setAdapter(adapter_state);
        if(currentUser.gender=="m"){
            spinner_genderVal.setSelection(0);
            selGender = "m";
        }
        else{
            spinner_genderVal.setSelection(1);
            selGender = "f";
        }
        spinner_genderVal.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener(){
            @Override
            public void onItemSelected(AdapterView<?> parent, View view, int position, long id){
                spinner_genderVal.setSelection(position);
                selGender = (String)spinner_genderVal.getSelectedItem();
                if(selGender == "Male"){selGender = "m";}
                else{selGender = "f";}
            }
            @Override
            public void onNothingSelected(AdapterView<?> arg0) {
            // TODO Auto-generated method stub
            }
        });

        editText_heightVal = (EditText)findViewById(R.id.editText_heightVal);
        editText_heightVal.setHint(currentUser.height);

        editText_weightVal = (EditText)findViewById(R.id.editText_weightVal);
        editText_weightVal.setHint(currentUser.weight);

        editText_targetWeightVal = (EditText)findViewById(R.id.editText_targetWeightVal);
        editText_targetWeightVal.setHint(currentUser.targetWeight);

        editText_targetIntakeVal = (EditText)findViewById(R.id.editText_targetIntakeVal);
        editText_targetIntakeVal.setHint(currentUser.targetIntake);

        button_saveChanges = (Button) findViewById(R.id.button_saveChanges);
        button_saveChanges.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v){
                String new_firstName = editText_firstNameVal.getText().toString();
                if(new_firstName.equals("")){new_firstName = currentUser.firstName;}
                String new_lastName = editText_lastNameVal.getText().toString();
                if(new_lastName.equals("")){new_lastName = currentUser.lastName;}
                String new_dob = selDob;
                if(new_dob.equals("")){new_dob = currentUser.dob;}
                String new_gender = selGender;
                if(new_gender.equals("")){new_gender = currentUser.gender;}
                String new_height = editText_heightVal.getText().toString();
                if(new_height.equals("")){new_height = currentUser.height;}
                String new_weight = editText_weightVal.getText().toString();
                if(new_weight.equals("")){new_weight = currentUser.weight;}
                String new_targetWeight = editText_targetWeightVal.getText().toString();
                if(new_targetWeight.equals("")){new_targetWeight = currentUser.targetWeight;}
                String new_targetIntake = editText_targetIntakeVal.getText().toString();
                if(new_targetIntake.equals("")){new_targetIntake = currentUser.targetIntake;}
                updateAccount(currentUser.id,new_firstName,new_lastName,new_dob,new_gender,new_height,new_weight,new_targetWeight,new_targetIntake);
            }
        });

    }

    private void updateAccount(int id,final String firstName,final String lastName, final String dob, final String gender, final String height, final String weight, final String targetWeight, final String targetIntake){
        DB_user_request db_user_request = new DB_user_request(this);
        db_user_request.updateUserAccount(id,firstName,lastName,dob,gender,height,weight,targetWeight,targetIntake, new updateDBCallBack() {
            @Override
            public void done(String result) {
                if (result == "SUCCESS") {
                    updateUserAccount(firstName, lastName, dob, gender, height, weight, targetWeight, targetIntake);
                } else {
                    showErrorMessage(result);
                }
            }
        });
    }

    private void updateUserAccount(String firstName,String lastName,String dob,String gender,String height,String weight, String targetWeight, String targetIntake){
        currentUser.firstName = firstName;
        currentUser.lastName = lastName;
        currentUser.dob = dob;
        currentUser.gender = gender;
        currentUser.height = height;
        currentUser.weight = weight;
        currentUser.targetWeight = targetWeight;
        currentUser.targetIntake = targetIntake;
        CurrentUserCache.setCurrentUser(currentUser);
        showSuccessMessage();
        Intent intent = new Intent(EditAccountActivity.this, AccountActivity.class);
        intent.addFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP);
        startActivity(intent);
    }

    private void showErrorMessage(String errorMessage) {
        AlertDialog.Builder dialogBuilder = new AlertDialog.Builder(EditAccountActivity.this);
        dialogBuilder.setMessage(errorMessage);
        dialogBuilder.setPositiveButton("OK", null);
        dialogBuilder.show();
    }

    private void showSuccessMessage(){
        AlertDialog.Builder dialogBuilder = new AlertDialog.Builder(EditAccountActivity.this);
        dialogBuilder.setMessage("SUCCESS: Changes Saved");
        dialogBuilder.setPositiveButton("Ok", null);
        dialogBuilder.show();
    }
}
