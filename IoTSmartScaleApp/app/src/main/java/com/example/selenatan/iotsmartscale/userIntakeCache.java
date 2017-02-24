package com.example.selenatan.iotsmartscale;

import android.content.Context;
import android.content.SharedPreferences;

public class userIntakeCache {
    SharedPreferences currentUserIntakeCache;

    public userIntakeCache(Context context){
        currentUserIntakeCache = context.getSharedPreferences("currentUserIntake",0);
    }

    public void setCurrentUserIntake(userIntake currentUserIntake){
        SharedPreferences.Editor editor = currentUserIntakeCache.edit();
        editor.putInt("id", currentUserIntake.id);
        editor.putString("date", currentUserIntake.date);
        editor.putString("energy", currentUserIntake.energy);
        editor.putString("fat", currentUserIntake.fat);
        editor.putString("saturates", currentUserIntake.saturates);
        editor.putString("carbohydrate", currentUserIntake.carbohydrate);
        editor.putString("sugars", currentUserIntake.sugars);
        editor.putString("fibre", currentUserIntake.fibre);
        editor.putString("protein", currentUserIntake.protein);
        editor.putString("salt", currentUserIntake.salt);

        editor.commit();
    }

    public userIntake getCurrentUserIntake (){
        int id = currentUserIntakeCache.getInt("id", -1);
        String date = currentUserIntakeCache.getString("date", "");
        String energy = currentUserIntakeCache.getString("energy", "");
        String fat = currentUserIntakeCache.getString("fat", "");
        String saturates = currentUserIntakeCache.getString("saturates","");
        String carbohydrate = currentUserIntakeCache.getString("carbohydrate", "");
        String sugars = currentUserIntakeCache.getString("sugars","");
        String fibre = currentUserIntakeCache.getString("fibre", "");
        String protein = currentUserIntakeCache.getString("protein", "");
        String salt = currentUserIntakeCache.getString("salt","");

        userIntake CurrentUserIntake = new userIntake(id,date,energy,fat,saturates,carbohydrate,sugars,fibre,protein,salt);
        return CurrentUserIntake;
    }

    public void logoutCurrentUserIntake (){
        SharedPreferences.Editor editor = currentUserIntakeCache.edit();
        editor.clear();
        editor.commit();
    }


}
