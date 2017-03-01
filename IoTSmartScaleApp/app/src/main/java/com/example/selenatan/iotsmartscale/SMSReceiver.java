package com.example.selenatan.iotsmartscale;

import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.telephony.SmsMessage;
import android.util.Log;


/**
 * Created by Terry on 24/2/16.
 */
public class SMSReceiver extends BroadcastReceiver {
    public SMSReceiver (){

    }

    @Override
    public void onReceive(Context context, Intent intent){
        Bundle bundle = intent.getExtras();

        SmsMessage [] msgs = null;
        String str = "";


        if (bundle != null){
            Object [] pdus = (Object[]) bundle.get("pdus");
            msgs = new SmsMessage[pdus.length];
            for (int i=0; i < msgs.length; i++) {
                msgs[i] = SmsMessage.createFromPdu((byte[]) pdus[i]);
                str = msgs[i].getMessageBody().toString();
            }

            Log.d("SMS_RES", str);

            String [] msgData = str.split(",");

            String dialogMessage = "Serial Number : " + "\n" + msgData[0] + "\n" + "Subject : " + "\n" ;

            switch (msgData[1]){
                case("COM"):{dialogMessage += "Input Command" + "\n";break;}
                case("ATC"):{dialogMessage += "Activation Code" + "\n";break;}
                case("PRK"):{dialogMessage += "Private Key" + "\n";break;}
                case("APN"):{dialogMessage += "APN & SYS setting" + "\n";break;}
                case("FTP"):{dialogMessage += "FTP setting" + "\n";break;}
                case("RES"):{dialogMessage += "Reset operation" + "\n";break;}
                case("STA"):{dialogMessage += "Status request" + "\n";break;}
            }

            dialogMessage += "Respond : " + "\n";

            switch (msgData[2]){
                case("ACC"):{dialogMessage += "ACCEPTED" + "\n";break;}
                case("ERR"):{dialogMessage += "ERROR" + "\n";break;}
                case("REJ"):{dialogMessage += "REJECTED" + "\n";break;}
            }


            if (msgData[1].equals("STA")){
                dialogMessage += "Message : " + "\n";
                dialogMessage += "Latitude : " + msgData[3] + "\n";
                dialogMessage += "Longitude : " + msgData[4] + "\n";
                dialogMessage += "Current System Time : " + msgData[5] + "/" + msgData[6] + "/" + msgData[7] + " " + msgData[8] + ":" + msgData[9] + "\n";
                dialogMessage += "Solar Panel Voltage : " + msgData[10] + "\n";
                dialogMessage += "Solar Panel Current : " + msgData[11] + "\n";
                dialogMessage += "Battery Voltage : " + msgData[12] + "\n";
                dialogMessage += "Battery Current : " + msgData[13] + "\n";
                dialogMessage += "Battery Percentage : " + msgData[14] + "\n";
                dialogMessage += "Output Voltage : " + msgData[15] + "\n";
                dialogMessage += "Output Current : " + msgData[16];
            }

            Log.d("SMS_RES",dialogMessage);


            //Intent dialogIntent = new Intent(context,SMSRespondDialogActivity.class);
            //dialogIntent.putExtra("Respond_Msg",dialogMessage);
            //dialogIntent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
            //context.startActivity(dialogIntent);


        }
    }
}
