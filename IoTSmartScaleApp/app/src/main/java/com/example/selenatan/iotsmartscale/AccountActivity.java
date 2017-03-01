package com.example.selenatan.iotsmartscale;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

public class AccountActivity extends AppCompatActivity {

    userCache CurrentUserCache;
    user currentUser;

    TextView textView_nameVal, textView_emailVal, textView_dobVal, textView_genderVal, textView_heightVal, textView_weightVal, textView_targetWeightVal,
            textView_targetIntakeVal;

    Button button_editAccount;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_account);

        CurrentUserCache = new userCache(this);
        currentUser = CurrentUserCache.getCurrentUser();

        textView_nameVal = (TextView)findViewById(R.id.textView_nameVal);
        textView_nameVal.setText(currentUser.firstName+" "+currentUser.lastName);

        textView_emailVal = (TextView)findViewById(R.id.textView_emailVal);
        textView_emailVal.setText(currentUser.email);

        textView_dobVal = (TextView)findViewById(R.id.textView_dobVal);
        textView_dobVal.setText(currentUser.dob);

        textView_genderVal = (TextView)findViewById(R.id.textView_genderVal);
        if(currentUser.gender == "m"){
            textView_genderVal.setText("Male");}
        else{textView_genderVal.setText("Female");}

        textView_heightVal = (TextView)findViewById(R.id.textView_heightVal);
        textView_heightVal.setText(currentUser.height);

        textView_weightVal = (TextView)findViewById(R.id.textView_weightVal);
        textView_weightVal.setText(currentUser.weight);

        textView_targetWeightVal = (TextView)findViewById(R.id.textView_targetWeightVal);
        textView_targetWeightVal.setText(currentUser.targetWeight);

        textView_targetIntakeVal = (TextView)findViewById(R.id.textView_targetIntakeVal);
        textView_targetIntakeVal.setText(currentUser.targetIntake);

        button_editAccount = (Button)findViewById(R.id.button_editAccount);
        button_editAccount.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v){
                startActivity(new Intent(AccountActivity.this, EditAccountActivity.class));
            }
        });
    }
}
