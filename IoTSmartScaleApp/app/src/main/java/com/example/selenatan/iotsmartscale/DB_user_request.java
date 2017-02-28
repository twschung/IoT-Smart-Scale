package com.example.selenatan.iotsmartscale;

import android.app.ProgressDialog;
import android.content.Context;
import android.os.AsyncTask;
import android.util.Log;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.InterfaceAddress;
import java.net.MalformedURLException;
import java.net.URL;
import java.net.URLConnection;
import java.util.ArrayList;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;
import java.util.Locale;
import java.util.List;
import java.util.Map;
import java.util.HashMap;

import org.apache.commons.io.IOUtils;

public class DB_user_request {
    ProgressDialog progressDialog;
    public static final String SERVER_ADDRESS = "http://192.168.1.7/~selenatan/iotsmartscale/php/";
    //public static final String SERVER_ADDRESS = "http://10.0.2.2/~selenatan/iotsmartscale/php/";

    public DB_user_request(Context context) {
        progressDialog = new ProgressDialog(context);
        progressDialog.setCancelable(false);
        progressDialog.setTitle("Processing...");
        progressDialog.setMessage("Please wait...");
    }

    public void updateUserAccount (int id, String firstName,String lastName,String dob,String gender,String height,String weight, String targetWeight, String targetIntake, updateDBCallBack dbCallBack){
        progressDialog.show();
        new updateUserAccountTask(id, firstName, lastName, dob, gender, height, weight, targetWeight, targetIntake,dbCallBack).execute();
    }

    public void addUserIntake (int id, String foodItem,String calorieContent,String dateConsumed, updateDBCallBack dbCallBack){
        progressDialog.show();
        new addUserIntakeTask(id, foodItem, calorieContent, dateConsumed,dbCallBack).execute();
    }

    public void getUserdata (user User, getUserCallBack userCallBack){
        progressDialog.show();
        new getUserDataTask(User,userCallBack).execute();
    }

    public void getUserIntakedata (int id, getUserIntakeCallBack userCallBack){
        progressDialog.show();
        new getUserIntakeDataTask(id,userCallBack).execute();
    }

    public void getUserIntakeWeeklydata (int id, getUserIntakeWMCallBack userCallBack){
        progressDialog.show();
        new getUserIntakeWeeklyDataTask(id,userCallBack).execute();
    }

    public void getUserIntakeMonthlydata (int id, getUserIntakeWMCallBack userCallBack){
        progressDialog.show();
        new getUserIntakeMonthlyDataTask(id,userCallBack).execute();
    }

    public void registerNewUser(user User, updateDBCallBack dbCallBack){
        progressDialog.show();
        new registerNewUserTask(User,dbCallBack).execute();
    }

    public void getAllUserData(getAllUserCallBack allUserCallBack){
        progressDialog.show();
        new getAllUserTask(allUserCallBack).execute();
    }

    public void getOneUserData(String username, getUserCallBack userCallBack){
        progressDialog.show();
        new getOneUserDataTask(username,userCallBack).execute();
    }

    public void deleteUser (int id, updateDBCallBack dbCallBack){
        progressDialog.show();
        new deleteUserTask(id,dbCallBack).execute();
    }

    public class updateUserAccountTask extends AsyncTask<Void,Void,String>{
        int id;
        String firstName, lastName, dob, gender, height, weight, targetWeight, targetIntake;
        updateDBCallBack dbCallBack;

        public updateUserAccountTask (int ID, String FirstName,String LastName,String Dob,String Gender,String Height,String Weight, String TargetWeight, String TargetIntake, updateDBCallBack DBCallBack){
            this.id = ID;
            this.firstName= FirstName;
            this.lastName = LastName;
            this.dob = Dob;
            this.gender = Gender;
            this.height = Height;
            this.weight = Weight;
            this.targetWeight = TargetWeight;
            this.targetIntake = TargetIntake;
            this.dbCallBack= DBCallBack;
        }

        @Override
        protected String doInBackground(Void... params){
            String responds = "";
            try {
                String link = SERVER_ADDRESS + "updateUserAccount.php?id=%27" + id + "%27&firstname=%27" + firstName + "%27&lastname=%27" + lastName + "%27&dob=%27" + dob + "%27&gender=%27" + gender +
                        "%27&height=%27" + height + "%27&weight=%27" + weight + "%27&targetweight=%27" + targetWeight + "%27&targetintake=%27" + targetIntake +"%27";
                Log.d("SQL",link);
                URL url = new URL(link);
                URLConnection urlConnection = url.openConnection();
                HttpURLConnection httpURLConnection = (HttpURLConnection) urlConnection;
                httpURLConnection.connect();
                InputStream inputStream = urlConnection.getInputStream();
                InputStreamReader inputStreamReader = new InputStreamReader(inputStream);
                BufferedReader bufferedReader = new BufferedReader(inputStreamReader);
                String encoding = urlConnection.getContentEncoding();
                encoding = encoding == null ? "UTF-8" : encoding;
                String line = "";
                while ((line = bufferedReader.readLine()) != null) {
                    responds += line;
                }
                httpURLConnection.disconnect();
                String body = IOUtils.toString(inputStream, encoding);
                System.out.println(body);
                Log.d("SQL",responds);

            } catch (MalformedURLException e){
                e.printStackTrace();
            } catch (IOException e){
                e.printStackTrace();
            }
            if (responds.equals("SUCCESS")== true ) {
                return "SUCCESS";
            } else {
                return "FAIL";
            }
        }
        @Override
        protected void onPostExecute (String returnedResult){
            super.onPostExecute(returnedResult);
            progressDialog.dismiss();
            dbCallBack.done(returnedResult);
        }
    }

        public class addUserIntakeTask extends AsyncTask<Void,Void,String> {
            int id;
            String foodItem, calorieContent, dateConsumed;
            updateDBCallBack dbCallBack;

        public addUserIntakeTask (int ID, String foodItem,String calorieContent,String dateConsumed, updateDBCallBack DBCallBack){
            SimpleDateFormat sdf = new SimpleDateFormat("HH:mm:ss", Locale.UK);
            String currentTime = sdf.format(new Date());
            this.id = ID;
            this.foodItem= foodItem;
            this.calorieContent = calorieContent;
            this.dateConsumed = dateConsumed+"_"+currentTime;
            this.dbCallBack= DBCallBack;
        }

        @Override
        protected String doInBackground(Void... params){
            String responds = "";
            try {
                String link = SERVER_ADDRESS + "addUserIntake.php?id=%27" + id + "%27&fooddescription=%27" + foodItem + "%27&energy=%27" + calorieContent + "%27&datetime=%27" + dateConsumed +"%27";
                Log.d("SQL",link);
                URL url = new URL(link);
                URLConnection urlConnection = url.openConnection();
                HttpURLConnection httpURLConnection = (HttpURLConnection) urlConnection;
                httpURLConnection.connect();
                InputStream inputStream = urlConnection.getInputStream();
                InputStreamReader inputStreamReader = new InputStreamReader(inputStream);
                BufferedReader bufferedReader = new BufferedReader(inputStreamReader);
                String encoding = urlConnection.getContentEncoding();
                encoding = encoding == null ? "UTF-8" : encoding;
                String line = "";
                while ((line = bufferedReader.readLine()) != null) {
                    responds += line;
                }
                httpURLConnection.disconnect();
                String body = IOUtils.toString(inputStream, encoding);
                System.out.println(body);
                Log.d("SQL",responds);

            } catch (MalformedURLException e){
                e.printStackTrace();
            } catch (IOException e){
                e.printStackTrace();
            }
            if (responds.equals("SUCCESS")== true ) {
                return "SUCCESS";
            } else {
                return "FAIL";
            }
        }
        @Override
        protected void onPostExecute (String returnedResult){
            super.onPostExecute(returnedResult);
            progressDialog.dismiss();
            dbCallBack.done(returnedResult);
        }
    }

    public class getUserDataTask extends AsyncTask<Void,Void,user> {
        user User;
        getUserCallBack userCallBack;

        public getUserDataTask (user User, getUserCallBack UserCallBack){
            this.User = User;
            this.userCallBack = UserCallBack;
        }
        @Override
        protected user doInBackground(Void... params) {
            String responds = "";
            try {
                String link = SERVER_ADDRESS + "login.php?username=%27" + User.username + "%27&password=%27" + User.password + "%27";
                Log.d("SQL",link);
                URL url = new URL(link);
                URLConnection urlConnection = url.openConnection();
                HttpURLConnection httpURLConnection = (HttpURLConnection) urlConnection;

                httpURLConnection.connect();

                InputStream inputStream = urlConnection.getInputStream();
                InputStreamReader inputStreamReader = new InputStreamReader(inputStream);
                BufferedReader bufferedReader = new BufferedReader(inputStreamReader);
                String line = "";

                while ((line = bufferedReader.readLine()) != null) {
                    responds += line;
                }
                httpURLConnection.disconnect();
                Log.d("SQL",responds);

            } catch (MalformedURLException e){
                e.printStackTrace();
            } catch (IOException e){
                e.printStackTrace();
            }

            String [] data = responds.split("<br>");
            if (data[0].equals("SUCCESS")== true ) {
                user User = new user(Integer.parseInt(data[1]), data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10], data[11], data[12]);
                return User;
            } else {
                return null;
            }
        }

        @Override
        protected void onPostExecute (user returnedUser){
            super.onPostExecute(returnedUser);
            progressDialog.dismiss();
            userCallBack.done(returnedUser);
        }
    }

    public class getUserIntakeDataTask extends AsyncTask<Void,Void,userIntake> {
        int id;
        getUserIntakeCallBack userCallBack;
        String myFormat = "yyyy-MM-dd";
        SimpleDateFormat sdf = new SimpleDateFormat(myFormat, Locale.UK);
        Calendar myCalendar = Calendar.getInstance();
        String date = sdf.format(myCalendar.getTime());
        String energy, fat, saturates, carbohydrate, sugars, fibre, protein, salt;

        public getUserIntakeDataTask (int Id, getUserIntakeCallBack UserCallBack){
            this.id = Id;
            this.userCallBack = UserCallBack;
        }
        @Override
        protected userIntake doInBackground(Void... params) {
            String responds = "";
            try {
                String link = SERVER_ADDRESS + "userFoodIntake.php?userid=%27" + id + "%27&date=%27" + date + "%27";
                Log.d("SQL", link);
                URL url = new URL(link);
                URLConnection urlConnection = url.openConnection();
                HttpURLConnection httpURLConnection = (HttpURLConnection) urlConnection;

                httpURLConnection.connect();

                InputStream inputStream = urlConnection.getInputStream();
                InputStreamReader inputStreamReader = new InputStreamReader(inputStream);
                BufferedReader bufferedReader = new BufferedReader(inputStreamReader);
                String line = "";

                while ((line = bufferedReader.readLine()) != null) {
                    responds += line;
                }
                httpURLConnection.disconnect();
                Log.d("SQL", responds);

            } catch (MalformedURLException e) {
                e.printStackTrace();
            } catch (IOException e) {
                e.printStackTrace();
            }

            String[] data = responds.split("<br>");
            if (data[0].equals("SUCCESS")== true ) {
                if(data.length==1){
                    energy = Integer.toString(0);
                    fat = Integer.toString(0);
                    carbohydrate = Integer.toString(0);
                    sugars = Integer.toString(0);
                    fibre = Integer.toString(0);
                    protein = Integer.toString(0);
                    salt = Integer.toString(0);
                }else{
                    energy = data[1];
                    fat = data[2];
                    carbohydrate = data[3];
                    sugars = data[4];
                    fibre = data[5];
                    protein = data[6];
                    salt = data[7];
                }
                userIntake UserIntake = new userIntake(id, date, energy, fat, saturates, carbohydrate, sugars, fibre, protein, salt);
                return UserIntake;
            } else {
                return null;
            }
        }

        @Override
        protected void onPostExecute (userIntake returnedUser){
            super.onPostExecute(returnedUser);
            progressDialog.dismiss();
            userCallBack.done(returnedUser);
        }

    }

    public class getUserIntakeWeeklyDataTask extends AsyncTask<Void,Void,Map> {
        int id;
        getUserIntakeWMCallBack userCallBack;

        public getUserIntakeWeeklyDataTask (int Id, getUserIntakeWMCallBack UserCallBack){
            this.id = Id;
            this.userCallBack = UserCallBack;
        }
        @Override
        protected Map doInBackground(Void... params) {
            String responds = "";
            try {
                String link = SERVER_ADDRESS + "userFoodIntakeWeekly.php?userid=%27" + id + "%27";
                Log.d("SQL", link);
                URL url = new URL(link);
                URLConnection urlConnection = url.openConnection();
                HttpURLConnection httpURLConnection = (HttpURLConnection) urlConnection;

                httpURLConnection.connect();

                InputStream inputStream = urlConnection.getInputStream();
                InputStreamReader inputStreamReader = new InputStreamReader(inputStream);
                BufferedReader bufferedReader = new BufferedReader(inputStreamReader);
                String line = "";

                while ((line = bufferedReader.readLine()) != null) {
                    responds += line;
                }
                httpURLConnection.disconnect();
                Log.d("SQL", responds);

            } catch (MalformedURLException e) {
                e.printStackTrace();
            } catch (IOException e) {
                e.printStackTrace();
            }

            String[] data = responds.split("<br>");
            List energy = new ArrayList();
            List week = new ArrayList();
            List year = new ArrayList();
            for(int i = 0; i<=data.length-4; i=i+4){
                if(data[i].equals("SUCCESS")==true){
                    energy.add(data[i+1]);
                    week.add(data[i+2]);
                    year.add(data[i+3]);
                }
                else{
                    energy.add(0);
                    week.add(0);
                    year.add(0);
                }
            }
            Map<String,List> map =new HashMap();
            map.put("energyList",energy);
            map.put("weekList",week);
            map.put("yearList",year);

            return map;
        }

        @Override
        protected void onPostExecute (Map map){
            super.onPostExecute(map);
            progressDialog.dismiss();
            userCallBack.done(map);
        }

    }

    public class getUserIntakeMonthlyDataTask extends AsyncTask<Void,Void,Map> {
        int id;
        getUserIntakeWMCallBack userCallBack;

        public getUserIntakeMonthlyDataTask (int Id, getUserIntakeWMCallBack UserCallBack){
            this.id = Id;
            this.userCallBack = UserCallBack;
        }
        @Override
        protected Map doInBackground(Void... params) {
            String responds = "";
            try {
                String link = SERVER_ADDRESS + "userFoodIntakeMonthly.php?userid=%27" + id + "%27";
                Log.d("SQL", link);
                URL url = new URL(link);
                URLConnection urlConnection = url.openConnection();
                HttpURLConnection httpURLConnection = (HttpURLConnection) urlConnection;

                httpURLConnection.connect();

                InputStream inputStream = urlConnection.getInputStream();
                InputStreamReader inputStreamReader = new InputStreamReader(inputStream);
                BufferedReader bufferedReader = new BufferedReader(inputStreamReader);
                String line = "";

                while ((line = bufferedReader.readLine()) != null) {
                    responds += line;
                }
                httpURLConnection.disconnect();
                Log.d("SQL", responds);

            } catch (MalformedURLException e) {
                e.printStackTrace();
            } catch (IOException e) {
                e.printStackTrace();
            }

            String[] data = responds.split("<br>");
            List energy = new ArrayList();
            List month = new ArrayList();
            List year = new ArrayList();
            for(int i = 0; i<=data.length-4; i=i+4){
                if(data[i].equals("SUCCESS")==true){
                    energy.add(data[i+1]);
                    month.add(data[i+2]);
                    year.add(data[i+3]);
                }
                else{
                    energy.add(0);
                    month.add(0);
                    year.add(0);
                }
            }
            Map<String,List> map =new HashMap();
            map.put("energyList",energy);
            map.put("monthList",month);
            map.put("yearList",year);
            return map;
        }

        @Override
        protected void onPostExecute (Map map){
            super.onPostExecute(map);
            progressDialog.dismiss();
            userCallBack.done(map);
        }

    }

    public class registerNewUserTask extends AsyncTask<Void,Void,String>{
        user newUser;
        updateDBCallBack dbCallBack;

        public registerNewUserTask (user User, updateDBCallBack DBCallBack){
            this.newUser = User;
            this.dbCallBack= DBCallBack;
        }

        @Override
        protected String doInBackground(Void... params){
            String responds = "";
            try {
                String link = SERVER_ADDRESS + "registerUser.php?username=%27" + newUser.username + "%27&password=%27" + newUser.password + "%27&firstName=%27" + newUser.firstName + "%27&lastName=%27" + newUser.lastName + "%27&email=%27" +newUser.email + "%27&root=%27";
                Log.d("SQL",link);
                URL url = new URL(link);
                URLConnection urlConnection = url.openConnection();
                HttpURLConnection httpURLConnection = (HttpURLConnection) urlConnection;
                httpURLConnection.connect();
                InputStream inputStream = urlConnection.getInputStream();
                InputStreamReader inputStreamReader = new InputStreamReader(inputStream);
                BufferedReader bufferedReader = new BufferedReader(inputStreamReader);
                String line = "";
                while ((line = bufferedReader.readLine()) != null) {
                    responds += line;
                }
                httpURLConnection.disconnect();
                Log.d("SQL",responds);

            } catch (MalformedURLException e){
                e.printStackTrace();
            } catch (IOException e){
                e.printStackTrace();
            }
            if (responds.equals("SUCCESS")== true ) {
                return "SUCCESS";
            } else {
                return "Failed : " + responds;
            }
        }
        @Override
        protected void onPostExecute (String returnedResult){
            super.onPostExecute(returnedResult);
            progressDialog.dismiss();
            dbCallBack.done(returnedResult);
        }
    }

    public class getAllUserTask extends AsyncTask<Void,Void,ArrayList<user>> {
        getAllUserCallBack allUserCallBack;

        public getAllUserTask (getAllUserCallBack allUserCallBack){
            this.allUserCallBack = allUserCallBack;
        }
        @Override
        protected ArrayList<user> doInBackground(Void... params) {
            String responds = "";
            try {
                String link = SERVER_ADDRESS + "showAllUser.php";
                Log.d("SQL",link);
                URL url = new URL(link);
                URLConnection urlConnection = url.openConnection();
                HttpURLConnection httpURLConnection = (HttpURLConnection) urlConnection;

                httpURLConnection.connect();

                InputStream inputStream = urlConnection.getInputStream();
                InputStreamReader inputStreamReader = new InputStreamReader(inputStream);
                BufferedReader bufferedReader = new BufferedReader(inputStreamReader);
                String line = "";

                while ((line = bufferedReader.readLine()) != null) {
                    responds += line;
                }
                httpURLConnection.disconnect();
                Log.d("SQL",responds);

            } catch (MalformedURLException e){
                e.printStackTrace();
            } catch (IOException e){
                e.printStackTrace();
            }
            ArrayList<user> allUser = new ArrayList<user>();
            String [] rowData = responds.split("<br>");
            if (rowData[0].equals("SUCCESS")== true ) {
                for (int k = 1; k < rowData.length; k++){
                    String [] columnData = rowData[k].split("&nbsp");
                    user User = new user(Integer.parseInt(columnData[1]),columnData[2],columnData[3],columnData[4],columnData[5],columnData[6],columnData[7],columnData[8],columnData[9],columnData[10],columnData[11],columnData[12]);
                    allUser.add(User);
                }
                return allUser;
            } else {
                return null;
            }
        }

        @Override
        protected void onPostExecute (ArrayList<user> returnedUsers){
            super.onPostExecute(returnedUsers);
            progressDialog.dismiss();
            allUserCallBack.done(returnedUsers);
        }

    }

    public class getOneUserDataTask extends AsyncTask<Void,Void,user> {
        String username;
        getUserCallBack userCallBack;

        public getOneUserDataTask (String username, getUserCallBack UserCallBack){
            this.username = username;
            this.userCallBack = UserCallBack;
        }
        @Override
        protected user doInBackground(Void... params) {
            String responds = "";
            try {
                String link = SERVER_ADDRESS + "showOneUser.php?username=%27" + username + "%27";
                Log.d("SQL",link);
                URL url = new URL(link);
                URLConnection urlConnection = url.openConnection();
                HttpURLConnection httpURLConnection = (HttpURLConnection) urlConnection;

                httpURLConnection.connect();

                InputStream inputStream = urlConnection.getInputStream();
                InputStreamReader inputStreamReader = new InputStreamReader(inputStream);
                BufferedReader bufferedReader = new BufferedReader(inputStreamReader);
                String line = "";

                while ((line = bufferedReader.readLine()) != null) {
                    responds += line;
                }
                httpURLConnection.disconnect();
                Log.d("SQL",responds);

            } catch (MalformedURLException e){
                e.printStackTrace();
            } catch (IOException e){
                e.printStackTrace();
            }

            String [] data = responds.split("<br>");
            if (data[0].equals("SUCCESS")== true ) {
                user User = new user(Integer.parseInt(data[1]), data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10], data[11], data[12]);
                return User;
            } else {
                return null;
            }
        }

        @Override
        protected void onPostExecute (user returnedUser){
            super.onPostExecute(returnedUser);
            progressDialog.dismiss();
            userCallBack.done(returnedUser);
        }

    }

    public class deleteUserTask extends AsyncTask<Void,Void,String>{
        int id;
        updateDBCallBack dbCallBack;

        public deleteUserTask (int ID, updateDBCallBack DBCallBack){
            this.id= ID;
            this.dbCallBack= DBCallBack;
        }

        @Override
        protected String doInBackground(Void... params){
            String responds = "";
            try {
                String link = SERVER_ADDRESS + "deleteUser.php?id=%27" + id + "%27";
                Log.d("SQL",link);
                URL url = new URL(link);
                URLConnection urlConnection = url.openConnection();
                HttpURLConnection httpURLConnection = (HttpURLConnection) urlConnection;
                httpURLConnection.connect();
                InputStream inputStream = urlConnection.getInputStream();
                InputStreamReader inputStreamReader = new InputStreamReader(inputStream);
                BufferedReader bufferedReader = new BufferedReader(inputStreamReader);
                String line = "";
                while ((line = bufferedReader.readLine()) != null) {
                    responds += line;
                }
                httpURLConnection.disconnect();
                Log.d("SQL",responds);

            } catch (MalformedURLException e){
                e.printStackTrace();
            } catch (IOException e){
                e.printStackTrace();
            }
            if (responds.equals("SUCCESS")== true ) {
                return "SUCCESS";
            } else {
                return "FAIL";
            }
        }
        @Override
        protected void onPostExecute (String returnedResult){
            super.onPostExecute(returnedResult);
            progressDialog.dismiss();
            dbCallBack.done(returnedResult);
        }
    }

}
