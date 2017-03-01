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

/**
 * Created by Terry on 26/1/16.
 */
public class DB_transaction_request {
    ProgressDialog progressDialog;
    public static final String SERVER_ADDRESS = "http://solarpaygogo.com/php/transaction/";

    public DB_transaction_request(Context context) {
        progressDialog = new ProgressDialog(context);
        progressDialog.setCancelable(false);
        progressDialog.setTitle("Processing...");
        progressDialog.setMessage("Please wait...");
    }

    public void addTransaction(Transaction newTransaction, updateDBCallBack dbCallBack){
        progressDialog.show();
        new addTransactionTask(newTransaction,dbCallBack).execute();
    }

    public void searchTransaction(String searchIndex, String searchParam, getAllTransactionCallBack allTransactionCallBack ){
        progressDialog.show();
        new searchTransactionTask(searchIndex,searchParam,allTransactionCallBack).execute();
    }

    public void getTransactionInfo(String activationCode, getAllTransactionCallBack allTransactionCallBack){
        progressDialog.show();
        new getTransactionInfoTask(activationCode, allTransactionCallBack).execute();
    }

    public class addTransactionTask extends AsyncTask<Void,Void,String> {
        Transaction newTransaction;
        updateDBCallBack dbCallBack;

        public addTransactionTask (Transaction newTransaction, updateDBCallBack DBCallBack){
            this.newTransaction = newTransaction;
            this.dbCallBack= DBCallBack;
        }

        @Override
        protected String doInBackground(Void... params){
            String responds = "";
            try {
                String link = SERVER_ADDRESS + "addTransaction.php?serialNum=%27" + newTransaction.serialNum +
                        "%27&activationCode=%27" + newTransaction.activationCode + "%27&numOfHours=%27" +
                        newTransaction.numOfHours + "%27&issueBy=%27" + newTransaction.issueBy + "%27&issueAt=%27" +
                        newTransaction.issueAt + "%27&expireAt=%27" + newTransaction.expireAt + "%27";
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

    public class searchTransactionTask extends AsyncTask<Void,Void,ArrayList<Transaction>> {
        String searchIndex, searchParam;
        getAllTransactionCallBack allTransactionCallBack;

        public searchTransactionTask (String searchIndex, String searchParam, getAllTransactionCallBack allTransactionCallBack){
            this.searchIndex = searchIndex;
            this.searchParam = searchParam;
            this.allTransactionCallBack = allTransactionCallBack;
        }
        @Override
        protected ArrayList<Transaction> doInBackground(Void... params) {
            String responds = "";
            try {
                String link = SERVER_ADDRESS + "searchTransaction.php?searchIndex=" + searchIndex + "&searchParam=" + searchParam ;
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
            ArrayList<Transaction> allTransaction = new ArrayList<Transaction>();
            String [] rowData = responds.split("<br>");
            if (rowData[0].equals("SUCCESS")== true ) {
                for (int k = 1; k < rowData.length; k++){
                    String [] columnData = rowData[k].split("&nbsp");
                    Transaction transaction = new Transaction(-1,columnData[0],
                            columnData[1],"",columnData[2],columnData[3],columnData[4]);
                    allTransaction.add(transaction);
                }
                return allTransaction;
            } else {
                return null;
            }
        }

        @Override
        protected void onPostExecute (ArrayList<Transaction> returnedTransactions){
            super.onPostExecute(returnedTransactions);
            progressDialog.dismiss();
            allTransactionCallBack.done(returnedTransactions);
        }

    }

    public class getTransactionInfoTask extends AsyncTask<Void,Void,ArrayList<Transaction>> {
        String activationCode;
        getAllTransactionCallBack allTransactionCallBack;

        public getTransactionInfoTask (String activationCode, getAllTransactionCallBack allTransactionCallBack){
            this.activationCode = activationCode;
            this.allTransactionCallBack = allTransactionCallBack;
        }
        @Override
        protected ArrayList<Transaction> doInBackground(Void... params) {
            String responds = "";
            try {
                String link = SERVER_ADDRESS + "getTransactionInfo.php?activationCode=%27" + activationCode + "%27";
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
            ArrayList<Transaction> allTransaction = new ArrayList<Transaction>();
            String [] rowData = responds.split("<br>");
            if (rowData[0].equals("SUCCESS")== true ) {
                String [] columnData = rowData[1].split("&nbsp");
                Transaction transaction = new Transaction(Integer.parseInt(columnData[0]),
                        columnData[1],columnData[2],columnData[3],columnData[4],columnData[5],columnData[6]);
                allTransaction.add(transaction);
                return allTransaction;
            } else {
                return null;
            }
        }

        @Override
        protected void onPostExecute (ArrayList<Transaction> returnedTransactions){
            super.onPostExecute(returnedTransactions);
            progressDialog.dismiss();
            allTransactionCallBack.done(returnedTransactions);
        }

    }
}
