package com.example.selenatan.iotsmartscale;

import java.util.ArrayList;

/**
 * Created by Terry on 27/1/16.
 */
interface getAllTransactionCallBack {
    public abstract void done(ArrayList<Transaction> returnedTransactions);
}
