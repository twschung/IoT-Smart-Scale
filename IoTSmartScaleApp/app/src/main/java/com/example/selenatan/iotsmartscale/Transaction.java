package com.example.selenatan.iotsmartscale;

import java.util.Date;

/**
 * Created by Terry on 26/1/16.
 *
 */

public class Transaction {
    public int id;
    public String serialNum, activationCode, numOfHours, issueBy, issueAt, expireAt;

    public Transaction (int id, String serialNum, String activationCode, String numOfHours, String issueBy, String issueAt, String expireAt){
        this.id = id;
        this.serialNum = serialNum;
        this.activationCode = activationCode;
        this.numOfHours = numOfHours;
        this.issueBy = issueBy;
        this.issueAt = issueAt;
        this.expireAt = expireAt;
    }
}
