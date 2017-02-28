package com.example.selenatan.iotsmartscale;

import android.app.AlertDialog;
import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.CheckBox;
import android.widget.CompoundButton;
import android.content.SharedPreferences;

public class LoginActivity extends AppCompatActivity{

    EditText editText_email, editText_password;
    Button button_login;
    userCache currentUserCache;
    userIntakeCache currentUserIntakeCache;
    boolean isChecked;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);
        editText_email = (EditText)findViewById(R.id.editText_email);
        editText_password = (EditText)findViewById(R.id.editText_password);
        button_login = (Button)findViewById(R.id.button_login);
        currentUserCache = new userCache(this);
        currentUserIntakeCache = new userIntakeCache(this);

        CheckBox checkBox_rememberMe = (CheckBox)findViewById(R.id.checkBox_rememberMe);
        isChecked = false;
        checkBox_rememberMe.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener(){
            @Override
            public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
                SharedPreferences settings = getSharedPreferences("PREFS_NAME", 0);
                SharedPreferences.Editor editor = settings.edit();
                editor.putBoolean("isChecked", isChecked);
                editor.commit();
            }
        });

        button_login.setOnClickListener(new Button.OnClickListener() {
            @Override
            public void onClick(View v) {
                String username = editText_email.getText().toString();
                String password = editText_password.getText().toString();
                user User = new user(username, password);
                authenticate(User);
            }
        });
    }

    public void authenticate(user User){
        final DB_user_request db_user_request = new DB_user_request(this);
        db_user_request.getUserdata(User, new getUserCallBack() {
            @Override
            public void done(user returnedUser) {
                if (returnedUser == null) {
                    showErrorMessage();
                } else {
                    db_user_request.getUserIntakedata(returnedUser.id, new getUserIntakeCallBack() {
                        @Override
                        public void done(userIntake returnedUser) {
                            currentUserIntakeCache.setCurrentUserIntake(returnedUser);
                        }
                    });
                    logUserIn(returnedUser);
                }
            }
        });
    }

    private void logUserIn(user returnedUser) {
        currentUserCache.setCurrentUser(returnedUser);
        startActivity(new Intent(LoginActivity.this, MainMenuActivity.class));
    }

    private void showErrorMessage() {
        AlertDialog.Builder dialogBuilder = new AlertDialog.Builder(LoginActivity.this);
        dialogBuilder.setMessage("Incorrect user details");
        dialogBuilder.setPositiveButton("Ok", null);
        dialogBuilder.show();
    }

}
