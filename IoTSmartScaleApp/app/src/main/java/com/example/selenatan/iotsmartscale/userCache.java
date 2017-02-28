package com.example.selenatan.iotsmartscale;

import android.content.Context;
import android.content.SharedPreferences;

public class userCache {
    SharedPreferences currentUserCache;

    public userCache(Context context){
        currentUserCache = context.getSharedPreferences("currentUser",0);
    }

    public void setCurrentUser(user currentUser){
        SharedPreferences.Editor editor = currentUserCache.edit();
        editor.putInt("id", currentUser.id);
        editor.putString("username", currentUser.username);
        editor.putString("password", currentUser.password);
        editor.putString("email", currentUser.email);
        editor.putString("firstName", currentUser.firstName);
        editor.putString("lastName", currentUser.lastName);
        editor.putString("dob", currentUser.dob);
        editor.putString("gender", currentUser.gender);
        editor.putString("height", currentUser.height);
        editor.putString("weight", currentUser.weight);
        editor.putString("targetWeight", currentUser.targetWeight);
        editor.putString("targetIntake", currentUser.targetIntake);

        editor.commit();
    }

    public user getCurrentUser (){
        int id = currentUserCache.getInt("id", -1);
        String username = currentUserCache.getString("username", "");
        String password = currentUserCache.getString("password", "");
        String email = currentUserCache.getString("email","");
        String firstName = currentUserCache.getString("firstName", "");
        String lastName = currentUserCache.getString("lastName","");
        String dob = currentUserCache.getString("dob", "");
        String gender = currentUserCache.getString("gender", "");
        String height = currentUserCache.getString("height","");
        String weight = currentUserCache.getString("weight", "");
        String targetWeight = currentUserCache.getString("targetWeight", "");
        String targetIntake = currentUserCache.getString("targetIntake", "");

        user CurrentUser = new user(id,username, password, email, firstName, lastName, dob, gender, height, weight, targetWeight, targetIntake);
        return CurrentUser;
    }

    public void logoutCurrentUser (){
        SharedPreferences.Editor editor = currentUserCache.edit();
        editor.clear();
        editor.commit();
    }


}
