package com.example.selenatan.iotsmartscale;

import java.math.BigInteger;

/**
 * Created by Terry on 24/1/16.
 */
public class Device {
    public int id, timezone, TimeUploadHH, TimeUploadMM;
    public String serialNum, devicePhoneNum, privateKey, clientFirstName, clientLastName, clientPhoneNum, clientEmail,
            APNname, APNusername, APNpassword, FTPaddress,FTPport, FTPusername, FTPpassword,
            FTPpath, createdBy, createdAt, updateBy, updateAt;

    public Device (int id, String serialNum, String devicePhoneNum, String privateKey, int timezone, String clientFirstName,
                   String clientLastName, String clientPhoneNum, String clientEmail, String APNname, String APNusername,
                   String APNpassword, String FTPaddress, String FTPport, String FTPusername, String FTPpassword,
                   String FTPpath, int timeUploadHH, int timeUploadMM, String createdBy, String createdAt,
                   String updateBy, String updateAt){
        this.id = id;
        this.serialNum = serialNum;
        this.devicePhoneNum = devicePhoneNum;
        this.privateKey = privateKey;
        this.timezone = timezone;
        this.clientFirstName = clientFirstName;
        this.clientLastName = clientLastName;
        this.clientPhoneNum = clientPhoneNum;
        this.clientEmail = clientEmail;
        this.APNname = APNname;
        this.APNusername = APNusername;
        this.APNpassword = APNpassword;
        this.FTPaddress = FTPaddress;
        this.FTPport = FTPport;
        this.FTPusername = FTPusername;
        this.FTPpassword = FTPpassword;
        this.FTPpath = FTPpath;
        this.TimeUploadHH = timeUploadHH;
        this.TimeUploadMM = timeUploadMM;
        this.createdBy = createdBy;
        this.createdAt = createdAt;
        this.updateBy = updateBy;
        this.updateAt = updateAt;
    }

    public Device (String serialNum, String devicePhoneNum, String clientFirstName, String clientLastName, String clientPhoneNum){
        this(-1,serialNum,devicePhoneNum,"",0,clientFirstName,clientLastName,clientPhoneNum,"","","","","","","","","",0,0,"","","","");
    }
}
