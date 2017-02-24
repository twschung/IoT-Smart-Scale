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
import java.net.MalformedURLException;
import java.net.URL;
import java.net.URLConnection;
import java.util.ArrayList;

public class DB_device_request {
    ProgressDialog progressDialog;
    public static final String SERVER_ADDRESS = "http://solarpaygogo.com/php/device/";

    public DB_device_request(Context context) {
        progressDialog = new ProgressDialog(context);
        progressDialog.setCancelable(false);
        progressDialog.setTitle("Processing...");
        progressDialog.setMessage("Please wait...");
    }

    public void getDefaultDeviceSetting(updateDBCallBack dbCallBack){
        progressDialog.show();
        new getDefaultDeviceSettingTask(dbCallBack).execute();
    }

    public void registerNewDevice(Device newDevice, updateDBCallBack dbCallBack){
        progressDialog.show();
        new registerNewDeviceTask(newDevice,dbCallBack).execute();
    }

    public void searchDevices(String searchIndex, String searchParam, getAllDeviceCallBack allDeviceCallBack ){
        progressDialog.show();
        new searchDevicesTask(searchIndex,searchParam,allDeviceCallBack).execute();
    }

    public void getDeviceInfo(String serialNum, getAllDeviceCallBack allDeviceCallBack){
        progressDialog.show();
        new getDeviceInfoTask(serialNum, allDeviceCallBack).execute();
    }

    public void deleteDevice (int id, updateDBCallBack dbCallBack){
        progressDialog.show();
        new deleteDeviceTask(id,dbCallBack).execute();
    }

    public class getDefaultDeviceSettingTask extends AsyncTask<Void,Void,String> {
        updateDBCallBack dbCallBack;

        public getDefaultDeviceSettingTask (updateDBCallBack dbCallBack){
            this.dbCallBack = dbCallBack;
        }
        @Override
        protected String doInBackground(Void... params) {
            String responds = "";
            try {
                String link = SERVER_ADDRESS + "defaultDeviceSetting.txt";
                Log.d("TXT", link);
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
                Log.d("TXT",responds);

            } catch (MalformedURLException e){
                e.printStackTrace();
            } catch (IOException e){
                e.printStackTrace();
            }
            return responds;
        }

        @Override
        protected void onPostExecute (String returnResult){
            super.onPostExecute(returnResult);
            progressDialog.dismiss();
            dbCallBack.done(returnResult);
        }

    }

    public class registerNewDeviceTask extends AsyncTask<Void,Void,String>{
        Device newDevice;
        updateDBCallBack dbCallBack;

        public registerNewDeviceTask (Device newDevice, updateDBCallBack DBCallBack){
            this.newDevice = newDevice;
            this.dbCallBack= DBCallBack;
        }

        @Override
        protected String doInBackground(Void... params){
            String responds = "";
            try {
                String link = SERVER_ADDRESS + "registerDevice.php?serialNum=%27" + newDevice.serialNum +
                        "%27&devicePhoneNum=%27" + newDevice.devicePhoneNum + "%27&privateKey=%27" +
                        newDevice.privateKey + "%27&timezone=%27" + newDevice.timezone + "%27&clientFirsName=%27" +
                        newDevice.clientFirstName + "%27&clientLastName=%27" + newDevice.clientLastName +
                        "%27&clientPhoneNum=%27" + newDevice.clientPhoneNum+ "%27&clientEmail=%27" + newDevice.clientEmail +
                        "%27&APNname=%27" + newDevice.APNname + "%27&APNusername=%27" + newDevice.APNusername +
                        "%27&APNpassword=%27" + newDevice.APNpassword + "%27&FTPaddress=%27" + newDevice.FTPaddress +
                        "%27&FTPport=%27" + newDevice.FTPport + "%27&FTPusername=%27" + newDevice.FTPusername +
                        "%27&FTPpassword=%27" + newDevice.FTPpassword + "%27&FTPpath=%27" + newDevice.FTPpath +
                        "%27&TimeUploadHH=%27" + newDevice.TimeUploadHH + "%27&TimeUploadMM=%27" + newDevice.TimeUploadMM +
                        "%27&createdBy=%27" + newDevice.createdBy + "%27&createdAt=%27" + newDevice.createdAt +
                        "%27&updateBy=%27" + newDevice.updateBy + "%27&updateAt=%27" + newDevice.updateAt + "%27";
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

    public class searchDevicesTask extends AsyncTask<Void,Void,ArrayList<Device>> {
        String searchIndex, searchParam;
        getAllDeviceCallBack allDeviceCallBack;

        public searchDevicesTask (String searchIndex, String searchParam, getAllDeviceCallBack allDeviceCallBack){
            this.searchIndex = searchIndex;
            this.searchParam = searchParam;
            this.allDeviceCallBack = allDeviceCallBack;
        }
        @Override
        protected ArrayList<Device> doInBackground(Void... params) {
            String responds = "";
            try {
                String link = SERVER_ADDRESS + "searchDevice.php?searchIndex=" + searchIndex + "&searchParam=%27" + searchParam + "%27" ;
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
            ArrayList<Device> allDevice = new ArrayList<Device>();
            String [] rowData = responds.split("<br>");
            if (rowData[0].equals("SUCCESS")== true ) {
                for (int k = 1; k < rowData.length; k++){
                    String [] columnData = rowData[k].split("&nbsp");
                    Device device = new Device(columnData[0],columnData[1],columnData[2],
                            columnData[3],columnData[4]);
                    allDevice.add(device);
                }
                return allDevice;
            } else {
                return null;
            }
        }

        @Override
        protected void onPostExecute (ArrayList<Device> returnedDevices){
            super.onPostExecute(returnedDevices);
            progressDialog.dismiss();
            allDeviceCallBack.done(returnedDevices);
        }

    }

    public class getDeviceInfoTask extends AsyncTask<Void,Void,ArrayList<Device>> {
        String serialNum;
        getAllDeviceCallBack allDeviceCallBack;

        public getDeviceInfoTask (String serialNum, getAllDeviceCallBack allDeviceCallBack){
            this.serialNum = serialNum;
            this.allDeviceCallBack = allDeviceCallBack;
        }
        @Override
        protected ArrayList<Device> doInBackground(Void... params) {
            String responds = "";
            try {
                String link = SERVER_ADDRESS + "getDeviceInfo.php?serialNum=%27" + serialNum + "%27";
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
            ArrayList<Device> allDevice = new ArrayList<Device>();
            String [] rowData = responds.split("<br>");
            if (rowData[0].equals("SUCCESS")== true ) {
                for (int k = 1; k < rowData.length; k++){
                    String [] columnData = rowData[k].split("&nbsp");
                    Device device = new Device(Integer.parseInt(columnData[0]),columnData[1],columnData[2],columnData[3],
                            Integer.parseInt(columnData[4]),columnData[5],columnData[6],columnData[7],columnData[8],
                            columnData[9],columnData[10],columnData[11],columnData[12],columnData[13],columnData[14],columnData[15],columnData[16],
                            Integer.parseInt(columnData[17]),Integer.parseInt(columnData[18]),columnData[19],columnData[20],columnData[21],columnData[22]);
                    allDevice.add(device);
                }
                return allDevice;
            } else {
                return null;
            }
        }

        @Override
        protected void onPostExecute (ArrayList<Device> returnedDevices){
            super.onPostExecute(returnedDevices);
            progressDialog.dismiss();
            allDeviceCallBack.done(returnedDevices);
        }

    }

    public class deleteDeviceTask extends AsyncTask<Void,Void,String>{
        int id;
        updateDBCallBack dbCallBack;

        public deleteDeviceTask (int ID, updateDBCallBack DBCallBack){
            this.id= ID;
            this.dbCallBack= DBCallBack;
        }

        @Override
        protected String doInBackground(Void... params){
            String responds = "";
            try {
                String link = SERVER_ADDRESS + "deleteDevice.php?id=%27" + id + "%27";
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
