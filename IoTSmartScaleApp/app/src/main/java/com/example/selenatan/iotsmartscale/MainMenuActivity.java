package com.example.selenatan.iotsmartscale;

import android.app.AlertDialog;
import android.content.Intent;
import android.content.SharedPreferences;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

public class MainMenuActivity extends AppCompatActivity {

    userCache CurrentUserCache;
    user currentUser;
    userIntakeCache CurrentUserIntakeCache;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main_menu);

        CurrentUserCache = new userCache(this);
        currentUser = CurrentUserCache.getCurrentUser();

        CurrentUserIntakeCache = new userIntakeCache(this);

        TextView textView_welcome = (TextView) findViewById(R.id.textView_welcome);
        textView_welcome.setText("Welcome "+currentUser.firstName+"!");

        Button button_addIntake = (Button) findViewById(R.id.button_addIntake);
        button_addIntake.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v) {
                startActivity(new Intent(MainMenuActivity.this, AddIntakeActivity.class));
            }
        });

        Button button_profile = (Button) findViewById(R.id.button_profile);
        button_profile.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v){
                startActivity(new Intent(MainMenuActivity.this, ProfileActivity.class));
            }
        });

        Button button_account = (Button) findViewById(R.id.button_account);
        button_account.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v){
                startActivity(new Intent(MainMenuActivity.this, AccountActivity.class));
            }
        });

        Button button_logout = (Button) findViewById(R.id.button_logout);
        button_logout.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v){
                SharedPreferences settings = getSharedPreferences("PREFS_NAME", 0);
                SharedPreferences.Editor editor = settings.edit();
                editor.putBoolean("isChecked", false);
                editor.commit();
                CurrentUserCache.logoutCurrentUser();
                CurrentUserIntakeCache.logoutCurrentUserIntake();
                startActivity(new Intent(MainMenuActivity.this, MainActivity.class));
            }
        });

    }

    @Override
    public void onBackPressed(){
        showMessage();
    }

    private void showMessage(){
        AlertDialog.Builder dialogBuilder = new AlertDialog.Builder(MainMenuActivity.this);
        dialogBuilder.setMessage("INFO: Please logout by clicking 'LOGOUT'");
        dialogBuilder.setPositiveButton("Ok", null);
        dialogBuilder.show();
    }
}
